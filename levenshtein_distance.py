import distance


class LevenshteinDistance:
    def __init__(self, dictionary):
        self._dictionary = dictionary

    def match(self, word, threshold=0.75):
        distances = [{'word': entry, 'distance': self.distance(word, entry)} for entry in self._dictionary]
        filtered_distances = [dist for dist in distances if dist['distance'] < threshold]
        if len(filtered_distances) > 0:
            return min(filtered_distances, key=lambda d: d['distance'])
        return None

    def distance(self, word1, word2):
        return distance.nlevenshtein(word1.lower(), word2.lower(), method=1)
