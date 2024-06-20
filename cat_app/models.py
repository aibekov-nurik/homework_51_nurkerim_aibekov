from random import random

from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    satiety = models.IntegerField(default=40)
    happiness = models.IntegerField(default=40)
    sleeping = models.BooleanField(default=False)

    def feed(self):
        if not self.sleeping:
            self.satiety = min(self.satiety + 15, 100)
            self.happiness = min(self.happiness + 5, 100)
            if self.satiety > 100:
                self.happiness = max(self.happiness - 30, 0)

    def play(self):
        if self.sleeping:
            self.sleeping = False
            self.happiness = max(self.happiness - 5, 0)
        else:
            self.satiety = max(self.satiety - 10, 0)
            self.happiness = min(self.happiness + 15, 100)
            if random.randint(1, 3) == 1:  # 1 in 3 chance to enrage the cat
                self.happiness = 0

    def sleep(self):
        self.sleeping = True

    def get_avatar(self):
        if self.happiness > 70:
            return "happy_cat.jpg"
        elif self.happiness > 30:
            return "neutral_cat.jpg"
        else:
            return "sad_cat.jpg"
