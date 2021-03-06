from django.test import TestCase, Client

from fb_bot import scheduler_tasks
from fb_bot.model_managers import latest_highlight_manager
from fb_highlights.tests.utils import helper
from fb_highlights.tests.utils.helper import TEST_USER_ID
from highlights import settings


class FetcherTestCase(TestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls):
        super(FetcherTestCase, cls).setUpClass()
        helper.class_setup()

        helper.init_db(TEST_USER_ID)
        scheduler_tasks.fetch_highlights('test_batch_1')
        helper.set_up_db()
        scheduler_tasks.fetch_highlights('test_batch_2')

    def setUp(self):
        self.client = Client()
        helper.set_up(TEST_USER_ID)

    def test_highlight_inverted_home_and_away_teams_inserted_swapped_if_more_than_1_matches_different(self):
        # Then
        highlight = latest_highlight_manager.get_highlight('http://hoofoot/chelsea-barcelona')

        self.assertEqual(highlight.team1.name, 'chelsea')
        self.assertEqual(highlight.score1, 0)
        self.assertEqual(highlight.team2.name, 'barcelona')
        self.assertEqual(highlight.score2, 2)

    def test_highlight_inverted_home_and_away_teams_inserted_not_swapped_if_only_one_other_match(self):
        # Then
        highlight = latest_highlight_manager.get_highlight('http://hoofoot/arsenal-liverpool2')

        self.assertEqual(highlight.team1.name, 'liverpool')
        self.assertEqual(highlight.score1, 4)
        self.assertEqual(highlight.team2.name, 'arsenal')
        self.assertEqual(highlight.score2, 0)

    def test_highlight_inverted_home_and_away_teams_inserted_swapped_if_already_sent_highlight(self):
        # Then
        highlight = latest_highlight_manager.get_highlight('http://hoofoot/swansea-arsenal')

        self.assertEqual(highlight.team1.name, 'swansea')
        self.assertEqual(highlight.score1, 4)
        self.assertEqual(highlight.team2.name, 'arsenal')
        self.assertEqual(highlight.score2, 0)

    def test_match_time_is_set_to_match_time_of_oldest_match_when_links_are_for_same_match(self):
        # Then
        h = latest_highlight_manager.get_highlight('http://footyroom/manchester_city-tottenham')
        ref_h = latest_highlight_manager.get_highlight('http://footyroom/manchester_city-tottenham2')

        self.assertNotEqual(h.time_since_added, ref_h.time_since_added)
        self.assertEqual(h.match_time, ref_h.match_time)

    def test_ids_are_added_incrementally(self):
        # Then
        h = latest_highlight_manager.get_highlight('http://footyroom/manchester_city-tottenham')

        self.assertEqual(h.id, 10)

    def test_default_image_url_is_replaced_by_website_logo(self):
        # Then
        h = latest_highlight_manager.get_highlight('http://hoofoot/france-england')

        self.assertEqual(h.img_link, settings.STATIC_URL + "img/logo.png")