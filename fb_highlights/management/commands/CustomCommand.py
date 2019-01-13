import abc

import time
from django.core.management import BaseCommand
from raven.contrib.django.raven_compat.models import client
from fb_bot.logger import logger
from highlights import settings


class CustomCommand(BaseCommand):

    def handle(self, *args, **options):
        try:
            # Monitor duration of the task
            start_time = time.time()

            logger.log("Task " + str(self.get_task_name(options)) + " started", forward=True)
            self.run_task(options)
            logger.log("Task " + str(self.get_task_name(options)) + " executed in " + str(round(time.time() - start_time, 2)) + "s", forward=True)

        except Exception as error:
            if settings.DEBUG:
                raise error

            # Say if PROD or PRE-PROD
            client.user_context({ 'prod_status': settings.PROD_STATUS })
            # Report to sentry if problem detected
            client.captureException()
            # Report task had a problem
            logger.log("Task " + str(self.get_task_name(options)) + " failed", forward=True)

    @abc.abstractmethod
    def get_task_name(self, options):
        """ Override method """

    @abc.abstractmethod
    def run_task(self, options):
        """ Override method """
