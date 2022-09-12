from .customer import Customer
from .trainer import Trainer
from .equipment import Equipment
from .exercise_plan import ExercisePlan
from .subscription import Subscription


class Gym:
    def __init__(self, ):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def __add_item(given_item, given_sequence):
        if given_item in given_sequence:
            return
        given_sequence.append(given_item)

    def add_customer(self, customer: Customer):
        self.__add_item(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.__add_item(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.__add_item(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_item(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.__add_item(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):
        subscription = self.__find_by_id(self.subscriptions, subscription_id)
        customer = self.__find_by_id(self.customers, subscription.customer_id)
        trainer = self.__find_by_id(self.trainers, subscription.trainer_id)
        exercise_plan = self.__find_by_id(self.plans, subscription.exercise_id)
        equipment = self.__find_by_id(self.equipment, exercise_plan.equipment_id)

        return repr(subscription) + '\n' + \
               repr(customer) + '\n' + \
               repr(trainer) + '\n' + \
               repr(equipment) + '\n' + \
               repr(exercise_plan)

    @staticmethod
    def __find_by_id(entities, entity_id):
        for entity in entities:
            if entity.id == entity_id:
                return entity