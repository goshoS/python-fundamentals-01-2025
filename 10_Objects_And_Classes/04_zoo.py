class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f" Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            result += f" Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            result += f" Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"

        return result


zoo_name = input()
zoo = Zoo(zoo_name)
iterations = int(input())

for _ in range(iterations):
    animal_info = input().split()
    animal_species = animal_info[0]
    animal_name = animal_info[1]
    zoo.add_animal(animal_species, animal_name)

species_info = input()
print(zoo.get_info(species_info))
