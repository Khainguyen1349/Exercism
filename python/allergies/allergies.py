class Allergies:

    def __init__(self, score):
        dict = {}
        self.allergies = []

    def allergic_to(self, item):
        return item in self.allergies

    @property
    def lst(self):
        list(self.allergies)
