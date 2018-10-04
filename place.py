from levenshtein_distance import LevenshteinDistance


class Place:
    def __init__(self, name, city, street):
        self.name = name
        self.city = city
        self.street = street

    def matches(self, tags):
        lev_dist = LevenshteinDistance(tags)
        name_match = lev_dist.match(self.name)
        street_match = lev_dist.match(self.street)
        if name_match is None and street_match is None:
            return 1
        elif name_match:
            return name_match['distance']
        elif street_match:
            return street_match['distance']
        else:
            return min(name_match['distance'], street_match['distance'])
