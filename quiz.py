import datetime
import os
import random

from players import Player
from questions import Add, Subtract, Multiply, Divide


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class Quiz:
    add_span = (1, 50)
    subtract_span = (1, 100)
    multiply_span = (2, 10)
    divide1_span = (10, 100)
    divide2_span = (2, 9)
    rounds = 0
    all_players = []

    def __init__(self):
        clear()
        self.players = self.get_players()
        self.length = self.get_length()
        self.round_limit = self.get_round_limit()

    def get_players(self):
        all_players = []
        while True:
            try:
                num_players = int(input("Kolik je hráčů? "))
                if num_players < 1:
                    raise ValueError()
            except ValueError:
                print("Zadej celé číslo, nejméně 1.")
            else:
                break
        for order in range(1, num_players + 1):
            while True:
                try:
                    name = input("Jméno {}. hráče: ".format(order))
                    if not name:
                        raise ValueError("Napiš jméno hráče.")
                    for player in all_players:
                        if str(player) == name:
                            raise ValueError("{} už hraje, zvol jiné jméno.".format(name))
                except ValueError as err:
                    print("{}".format(err))
                else:
                    all_players.append(Player(order, name))
                    break
        return all_players

    def get_length(self):
        while True:
            try:
                num_lines = int(input("Počet příkladů za kolo: "))
                if num_lines < 1:
                    raise ValueError()
            except ValueError:
                print("Zadej celé číslo, nejméně 1.")
            else:
                break
        return num_lines

    def get_round_limit(self):
        while True:
            try:
                num_rounds = int(input("Počet kol: "))
                if num_rounds < 1:
                    raise ValueError()
            except ValueError:
                print("Zadej celé číslo, nejméně 1.")
            else:
                break
        return num_rounds

    def get_questions(self):
        questions = []
        question_count = 0
        while question_count < self.length:
            question_types = (Add, Subtract, Multiply, Divide)
            question_type = random.choice(question_types)
            if question_type == Add:
                num1 = random.randint(self.add_span[0], self.add_span[1])
                num2 = random.randint(self.add_span[0], self.add_span[1])
            elif question_type == Subtract:
                number1 = random.randint(self.subtract_span[0], self.subtract_span[1])
                number2 = random.randint(self.subtract_span[0], self.subtract_span[1])
                num1 = max(number1, number2)
                num2 = min(number1, number2)
            elif question_type == Multiply:
                num1 = random.randint(self.multiply_span[0], self.multiply_span[1])
                num2 = random.randint(self.multiply_span[0], self.multiply_span[1])
            elif question_type == Divide:
                num1 = random.randint(self.divide1_span[0], self.divide1_span[1])
                num2 = random.randint(self.divide2_span[0], self.divide2_span[1])
            question = question_type(num1, num2)
            if question not in questions:
                questions.append(question)
                question_count += 1
        return questions

    def take_quiz(self):
        clear()
        next = input("Na řadě je {}. Začni stisknutím ENTER.".format(str(self.players[0])))
        while self.rounds < self.round_limit:
            self.play_round()
        else:
            self.summary()

    def play_round(self):
        clear()
        for player in self.players:
            self.get_questions()
            for question in self.get_questions():
                self.ask(question, player)
            self.next_turn(player)

    def next_turn(self, player):
        if not player == self.players[-1]:
            clear()
            next = input(
                "Na řadě je {}. Začni stisknutím ENTER.".format(str(self.players[self.players.index(player) + 1])))
        else:
            self.rounds += 1
            clear()
            if self.rounds < self.round_limit:
                self.round_summary()
                next = input("Na řadě je {}. Začni stisknutím ENTER.".format(str(self.players[0])))

    def ask(self, question, player):
        question_start = datetime.datetime.now()
        correct = False
        while correct == False:
            answer = input(question.text + " = ")
            if answer == str(question.answer):
                correct = True
            else:
                print("Špatně!")
        question_end = datetime.datetime.now()
        if str(question) == "Add":
            player.add_times.append((question_end - question_start).total_seconds())
        elif str(question) == "Subtract":
            player.subtract_times.append((question_end - question_start).total_seconds())
        elif str(question) == "Multiply":
            player.multiply_times.append((question_end - question_start).total_seconds())
        elif str(question) == "Divide":
            player.divide_times.append((question_end - question_start).total_seconds())

    def get_position(self, position):
        sorted_players = self.players[:]
        sorted_players.sort()
        return str(sorted_players[position])

    def round_summary(self):
        clear()
        print("Mezisoučet:")
        for player in self.players:
            print("{}: {} sekund".format(player.name, round(player.count_times(), 2)))
        if len(self.players) > 1:
            print("\n{} musí zabrat!\n".format(self.get_position(-1)))

    def summary(self):
        clear()
        for player in self.players:
            if player.add_times:
                add_average = round(sum(player.add_times) / len(player.add_times), 2)
            else:
                add_average = "N/A"
            if player.subtract_times:
                subtract_average = round(sum(player.subtract_times) / len(player.subtract_times), 2)
            else:
                subtract_average = "N/A"
            if player.multiply_times:
                multiply_average = round(sum(player.multiply_times) / len(player.multiply_times), 2)
            else:
                multiply_average = "N/A"
            if player.divide_times:
                divide_average = round(sum(player.divide_times) / len(player.divide_times), 2)
            else:
                divide_average = "N/A"
            print(
                "<-------- {} -------->\nCelkový čas: {} sekund.\nPrůměrné časy odpovědí:\nSčítání: {} s\nOdčítání: {} s\nNásobení: {} s\nDělení: {} s\n".format(
                    player.name, round(player.count_times(), 2), add_average, subtract_average, multiply_average,
                    divide_average))
        if len(self.players) > 1:
            print("Vítězem je {}!".format(self.get_position(0)))
        replay = input('\nZadej "o" pro odvetu, "k" pro konec nebo stiskni ENTER pro nastavení nové hry.').lower()
        if replay == "o":
            self.rounds = 0
            for player in self.players:
                player.add_times = []
                player.subtract_times = []
                player.multiply_times = []
                player.divide_times = []
            self.take_quiz()
        elif replay == "k":
            exit()
        else:
            Quiz().take_quiz()


Quiz().take_quiz()
