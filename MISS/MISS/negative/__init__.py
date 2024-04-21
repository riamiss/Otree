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
    treatment = models.StringField(choices=['Control', 'Treatment1', 'Treatment2'])
    height_guess1 = models.IntegerField(min=100, max=220, label="Guess the height (in cm)")
    height_guess2 = models.IntegerField(min=100, max=220, label="Guess the height (in cm)")
    height_guess3 = models.IntegerField(min=100, max=220, label="Guess the height (in cm)")
    height_guess4 = models.IntegerField(min=100, max=220, label="Guess the height (in cm)")
    height_guess5 = models.IntegerField(min=100, max=220, label="Guess the height (in cm)")
    height_guess6 = models.IntegerField(min=100, max=220, label="Guess the height (in cm)")
    # Add the reinforcement_type field
    reinforcement_type = models.StringField(choices=['Negative', 'Positive', 'None'])

def creating_session(subsession):
    players = subsession.get_players()
    num_players = len(players)
    treatments = ['Control', 'Negative', 'Positive']

    for i, player in enumerate(players):
        # Calculate the index within the treatments list
        treatment_index = i % 3
        # Assign treatment and reinforcement type based on the index
        player.treatment = treatments[treatment_index]
        if treatment_index == 0:
            player.reinforcement_type = 'None'
        elif treatment_index == 1:
            player.reinforcement_type = 'Negative'
        else:
            player.reinforcement_type = 'Positive'

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

class GuessHeight6(Page):
    form_model = 'player'
    form_fields = ['height_guess6']

class NegativeReinforcement2(Page):
    def is_displayed(player: Player):
        return player.reinforcement_type == 'Negative'

class NegativeReinforcement3(Page):
    def is_displayed(player: Player):
        return player.reinforcement_type == 'Negative'

class NegativeReinforcement4(Page):
    def is_displayed(player: Player):
        return player.reinforcement_type == 'Negative'

class NegativeReinforcement5(Page):
    def is_displayed(player: Player):
        return player.reinforcement_type == 'Negative'

class NegativeReinforcement6(Page):
    def is_displayed(player: Player):
        return player.reinforcement_type == 'Negative'

class PositiveReinforcement2(Page):
    def is_displayed(player: Player):
        return player.reinforcement_type == 'Positive'

class PositiveReinforcement3(Page):
    def is_displayed(player: Player):
        return player.reinforcement_type == 'Positive'

class PositiveReinforcement4(Page):
    def is_displayed(player: Player):
        return player.reinforcement_type == 'Positive'

class PositiveReinforcement5(Page):
    def is_displayed(player: Player):
        return player.reinforcement_type == 'Positive'

class PositiveReinforcement6(Page):
    def is_displayed(player: Player):
        return player.reinforcement_type == 'Positive'

class EndPage(Page):
    pass

# sequence of pages for each round
page_sequence = [
    Introduction,
    GuessHeight1,
    NegativeReinforcement2,
    PositiveReinforcement2,
    GuessHeight2,
    NegativeReinforcement3,
    PositiveReinforcement3,
    GuessHeight3,
    NegativeReinforcement4,
    PositiveReinforcement4,
    GuessHeight4,
    NegativeReinforcement5,
    PositiveReinforcement5,
    GuessHeight5,
    NegativeReinforcement6,
    PositiveReinforcement6,
    GuessHeight6,
    EndPage
]
