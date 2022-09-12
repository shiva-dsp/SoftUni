from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = ['Appaloosa', 'Thoroughbred']
    VALID_RACE_TYPES = ["Winter", "Spring", "Autumn", "Summer"]

    def __init__(self, horses: list, jockeys: list, horse_races: list):
        self.horses = horses
        self.jockeys = jockeys
        self.horse_races = horse_races

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        global curr_horse
        if horse_type in self.VALID_HORSE_TYPES:
            for horse in self.horses:
                if horse.name == horse_name:
                    raise Exception(f'Horse {horse_name} has been already added!')
            if horse_type == 'Appaloosa':
                curr_horse = Appaloosa(horse_name, horse_speed)
                curr_horse.is_taken = True
            if horse_type == 'Thoroughbred':
                curr_horse = Thoroughbred(horse_name, horse_speed)
                curr_horse.is_taken = True
            self.horses.append(curr_horse)
            return f'{horse_type} horse {horse_name} is added.'

    def add_jockey(self, jockey_name: str, age: int):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f'Jockey {jockey_name} has been already added!')
            curr_jockey = Jockey(jockey_name, age)
            self.jockeys.append(curr_jockey)
            return f'Jockey {jockey_name} is added.'

    def create_horse_race(self, race_type: str):
        if race_type in self.VALID_RACE_TYPES:
            for race in self.horse_races:
                if race.race_type == race_type:
                    raise Exception(f'Race {race_type} has been already created!')
            curr_race = HorseRace(race_type, [])
            self.horse_races.append(curr_race)
            return f'Race {race_type} is created.'

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                break
        else:
            raise Exception(f'Jockey {jockey_name} could not be found!')

        for horse in self.horses:
            if horse.__class__.__name__ == horse_type:
                if horse.is_taken is False:
                    horse.is_taken = True


    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        pass

    def start_horse_race(self, race_type: str):
        pass