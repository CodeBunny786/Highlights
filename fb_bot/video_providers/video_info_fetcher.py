from fb_bot.exceptions.TooManyRequestException import TooManyRequestsException
from fb_bot.logger import logger
from fb_bot.video_providers import dailymotion
from fb_bot.video_providers import streamable

ALL_VIDEO_INFO_FETCHER = [
    {
        'name': 'dailymotion',
        'fetch': dailymotion.get_video_info
    },
    {
        'name': 'streamable',
        'fetch': streamable.get_video_info
    }
]


def get_info(link):
    """
    Find the video info for video link

    :param link: the video link
    :return: the info of the video (duration, ressource url)
    """

    for fetcher in ALL_VIDEO_INFO_FETCHER:
        info = None

        try:
            info = fetcher['fetch'](link)
        except TooManyRequestsException:
            # remove temporarily fetcher for which too many request
            for fetcher_from_list in ALL_VIDEO_INFO_FETCHER:
                if fetcher['name'] == fetcher_from_list['name']:
                    logger.log('REMOVING fetcher: ' + fetcher['name'])
                    ALL_VIDEO_INFO_FETCHER.remove(fetcher_from_list)

        if info:
            return info

    return None