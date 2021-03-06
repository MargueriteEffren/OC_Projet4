from view import ROUNDS_NUMBER


class Tournament:
    """Stocke les données du tournoi du jour"""

    def __init__(self, tournament_name, location, date, rondes,
                 tournament_notes, players, rounds_number=ROUNDS_NUMBER):
        self.tournament_name = tournament_name
        self.location = location
        self.date = date
        self.rondes = rondes
        self.tournament_notes = tournament_notes
        self.players = players
        self.rounds_number = rounds_number


class Player:
    """Stocke les données d'un joueur"""

    def __init__(self, fullname_player, birth_date, gender, ranking):
        self.fullname_player = fullname_player
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking


class Ronde:
    """stocke les données d'une ronde"""

    def __init__(self, list_of_matchs, round_name, round_number,
                 start_date_time, end_time):
        self.round_name = round_name
        self.round_number = round_number
        self.start_date_time = start_date_time
        self.list_of_matchs = list_of_matchs
        self.end_time = end_time
