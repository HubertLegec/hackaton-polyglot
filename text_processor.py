from flask_restful import Resource
from flask import request, jsonify
from levenshtein_distance import LevenshteinDistance
from place import Place
from text_context import TextContext


class TextProcessor(Resource):
    cities = [
        "Warszawa",
        "Łódź"
    ]

    places = [
        Place("C.H.Manufaktura", cities[1], 'Karskiego 5'),
        Place("Puławska", cities[0], 'Puławska 12a'),
        Place("Galeria Mokotów", cities[0], 'Wołoska 12'),
        Place("Galeria Łódzka", cities[1], "Piłsudskiego 15/23")
    ]

    lev_distance = LevenshteinDistance(cities)

    def post(self):
        polyglotText = TextContext(request.json['text'])
        print('Entities: ', polyglotText.entities)
        print('Persons: ', polyglotText.people())
        print('Locations: ', polyglotText.locations())
        places = self.find_places(polyglotText)
        print('Places: ', places)
        result = {
            'people': [person._collection for person in polyglotText.people()],
            'places': [p.__dict__ for p in places],
            'service': '',
            'message': 'hello'
        }
        return jsonify(result)

    def find_places(self, text_context):
        location_names = [location[0] for location in text_context.locations()]
        city = self.find_city(location_names)
        places = [p for p in self.places if p.city == city['city']]
        to_remove = [city['location']] + [y for x in text_context.people() for y in x]
        words_to_check = text_context.words_without(to_remove)
        return self.filter_places(places, words_to_check)

    def find_city(self, location_names):
        distances = [{'distance': self.lev_distance.match(location_name), 'location': location_name} for location_name in location_names]
        valid_distances = [dist for dist in distances if dist['distance'] is not None]
        if len(valid_distances) < 1:
            return None
        min_distance = min(valid_distances, key=lambda d: d['distance']['distance'])
        if min_distance is not None:
            return {'city': min_distance['distance']['word'], 'location': min_distance['location']}
        else:
            return None

    def filter_places(self, places, tags):
        place_matches = [{'place': p, 'match': p.matches(tags)} for p in places]
        place_matches.sort(key=lambda p: p['match'])
        return [p['place'] for p in place_matches if p['match'] < 0.75]




