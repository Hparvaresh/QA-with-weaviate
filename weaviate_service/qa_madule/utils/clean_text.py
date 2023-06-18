from hazm import Normalizer

class CleanText():
    def __init__(self):
        self.normalizer = Normalizer()


    def clean_text(self, text):
        return self.normalizer.normalize(text)