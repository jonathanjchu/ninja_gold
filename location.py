import random

class Location:
    def __init__(self, name, min_gold, max_gold, fail_chance, min_level, success_msg, fail_msg):
        self.name = name
        self.min_gold = min_gold
        self.max_gold = max_gold
        self.fail_chance = fail_chance
        self.min_level = min_level
        self.success_msg = success_msg
        self.fail_msg = fail_msg
    
    def dig_gold(self):
        rnd = random.random()
        result = GoldDigResult()

        if rnd < self.fail_chance:
            result.is_success = False
            result.output = self.fail_msg
        else:
            result.income = random.randint(self.min_gold, self.max_gold)
            result.output = self.success_msg
        return result


class NinjaGold():
    def __init__(self):
        self.data = []
        self.data.append(Location("farm", 10, 20, 0, 0, "farming", ""))
        self.data.append(Location("cave", 5, 10, 0.01, 0, "exploring cave", "injured in cave, paid {} to doctor"))
        self.data.append(Location("house", 40, 80, 0.4, 0, "breaking and entering into house", "busted by police, paid {} to bribe police"))
        self.data.append(Location("casino", -50, 50, 0, 0, "gambling at casino", ""))
        self.data.append(Location("bank", 100, 800, 0.8, 5, "robbing bank", "gunned down by police, paid {} to bribe police and pay hospital bills"))

class GoldDigResult():
    def __init__(self, is_success=True, income=0, output=""):
        self.is_success = is_success
        self.income = income
        self.output = output
    

