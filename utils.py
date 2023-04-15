class Util:

    def __init__(self, pets):
        self.pets = pets

    def get_pets_names(self):
        pets_names = []
        for pet in self.pets:
            pets_names.append(pet.get_name())
        return pets_names

    def count_pets_names(self):
        pets_counter = {}
        pets_names = self.get_pets_names()
        for pet in self.pets:
            counter = 1
            for name in pets_names:
                if pet.get_name == name:
                    counter += 1
            pets_counter[pet.get_name()] = counter
        return pets_counter
