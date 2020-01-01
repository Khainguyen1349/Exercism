class Allergies:

    def __init__(self, score):
        all = ['eggs', 'peanuts', 'shellfish', 'strawberries',
               'tomatoes', 'chocolate', 'pollen', 'cats']
        self.allergies = [all[i] for i in range(8) if score & 2**i]

    def allergic_to(self, item):
        return item in self.allergies

    @property
    def lst(self):
        return list(self.allergies)
