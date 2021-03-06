from datetime import timedelta, datetime

from django.db.models import Q

from fb_highlights.models import ScraperApiKey


def get_scraper_api_keys():
    """
    :return: Get the valid keys or the keys that had an invalid try more than 2 days ago
    """
    return ScraperApiKey.objects.filter(
        Q(valid=True) |
        Q(last_invalid_try__lt=datetime.now() - timedelta(days=2))
    ).order_by('valid', 'last_invalid_try')


def validate_key(scraper_api_key):
    scraper_api_key.valid = True
    scraper_api_key.save()


def invalidate_key(scraper_api_key):
    scraper_api_key.valid = False
    scraper_api_key.last_invalid_try = datetime.now()
    scraper_api_key.save()


def remove_key(scraper_api_key):
    scraper_api_key.delete()