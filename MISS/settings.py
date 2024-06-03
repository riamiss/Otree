# models.py

from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'MISS'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    treatment = models.BooleanField()
    height_guess1 = models.IntegerField(min=100, max=220, label="Guess the height (in cm)")
    height_guess2 = models.IntegerField(min=100, max=220, label="Guess the height (in cm)")
    height_guess3 = models.IntegerField(min=100, max=220, label="Guess the height (in cm)")
    height_guess4 = models.IntegerField(min=100, max=220, label="Guess the height (in cm)")
    height_guess5 = models.IntegerField(min=100, max=220, label="Guess the height (in cm)")

def creating_session(subsession):
    for p in subsession.get_players():
        p.treatment = random.choice([False, True])

# pages.py

class Introduction(Page):
    pass

class GuessHeight1(Page):
    form_model = 'player'
    form_fields = ['height_guess1']
class GuessHeight2(Page):
    form_model = 'player'
    form_fields = ['height_guess2']
class GuessHeight3(Page):
    form_model = 'player'
    form_fields = ['height_guess3']
class GuessHeight4(Page):
    form_model = 'player'
    form_fields = ['height_guess4']
class GuessHeight5(Page):
    form_model = 'player'
    form_fields = ['height_guess5']

class NegativeReinforcement2(Page):
    def is_displayed(player: Player):
        return player.treatment1
class NegativeReinforcement3(Page):
    def is_displayed(player: Player):
        return player.treatment1
class NegativeReinforcement4(Page):
    def is_displayed(player: Player):
        return player.treatment1
class NegativeReinforcement5(Page):
    def is_displayed(player: Player):
        return player.treatment1


class PositiveReinforcement2(Page):
    def is_displayed(player: Player):
        return player.treatment2
class PositiveReinforcement3(Page):
    def is_displayed(player: Player):
        return player.treatment2
class  PositiveReinforcement4(Page):
    def is_displayed(player: Player):
        return player.treatment2
class  PositiveReinforcement5(Page):
    def is_displayed(player: Player):
        return player.treatment2

class EndPage(Page):
    pass


# sequence of pages for each round
page_sequence = [
    Introduction,
    GuessHeight1,
    NegativeReinforcement2,
    GuessHeight2,
    NegativeReinforcement3,
    GuessHeight3,
    NegativeReinforcement4,
    GuessHeight4,
    NegativeReinforcement5,
    GuessHeight5,
    EndPage
]

