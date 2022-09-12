from .animal import Animal
from .worker import Worker
from .lion import Lion
from .tiger import Tiger
from .cheetah import Cheetah
from .keeper import Keeper
from .caretaker import Caretaker
from .vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if self.__animal_capacity == len(self.animals):
            return 'Not enough space for animal'
        if self.__budget < price:
            return 'Not enough budget'
        self.animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return 'Not enough space for worker'
        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        needed_money = sum(worker.salary for worker in self.workers)
        # needed_money = 0
        # for worker in self.workers:
        #     needed_money += worker.salary
        if needed_money > self.__budget:
            return 'You have no budget to pay your workers. They are unhappy'
        self.__budget = self.__budget - needed_money
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self):
        needed_money_for_care = sum(animal.money_for_care for animal in self.animals)
        if needed_money_for_care > self.__budget:
            return f'You have no budget to tend the animals. They are unhappy.'
        self.__budget -= needed_money_for_care
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'
        lions = [repr(animal) for animal in self.animals if isinstance(animal, Lion)]
        result += f'----- {len(lions)} Lions:\n' + '\n'.join(lions) + '\n'
        # result += f'----- {len(lions)} Lions:\n'
        # for lion in lions:
        #     result += f'{lion}\n'
        tigers = [repr(animal) for animal in self.animals if isinstance(animal, Tiger)]
        result += f'----- {len(tigers)} Tigers:\n' + '\n'.join(tigers) + '\n'

        cheetahs = [repr(animal) for animal in self.animals if isinstance(animal, Cheetah)]
        result += f'----- {len(cheetahs)} Cheetahs:\n' + '\n'.join(cheetahs)

        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'

        keepers = [repr(keeper) for keeper in self.workers if isinstance(keeper, Keeper)]
        result += f'----- {len(keepers)} Keepers:\n' + '\n'.join(keepers) + '\n'

        caretakers = [repr(caretaker) for caretaker in self.workers if isinstance(caretaker, Caretaker)]
        result += f'----- {len(caretakers)} Caretakers:\n' + '\n'.join(caretakers) + '\n'

        vets = [repr(vet) for vet in self.workers if isinstance(vet, Vet)]
        result += f'----- {len(vets)} Vets:\n' + '\n'.join(vets)

        return result