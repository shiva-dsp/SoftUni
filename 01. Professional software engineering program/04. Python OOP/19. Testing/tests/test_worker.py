from unittest import TestCase

from apps.worker import Worker

'''
•	Test if the worker is initialized with the correct name, salary, and energy
•	Test if the worker's energy is incremented after the rest method is called
•	Test if an error is raised if the worker tries to work with negative energy or equal to 0
•	Test if the worker's money is increased by his salary correctly after the work method is called
•	Test if the worker's energy is decreased after the work method is called	
•	Test if the get_info method returns the proper string with correct values
'''


class WorkerTests(TestCase):
    NAME = 'Test Worker'
    SALARY = 1024
    ENERGY = 1

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)


    def test__init__when_valid_props__expect_correct_values(self):
        pass

    def test__rest__expect_energy_to_be_incremented(self):
        pass

    def test__work__when_energy_is_0_expect_to_be_raise(self):
        pass

    def test__work__when_enough_energy__expect_money_to_be_increased_by_salary(self):
        pass

    def test__work__when_enough_energy__expect_energy_to_decrement(self):
        pass

    def test__get_info__expect_corect_result(self):
        pass