class Birds:
    def move(self):
        print("Birds is Flying!")

class Fishes:
    def move(self):
        print("Fish is Swimming!")

def make_move(animal):
    animal.move()

bird = Birds()
fish = Fishes()

make_move(bird)
make_move(fish)
