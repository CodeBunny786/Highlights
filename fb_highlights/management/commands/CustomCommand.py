import abc

import time
from django.core.management import BaseCommand
from raven.contrib.django.raven_compat.models import client
from fb_bot.logger import logger
from highlights import env
from monitoring import metrics


class CustomCommand(BaseCommand):

    def handle(self, *args, **options):
        task_name = self.get_task_name(options)

        try:
            start_time = time.time()
            self.run_task(options)

            runtime = round(time.time() - start_time, 2)

            # Monitor duration of the task
            logger.info("Task " + task_name + " executed in " + str(runtime) + "s", extra={
                'task': task_name,
                'success': True,
                'runtime': runtime
            })

            metrics.send_metric("scheduler.task", tags=["task:{}".format(task_name)], success=True)

        except Exception as error:
            metrics.send_metric("scheduler.task", tags=["task:{}".format(task_name)], error=True)

            if not env.DEBUG:
                # Say if PROD or PRE-PROD and report to sentry a problem has been detected
                client.user_context({ 'prod_status': env.PROD_STATUS })
                client.captureException()

                # Log the error
                logger.error("Task " + task_name + " failed", extra={
                    'task': task_name,
                    'success': False
                })
            else:
                raise error

    @abc.abstractmethod
    def get_task_name(self, options):
        """ Override method """

    @abc.abstractmethod
    def run_task(self, options):
        """ Override method """