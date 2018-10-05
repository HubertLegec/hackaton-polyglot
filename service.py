from levenshtein_distance import LevenshteinDistance


class Service:
    def __init__(self, name):
        self.name = name

    def matches(self, tags):
        lev_dist = LevenshteinDistance(tags)
        words = self.name.split(' ')
        matches = [lev_dist.match(w) for w in words]
        filtered_matches = [m['distance'] for m in matches if m is not None]
        if len(filtered_matches) == 0:
            return 1
        average_match = sum(filtered_matches) / float(len(matches))
        return average_match
