FOOTYROOM = 'footyroom'
FOOTYROOM_VIDEOS = 'footyroom_video'
HOOFOOT = 'hoofoot'
SPORTYHL = 'sportyhl'
HIGHLIGHTS_FOOTBALL = 'highlightsfootball'
OUR_MATCH = 'ourmatch'
BOT = 'bot'


# Sources ready to be show
def get_available_sources():
    return [
        FOOTYROOM,
        FOOTYROOM_VIDEOS,
        HOOFOOT,
        HIGHLIGHTS_FOOTBALL,
        SPORTYHL,
        BOT,
        OUR_MATCH
    ]


# Sources with all the information such as scores, goal scorers and image
def get_sources_with_complete_data():
    return [
        FOOTYROOM,
        FOOTYROOM_VIDEOS,
        OUR_MATCH
    ]


def get_sources_with_incomplete_data():
    return [
        HOOFOOT,
        SPORTYHL,
        HIGHLIGHTS_FOOTBALL,
        BOT
    ]