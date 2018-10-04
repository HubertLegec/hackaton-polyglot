from unittest import TestCase
from levenshtein_distance import LevenshteinDistance


class LevenshteinDistanceTest(TestCase):
    cities = [
        "Warszawa",
        "Łódź"
    ]

    def test_match(self):
        lev_dist = LevenshteinDistance(self.cities)
        result = lev_dist.match('warszawa')
        assert result is not None
        assert result['word'] == 'Warszawa'

    def test_match_for_empty_dictionary(self):
        lev_dist = LevenshteinDistance([])
        result = lev_dist.match('warszawa')
        assert result is None
