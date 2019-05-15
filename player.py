import datetime

class Player:
    def __init__(self):
        self.gold = 0
        self.activities = []
    
    def update_gold(self, profit):
        self.gold += profit
        return self

    def log_activity(self, event):
        self.activities.append(event + datetime.datetime.now().strftime(" (%Y-%b-%d %H:%M:%S)"))
        return self
