from polyglot.text import Text


class TextContext:
    def __init__(self, text):
        self._polyglotText = Text(text, hint_language_code='pl')
        self.entities = self._polyglotText.entities

    def people(self):
        return [entity for entity in self.entities if entity.tag == 'I-PER']

    def locations(self):
        return [entity for entity in self.entities if entity.tag == 'I-LOC']

    def people_text(self):
        return [p._collection for p in self.people()]

    def locations_text(self):
        return [p._collection for p in self.locations()]

    def words(self):
        return [word for word in self._polyglotText.words if len(word) > 2]

    def words_without(self, to_remove):
        return [word for word in self.words() if word not in to_remove]
