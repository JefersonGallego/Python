

class Animals:

    def __init__(self,animal):
        self.animal = animal
    
    def feeding(self):
        print(f'The {self.animal} is eating')

class Carnivorous(Animals):

    def __init__(self,carnivorus_animal):
        super().__init__(carnivorus_animal)
    
    def feeding(self):
        print(f'The {self.animal} is eating meat')


if __name__=='__main__':
    
    animal= Animals('Deer')
    animal.feeding()

    lion=Carnivorous('Lion')
    lion.feeding()
