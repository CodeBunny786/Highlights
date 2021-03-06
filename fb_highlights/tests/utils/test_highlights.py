from datetime import datetime, timedelta

from fb_bot.highlight_fetchers.fetcher_footyroom import FootyroomHighlight, FootyroomVideoHighlight
from fb_bot.highlight_fetchers.fetcher_hoofoot import HoofootHighlight
from fb_bot.highlight_fetchers.fetcher_our_match import OurMatchHighlight
from fb_bot.highlight_fetchers.fetcher_sportyhl import SportyHLHighlight

TIME_NOW = datetime.now()
TIME_10_MINUTES_EARLIER = datetime.now() - timedelta(minutes=10)
TIME_40_MINUTES_EARLIER = datetime.now() - timedelta(minutes=40)
TIME_1_DAY_EARLIER = datetime.now() - timedelta(hours=24)
TIME_4_DAYS_EARLIER = datetime.now() - timedelta(hours=96)

DEFAULT_TEST_IMAGE = 'http://localhost:8000/static/img/logo.png'
TEST_IMAGE = 'http://footyroom/img/match'
TEST_UPLOADED_IMAGE = 'http://cloudinary/img/match'


SENT_HIGHLIGHTS = [
    'http://hoofoot/chelsea-barcelona',
    'http://sportyhl/marseille-monaco-2',
    'http://footyroom/swansea-arsenal'
]


INCREMENT_CLICK_COUNT = [
    ('http://footyroom/swansea-arsenal', 3),
    ('http://hoofoot/swansea-liverpool', 2),
    ('http://hoofoot/chelsea-barcelona', 1),
]


TEST_HIGHLIGHTS = [

    #1 Chelsea 0 - 2 Barcelona

    HoofootHighlight(
        'http://hoofoot/chelsea-barcelona',
        'Chelsea 0 - 2 Barcelona',
        DEFAULT_TEST_IMAGE,
        0,
        'Champions League',
        TIME_40_MINUTES_EARLIER
    ),

    HoofootHighlight(
        'http://hoofoot/chelsea-barcelona2',
        'Chelsea 0 - 2 Barcelona',
        DEFAULT_TEST_IMAGE,
        0,
        'Champions League',
        TIME_40_MINUTES_EARLIER
    ),

    HoofootHighlight(
        'http://hoofoot/chelsea-barcelona3',
        'Barcelona 2 - 0 Chelsea',
        DEFAULT_TEST_IMAGE,
        0,
        'Champions League',
        TIME_40_MINUTES_EARLIER
    ),

    #2 Burnley 0 - 2 Barcelona

    HoofootHighlight(
        'http://hoofoot/burnley-barcelona',
        'Burnley 0 - 2 Barcelona',
        DEFAULT_TEST_IMAGE,
        0,
        'Champions League',
        TIME_40_MINUTES_EARLIER
    ),

    #3 Barcelona 1 - 1 Liverpool

    HoofootHighlight(
        'http://hoofoot/barcelona-liverpool',
        'Barcelona 1 - 1 Liverpool',
        DEFAULT_TEST_IMAGE,
        0,
        'Champions League',
        TIME_NOW
    ),

    #4 Arsenal 1 - 0 Real Madrid

    HoofootHighlight(
        'http://hoofoot/chelsea-real_madrid',
        'Arsenal 1 - 0 Real Madrid',
        DEFAULT_TEST_IMAGE,
        0,
        'Champions League',
        TIME_40_MINUTES_EARLIER
    ),

    #5 Arsenal 0 - 4 Liverpool

    HoofootHighlight(
        'http://hoofoot/arsenal-liverpool',
        'Arsenal 0 - 4 Liverpool',
        DEFAULT_TEST_IMAGE,
        0,
        'Premier League',
        TIME_40_MINUTES_EARLIER
    ),

    HoofootHighlight( # Different
        'http://hoofoot/arsenal-liverpool2',
        'Liverpool 4 - 0 Arsenal',
        DEFAULT_TEST_IMAGE,
        0,
        'Premier League',
        TIME_40_MINUTES_EARLIER
    ),

    #7 Swansea 4 - 0 Arsenal

    FootyroomHighlight(
        'http://footyroom/swansea-arsenal',
        'Swansea 4 - 0 Arsenal',
        DEFAULT_TEST_IMAGE,
        0,
        'Premier League',
        str(TIME_40_MINUTES_EARLIER)
    ),

    #8 Barcelona 3 - 2 Real Madrid

    FootyroomVideoHighlight(
        'http://hoofoot/barcelona-real_madrid',
        'Barcelona 3 - 2 Real Madrid',
        DEFAULT_TEST_IMAGE,
        0,
        'La Liga',
        TIME_40_MINUTES_EARLIER,
        [
            {'team': 1, 'player': 'Lionel Messi',      'elapsed': 4,  'goal_type': 'penalty'},
            {'team': 2, 'player': 'Cristiano Ronaldo', 'elapsed': 10, 'goal_type': 'goal'},
            {'team': 1, 'player': 'Luis Suarez',       'elapsed': 43, 'goal_type': 'goal'},
            {'team': 2, 'player': 'Gerard Pique',      'elapsed': 56, 'goal_type': 'own goal'},
            {'team': 1, 'player': 'Lionel Messi',      'elapsed': 90, 'goal_type': 'goal'}
        ]
    ),

    #9 Barcelona 0 - 1 Arsenal

    FootyroomVideoHighlight(
        'http://hoofoot/barcelona-arsenal',
        'Barcelona 0 - 1 Arsenal',
        DEFAULT_TEST_IMAGE,
        0,
        'Champions League',
        TIME_40_MINUTES_EARLIER,
        [
            {'team': 2, 'player': 'Olivier Giroud', 'elapsed': 15, 'goal_type': 'goal'}
        ]
    ),

    #10 Manchester City 0 - 0 Tottenham

    FootyroomHighlight(
        'http://footyroom/manchester_city-tottenham',
        'Manchester City 0 - 0 Tottenham',
        DEFAULT_TEST_IMAGE,
        0,
        'Premier League',
        TIME_40_MINUTES_EARLIER
    ),

    FootyroomHighlight(
        'http://footyroom/manchester_city-tottenham2',
        'Manchester City 0 - 0 Tottenham',
        DEFAULT_TEST_IMAGE,
        0,
        'Premier League',
        TIME_1_DAY_EARLIER
    ),

    HoofootHighlight(
        'http://hoofoot/manchester_city-tottenham',
        'Manchester City 0 - 0 Tottenham',
        DEFAULT_TEST_IMAGE,
        0,
        'Premier League',
        TIME_40_MINUTES_EARLIER
    ),

    HoofootHighlight(
        'http://hoofoot/manchester_city-tottenham',
        'Manchester City 0 - 0 Tottenham',
        DEFAULT_TEST_IMAGE,
        0,
        'Premier League',
        TIME_40_MINUTES_EARLIER
    ),

    OurMatchHighlight(
        'http://ourmatch/manchester_city-tottenham',
        'Manchester City vs Tottenham',
        DEFAULT_TEST_IMAGE,
        0,
        'Premier League',
        TIME_40_MINUTES_EARLIER, [], 'normal'
    ).set_score(0, 0),

    #11 Marseille vs Monaco

    SportyHLHighlight(
        'http://sportyhl/marseille-monaco',
        'Marseille vs Monaco',
        DEFAULT_TEST_IMAGE,
        0,
        'Ligue 1',
        TIME_40_MINUTES_EARLIER, 'normal'
    ),

    SportyHLHighlight( # Different
        'http://sportyhl/marseille-monaco-2',
        'Marseille vs Monaco',
        DEFAULT_TEST_IMAGE,
        0,
        'Ligue 1',
        TIME_4_DAYS_EARLIER, 'normal'
    ),

    #13 Swansea 0 - 3 Barcelona

    FootyroomHighlight(
        'http://footyroom/swansea-barcelona',
        'Swansea 0 - 3 Barcelona',
        DEFAULT_TEST_IMAGE,
        0,
        'Champions League',
        TIME_4_DAYS_EARLIER
    ),

    #14 Swansea 2 - 0 Liverpool

    HoofootHighlight(
        'http://hoofoot/swansea-liverpool',
        'Swansea 2 - 0 Liverpool',
        DEFAULT_TEST_IMAGE,
        0,
        'Europa League',
        TIME_40_MINUTES_EARLIER
    ),

    #15 France 2 - 0 Belgium

    HoofootHighlight(
        'http://hoofoot/france-belgium',
        'France 2 - 0 Belgium',
        DEFAULT_TEST_IMAGE,
        0,
        'Nations League',
        TIME_40_MINUTES_EARLIER
    ),

    #16 France 2 - 0 England

    HoofootHighlight(
        'http://hoofoot/france-england',
        'France 2 - 0 England',
        DEFAULT_TEST_IMAGE,
        0,
        'Nations League',
        TIME_40_MINUTES_EARLIER
    ),

    #17 Liverpool 1 - 0 England

    FootyroomVideoHighlight(
        'http://footyroom/liverpool-england',
        'Liverpool 1 - 0 England',
        TEST_IMAGE,
        0,
        'Nations League',
        TIME_10_MINUTES_EARLIER,
        goal_data=[
            {
                'team': 1,
                'player': 'Sane',
                'elapsed': '50',
                'goal_type': 'goal'
            }
        ]
    ),

    #18 Liverpool 1 - 0 France

    FootyroomVideoHighlight(
        'http://footyroom/liverpool-france',
        'Liverpool 2 - 0 France',
        TEST_IMAGE,
        0,
        'Nations League',
        TIME_NOW,
        goal_data=[
            {
                'team': 1,
                'player': 'Salah',
                'elapsed': '90',
                'goal_type': 'goal'
            }
        ]
    ),

    #19 Belgium 1 - 0 Liverpool

    FootyroomVideoHighlight(
        'http://footyroom/belgium-liverpool',
        'Belgium 1 - 0 Liverpool',
        TEST_IMAGE,
        0,
        'Nations League',
        TIME_NOW,
        goal_data=[]
    ),

    #20 Belgium 0 - 0 England

    FootyroomVideoHighlight(
        'http://footyroom/belgium-england',
        'Belgium 0 - 0 England',
        TEST_IMAGE,
        0,
        'Nations League',
        TIME_10_MINUTES_EARLIER,
        goal_data=[]
    )
]

TEST_HIGHLIGHTS_2 = [

    # Swansea 4 - 0 Arsenal

    HoofootHighlight(
        'http://hoofoot/swansea-arsenal',
        'Arsenal 0 - 4 Swansea',
        DEFAULT_TEST_IMAGE,
        0,
        'Premier League',
        str(TIME_40_MINUTES_EARLIER)
    ),
]