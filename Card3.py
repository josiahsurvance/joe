import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
players = 2
check = 1
wow = "13"
round = 1
names = ""
reset = 1
p1s = ["0"]
p2s = ["0"]
p3s = ["0"]
p4s = ["0"]
p5s = ["0"]
p6s = ["0"]
p7s = ["0"]
p8s = ["0"]
p9s = ["0"]
p10s = ["0"]
p11s = ["0"]
p12s = ["0"]

class MainWindow(Screen):
    def check_check(self):
        global players
        global check
        if check == 1:
            self.ids.resume.text = "Resume Game"
        elif check == 2:
            self.ids.resume.text = " Resume Game "
        elif check == 3:
            self.ids.resume.text = "  Resume Game  "
        elif check == 4:
            self.ids.resume.text = "   Resume Game   "
        elif check == 5:
            self.ids.resume.text = "    Resume Game    "
        elif check == 6:
            self.ids.resume.text = "     Resume Game     "
        elif check == 7:
            self.ids.resume.text = "      Resume Game      "
        elif check == 8:
            self.ids.resume.text = "       Resume Game       "
        elif check == 9:
            self.ids.resume.text = "        Resume Game        "
        elif check == 10:
            self.ids.resume.text = "         Resume Game         "
        elif check == 11:
            self.ids.resume.text = "          Resume Game          "
        elif check == 12:
            self.ids.resume.text = "           Resume Game           "

class WhichScoreWindow(Screen):
    pass

class ScoreWindow(Screen):
    def create_new_number(self, x):
        global wow
        wow = x
    def change_text1(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c1.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c1.text = wow
    def change_text2(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c2.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c2.text = wow
    def change_text3(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c3.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c3.text = wow
    def change_text4(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c4.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c4.text = wow
    def change_text5(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c5.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c5.text = wow
    def change_text6(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c6.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c6.text = wow
    def change_text7(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c7.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c7.text = wow
    def change_text8(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c8.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c8.text = wow
    def change_text9(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c9.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c9.text = wow
    def change_text10(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c10.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c10.text = wow
    def change_text11(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c11.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c11.text = wow
    def change_text12(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c12.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c12.text = wow
    def get_score(self, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12):
        score = 0  # Score starts at 0
        cards = []

        cardlist = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12]
        for n in list(range(12)):
            if cardlist[n] == 'Skip\n-Bo':
                cardlist[n] = '0'
            elif cardlist[n] == "":
                popupWindow = Popup(title="Error", title_align='center', size_hint=(0.8, 0.2), size=(400, 400),
                                    content=Label(text='Not all entries are filled.\nPlease fill in each entry.'))
                popupWindow.open()
                return
            cards.append(int(cardlist[n]))

        for n in list(range(12)):
            if cards[n] == 0:
                score -= 3

        top_row = cards[0:6]
        bottom_row = cards[6:12]

        # This sequence determines a vertical set's point value
        for n in list(range(6)):
            if top_row[n] != bottom_row[n]:
                if top_row[n] == 7 or top_row[n] == 11:
                    if bottom_row[n] != 7 and bottom_row[n] != 11:
                        score += int(bottom_row[n])
                elif bottom_row[n] == 7 or bottom_row[n] == 11:
                    if top_row[n] != 7 and top_row[n] != 11:
                        score += int(top_row[n])
                else:
                    score += int(top_row[n]) + int(bottom_row[n])

        # This sequence subtracts from score if numbers in 2x2 squares equal each other
        for n in list(range(5)):
            if top_row[n] == top_row[n + 1] and top_row[n] == bottom_row[n] and top_row[n + 1] == bottom_row[n + 1]:
                score -= 20

        # This sequence subtracts from score if 2x3 rectangles equal each other
        for n in list(range(4)):
            if top_row[n] == top_row[n + 1] and top_row[n + 1] == top_row[n + 2] and top_row[n] == bottom_row[n] and \
                    top_row[n + 1] == bottom_row[n + 1] and top_row[n + 2] == bottom_row[n + 2]:
                score += 10
        popupWindow = Popup(title='Score = ' + str(score), title_align='center', size_hint=(0.8, 0.1), size=(400, 400))
        popupWindow.open()
    def get_help(self):
        popupWindow = Popup(title="Help", title_align='center', size_hint=(0.8, 0.2), size=(400, 400),
                            content=Label(text="Lol you can't figure it out? Idiot."))
        popupWindow.open()
    def check_check(self):
        if check == 1:
            self.ids.gotogame.text = "Game"
        elif check == 2:
            self.ids.gotogame.text = " Game "
        elif check == 3:
            self.ids.gotogame.text = "  Game  "
        elif check == 4:
            self.ids.gotogame.text = "   Game   "
        elif check == 5:
            self.ids.gotogame.text = "    Game    "
        elif check == 6:
            self.ids.gotogame.text = "     Game     "
        elif check == 7:
            self.ids.gotogame.text = "      Game      "
        elif check == 8:
            self.ids.gotogame.text = "       Game       "
        elif check == 9:
            self.ids.gotogame.text = "        Game        "
        elif check == 10:
            self.ids.gotogame.text = "         Game         "
        elif check == 11:
            self.ids.gotogame.text = "          Game          "
        elif check == 12:
            self.ids.gotogame.text = "           Game           "

class Score2Window(Screen):
    def create_new_number(self, x):
        global wow
        wow = x
    def change_text1(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c1.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c1.text = wow
    def change_text2(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c2.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c2.text = wow
    def change_text3(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c3.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c3.text = wow
    def change_text4(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c4.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c4.text = wow
    def change_text5(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c5.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c5.text = wow
    def change_text6(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c6.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c6.text = wow
    def change_text7(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c7.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c7.text = wow
    def change_text8(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c8.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c8.text = wow
    def change_text9(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c9.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c9.text = wow
    def change_text10(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c10.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c10.text = wow
    def change_text11(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c11.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c11.text = wow
    def change_text12(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c12.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c12.text = wow
    def change_text13(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c13.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c13.text = wow
    def change_text14(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c14.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c14.text = wow
    def change_text15(self):
        global wow
        if wow == "Skip-Bo":
            self.ids.c15.text = "Skip\n-Bo"
        elif int(wow) < 13:
            self.ids.c15.text = wow
    def get_score(self, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15):
        score = 0  # Score starts at 0
        cards = []

        cardlist = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15]
        for n in list(range(15)):
            if cardlist[n] == 'Skip\n-Bo':
                cardlist[n] = '0'
            elif cardlist[n] == "":
                popupWindow = Popup(title="Error", title_align='center', size_hint=(0.8, 0.2), size=(400, 400),
                                    content=Label(text='Not all entries are filled.\nPlease fill in each entry.'))
                popupWindow.open()
                return
            cards.append(int(cardlist[n]))

        for n in list(range(15)):
            if cards[n] == 0:
                score -= 3

        top_row = cards[0:5]
        middle_row = cards[5:10]
        bottom_row = cards[10:15]
        # This sequence subtracts from score if numbers in 2x2 squares = each other and determines vertical set's value
        for n in list(range(4)):
            if top_row[n] == top_row[n + 1] and top_row[n] == middle_row[n] and top_row[n + 1] == middle_row[n + 1]:
                score -= 20
                if bottom_row[n] != middle_row[n]:
                    if bottom_row[n] != 7 and bottom_row[n] != 11:
                        score += int(bottom_row[n])
                if bottom_row[n+1] != middle_row[n]:
                    if bottom_row[n+1] != 7 and bottom_row[n+1] != 11:
                        score += int(bottom_row[n+1])
            elif middle_row[n] == middle_row[n + 1] and middle_row[n] == bottom_row[n] and middle_row[n + 1] == bottom_row[n + 1]:
                score -= 20
                if top_row[n] != middle_row[n]:
                    if top_row[n] != 7 and top_row[n] != 11:
                        score += int(top_row[n])
                if top_row[n+1] != middle_row[n]:
                    if top_row[n+1] != 7 and top_row[n+1] != 11:
                        score += int(top_row[n+1])
            else:
                if n == 0:
                    if top_row[n] != middle_row[n] or top_row[n] != bottom_row[n] or middle_row[n] != bottom_row[n]:
                        if top_row[n] == 7 or top_row[n] == 11:
                            top_row[n] = 0
                        if middle_row[n] == 7 or middle_row[n] == 11:
                            middle_row[n] = 0
                        if bottom_row[n] == 7 or bottom_row[n] == 11:
                            bottom_row[n] = 0
                        score += int(top_row[n]) + int(middle_row[n]) + int(bottom_row[n])
                else:
                    if top_row[n] == top_row[n-1] and top_row[n] == middle_row[n] and top_row[n-1] == middle_row[n-1]:
                        if n == 3:
                            if top_row[n+1] != middle_row[n+1] or top_row[n+1] != bottom_row[n+1] or middle_row[n+1] != bottom_row[n+1]:
                                if top_row[n+1] == 7 or top_row[n+1] == 11:
                                    top_row[n+1] = 0
                                if middle_row[n+1] == 7 or middle_row[n+1] == 11:
                                    middle_row[n+1] = 0
                                if bottom_row[n+1] == 7 or bottom_row[n+1] == 11:
                                    bottom_row[n+1] = 0
                                score += int(top_row[n+1]) + int(middle_row[n+1]) + int(bottom_row[n+1])
                    elif middle_row[n] == middle_row[n-1] and middle_row[n] == bottom_row[n] and middle_row[n-1] == bottom_row[n-1]:
                        if n == 3:
                            if top_row[n + 1] != middle_row[n + 1] or top_row[n + 1] != bottom_row[n + 1] or middle_row[n + 1] != bottom_row[n + 1]:
                                if top_row[n+1] == 7 or top_row[n+1] == 11:
                                    top_row[n+1] = 0
                                if middle_row[n+1] == 7 or middle_row[n+1] == 11:
                                    middle_row[n+1] = 0
                                if bottom_row[n+1] == 7 or bottom_row[n+1] == 11:
                                    bottom_row[n+1] = 0
                                score += int(top_row[n+1]) + int(middle_row[n+1]) + int(bottom_row[n+1])
                    else:
                        if top_row[n] != middle_row[n] or top_row[n] != bottom_row[n] or middle_row[n] != bottom_row[n]:
                            if top_row[n] == 7 or top_row[n] == 11:
                                top_row[n] = 0
                            if middle_row[n] == 7 or middle_row[n] == 11:
                                middle_row[n] = 0
                            if bottom_row[n] == 7 or bottom_row[n] == 11:
                                bottom_row[n] = 0
                            score += int(top_row[n]) + int(middle_row[n]) + int(bottom_row[n])
                        if n == 3:
                            if top_row[n + 1] != middle_row[n + 1] or top_row[n + 1] != bottom_row[n + 1] or middle_row[n + 1] != bottom_row[n + 1]:
                                if top_row[n + 1] == 7 or top_row[n + 1] == 11:
                                    top_row[n + 1] = 0
                                if middle_row[n + 1] == 7 or middle_row[n + 1] == 11:
                                    middle_row[n + 1] = 0
                                if bottom_row[n + 1] == 7 or bottom_row[n + 1] == 11:
                                    bottom_row[n + 1] = 0
                                score += int(top_row[n + 1]) + int(middle_row[n + 1]) + int(bottom_row[n + 1])
        # This sequence subtracts from score if 2x3 rectangles equal each other
        for n in list(range(3)):
            if top_row[n] == top_row[n + 1] and top_row[n + 1] == top_row[n + 2] and top_row[n] == middle_row[n] and \
                    top_row[n + 1] == middle_row[n + 1] and top_row[n + 2] == middle_row[n + 2]:
                score += 10
                if bottom_row[n + 1] != middle_row[n + 1]:
                    if bottom_row[n + 1] != 7 and bottom_row[n + 1] != 11:
                        score -= int(bottom_row[n + 1])
            elif middle_row[n] == middle_row[n + 1] and middle_row[n + 1] == middle_row[n + 2] and middle_row[n] == bottom_row[n] and \
                    middle_row[n + 1] == bottom_row[n + 1] and middle_row[n + 2] == bottom_row[n + 2]:
                score += 10
                if top_row[n + 1] != middle_row[n + 1]:
                    if top_row[n + 1] != 7 and top_row[n + 1] != 11:
                        score -= int(top_row[n + 1])

        popupWindow = Popup(title='Score = ' + str(score), title_align='center', size_hint=(0.8, 0.1), size=(400, 400))
        popupWindow.open()

    def get_help(self):
        popupWindow = Popup(title="Help", title_align='center', size_hint=(0.8, 0.2), size=(400, 400),
                            content=Label(text="Lol you can't figure it out? Idiot."))
        popupWindow.open()

    def check_check(self):
        if check == 1:
            self.ids.gotogame.text = "Game"
        elif check == 2:
            self.ids.gotogame.text = " Game "
        elif check == 3:
            self.ids.gotogame.text = "  Game  "
        elif check == 4:
            self.ids.gotogame.text = "   Game   "
        elif check == 5:
            self.ids.gotogame.text = "    Game    "
        elif check == 6:
            self.ids.gotogame.text = "     Game     "
        elif check == 7:
            self.ids.gotogame.text = "      Game      "
        elif check == 8:
            self.ids.gotogame.text = "       Game       "
        elif check == 9:
            self.ids.gotogame.text = "        Game        "
        elif check == 10:
            self.ids.gotogame.text = "         Game         "
        elif check == 11:
            self.ids.gotogame.text = "          Game          "
        elif check == 12:
            self.ids.gotogame.text = "           Game           "

class GameWindow(Screen):
    def update_players(self, x):
        global players
        if x == 1:
            if players > 2:
                players -= 1
                self.ids.players.text = str(players)
        else:
            if players < 12:
                players += 1
                self.ids.players.text = str(players)
    def update_check(self):
        global check
        global players
        if players == 2:
            check = 2
            self.ids.start.text = "Next"
        elif players == 3:
            check = 3
            self.ids.start.text = " Next "
        elif players == 4:
            check = 4
            self.ids.start.text = "  Next  "
        elif players == 5:
            check = 5
            self.ids.start.text = "   Next   "
        elif players == 6:
            check = 6
            self.ids.start.text = "    Next    "
        elif players == 7:
            check = 7
            self.ids.start.text = "     Next     "
        elif players == 8:
            check = 8
            self.ids.start.text = "      Next      "
        elif players == 9:
            check = 9
            self.ids.start.text = "       Next       "
        elif players == 10:
            check = 10
            self.ids.start.text = "        Next        "
        elif players == 11:
            check = 11
            self.ids.start.text = "         Next         "
        elif players == 12:
            check = 12
            self.ids.start.text = "          Next          "


class Name2Window(Screen):
    def start_game(self, a, b):
        global names
        names = [str(a), str(b)]
    def check_next(self, t1, t2):
        if t1 != "" and t2 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
    def back(self):
        global check
        check = 1

class Game2PlayerWindow(Screen):
    def setup(self):
        global name
        global round
        global reset
        global p1s
        global p2s
        self.ids.p1n.text = names[0]
        self.ids.p2n.text = names[1]
        if reset == 1:
            self.ids.p1.text = ""
            self.ids.p2.text = ""
            self.ids.score1.text = ""
            self.ids.score2.text = ""
            p1s = [0]
            p2s = [0]
            round = 1
            self.ids.round.text = "Round 1"
            reset = 2
    def update_round(self, x):
        global round
        global p1s
        global p2s
        if x == 2:
            round += 1
            self.ids.round.text = "Round " + str(round)
            if len(p1s) > round:
                self.ids.p1.text = str(p1s[round - 1])
                self.ids.p2.text = str(p2s[round - 1])
        if round != 1:
            if x == 1:
                round -= 1
                self.ids.round.text = "Round " + str(round)
                self.ids.p1.text = str(p1s[round-1])
                self.ids.p2.text = str(p2s[round-1])
        if round == 1:
            self.ids.back.disabled = True
        else:
            self.ids.back.disabled = False
    def update_score(self, s1, s2, y):
        global round
        global p1s
        global p2s
        score1 = 0
        score2 = 0
        s = [s1, s2]
        for n in list(range(len(s))):
            if s[n] == "":
                s[n] = "0"
            else:
                s[n] = int(s[n])
                p1s[round - 1] = s[0]
                p2s[round - 1] = s[1]
        if y == 2 and p1s[len(p1s)-1] != "0":
            p1s.append("0")
            p2s.append("0")
        if y == 2:
            p1s[round-1] = s[0]
            p2s[round-1] = s[1]
        x = len(p1s)
        for n in list(range(x)):
            score1 += int(p1s[n])
            score2 += int(p2s[n])
        self.ids.p1.text = ""
        self.ids.p2.text = ""
        self.ids.score1.text = str(score1)
        self.ids.score2.text = str(score2)

    def check_next(self, t1, t2):
        global round
        x = 0
        y = 0
        if t1 != "" and t2 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
        t = [t1, t2]
        if round != 1:
            for n in list(range(len(t))):
                if t[n] != "":
                    x = 1
                if t[n] == "":
                    y = 1
            if x == 1 and y == 1:
                self.ids.back.disabled = True
            else:
                self.ids.back.disabled = False

class Name3Window(Screen):
    def start_game(self, a, b, c):
        global names
        names = [str(a), str(b), str(c)]

    def check_next(self, t1, t2, t3):
        if t1 != "" and t2 != "" and t3 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
    def back(self):
        global check
        check = 1

class Game3PlayerWindow(Screen):
    def setup(self):
        global names
        global round
        global reset
        global p1s
        global p2s
        global p3s
        self.ids.p1n.text = names[0]
        self.ids.p2n.text = names[1]
        self.ids.p3n.text = names[2]
        if reset == 1:
            self.ids.p1.text = ""
            self.ids.p2.text = ""
            self.ids.p3.text = ""
            self.ids.score1.text = ""
            self.ids.score2.text = ""
            self.ids.score3.text = ""
            p1s = [0]
            p2s = [0]
            p3s = [0]
            round = 1
            self.ids.round.text = "Round 1"
            reset = 2
    def update_round(self, x):
        global round
        global p1s
        global p2s
        global p3s
        if x == 2:
            round += 1
            self.ids.round.text = "Round " + str(round)
            if len(p1s) > round:
                self.ids.p1.text = str(p1s[round - 1])
                self.ids.p2.text = str(p2s[round - 1])
                self.ids.p3.text = str(p3s[round - 1])
        if round != 1:
            if x == 1:
                round -= 1
                self.ids.round.text = "Round " + str(round)
                self.ids.p1.text = str(p1s[round-1])
                self.ids.p2.text = str(p2s[round-1])
                self.ids.p3.text = str(p3s[round - 1])
        if round == 1:
            self.ids.back.disabled = True
        else:
            self.ids.back.disabled = False
    def update_score(self, s1, s2, s3, y):
        global round
        global p1s
        global p2s
        global p3s
        score1 = 0
        score2 = 0
        score3 = 0
        s = [s1, s2, s3]
        for n in list(range(len(s))):
            if s[n] == "":
                s[n] = "0"
            else:
                s[n] = int(s[n])
                p1s[round - 1] = s[0]
                p2s[round - 1] = s[1]
                p3s[round - 1] = s[2]
        if y == 2 and p1s[len(p1s)-1] != "0":
            p1s.append("0")
            p2s.append("0")
            p3s.append("0")
        if y == 2:
            p1s[round-1] = s[0]
            p2s[round-1] = s[1]
            p3s[round - 1] = s[2]
        x = len(p1s)
        for n in list(range(x)):
            score1 += int(p1s[n])
            score2 += int(p2s[n])
            score3 += int(p3s[n])
        self.ids.p1.text = ""
        self.ids.p2.text = ""
        self.ids.p3.text = ""
        self.ids.score1.text = str(score1)
        self.ids.score2.text = str(score2)
        self.ids.score3.text = str(score3)

    def check_next(self, t1, t2, t3):
        global round
        x = 0
        y = 0
        if t1 != "" and t2 != "" and t3 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
        t = [t1, t2, t3]
        if round != 1:
            for n in list(range(len(t))):
                if t[n] != "":
                    x = 1
                if t[n] == "":
                    y = 1
            if x == 1 and y == 1:
                self.ids.back.disabled = True
            else:
                self.ids.back.disabled = False

class Name4Window(Screen):
    def start_game(self, a, b, c, d):
        global names
        names = [str(a), str(b), str(c), str(d)]

    def check_next(self, t1, t2, t3, t4):
        if t1 != "" and t2 != "" and t3 != "" and t4 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
    def back(self):
        global check
        check = 1

class Game4PlayerWindow(Screen):
    def setup(self):
        global names
        global round
        global reset
        global p1s
        global p2s
        global p3s
        global p4s
        self.ids.p1n.text = names[0]
        self.ids.p2n.text = names[1]
        self.ids.p3n.text = names[2]
        self.ids.p4n.text = names[3]
        if reset == 1:
            self.ids.p1.text = ""
            self.ids.p2.text = ""
            self.ids.p3.text = ""
            self.ids.p4.text = ""
            self.ids.score1.text = ""
            self.ids.score2.text = ""
            self.ids.score3.text = ""
            self.ids.score4.text = ""
            p1s = [0]
            p2s = [0]
            p3s = [0]
            p4s = [0]
            round = 1
            self.ids.round.text = "Round 1"
            reset = 2
    def update_round(self, x):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        if x == 2:
            round += 1
            self.ids.round.text = "Round " + str(round)
            if len(p1s) > round:
                self.ids.p1.text = str(p1s[round - 1])
                self.ids.p2.text = str(p2s[round - 1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
        if round != 1:
            if x == 1:
                round -= 1
                self.ids.round.text = "Round " + str(round)
                self.ids.p1.text = str(p1s[round-1])
                self.ids.p2.text = str(p2s[round-1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
        if round == 1:
            self.ids.back.disabled = True
        else:
            self.ids.back.disabled = False
    def update_score(self, s1, s2, s3, s4, y):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        s = [s1, s2, s3, s4]
        for n in list(range(len(s))):
            if s[n] == "":
                s[n] = "0"
            else:
                s[n] = int(s[n])
                p1s[round - 1] = s[0]
                p2s[round - 1] = s[1]
                p3s[round - 1] = s[2]
                p4s[round - 1] = s[3]
        if y == 2 and p1s[len(p1s)-1] != "0":
            p1s.append("0")
            p2s.append("0")
            p3s.append("0")
            p4s.append("0")
        if y == 2:
            p1s[round-1] = s[0]
            p2s[round-1] = s[1]
            p3s[round - 1] = s[2]
            p4s[round - 1] = s[3]
        x = len(p1s)
        for n in list(range(x)):
            score1 += int(p1s[n])
            score2 += int(p2s[n])
            score3 += int(p3s[n])
            score4 += int(p4s[n])
        self.ids.p1.text = ""
        self.ids.p2.text = ""
        self.ids.p3.text = ""
        self.ids.p4.text = ""
        self.ids.score1.text = str(score1)
        self.ids.score2.text = str(score2)
        self.ids.score3.text = str(score3)
        self.ids.score4.text = str(score4)

    def check_next(self, t1, t2, t3, t4):
        global round
        x = 0
        y = 0
        if t1 != "" and t2 != "" and t3 != "" and t4 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
        t = [t1, t2, t3, t4]
        if round != 1:
            for n in list(range(len(t))):
                if t[n] != "":
                    x = 1
                if t[n] == "":
                    y = 1
            if x == 1 and y == 1:
                self.ids.back.disabled = True
            else:
                self.ids.back.disabled = False

class Name5Window(Screen):
    def start_game(self, a, b, c, d, e):
        global names
        names = [str(a), str(b), str(c), str(d), str(e)]

    def check_next(self, t1, t2, t3, t4, t5):
        if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
    def back(self):
        global check
        check = 1

class Game5PlayerWindow(Screen):
    def setup(self):
        global names
        global round
        global reset
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        self.ids.p1n.text = names[0]
        self.ids.p2n.text = names[1]
        self.ids.p3n.text = names[2]
        self.ids.p4n.text = names[3]
        self.ids.p5n.text = names[4]
        if reset == 1:
            self.ids.p1.text = ""
            self.ids.p2.text = ""
            self.ids.p3.text = ""
            self.ids.p4.text = ""
            self.ids.p5.text = ""
            self.ids.score1.text = ""
            self.ids.score2.text = ""
            self.ids.score3.text = ""
            self.ids.score4.text = ""
            self.ids.score5.text = ""
            p1s = [0]
            p2s = [0]
            p3s = [0]
            p4s = [0]
            p5s = [0]
            round = 1
            self.ids.round.text = "Round 1"
            reset = 2
    def update_round(self, x):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        if x == 2:
            round += 1
            self.ids.round.text = "Round " + str(round)
            if len(p1s) > round:
                self.ids.p1.text = str(p1s[round - 1])
                self.ids.p2.text = str(p2s[round - 1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
                self.ids.p5.text = str(p5s[round - 1])
        if round != 1:
            if x == 1:
                round -= 1
                self.ids.round.text = "Round " + str(round)
                self.ids.p1.text = str(p1s[round-1])
                self.ids.p2.text = str(p2s[round-1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
                self.ids.p5.text = str(p5s[round - 1])
        if round == 1:
            self.ids.back.disabled = True
        else:
            self.ids.back.disabled = False
    def update_score(self, s1, s2, s3, s4, s5, y):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        score5 = 0
        s = [s1, s2, s3, s4, s5]
        for n in list(range(len(s))):
            if s[n] == "":
                s[n] = "0"
            else:
                s[n] = int(s[n])
                p1s[round - 1] = s[0]
                p2s[round - 1] = s[1]
                p3s[round - 1] = s[2]
                p4s[round - 1] = s[3]
                p5s[round - 1] = s[4]
        if y == 2 and p1s[len(p1s)-1] != "0":
            p1s.append("0")
            p2s.append("0")
            p3s.append("0")
            p4s.append("0")
            p5s.append("0")
        if y == 2:
            p1s[round-1] = s[0]
            p2s[round-1] = s[1]
            p3s[round - 1] = s[2]
            p4s[round - 1] = s[3]
            p5s[round - 1] = s[4]
        x = len(p1s)
        for n in list(range(x)):
            score1 += int(p1s[n])
            score2 += int(p2s[n])
            score3 += int(p3s[n])
            score4 += int(p4s[n])
            score5 += int(p5s[n])
        self.ids.p1.text = ""
        self.ids.p2.text = ""
        self.ids.p3.text = ""
        self.ids.p4.text = ""
        self.ids.p5.text = ""
        self.ids.score1.text = str(score1)
        self.ids.score2.text = str(score2)
        self.ids.score3.text = str(score3)
        self.ids.score4.text = str(score4)
        self.ids.score5.text = str(score5)

    def check_next(self, t1, t2, t3, t4, t5):
        global round
        x = 0
        y = 0
        if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
        t = [t1, t2, t3, t4, t5]
        if round != 1:
            for n in list(range(len(t))):
                if t[n] != "":
                    x = 1
                if t[n] == "":
                    y = 1
            if x == 1 and y == 1:
                self.ids.back.disabled = True
            else:
                self.ids.back.disabled = False

class Name6Window(Screen):
    def start_game(self, a, b, c, d, e, f):
        global names
        names = [str(a), str(b), str(c), str(d), str(e), str(f)]

    def check_next(self, t1, t2, t3, t4, t5, t6):
        if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "" and t6 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
    def back(self):
        global check
        check = 1

class Game6PlayerWindow(Screen):
    def setup(self):
        global names
        global round
        global reset
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        self.ids.p1n.text = names[0]
        self.ids.p2n.text = names[1]
        self.ids.p3n.text = names[2]
        self.ids.p4n.text = names[3]
        self.ids.p5n.text = names[4]
        self.ids.p6n.text = names[5]
        if reset == 1:
            self.ids.p1.text = ""
            self.ids.p2.text = ""
            self.ids.p3.text = ""
            self.ids.p4.text = ""
            self.ids.p5.text = ""
            self.ids.p6.text = ""
            self.ids.score1.text = ""
            self.ids.score2.text = ""
            self.ids.score3.text = ""
            self.ids.score4.text = ""
            self.ids.score5.text = ""
            self.ids.score6.text = ""
            p1s = [0]
            p2s = [0]
            p3s = [0]
            p4s = [0]
            p5s = [0]
            p6s = [0]
            round = 1
            self.ids.round.text = "Round 1"
            reset = 2
    def update_round(self, x):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        if x == 2:
            round += 1
            self.ids.round.text = "Round " + str(round)
            if len(p1s) > round:
                self.ids.p1.text = str(p1s[round - 1])
                self.ids.p2.text = str(p2s[round - 1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
                self.ids.p5.text = str(p5s[round - 1])
                self.ids.p6.text = str(p6s[round - 1])
        if round != 1:
            if x == 1:
                round -= 1
                self.ids.round.text = "Round " + str(round)
                self.ids.p1.text = str(p1s[round-1])
                self.ids.p2.text = str(p2s[round-1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
                self.ids.p5.text = str(p5s[round - 1])
                self.ids.p6.text = str(p6s[round - 1])
        if round == 1:
            self.ids.back.disabled = True
        else:
            self.ids.back.disabled = False
    def update_score(self, s1, s2, s3, s4, s5, s6, y):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        score5 = 0
        score6 = 0
        s = [s1, s2, s3, s4, s5, s6]
        for n in list(range(len(s))):
            if s[n] == "":
                s[n] = "0"
            else:
                s[n] = int(s[n])
                p1s[round - 1] = s[0]
                p2s[round - 1] = s[1]
                p3s[round - 1] = s[2]
                p4s[round - 1] = s[3]
                p5s[round - 1] = s[4]
                p6s[round - 1] = s[5]
        if y == 2 and p1s[len(p1s)-1] != "0":
            p1s.append("0")
            p2s.append("0")
            p3s.append("0")
            p4s.append("0")
            p5s.append("0")
            p6s.append("0")
        if y == 2:
            p1s[round-1] = s[0]
            p2s[round-1] = s[1]
            p3s[round - 1] = s[2]
            p4s[round - 1] = s[3]
            p5s[round - 1] = s[4]
            p6s[round - 1] = s[5]
        x = len(p1s)
        for n in list(range(x)):
            score1 += int(p1s[n])
            score2 += int(p2s[n])
            score3 += int(p3s[n])
            score4 += int(p4s[n])
            score5 += int(p5s[n])
            score6 += int(p6s[n])
        self.ids.p1.text = ""
        self.ids.p2.text = ""
        self.ids.p3.text = ""
        self.ids.p4.text = ""
        self.ids.p5.text = ""
        self.ids.p6.text = ""
        self.ids.score1.text = str(score1)
        self.ids.score2.text = str(score2)
        self.ids.score3.text = str(score3)
        self.ids.score4.text = str(score4)
        self.ids.score5.text = str(score5)
        self.ids.score6.text = str(score6)

    def check_next(self, t1, t2, t3, t4, t5, t6):
        global round
        x = 0
        y = 0
        if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "" and t6 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
        t = [t1, t2, t3, t4, t5, t6]
        if round != 1:
            for n in list(range(len(t))):
                if t[n] != "":
                    x = 1
                if t[n] == "":
                    y = 1
            if x == 1 and y == 1:
                self.ids.back.disabled = True
            else:
                self.ids.back.disabled = False

class Name7Window(Screen):
    def start_game(self, a, b, c, d, e, f, g):
        global names
        names = [str(a), str(b), str(c), str(d), str(e), str(f), str(g)]

    def check_next(self, t1, t2, t3, t4, t5, t6, t7):
        if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "" and t6 != "" and t7 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
    def back(self):
        global check
        check = 1

class Game7PlayerWindow(Screen):
    def setup(self):
        global names
        global round
        global reset
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        self.ids.p1n.text = names[0]
        self.ids.p2n.text = names[1]
        self.ids.p3n.text = names[2]
        self.ids.p4n.text = names[3]
        self.ids.p5n.text = names[4]
        self.ids.p6n.text = names[5]
        self.ids.p7n.text = names[6]
        if reset == 1:
            self.ids.p1.text = ""
            self.ids.p2.text = ""
            self.ids.p3.text = ""
            self.ids.p4.text = ""
            self.ids.p5.text = ""
            self.ids.p6.text = ""
            self.ids.p7.text = ""
            self.ids.score1.text = ""
            self.ids.score2.text = ""
            self.ids.score3.text = ""
            self.ids.score4.text = ""
            self.ids.score5.text = ""
            self.ids.score6.text = ""
            self.ids.score7.text = ""
            p1s = [0]
            p2s = [0]
            p3s = [0]
            p4s = [0]
            p5s = [0]
            p6s = [0]
            p7s = [0]
            round = 1
            self.ids.round.text = "Round 1"
            reset = 2
    def update_round(self, x):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        if x == 2:
            round += 1
            self.ids.round.text = "Round " + str(round)
            if len(p1s) > round:
                self.ids.p1.text = str(p1s[round - 1])
                self.ids.p2.text = str(p2s[round - 1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
                self.ids.p5.text = str(p5s[round - 1])
                self.ids.p6.text = str(p6s[round - 1])
                self.ids.p7.text = str(p7s[round - 1])
        if round != 1:
            if x == 1:
                round -= 1
                self.ids.round.text = "Round " + str(round)
                self.ids.p1.text = str(p1s[round-1])
                self.ids.p2.text = str(p2s[round-1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
                self.ids.p5.text = str(p5s[round - 1])
                self.ids.p6.text = str(p6s[round - 1])
                self.ids.p7.text = str(p7s[round - 1])
        if round == 1:
            self.ids.back.disabled = True
        else:
            self.ids.back.disabled = False
    def update_score(self, s1, s2, s3, s4, s5, s6, s7, y):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        score5 = 0
        score6 = 0
        score7 = 0
        s = [s1, s2, s3, s4, s5, s6, s7]
        for n in list(range(len(s))):
            if s[n] == "":
                s[n] = "0"
            else:
                s[n] = int(s[n])
                p1s[round - 1] = s[0]
                p2s[round - 1] = s[1]
                p3s[round - 1] = s[2]
                p4s[round - 1] = s[3]
                p5s[round - 1] = s[4]
                p6s[round - 1] = s[5]
                p7s[round - 1] = s[6]
        if y == 2 and p1s[len(p1s)-1] != "0":
            p1s.append("0")
            p2s.append("0")
            p3s.append("0")
            p4s.append("0")
            p5s.append("0")
            p6s.append("0")
            p7s.append("0")
        if y == 2:
            p1s[round-1] = s[0]
            p2s[round-1] = s[1]
            p3s[round - 1] = s[2]
            p4s[round - 1] = s[3]
            p5s[round - 1] = s[4]
            p6s[round - 1] = s[5]
            p7s[round - 1] = s[6]
        x = len(p1s)
        for n in list(range(x)):
            score1 += int(p1s[n])
            score2 += int(p2s[n])
            score3 += int(p3s[n])
            score4 += int(p4s[n])
            score5 += int(p5s[n])
            score6 += int(p6s[n])
            score7 += int(p7s[n])
        self.ids.p1.text = ""
        self.ids.p2.text = ""
        self.ids.p3.text = ""
        self.ids.p4.text = ""
        self.ids.p5.text = ""
        self.ids.p6.text = ""
        self.ids.p7.text = ""
        self.ids.score1.text = str(score1)
        self.ids.score2.text = str(score2)
        self.ids.score3.text = str(score3)
        self.ids.score4.text = str(score4)
        self.ids.score5.text = str(score5)
        self.ids.score6.text = str(score6)
        self.ids.score7.text = str(score7)

    def check_next(self, t1, t2, t3, t4, t5, t6, t7):
        global round
        x = 0
        y = 0
        if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "" and t6 != "" and t7 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
        t = [t1, t2, t3, t4, t5, t6, t7]
        if round != 1:
            for n in list(range(len(t))):
                if t[n] != "":
                    x = 1
                if t[n] == "":
                    y = 1
            if x == 1 and y == 1:
                self.ids.back.disabled = True
            else:
                self.ids.back.disabled = False

class Name8Window(Screen):
    def start_game(self, a, b, c, d, e, f, g, h):
        global names
        names = [str(a), str(b), str(c), str(d), str(e), str(f), str(g), str(h)]

    def check_next(self, t1, t2, t3, t4, t5, t6, t7, t8):
        if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "" and t6 != "" and t7 != "" and t8 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
    def back(self):
        global check
        check = 1

class Game8PlayerWindow(Screen):
    def setup(self):
        global names
        global round
        global reset
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        global p8s
        self.ids.p1n.text = names[0]
        self.ids.p2n.text = names[1]
        self.ids.p3n.text = names[2]
        self.ids.p4n.text = names[3]
        self.ids.p5n.text = names[4]
        self.ids.p6n.text = names[5]
        self.ids.p7n.text = names[6]
        self.ids.p8n.text = names[7]
        if reset == 1:
            self.ids.p1.text = ""
            self.ids.p2.text = ""
            self.ids.p3.text = ""
            self.ids.p4.text = ""
            self.ids.p5.text = ""
            self.ids.p6.text = ""
            self.ids.p7.text = ""
            self.ids.p8.text = ""
            self.ids.score1.text = ""
            self.ids.score2.text = ""
            self.ids.score3.text = ""
            self.ids.score4.text = ""
            self.ids.score5.text = ""
            self.ids.score6.text = ""
            self.ids.score7.text = ""
            self.ids.score8.text = ""
            p1s = [0]
            p2s = [0]
            p3s = [0]
            p4s = [0]
            p5s = [0]
            p6s = [0]
            p7s = [0]
            p8s = [0]
            round = 1
            self.ids.round.text = "Round 1"
            reset = 2
    def update_round(self, x):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        global p8s
        if x == 2:
            round += 1
            self.ids.round.text = "Round " + str(round)
            if len(p1s) > round:
                self.ids.p1.text = str(p1s[round - 1])
                self.ids.p2.text = str(p2s[round - 1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
                self.ids.p5.text = str(p5s[round - 1])
                self.ids.p6.text = str(p6s[round - 1])
                self.ids.p7.text = str(p7s[round - 1])
                self.ids.p8.text = str(p8s[round - 1])
        if round != 1:
            if x == 1:
                round -= 1
                self.ids.round.text = "Round " + str(round)
                self.ids.p1.text = str(p1s[round-1])
                self.ids.p2.text = str(p2s[round-1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
                self.ids.p5.text = str(p5s[round - 1])
                self.ids.p6.text = str(p6s[round - 1])
                self.ids.p7.text = str(p7s[round - 1])
                self.ids.p8.text = str(p8s[round - 1])
        if round == 1:
            self.ids.back.disabled = True
        else:
            self.ids.back.disabled = False
    def update_score(self, s1, s2, s3, s4, s5, s6, s7, s8, y):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        global p8s
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        score5 = 0
        score6 = 0
        score7 = 0
        score8 = 0
        s = [s1, s2, s3, s4, s5, s6, s7, s8]
        for n in list(range(len(s))):
            if s[n] == "":
                s[n] = "0"
            else:
                s[n] = int(s[n])
                p1s[round - 1] = s[0]
                p2s[round - 1] = s[1]
                p3s[round - 1] = s[2]
                p4s[round - 1] = s[3]
                p5s[round - 1] = s[4]
                p6s[round - 1] = s[5]
                p7s[round - 1] = s[6]
                p8s[round - 1] = s[7]
        if y == 2 and p1s[len(p1s)-1] != "0":
            p1s.append("0")
            p2s.append("0")
            p3s.append("0")
            p4s.append("0")
            p5s.append("0")
            p6s.append("0")
            p7s.append("0")
            p8s.append("0")
        if y == 2:
            p1s[round-1] = s[0]
            p2s[round-1] = s[1]
            p3s[round - 1] = s[2]
            p4s[round - 1] = s[3]
            p5s[round - 1] = s[4]
            p6s[round - 1] = s[5]
            p7s[round - 1] = s[6]
            p8s[round - 1] = s[7]
        x = len(p1s)
        for n in list(range(x)):
            score1 += int(p1s[n])
            score2 += int(p2s[n])
            score3 += int(p3s[n])
            score4 += int(p4s[n])
            score5 += int(p5s[n])
            score6 += int(p6s[n])
            score7 += int(p7s[n])
            score8 += int(p8s[n])
        self.ids.p1.text = ""
        self.ids.p2.text = ""
        self.ids.p3.text = ""
        self.ids.p4.text = ""
        self.ids.p5.text = ""
        self.ids.p6.text = ""
        self.ids.p7.text = ""
        self.ids.p8.text = ""
        self.ids.score1.text = str(score1)
        self.ids.score2.text = str(score2)
        self.ids.score3.text = str(score3)
        self.ids.score4.text = str(score4)
        self.ids.score5.text = str(score5)
        self.ids.score6.text = str(score6)
        self.ids.score7.text = str(score7)
        self.ids.score8.text = str(score8)

    def check_next(self, t1, t2, t3, t4, t5, t6, t7, t8):
        global round
        x = 0
        y = 0
        if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "" and t6 != "" and t7 != "" and t8 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
        t = [t1, t2, t3, t4, t5, t6, t7, t8]
        if round != 1:
            for n in list(range(len(t))):
                if t[n] != "":
                    x = 1
                if t[n] == "":
                    y = 1
            if x == 1 and y == 1:
                self.ids.back.disabled = True
            else:
                self.ids.back.disabled = False

class Name9Window(Screen):
    def start_game(self, a, b, c, d, e, f, g, h, i):
        global names
        names = [str(a), str(b), str(c), str(d), str(e), str(f), str(g), str(h), str(i)]

    def check_next(self, t1, t2, t3, t4, t5, t6, t7, t8, t9):
        if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "" and t6 != "" and t7 != "" and t8 != "" and t9 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
    def back(self):
        global check
        check = 1

class Game9PlayerWindow(Screen):
    def setup(self):
        global names
        global round
        global reset
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        global p8s
        global p9s
        self.ids.p1n.text = names[0]
        self.ids.p2n.text = names[1]
        self.ids.p3n.text = names[2]
        self.ids.p4n.text = names[3]
        self.ids.p5n.text = names[4]
        self.ids.p6n.text = names[5]
        self.ids.p7n.text = names[6]
        self.ids.p8n.text = names[7]
        self.ids.p9n.text = names[8]
        if reset == 1:
            self.ids.p1.text = ""
            self.ids.p2.text = ""
            self.ids.p3.text = ""
            self.ids.p4.text = ""
            self.ids.p5.text = ""
            self.ids.p6.text = ""
            self.ids.p7.text = ""
            self.ids.p8.text = ""
            self.ids.p9.text = ""
            self.ids.score1.text = ""
            self.ids.score2.text = ""
            self.ids.score3.text = ""
            self.ids.score4.text = ""
            self.ids.score5.text = ""
            self.ids.score6.text = ""
            self.ids.score7.text = ""
            self.ids.score8.text = ""
            self.ids.score9.text = ""
            p1s = [0]
            p2s = [0]
            p3s = [0]
            p4s = [0]
            p5s = [0]
            p6s = [0]
            p7s = [0]
            p8s = [0]
            p9s = [0]
            round = 1
            self.ids.round.text = "Round 1"
            reset = 2
    def update_round(self, x):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        global p8s
        global p9s
        if x == 2:
            round += 1
            self.ids.round.text = "Round " + str(round)
            if len(p1s) > round:
                self.ids.p1.text = str(p1s[round - 1])
                self.ids.p2.text = str(p2s[round - 1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
                self.ids.p5.text = str(p5s[round - 1])
                self.ids.p6.text = str(p6s[round - 1])
                self.ids.p7.text = str(p7s[round - 1])
                self.ids.p8.text = str(p8s[round - 1])
                self.ids.p9.text = str(p9s[round - 1])
        if round != 1:
            if x == 1:
                round -= 1
                self.ids.round.text = "Round " + str(round)
                self.ids.p1.text = str(p1s[round-1])
                self.ids.p2.text = str(p2s[round-1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
                self.ids.p5.text = str(p5s[round - 1])
                self.ids.p6.text = str(p6s[round - 1])
                self.ids.p7.text = str(p7s[round - 1])
                self.ids.p8.text = str(p8s[round - 1])
                self.ids.p9.text = str(p9s[round - 1])
        if round == 1:
            self.ids.back.disabled = True
        else:
            self.ids.back.disabled = False
    def update_score(self, s1, s2, s3, s4, s5, s6, s7, s8, s9, y):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        global p8s
        global p9s
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        score5 = 0
        score6 = 0
        score7 = 0
        score8 = 0
        score9 = 0
        s = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
        for n in list(range(len(s))):
            if s[n] == "":
                s[n] = "0"
            else:
                s[n] = int(s[n])
                p1s[round - 1] = s[0]
                p2s[round - 1] = s[1]
                p3s[round - 1] = s[2]
                p4s[round - 1] = s[3]
                p5s[round - 1] = s[4]
                p6s[round - 1] = s[5]
                p7s[round - 1] = s[6]
                p8s[round - 1] = s[7]
                p9s[round - 1] = s[8]
        if y == 2 and p1s[len(p1s)-1] != "0":
            p1s.append("0")
            p2s.append("0")
            p3s.append("0")
            p4s.append("0")
            p5s.append("0")
            p6s.append("0")
            p7s.append("0")
            p8s.append("0")
            p9s.append("0")
        if y == 2:
            p1s[round-1] = s[0]
            p2s[round-1] = s[1]
            p3s[round - 1] = s[2]
            p4s[round - 1] = s[3]
            p5s[round - 1] = s[4]
            p6s[round - 1] = s[5]
            p7s[round - 1] = s[6]
            p8s[round - 1] = s[7]
            p9s[round - 1] = s[8]
        x = len(p1s)
        for n in list(range(x)):
            score1 += int(p1s[n])
            score2 += int(p2s[n])
            score3 += int(p3s[n])
            score4 += int(p4s[n])
            score5 += int(p5s[n])
            score6 += int(p6s[n])
            score7 += int(p7s[n])
            score8 += int(p8s[n])
            score9 += int(p9s[n])
        self.ids.p1.text = ""
        self.ids.p2.text = ""
        self.ids.p3.text = ""
        self.ids.p4.text = ""
        self.ids.p5.text = ""
        self.ids.p6.text = ""
        self.ids.p7.text = ""
        self.ids.p8.text = ""
        self.ids.p9.text = ""
        self.ids.score1.text = str(score1)
        self.ids.score2.text = str(score2)
        self.ids.score3.text = str(score3)
        self.ids.score4.text = str(score4)
        self.ids.score5.text = str(score5)
        self.ids.score6.text = str(score6)
        self.ids.score7.text = str(score7)
        self.ids.score8.text = str(score8)
        self.ids.score9.text = str(score9)

    def check_next(self, t1, t2, t3, t4, t5, t6, t7, t8, t9):
        global round
        x = 0
        y = 0
        if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "" and t6 != "" and t7 != "" and t8 != "" and t9 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
        t = [t1, t2, t3, t4, t5, t6, t7, t8, t9]
        if round != 1:
            for n in list(range(len(t))):
                if t[n] != "":
                    x = 1
                if t[n] == "":
                    y = 1
            if x == 1 and y == 1:
                self.ids.back.disabled = True
            else:
                self.ids.back.disabled = False

class Name10Window(Screen):
    def start_game(self, a, b, c, d, e, f, g, h, i, j):
        global names
        names = [str(a), str(b), str(c), str(d), str(e), str(f), str(g), str(h), str(i), str(j)]

    def check_next(self, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10):
        if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "" and t6 != "" and t7 != "" and t8 != "" and t9 != "" and t10 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
    def back(self):
        global check
        check = 1

class Game10PlayerWindow(Screen):
    def setup(self):
        global names
        global round
        global reset
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        global p8s
        global p9s
        global p10s
        self.ids.p1n.text = names[0]
        self.ids.p2n.text = names[1]
        self.ids.p3n.text = names[2]
        self.ids.p4n.text = names[3]
        self.ids.p5n.text = names[4]
        self.ids.p6n.text = names[5]
        self.ids.p7n.text = names[6]
        self.ids.p8n.text = names[7]
        self.ids.p9n.text = names[8]
        self.ids.p10n.text = names[9]
        if reset == 1:
            self.ids.p1.text = ""
            self.ids.p2.text = ""
            self.ids.p3.text = ""
            self.ids.p4.text = ""
            self.ids.p5.text = ""
            self.ids.p6.text = ""
            self.ids.p7.text = ""
            self.ids.p8.text = ""
            self.ids.p9.text = ""
            self.ids.p10.text = ""
            self.ids.score1.text = ""
            self.ids.score2.text = ""
            self.ids.score3.text = ""
            self.ids.score4.text = ""
            self.ids.score5.text = ""
            self.ids.score6.text = ""
            self.ids.score7.text = ""
            self.ids.score8.text = ""
            self.ids.score9.text = ""
            self.ids.score10.text = ""
            p1s = [0]
            p2s = [0]
            p3s = [0]
            p4s = [0]
            p5s = [0]
            p6s = [0]
            p7s = [0]
            p8s = [0]
            p9s = [0]
            p10s = [0]
            round = 1
            self.ids.round.text = "Round 1"
            reset = 2
    def update_round(self, x):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        global p8s
        global p9s
        global p10s
        if x == 2:
            round += 1
            self.ids.round.text = "Round " + str(round)
            if len(p1s) > round:
                self.ids.p1.text = str(p1s[round - 1])
                self.ids.p2.text = str(p2s[round - 1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
                self.ids.p5.text = str(p5s[round - 1])
                self.ids.p6.text = str(p6s[round - 1])
                self.ids.p7.text = str(p7s[round - 1])
                self.ids.p8.text = str(p8s[round - 1])
                self.ids.p9.text = str(p9s[round - 1])
                self.ids.p10.text = str(p10s[round - 1])
        if round != 1:
            if x == 1:
                round -= 1
                self.ids.round.text = "Round " + str(round)
                self.ids.p1.text = str(p1s[round-1])
                self.ids.p2.text = str(p2s[round-1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
                self.ids.p5.text = str(p5s[round - 1])
                self.ids.p6.text = str(p6s[round - 1])
                self.ids.p7.text = str(p7s[round - 1])
                self.ids.p8.text = str(p8s[round - 1])
                self.ids.p9.text = str(p9s[round - 1])
                self.ids.p10.text = str(p10s[round - 1])
        if round == 1:
            self.ids.back.disabled = True
        else:
            self.ids.back.disabled = False
    def update_score(self, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, y):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        global p8s
        global p9s
        global p10s
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        score5 = 0
        score6 = 0
        score7 = 0
        score8 = 0
        score9 = 0
        score10 = 0
        s = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
        for n in list(range(len(s))):
            if s[n] == "":
                s[n] = "0"
            else:
                s[n] = int(s[n])
                p1s[round - 1] = s[0]
                p2s[round - 1] = s[1]
                p3s[round - 1] = s[2]
                p4s[round - 1] = s[3]
                p5s[round - 1] = s[4]
                p6s[round - 1] = s[5]
                p7s[round - 1] = s[6]
                p8s[round - 1] = s[7]
                p9s[round - 1] = s[8]
                p10s[round - 1] = s[9]
        if y == 2 and p1s[len(p1s)-1] != "0":
            p1s.append("0")
            p2s.append("0")
            p3s.append("0")
            p4s.append("0")
            p5s.append("0")
            p6s.append("0")
            p7s.append("0")
            p8s.append("0")
            p9s.append("0")
            p10s.append("0")
        if y == 2:
            p1s[round-1] = s[0]
            p2s[round-1] = s[1]
            p3s[round - 1] = s[2]
            p4s[round - 1] = s[3]
            p5s[round - 1] = s[4]
            p6s[round - 1] = s[5]
            p7s[round - 1] = s[6]
            p8s[round - 1] = s[7]
            p9s[round - 1] = s[8]
            p10s[round - 1] = s[9]
        x = len(p1s)
        for n in list(range(x)):
            score1 += int(p1s[n])
            score2 += int(p2s[n])
            score3 += int(p3s[n])
            score4 += int(p4s[n])
            score5 += int(p5s[n])
            score6 += int(p6s[n])
            score7 += int(p7s[n])
            score8 += int(p8s[n])
            score9 += int(p9s[n])
            score10 += int(p10s[n])
        self.ids.p1.text = ""
        self.ids.p2.text = ""
        self.ids.p3.text = ""
        self.ids.p4.text = ""
        self.ids.p5.text = ""
        self.ids.p6.text = ""
        self.ids.p7.text = ""
        self.ids.p8.text = ""
        self.ids.p9.text = ""
        self.ids.p10.text = ""
        self.ids.score1.text = str(score1)
        self.ids.score2.text = str(score2)
        self.ids.score3.text = str(score3)
        self.ids.score4.text = str(score4)
        self.ids.score5.text = str(score5)
        self.ids.score6.text = str(score6)
        self.ids.score7.text = str(score7)
        self.ids.score8.text = str(score8)
        self.ids.score9.text = str(score9)
        self.ids.score10.text = str(score10)

    def check_next(self, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10):
        global round
        x = 0
        y = 0
        if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "" and t6 != "" and t7 != "" and t8 != "" and t9 != "" and t10 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
        t = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
        if round != 1:
            for n in list(range(len(t))):
                if t[n] != "":
                    x = 1
                if t[n] == "":
                    y = 1
            if x == 1 and y == 1:
                self.ids.back.disabled = True
            else:
                self.ids.back.disabled = False

class Name11Window(Screen):
    def start_game(self, a, b, c, d, e, f, g, h, i, j, k):
        global names
        names = [str(a), str(b), str(c), str(d), str(e), str(f), str(g), str(h), str(i), str(j), str(k)]

    def check_next(self, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11):
        if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "" and t6 != "" and t7 != "" and t8 != "" and t9 != "" and t10 != "" and t11 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
    def back(self):
        global check
        check = 1

class Game11PlayerWindow(Screen):
    def setup(self):
        global names
        global round
        global reset
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        global p8s
        global p9s
        global p10s
        global p11s
        self.ids.p1n.text = names[0]
        self.ids.p2n.text = names[1]
        self.ids.p3n.text = names[2]
        self.ids.p4n.text = names[3]
        self.ids.p5n.text = names[4]
        self.ids.p6n.text = names[5]
        self.ids.p7n.text = names[6]
        self.ids.p8n.text = names[7]
        self.ids.p9n.text = names[8]
        self.ids.p10n.text = names[9]
        self.ids.p11n.text = names[10]
        if reset == 1:
            self.ids.p1.text = ""
            self.ids.p2.text = ""
            self.ids.p3.text = ""
            self.ids.p4.text = ""
            self.ids.p5.text = ""
            self.ids.p6.text = ""
            self.ids.p7.text = ""
            self.ids.p8.text = ""
            self.ids.p9.text = ""
            self.ids.p10.text = ""
            self.ids.p11.text = ""
            self.ids.score1.text = ""
            self.ids.score2.text = ""
            self.ids.score3.text = ""
            self.ids.score4.text = ""
            self.ids.score5.text = ""
            self.ids.score6.text = ""
            self.ids.score7.text = ""
            self.ids.score8.text = ""
            self.ids.score9.text = ""
            self.ids.score10.text = ""
            self.ids.score11.text = ""
            p1s = [0]
            p2s = [0]
            p3s = [0]
            p4s = [0]
            p5s = [0]
            p6s = [0]
            p7s = [0]
            p8s = [0]
            p9s = [0]
            p10s = [0]
            p11s = [0]
            round = 1
            self.ids.round.text = "Round 1"
            reset = 2
    def update_round(self, x):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        global p8s
        global p9s
        global p10s
        global p11s
        if x == 2:
            round += 1
            self.ids.round.text = "Round " + str(round)
            if len(p1s) > round:
                self.ids.p1.text = str(p1s[round - 1])
                self.ids.p2.text = str(p2s[round - 1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
                self.ids.p5.text = str(p5s[round - 1])
                self.ids.p6.text = str(p6s[round - 1])
                self.ids.p7.text = str(p7s[round - 1])
                self.ids.p8.text = str(p8s[round - 1])
                self.ids.p9.text = str(p9s[round - 1])
                self.ids.p10.text = str(p10s[round - 1])
                self.ids.p11.text = str(p11s[round - 1])
        if round != 1:
            if x == 1:
                round -= 1
                self.ids.round.text = "Round " + str(round)
                self.ids.p1.text = str(p1s[round-1])
                self.ids.p2.text = str(p2s[round-1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
                self.ids.p5.text = str(p5s[round - 1])
                self.ids.p6.text = str(p6s[round - 1])
                self.ids.p7.text = str(p7s[round - 1])
                self.ids.p8.text = str(p8s[round - 1])
                self.ids.p9.text = str(p9s[round - 1])
                self.ids.p10.text = str(p10s[round - 1])
                self.ids.p11.text = str(p11s[round - 1])
        if round == 1:
            self.ids.back.disabled = True
        else:
            self.ids.back.disabled = False
    def update_score(self, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, y):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        global p8s
        global p9s
        global p10s
        global p11s
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        score5 = 0
        score6 = 0
        score7 = 0
        score8 = 0
        score9 = 0
        score10 = 0
        score11 = 0
        s = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11]
        for n in list(range(len(s))):
            if s[n] == "":
                s[n] = "0"
            else:
                s[n] = int(s[n])
                p1s[round - 1] = s[0]
                p2s[round - 1] = s[1]
                p3s[round - 1] = s[2]
                p4s[round - 1] = s[3]
                p5s[round - 1] = s[4]
                p6s[round - 1] = s[5]
                p7s[round - 1] = s[6]
                p8s[round - 1] = s[7]
                p9s[round - 1] = s[8]
                p10s[round - 1] = s[9]
                p11s[round - 1] = s[10]
        if y == 2 and p1s[len(p1s)-1] != "0":
            p1s.append("0")
            p2s.append("0")
            p3s.append("0")
            p4s.append("0")
            p5s.append("0")
            p6s.append("0")
            p7s.append("0")
            p8s.append("0")
            p9s.append("0")
            p10s.append("0")
            p11s.append("0")
        if y == 2:
            p1s[round-1] = s[0]
            p2s[round-1] = s[1]
            p3s[round - 1] = s[2]
            p4s[round - 1] = s[3]
            p5s[round - 1] = s[4]
            p6s[round - 1] = s[5]
            p7s[round - 1] = s[6]
            p8s[round - 1] = s[7]
            p9s[round - 1] = s[8]
            p10s[round - 1] = s[9]
            p11s[round - 1] = s[10]
        x = len(p1s)
        for n in list(range(x)):
            score1 += int(p1s[n])
            score2 += int(p2s[n])
            score3 += int(p3s[n])
            score4 += int(p4s[n])
            score5 += int(p5s[n])
            score6 += int(p6s[n])
            score7 += int(p7s[n])
            score8 += int(p8s[n])
            score9 += int(p9s[n])
            score10 += int(p10s[n])
            score11 += int(p11s[n])
        self.ids.p1.text = ""
        self.ids.p2.text = ""
        self.ids.p3.text = ""
        self.ids.p4.text = ""
        self.ids.p5.text = ""
        self.ids.p6.text = ""
        self.ids.p7.text = ""
        self.ids.p8.text = ""
        self.ids.p9.text = ""
        self.ids.p10.text = ""
        self.ids.p11.text = ""
        self.ids.score1.text = str(score1)
        self.ids.score2.text = str(score2)
        self.ids.score3.text = str(score3)
        self.ids.score4.text = str(score4)
        self.ids.score5.text = str(score5)
        self.ids.score6.text = str(score6)
        self.ids.score7.text = str(score7)
        self.ids.score8.text = str(score8)
        self.ids.score9.text = str(score9)
        self.ids.score10.text = str(score10)
        self.ids.score11.text = str(score11)

    def check_next(self, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11):
        global round
        x = 0
        y = 0
        if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "" and t6 != "" and t7 != "" and t8 != "" and t9 != "" and t10 != "" and t11 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
        t = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11]
        if round != 1:
            for n in list(range(len(t))):
                if t[n] != "":
                    x = 1
                if t[n] == "":
                    y = 1
            if x == 1 and y == 1:
                self.ids.back.disabled = True
            else:
                self.ids.back.disabled = False

class Name12Window(Screen):
    def start_game(self, a, b, c, d, e, f, g, h, i, j, k, l):
        global names
        names = [str(a), str(b), str(c), str(d), str(e), str(f), str(g), str(h), str(i), str(j), str(k), str(l)]

    def check_next(self, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12):
        if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "" and t6 != "" and t7 != "" and t8 != "" and t9 != "" and t10 != "" and t11 != "" and t12 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
    def back(self):
        global check
        check = 1

class Game12PlayerWindow(Screen):
    def setup(self):
        global names
        global round
        global reset
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        global p8s
        global p9s
        global p10s
        global p11s
        global p12s
        self.ids.p1n.text = names[0]
        self.ids.p2n.text = names[1]
        self.ids.p3n.text = names[2]
        self.ids.p4n.text = names[3]
        self.ids.p5n.text = names[4]
        self.ids.p6n.text = names[5]
        self.ids.p7n.text = names[6]
        self.ids.p8n.text = names[7]
        self.ids.p9n.text = names[8]
        self.ids.p10n.text = names[9]
        self.ids.p11n.text = names[10]
        self.ids.p12n.text = names[11]
        if reset == 1:
            self.ids.p1.text = ""
            self.ids.p2.text = ""
            self.ids.p3.text = ""
            self.ids.p4.text = ""
            self.ids.p5.text = ""
            self.ids.p6.text = ""
            self.ids.p7.text = ""
            self.ids.p8.text = ""
            self.ids.p9.text = ""
            self.ids.p10.text = ""
            self.ids.p11.text = ""
            self.ids.p12.text = ""
            self.ids.score1.text = ""
            self.ids.score2.text = ""
            self.ids.score3.text = ""
            self.ids.score4.text = ""
            self.ids.score5.text = ""
            self.ids.score6.text = ""
            self.ids.score7.text = ""
            self.ids.score8.text = ""
            self.ids.score9.text = ""
            self.ids.score10.text = ""
            self.ids.score11.text = ""
            self.ids.score12.text = ""
            p1s = [0]
            p2s = [0]
            p3s = [0]
            p4s = [0]
            p5s = [0]
            p6s = [0]
            p7s = [0]
            p8s = [0]
            p9s = [0]
            p10s = [0]
            p11s = [0]
            p12s = [0]
            round = 1
            self.ids.round.text = "Round 1"
            reset = 2
    def update_round(self, x):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        global p8s
        global p9s
        global p10s
        global p11s
        global p12s
        if x == 2:
            round += 1
            self.ids.round.text = "Round " + str(round)
            if len(p1s) > round:
                self.ids.p1.text = str(p1s[round - 1])
                self.ids.p2.text = str(p2s[round - 1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
                self.ids.p5.text = str(p5s[round - 1])
                self.ids.p6.text = str(p6s[round - 1])
                self.ids.p7.text = str(p7s[round - 1])
                self.ids.p8.text = str(p8s[round - 1])
                self.ids.p9.text = str(p9s[round - 1])
                self.ids.p10.text = str(p10s[round - 1])
                self.ids.p11.text = str(p11s[round - 1])
                self.ids.p12.text = str(p12s[round - 1])
        if round != 1:
            if x == 1:
                round -= 1
                self.ids.round.text = "Round " + str(round)
                self.ids.p1.text = str(p1s[round-1])
                self.ids.p2.text = str(p2s[round-1])
                self.ids.p3.text = str(p3s[round - 1])
                self.ids.p4.text = str(p4s[round - 1])
                self.ids.p5.text = str(p5s[round - 1])
                self.ids.p6.text = str(p6s[round - 1])
                self.ids.p7.text = str(p7s[round - 1])
                self.ids.p8.text = str(p8s[round - 1])
                self.ids.p9.text = str(p9s[round - 1])
                self.ids.p10.text = str(p10s[round - 1])
                self.ids.p11.text = str(p11s[round - 1])
                self.ids.p12.text = str(p12s[round - 1])
        if round == 1:
            self.ids.back.disabled = True
        else:
            self.ids.back.disabled = False
    def update_score(self, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, y):
        global round
        global p1s
        global p2s
        global p3s
        global p4s
        global p5s
        global p6s
        global p7s
        global p8s
        global p9s
        global p10s
        global p11s
        global p12s
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        score5 = 0
        score6 = 0
        score7 = 0
        score8 = 0
        score9 = 0
        score10 = 0
        score11 = 0
        score12 = 0
        s = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12]
        for n in list(range(len(s))):
            if s[n] == "":
                s[n] = "0"
            else:
                s[n] = int(s[n])
                p1s[round - 1] = s[0]
                p2s[round - 1] = s[1]
                p3s[round - 1] = s[2]
                p4s[round - 1] = s[3]
                p5s[round - 1] = s[4]
                p6s[round - 1] = s[5]
                p7s[round - 1] = s[6]
                p8s[round - 1] = s[7]
                p9s[round - 1] = s[8]
                p10s[round - 1] = s[9]
                p11s[round - 1] = s[10]
                p12s[round - 1] = s[11]
        if y == 2 and p1s[len(p1s)-1] != "0":
            p1s.append("0")
            p2s.append("0")
            p3s.append("0")
            p4s.append("0")
            p5s.append("0")
            p6s.append("0")
            p7s.append("0")
            p8s.append("0")
            p9s.append("0")
            p10s.append("0")
            p11s.append("0")
            p12s.append("0")
        if y == 2:
            p1s[round-1] = s[0]
            p2s[round-1] = s[1]
            p3s[round - 1] = s[2]
            p4s[round - 1] = s[3]
            p5s[round - 1] = s[4]
            p6s[round - 1] = s[5]
            p7s[round - 1] = s[6]
            p8s[round - 1] = s[7]
            p9s[round - 1] = s[8]
            p10s[round - 1] = s[9]
            p11s[round - 1] = s[10]
            p12s[round - 1] = s[11]
        x = len(p1s)
        for n in list(range(x)):
            score1 += int(p1s[n])
            score2 += int(p2s[n])
            score3 += int(p3s[n])
            score4 += int(p4s[n])
            score5 += int(p5s[n])
            score6 += int(p6s[n])
            score7 += int(p7s[n])
            score8 += int(p8s[n])
            score9 += int(p9s[n])
            score10 += int(p10s[n])
            score11 += int(p11s[n])
            score12 += int(p12s[n])
        self.ids.p1.text = ""
        self.ids.p2.text = ""
        self.ids.p3.text = ""
        self.ids.p4.text = ""
        self.ids.p5.text = ""
        self.ids.p6.text = ""
        self.ids.p7.text = ""
        self.ids.p8.text = ""
        self.ids.p9.text = ""
        self.ids.p10.text = ""
        self.ids.p11.text = ""
        self.ids.p12.text = ""
        self.ids.score1.text = str(score1)
        self.ids.score2.text = str(score2)
        self.ids.score3.text = str(score3)
        self.ids.score4.text = str(score4)
        self.ids.score5.text = str(score5)
        self.ids.score6.text = str(score6)
        self.ids.score7.text = str(score7)
        self.ids.score8.text = str(score8)
        self.ids.score9.text = str(score9)
        self.ids.score10.text = str(score10)
        self.ids.score11.text = str(score11)
        self.ids.score12.text = str(score12)

    def check_next(self, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12):
        global round
        x = 0
        y = 0
        if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "" and t6 != "" and t7 != "" and t8 != "" and t9 != "" and t10 != "" and t11 != "" and t12 != "":
            self.ids.next.disabled = False
        else:
            self.ids.next.disabled = True
        t = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12]
        if round != 1:
            for n in list(range(len(t))):
                if t[n] != "":
                    x = 1
                if t[n] == "":
                    y = 1
            if x == 1 and y == 1:
                self.ids.back.disabled = True
            else:
                self.ids.back.disabled = False

class AreYouSureWindow(Screen):
    def update_check(self, x):
        global check
        global reset
        if x == 2:
            check = 1
            reset = 1
        else:
            if check == 2:
                self.ids.no.text = "No"
            elif check == 3:
                self.ids.no.text = " No "
            elif check == 4:
                self.ids.no.text = "  No  "
            elif check == 5:
                self.ids.no.text = "   No   "
            elif check == 6:
                self.ids.no.text = "    No    "
            elif check == 7:
                self.ids.no.text = "     No     "
            elif check == 8:
                self.ids.no.text = "      No      "
            elif check == 9:
                self.ids.no.text = "       No       "
            elif check == 10:
                self.ids.no.text = "        No        "
            elif check == 11:
                self.ids.no.text = "         No         "
            elif check == 12:
                self.ids.no.text = "          No          "

class WindowManager(ScreenManager):
    pass

kv = Builder.load_string("""
<BackgroundColor@Widget>
    background_color: 1, 1, 1, 1
    canvas.before:
        Color:
            rgba: root.background_color
        Rectangle:
            size: self.size
            pos: self.pos
<BackgroundLabel@Label+BackgroundColor>
    background_color: 0, 0, 0, 0
    # to r 0, g 0, b 0, a 0

WindowManager:
    MainWindow:
    WhichScoreWindow:
    ScoreWindow:
    Score2Window:
    GameWindow:
    Name2Window:
    Game2PlayerWindow:
    Name3Window:
    Game3PlayerWindow:
    Name4Window:
    Game4PlayerWindow:
    Name5Window:
    Game5PlayerWindow:
    Name6Window:
    Game6PlayerWindow:
    Name7Window:
    Game7PlayerWindow:
    Name8Window:
    Game8PlayerWindow:
    Name9Window:
    Game9PlayerWindow:
    Name10Window:
    Game10PlayerWindow:
    Name11Window:
    Game11PlayerWindow:
    Name12Window:
    Game12PlayerWindow:
    AreYouSureWindow:

<MainWindow>:
    name: "main"

    GridLayout:
        cols: 1
        Button:
            id: resume
            text: "Resume Game"
            background_color: 1,1,1,0.5
            on_release:
                root.check_check()
                if self.text == "Resume Game": app.root.current = "game"
                elif self.text == " Resume Game ": app.root.current = "game2"
                elif self.text == "  Resume Game  ": app.root.current = "game3"
                elif self.text == "   Resume Game   ": app.root.current = "game4"
                elif self.text == "    Resume Game    ": app.root.current = "game5"
                elif self.text == "     Resume Game     ": app.root.current = "game6"
                elif self.text == "      Resume Game      ": app.root.current = "game7"
                elif self.text == "       Resume Game       ": app.root.current = "game8"
                elif self.text == "        Resume Game        ": app.root.current = "game9"
                elif self.text == "         Resume Game         ": app.root.current = "game10"
                elif self.text == "          Resume Game          ": app.root.current = "game11"
                elif self.text == "           Resume Game           ": app.root.current = "game12"
                root.manager.transition.direction = "left"
        Button:
            text: "Quick Score"
            background_color: 1,1,1,0.5
            on_release:
                root.check_check()
                app.root.current = "whichscore"
                root.manager.transition.direction = "left"
        Button:
            text: "Exit App"
            background_color: 1,1,1,0.5
            on_release: app.stop()

<WhichScoreWindow>:
    name: "whichscore"
    GridLayout:
        cols: 1
        Label: 
            text: "Which version of baseball would you like to score?"
            background_color: 1,1,1,0.5
        Button:
            text: "Regular 6x2"
            background_color: 1,1,1,0.5
            on_release:
                app.root.current = "score"
                root.manager.transition.direction = "left"
        Button:
            text: "Alternate 5x3"
            background_color: 1,1,1,0.5
            on_release:
                app.root.current = "score2"
                root.manager.transition.direction = "left"
                
<ScoreWindow>:
    name: "score"

    GridLayout:
        cols: 1
        Label:
            text: '1. The blue rows represent your cards.\\n2. Select number from green rows.\\n3. Select your cards that have this value.\\n4. When done, click score to find score.'
        
        GridLayout:
            cols: 6

            Button:
                id: c1
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text1()
            Button:
                id: c2
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text2()
            Button:
                id: c3
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text3()
            Button:
                id: c4
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text4()
            Button:
                id: c5
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text5()
            Button:
                id: c6
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text6()
        GridLayout:
            cols: 6
            Button:
                id: c7
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text7()
            Button:
                id: c8
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text8()
            Button:
                id: c9
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text9()
            Button:
                id: c10
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text10()
            Button:
                id: c11
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text11()
            Button:
                id: c12
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text12()
                    
        GridLayout:
            cols: 6
            Button:
                text: '1'
                background_color: 0,1,0,1
                id: s1
                on_release: root.create_new_number(s1.text)
            Button:
                text: '2'
                background_color: 0,1,0,1
                id: s2
                on_release: root.create_new_number(s2.text)
            Button:
                text: '3'
                background_color: 0,1,0,1
                id: s3
                on_release: root.create_new_number(s3.text)  
            Button:
                text: '4'
                background_color: 0,1,0,1
                id: s4
                on_release: root.create_new_number(s4.text)
            Button:
                text: '5'
                background_color: 0,1,0,1
                id: s5
                on_release: root.create_new_number(s5.text)
            Button:
                text: '6'
                background_color: 0,1,0,1
                id: s6
                on_release: root.create_new_number(s6.text)  
        GridLayout:
            cols: 6
            Button:
                text: '7'
                background_color: 0,1,0,1
                id: s7
                on_release: root.create_new_number(s7.text)
            Button:
                text: '8'
                background_color: 0,1,0,1
                id: s8
                on_release: root.create_new_number(s8.text)
            Button:
                text: '9'
                background_color: 0,1,0,1
                id: s9
                on_release: root.create_new_number(s9.text)  
            Button:
                text: '10'
                background_color: 0,1,0,1
                id: s10
                on_release: root.create_new_number(s10.text)
            Button:
                text: '11'
                background_color: 0,1,0,1
                id: s11
                on_release: root.create_new_number(s11.text)
            Button:
                text: '12'
                background_color: 0,1,0,1
                id: s12
                on_release: root.create_new_number(s12.text)
        GridLayout:
            cols: 6
            Button:
                text: 'Skip\\n-Bo'
                background_color: 0,1,0,1
                on_release: root.create_new_number('Skip-Bo')      
            
            Button:
                text: "Score"
                background_color: 1,0,0,1
                on_release:
                    root.get_score(c1.text, c2.text, c3.text, c4.text, c5.text, c6.text, c7.text, c8.text, c9.text, c10.text, c11.text, c12.text)
            Button:
                text: "Reset"
                background_color: 1,0,0,1
                on_release:
                    c1.text = ""
                    c2.text = ""
                    c3.text = ""
                    c4.text = ""
                    c5.text = ""
                    c6.text = ""
                    c7.text = ""
                    c8.text = ""
                    c9.text = ""
                    c10.text = ""
                    c11.text = ""
                    c12.text = ""
            Button:
                text: "Menu"
                background_color: 1,0,0,1
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            Button:
                text: "Help"
                background_color: 1,0,0,1
                on_release: root.get_help()
            Button:
                id: gotogame
                text: "Game"
                background_color: 1,0,0,1
                on_release:
                    root.check_check()
                    if self.text == "Game": app.root.current = "game"
                    elif self.text == " Game ": app.root.current = "game2"
                    elif self.text == "  Game  ": app.root.current = "game3"
                    elif self.text == "   Game   ": app.root.current = "game4"
                    elif self.text == "    Game    ": app.root.current = "game5"
                    elif self.text == "     Game     ": app.root.current = "game6"
                    elif self.text == "      Game      ": app.root.current = "game7"
                    elif self.text == "       Game       ": app.root.current = "game8"
                    elif self.text == "        Game        ": app.root.current = "game9"
                    elif self.text == "         Game         ": app.root.current = "game10"
                    elif self.text == "          Game          ": app.root.current = "game11"
                    elif self.text == "           Game           ": app.root.current = "game12"
                    root.manager.transition.direction = "down"
<Score2Window>:
    name: "score2"
    GridLayout:
        cols: 1
        Label:
            text: '1. The blue rows represent your cards.\\n2. Select number from green rows.\\n3. Select your cards that have this value.\\n4. When done, click score to find score.'
        
        GridLayout:
            cols: 5

            Button:
                id: c1
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text1()
            Button:
                id: c2
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text2()
            Button:
                id: c3
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text3()
            Button:
                id: c4
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text4()
            Button:
                id: c5
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text5()
        GridLayout:
            cols: 5
            Button:
                id: c6
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text6()
            Button:
                id: c7
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text7()
            Button:
                id: c8
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text8()
            Button:
                id: c9
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text9()
            Button:
                id: c10
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text10()
        GridLayout:
            cols: 5
            Button:
                id: c11
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text11()
            Button:
                id: c12
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text12()
            Button:
                id: c13
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text13()
            Button:
                id: c14
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text14()
            Button:
                id: c15
                background_color: 0,0.5,1,1
                on_release: 
                    root.change_text15()
                    
        GridLayout:
            cols: 6
            Button:
                text: '1'
                background_color: 0,1,0,1
                id: s1
                on_release: root.create_new_number(s1.text)
            Button:
                text: '2'
                background_color: 0,1,0,1
                id: s2
                on_release: root.create_new_number(s2.text)
            Button:
                text: '3'
                background_color: 0,1,0,1
                id: s3
                on_release: root.create_new_number(s3.text)  
            Button:
                text: '4'
                background_color: 0,1,0,1
                id: s4
                on_release: root.create_new_number(s4.text)
            Button:
                text: '5'
                background_color: 0,1,0,1
                id: s5
                on_release: root.create_new_number(s5.text)
            Button:
                text: '6'
                background_color: 0,1,0,1
                id: s6
                on_release: root.create_new_number(s6.text)  
        GridLayout:
            cols: 6
            Button:
                text: '7'
                background_color: 0,1,0,1
                id: s7
                on_release: root.create_new_number(s7.text)
            Button:
                text: '8'
                background_color: 0,1,0,1
                id: s8
                on_release: root.create_new_number(s8.text)
            Button:
                text: '9'
                background_color: 0,1,0,1
                id: s9
                on_release: root.create_new_number(s9.text)  
            Button:
                text: '10'
                background_color: 0,1,0,1
                id: s10
                on_release: root.create_new_number(s10.text)
            Button:
                text: '11'
                background_color: 0,1,0,1
                id: s11
                on_release: root.create_new_number(s11.text)
            Button:
                text: '12'
                background_color: 0,1,0,1
                id: s12
                on_release: root.create_new_number(s12.text)
        GridLayout:
            cols: 6
            Button:
                text: 'Skip\\n-Bo'
                background_color: 0,1,0,1
                on_release: root.create_new_number('Skip-Bo')      
            
            Button:
                text: "Score"
                background_color: 1,0,0,1
                on_release:
                    root.get_score(c1.text, c2.text, c3.text, c4.text, c5.text, c6.text, c7.text, c8.text, c9.text, c10.text, c11.text, c12.text, c13.text, c14.text, c15.text)
            Button:
                text: "Reset"
                background_color: 1,0,0,1
                on_release:
                    c1.text = ""
                    c2.text = ""
                    c3.text = ""
                    c4.text = ""
                    c5.text = ""
                    c6.text = ""
                    c7.text = ""
                    c8.text = ""
                    c9.text = ""
                    c10.text = ""
                    c11.text = ""
                    c12.text = ""
                    c13.text = ""
                    c14.text = ""
                    c15.text = ""
            Button:
                text: "Menu"
                background_color: 1,0,0,1
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            Button:
                text: "Help"
                background_color: 1,0,0,1
                on_release: root.get_help()
            Button:
                id: gotogame
                text: "Game"
                background_color: 1,0,0,1
                on_release:
                    root.check_check()
                    if self.text == "Game": app.root.current = "game"
                    elif self.text == " Game ": app.root.current = "game2"
                    elif self.text == "  Game  ": app.root.current = "game3"
                    elif self.text == "   Game   ": app.root.current = "game4"
                    elif self.text == "    Game    ": app.root.current = "game5"
                    elif self.text == "     Game     ": app.root.current = "game6"
                    elif self.text == "      Game      ": app.root.current = "game7"
                    elif self.text == "       Game       ": app.root.current = "game8"
                    elif self.text == "        Game        ": app.root.current = "game9"
                    elif self.text == "         Game         ": app.root.current = "game10"
                    elif self.text == "          Game          ": app.root.current = "game11"
                    elif self.text == "           Game           ": app.root.current = "game12"
                    root.manager.transition.direction = "down"

<GameWindow>
    name: "game"
    GridLayout:
        cols:3
        Button:
            text: 'Menu'
            background_color: 1,0,0,1
            on_release:
                app.root.current = "main"
                root.manager.transition.direction = "right"
        BackgroundLabel:
            text: 'Number of\\nPlayers:'
            background_color: 1, 1, 1, 0.2
        Button:
            text: 'Quick Score'
            background_color: 1,0,0,1
            on_release:
                app.root.current = "whichscore"
                root.manager.transition.direction = "up"
        Button:
            text: '<'
            background_color: 1,0,0,0.6
            on_release:
                root.update_players(1)
        Label:
            id: players
            text: '2'
        Button:
            text: '>'
            background_color: 1,0,0,0.6
            on_release:
                root.update_players(2)
        Label:
            text: ""
        Button:
            id: start
            text: 'Next'
            background_color: 1,0,0,1
            on_release: 
                root.update_check()
                if self.text == "Next": app.root.current = "name2"
                elif self.text == " Next ": app.root.current = "name3"
                elif self.text == "  Next  ": app.root.current = "name4"
                elif self.text == "   Next   ": app.root.current = "name5"
                elif self.text == "    Next    ": app.root.current = "name6"
                elif self.text == "     Next     ": app.root.current = "name7"
                elif self.text == "      Next      ": app.root.current = "name8"
                elif self.text == "       Next       ": app.root.current = "name9"
                elif self.text == "        Next        ": app.root.current = "name10"
                elif self.text == "         Next         ": app.root.current = "name11"
                elif self.text == "          Next          ": app.root.current = "name12"
                root.manager.transition.direction = "left"
        Label:
            text: ""
                
<Name2Window>
    name: "name2"
    GridLayout:
        cols: 1
        GridLayout:
            cols: 2
            Label:
                text: "Player 1"
            TextInput:
                id: p1
                on_text: root.check_next(p1.text, p2.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 2"
            TextInput:
                id: p2
                on_text: root.check_next(p1.text, p2.text)
        GridLayout:
            cols:2
            Button:
                id: next
                disabled: True
                text: "Start Game"
                on_press:
                    root.start_game(p1.text, p2.text)
                    app.root.current = "game2"
                    root.manager.transition.direction = "left"
            Button:
                text: "Back"
                on_press:
                    root.back()
                    app.root.current = "game"
                    root.manager.transition.direction = "right"
        
                
<Game2PlayerWindow>
    name: "game2"
    GridLayout:
        id: grid
        cols: 1
        Button:
            text: '       PRESS ME to        \\n       setup game.'
            background_color: 0, 1, 0, 1
            on_release: 
                root.setup()
        GridLayout:
            cols: 3
            Button:
                id: back
                text: '<'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, 1)
                    root.update_round(1)
            BackgroundLabel:
                text: 'Round 1'
                id: round
            Button:
                id: next
                text: '>'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, 2)
                    root.update_round(2)
        GridLayout:
            cols: 3
            BackgroundLabel:
                text: 'Names'
                background_color: 1, 0, 0, 0.3
            BackgroundLabel:
                text: 'Score'
                background_color: 1, 0, 1, 0.3
            BackgroundLabel:
                text: 'Totals'
                background_color: 0, 0, 1, 0.45
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p1n
                text: 'Player 1'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ""
                id: p1
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text)
            BackgroundLabel:
                id: score1
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p2n
                text: 'Player 2'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p2
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text)
            BackgroundLabel:
                id: score2
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            Button:
                text: "Main Menu"
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            Button:
                text: "Quick Score"
                on_release:
                    app.root.current = "whichscore"
                    root.manager.transition.direction = "up"
            Button:
                text: "End Game"
                on_release:
                    app.root.current = "rusure"
                    root.manager.transition.direction = "left"

<Name3Window>
    name: "name3"
    GridLayout:
        cols: 1
        GridLayout:
            cols: 2
            Label:
                text: "Player 1"
            TextInput:
                id: p1
                on_text: root.check_next(p1.text, p2.text, p3.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 2"
            TextInput:
                id: p2
                on_text: root.check_next(p1.text, p2.text, p3.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 3"
            TextInput:
                id: p3
                on_text: root.check_next(p1.text, p2.text, p3.text)
        GridLayout:
            cols:2
            Button:
                id: next
                disabled: True
                text: "Start Game"
                on_press:
                    root.start_game(p1.text, p2.text, p3.text)
                    app.root.current = "game3"
                    root.manager.transition.direction = "left"
            Button:
                text: "Back"
                on_press:
                    root.back()
                    app.root.current = "game"
                    root.manager.transition.direction = "right"
                
<Game3PlayerWindow>
    name: "game3"
    GridLayout:
        id: grid
        cols: 1
        Button:
            text: '       PRESS ME to        \\n       setup game.'
            background_color: 0, 1, 0, 1
            on_release: 
                root.setup()
        GridLayout:
            cols: 3
            Button:
                id: back
                text: '<'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, 1)
                    root.update_round(1)
            BackgroundLabel:
                text: 'Round 1'
                id: round
            Button:
                id: next
                text: '>'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, 2)
                    root.update_round(2)
        GridLayout:
            cols: 3
            BackgroundLabel:
                text: 'Names'
                background_color: 1, 0, 0, 0.3
            BackgroundLabel:
                text: 'Score'
                background_color: 1, 0, 1, 0.3
            BackgroundLabel:
                text: 'Totals'
                background_color: 0, 0, 1, 0.45
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p1n
                text: 'Player 1'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ""
                id: p1
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text)
            BackgroundLabel:
                id: score1
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p2n
                text: 'Player 2'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p2
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text)
            BackgroundLabel:
                id: score2
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p3n
                text: 'Player 3'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p3
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text)
            BackgroundLabel:
                id: score3
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            Button:
                text: "Main Menu"
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            Button:
                text: "Quick Score"
                on_release:
                    app.root.current = "whichscore"
                    root.manager.transition.direction = "up"
            Button:
                text: "End Game"
                on_release:
                    app.root.current = "rusure"
                    root.manager.transition.direction = "left"
                
<Name4Window>
    name: "name4"
    GridLayout:
        cols: 1
        GridLayout:
            cols: 2
            Label:
                text: "Player 1"
            TextInput:
                id: p1
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 2"
            TextInput:
                id: p2
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 3"
            TextInput:
                id: p3
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 4"
            TextInput:
                id: p4
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text)
        GridLayout:
            cols:2
            Button:
                id: next
                disabled: True
                text: "Start Game"
                on_press:
                    root.start_game(p1.text, p2.text, p3.text, p4.text)
                    app.root.current = "game4"
                    root.manager.transition.direction = "left"
            Button:
                text: "Back"
                on_press:
                    root.back()
                    app.root.current = "game"
                    root.manager.transition.direction = "right"
                
<Game4PlayerWindow>
    name: "game4"
    GridLayout:
        id: grid
        cols: 1
        Button:
            text: '       PRESS ME to        \\n       setup game.'
            background_color: 0, 1, 0, 1
            on_release: 
                root.setup()
        GridLayout:
            cols: 3
            Button:
                id: back
                text: '<'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, 1)
                    root.update_round(1)
            BackgroundLabel:
                text: 'Round 1'
                id: round
            Button:
                id: next
                text: '>'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, 2)
                    root.update_round(2)
        GridLayout:
            cols: 3
            BackgroundLabel:
                text: 'Names'
                background_color: 1, 0, 0, 0.3
            BackgroundLabel:
                text: 'Score'
                background_color: 1, 0, 1, 0.3
            BackgroundLabel:
                text: 'Totals'
                background_color: 0, 0, 1, 0.45
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p1n
                text: 'Player 1'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ""
                id: p1
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text)
            BackgroundLabel:
                id: score1
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p2n
                text: 'Player 2'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p2
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text)
            BackgroundLabel:
                id: score2
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p3n
                text: 'Player 3'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p3
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text)
            BackgroundLabel:
                id: score3
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p4n
                text: 'Player 4'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p4
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text)
            BackgroundLabel:
                id: score4
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            Button:
                text: "Main Menu"
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            Button:
                text: "Quick Score"
                on_release:
                    app.root.current = "whichscore"
                    root.manager.transition.direction = "up"
            Button:
                text: "End Game"
                on_release:
                    app.root.current = "rusure"
                    root.manager.transition.direction = "left"
                    
<Name5Window>
    name: "name5"
    GridLayout:
        cols: 1
        GridLayout:
            cols: 2
            Label:
                text: "Player 1"
            TextInput:
                id: p1
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 2"
            TextInput:
                id: p2
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 3"
            TextInput:
                id: p3
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 4"
            TextInput:
                id: p4
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 5"
            TextInput:
                id: p5
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text)
        GridLayout:
            cols:2
            Button:
                id: next
                disabled: True
                text: "Start Game"
                on_press:
                    root.start_game(p1.text, p2.text, p3.text, p4.text, p5.text)
                    app.root.current = "game5"
                    root.manager.transition.direction = "left"
            Button:
                text: "Back"
                on_press:
                    root.back()
                    app.root.current = "game"
                    root.manager.transition.direction = "right"
                
<Game5PlayerWindow>
    name: "game5"
    GridLayout:
        id: grid
        cols: 1
        Button:
            text: '       PRESS ME to        \\n       setup game.'
            background_color: 0, 1, 0, 1
            on_release: 
                root.setup()
        GridLayout:
            cols: 3
            Button:
                id: back
                text: '<'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, p5.text, 1)
                    root.update_round(1)
            BackgroundLabel:
                text: 'Round 1'
                id: round
            Button:
                id: next
                text: '>'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, p5.text, 2)
                    root.update_round(2)
        GridLayout:
            cols: 3
            BackgroundLabel:
                text: 'Names'
                background_color: 1, 0, 0, 0.3
            BackgroundLabel:
                text: 'Score'
                background_color: 1, 0, 1, 0.3
            BackgroundLabel:
                text: 'Totals'
                background_color: 0, 0, 1, 0.45
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p1n
                text: 'Player 1'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ""
                id: p1
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text)
            BackgroundLabel:
                id: score1
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p2n
                text: 'Player 2'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p2
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text)
            BackgroundLabel:
                id: score2
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p3n
                text: 'Player 3'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p3
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text)
            BackgroundLabel:
                id: score3
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p4n
                text: 'Player 4'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p4
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text)
            BackgroundLabel:
                id: score4
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p5n
                text: 'Player 5'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p5
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text)
            BackgroundLabel:
                id: score5
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            Button:
                text: "Main Menu"
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            Button:
                text: "Quick Score"
                on_release:
                    app.root.current = "whichscore"
                    root.manager.transition.direction = "up"
            Button:
                text: "End Game"
                on_release:
                    app.root.current = "rusure"
                    root.manager.transition.direction = "left"

<Name6Window>
    name: "name6"
    GridLayout:
        cols: 1
        GridLayout:
            cols: 2
            Label:
                text: "Player 1"
            TextInput:
                id: p1
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 2"
            TextInput:
                id: p2
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 3"
            TextInput:
                id: p3
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 4"
            TextInput:
                id: p4
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 5"
            TextInput:
                id: p5
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 6"
            TextInput:
                id: p6
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text)
        GridLayout:
            cols:2
            Button:
                id: next
                disabled: True
                text: "Start Game"
                on_press:
                    root.start_game(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text)
                    app.root.current = "game6"
                    root.manager.transition.direction = "left"
            Button:
                text: "Back"
                on_press:
                    root.back()
                    app.root.current = "game"
                    root.manager.transition.direction = "right"
                
<Game6PlayerWindow>
    name: "game6"
    GridLayout:
        id: grid
        cols: 1
        Button:
            text: '       PRESS ME to        \\n       setup game.'
            background_color: 0, 1, 0, 1
            on_release: 
                root.setup()
        GridLayout:
            cols: 3
            Button:
                id: back
                text: '<'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, 1)
                    root.update_round(1)
            BackgroundLabel:
                text: 'Round 1'
                id: round
            Button:
                id: next
                text: '>'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, 2)
                    root.update_round(2)
        GridLayout:
            cols: 3
            BackgroundLabel:
                text: 'Names'
                background_color: 1, 0, 0, 0.3
            BackgroundLabel:
                text: 'Score'
                background_color: 1, 0, 1, 0.3
            BackgroundLabel:
                text: 'Totals'
                background_color: 0, 0, 1, 0.45
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p1n
                text: 'Player 1'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ""
                id: p1
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text)
            BackgroundLabel:
                id: score1
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p2n
                text: 'Player 2'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p2
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text)
            BackgroundLabel:
                id: score2
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p3n
                text: 'Player 3'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p3
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text)
            BackgroundLabel:
                id: score3
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p4n
                text: 'Player 4'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p4
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text)
            BackgroundLabel:
                id: score4
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p5n
                text: 'Player 5'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p5
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text)
            BackgroundLabel:
                id: score5
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p6n
                text: 'Player 6'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p6
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text)
            BackgroundLabel:
                id: score6
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            Button:
                text: "Main Menu"
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            Button:
                text: "Quick Score"
                on_release:
                    app.root.current = "whichscore"
                    root.manager.transition.direction = "up"
            Button:
                text: "End Game"
                on_release:
                    app.root.current = "rusure"
                    root.manager.transition.direction = "left"
                    
<Name7Window>
    name: "name7"
    GridLayout:
        cols: 1
        GridLayout:
            cols: 2
            Label:
                text: "Player 1"
            TextInput:
                id: p1
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 2"
            TextInput:
                id: p2
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 3"
            TextInput:
                id: p3
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 4"
            TextInput:
                id: p4
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 5"
            TextInput:
                id: p5
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 6"
            TextInput:
                id: p6
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 7"
            TextInput:
                id: p7
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text)
        GridLayout:
            cols:2
            Button:
                id: next
                disabled: True
                text: "Start Game"
                on_press:
                    root.start_game(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text)
                    app.root.current = "game7"
                    root.manager.transition.direction = "left"
            Button:
                text: "Back"
                on_press:
                    root.back()
                    app.root.current = "game"
                    root.manager.transition.direction = "right"
                
<Game7PlayerWindow>
    name: "game7"
    GridLayout:
        id: grid
        cols: 1
        Button:
            text: '       PRESS ME to        \\n       setup game.'
            background_color: 0, 1, 0, 1
            on_release: 
                root.setup()
        GridLayout:
            cols: 3
            Button:
                id: back
                text: '<'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, 1)
                    root.update_round(1)
            BackgroundLabel:
                text: 'Round 1'
                id: round
            Button:
                id: next
                text: '>'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, 2)
                    root.update_round(2)
        GridLayout:
            cols: 3
            BackgroundLabel:
                text: 'Names'
                background_color: 1, 0, 0, 0.3
            BackgroundLabel:
                text: 'Score'
                background_color: 1, 0, 1, 0.3
            BackgroundLabel:
                text: 'Totals'
                background_color: 0, 0, 1, 0.45
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p1n
                text: 'Player 1'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ""
                id: p1
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text)
            BackgroundLabel:
                id: score1
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p2n
                text: 'Player 2'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p2
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text)
            BackgroundLabel:
                id: score2
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p3n
                text: 'Player 3'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p3
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text)
            BackgroundLabel:
                id: score3
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p4n
                text: 'Player 4'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p4
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text)
            BackgroundLabel:
                id: score4
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p5n
                text: 'Player 5'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p5
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text)
            BackgroundLabel:
                id: score5
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p6n
                text: 'Player 6'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p6
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text)
            BackgroundLabel:
                id: score6
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p7n
                text: 'Player 7'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p7
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text)
            BackgroundLabel:
                id: score7
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            Button:
                text: "Main Menu"
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            Button:
                text: "Quick Score"
                on_release:
                    app.root.current = "whichscore"
                    root.manager.transition.direction = "up"
            Button:
                text: "End Game"
                on_release:
                    app.root.current = "rusure"
                    root.manager.transition.direction = "left"
                    
<Name8Window>
    name: "name8"
    GridLayout:
        cols: 1
        GridLayout:
            cols: 2
            Label:
                text: "Player 1"
            TextInput:
                id: p1
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 2"
            TextInput:
                id: p2
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 3"
            TextInput:
                id: p3
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 4"
            TextInput:
                id: p4
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 5"
            TextInput:
                id: p5
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 6"
            TextInput:
                id: p6
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 7"
            TextInput:
                id: p7
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 8"
            TextInput:
                id: p8
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
        GridLayout:
            cols:2
            Button:
                id: next
                disabled: True
                text: "Start Game"
                on_press:
                    root.start_game(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
                    app.root.current = "game8"
                    root.manager.transition.direction = "left"
            Button:
                text: "Back"
                on_press:
                    root.back()
                    app.root.current = "game"
                    root.manager.transition.direction = "right"
                
<Game8PlayerWindow>
    name: "game8"
    GridLayout:
        id: grid
        cols: 1
        Button:
            text: '       PRESS ME to        \\n       setup game.'
            background_color: 0, 1, 0, 1
            on_release: 
                root.setup()
        GridLayout:
            cols: 3
            Button:
                id: back
                text: '<'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, 1)
                    root.update_round(1)
            BackgroundLabel:
                text: 'Round 1'
                id: round
            Button:
                id: next
                text: '>'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, 2)
                    root.update_round(2)
        GridLayout:
            cols: 3
            BackgroundLabel:
                text: 'Names'
                background_color: 1, 0, 0, 0.3
            BackgroundLabel:
                text: 'Score'
                background_color: 1, 0, 1, 0.3
            BackgroundLabel:
                text: 'Totals'
                background_color: 0, 0, 1, 0.45
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p1n
                text: 'Player 1'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ""
                id: p1
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
            BackgroundLabel:
                id: score1
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p2n
                text: 'Player 2'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p2
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
            BackgroundLabel:
                id: score2
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p3n
                text: 'Player 3'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p3
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
            BackgroundLabel:
                id: score3
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p4n
                text: 'Player 4'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p4
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
            BackgroundLabel:
                id: score4
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p5n
                text: 'Player 5'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p5
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
            BackgroundLabel:
                id: score5
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p6n
                text: 'Player 6'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p6
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
            BackgroundLabel:
                id: score6
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p7n
                text: 'Player 7'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p7
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
            BackgroundLabel:
                id: score7
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p8n
                text: 'Player 8'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p8
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text)
            BackgroundLabel:
                id: score8
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            Button:
                text: "Main Menu"
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            Button:
                text: "Quick Score"
                on_release:
                    app.root.current = "whichscore"
                    root.manager.transition.direction = "up"
            Button:
                text: "End Game"
                on_release:
                    app.root.current = "rusure"
                    root.manager.transition.direction = "left"

<Name9Window>
    name: "name9"
    GridLayout:
        cols: 1
        GridLayout:
            cols: 2
            Label:
                text: "Player 1"
            TextInput:
                id: p1
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 2"
            TextInput:
                id: p2
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 3"
            TextInput:
                id: p3
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 4"
            TextInput:
                id: p4
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 5"
            TextInput:
                id: p5
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 6"
            TextInput:
                id: p6
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 7"
            TextInput:
                id: p7
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 8"
            TextInput:
                id: p8
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 9"
            TextInput:
                id: p9
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
        GridLayout:
            cols:2
            Button:
                id: next
                disabled: True
                text: "Start Game"
                on_press:
                    root.start_game(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
                    app.root.current = "game9"
                    root.manager.transition.direction = "left"
            Button:
                text: "Back"
                on_press:
                    root.back()
                    app.root.current = "game"
                    root.manager.transition.direction = "right"
                
<Game9PlayerWindow>
    name: "game9"
    GridLayout:
        id: grid
        cols: 1
        Button:
            text: '       PRESS ME to        \\n       setup game.'
            background_color: 0, 1, 0, 1
            on_release: 
                root.setup()
        GridLayout:
            cols: 3
            Button:
                id: back
                text: '<'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, 1)
                    root.update_round(1)
            BackgroundLabel:
                text: 'Round 1'
                id: round
            Button:
                id: next
                text: '>'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, 2)
                    root.update_round(2)
        GridLayout:
            cols: 3
            BackgroundLabel:
                text: 'Names'
                background_color: 1, 0, 0, 0.3
            BackgroundLabel:
                text: 'Score'
                background_color: 1, 0, 1, 0.3
            BackgroundLabel:
                text: 'Totals'
                background_color: 0, 0, 1, 0.45
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p1n
                text: 'Player 1'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ""
                id: p1
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
            BackgroundLabel:
                id: score1
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p2n
                text: 'Player 2'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p2
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
            BackgroundLabel:
                id: score2
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p3n
                text: 'Player 3'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p3
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
            BackgroundLabel:
                id: score3
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p4n
                text: 'Player 4'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p4
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
            BackgroundLabel:
                id: score4
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p5n
                text: 'Player 5'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p5
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
            BackgroundLabel:
                id: score5
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p6n
                text: 'Player 6'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p6
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
            BackgroundLabel:
                id: score6
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p7n
                text: 'Player 7'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p7
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
            BackgroundLabel:
                id: score7
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p8n
                text: 'Player 8'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p8
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
            BackgroundLabel:
                id: score8
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p9n
                text: 'Player 9'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p9
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text)
            BackgroundLabel:
                id: score9
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            Button:
                text: "Main Menu"
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            Button:
                text: "Quick Score"
                on_release:
                    app.root.current = "whichscore"
                    root.manager.transition.direction = "up"
            Button:
                text: "End Game"
                on_release:
                    app.root.current = "rusure"
                    root.manager.transition.direction = "left"
                    
<Name10Window>
    name: "name10"
    GridLayout:
        cols: 1
        GridLayout:
            cols: 2
            Label:
                text: "Player 1"
            TextInput:
                id: p1
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 2"
            TextInput:
                id: p2
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 3"
            TextInput:
                id: p3
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 4"
            TextInput:
                id: p4
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 5"
            TextInput:
                id: p5
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 6"
            TextInput:
                id: p6
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 7"
            TextInput:
                id: p7
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 8"
            TextInput:
                id: p8
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 9"
            TextInput:
                id: p9
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 10"
            TextInput:
                id: p10
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
        GridLayout:
            cols:2
            Button:
                id: next
                disabled: True
                text: "Start Game"
                on_press:
                    root.start_game(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
                    app.root.current = "game10"
                    root.manager.transition.direction = "left"
            Button:
                text: "Back"
                on_press:
                    root.back()
                    app.root.current = "game"
                    root.manager.transition.direction = "right"
                
<Game10PlayerWindow>
    name: "game10"
    GridLayout:
        id: grid
        cols: 1
        Button:
            text: '       PRESS ME to        \\n       setup game.'
            background_color: 0, 1, 0, 1
            on_release: 
                root.setup()
        GridLayout:
            cols: 3
            Button:
                id: back
                text: '<'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, 1)
                    root.update_round(1)
            BackgroundLabel:
                text: 'Round 1'
                id: round
            Button:
                id: next
                text: '>'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, 2)
                    root.update_round(2)
        GridLayout:
            cols: 3
            BackgroundLabel:
                text: 'Names'
                background_color: 1, 0, 0, 0.3
            BackgroundLabel:
                text: 'Score'
                background_color: 1, 0, 1, 0.3
            BackgroundLabel:
                text: 'Totals'
                background_color: 0, 0, 1, 0.45
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p1n
                text: 'Player 1'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ""
                id: p1
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
            BackgroundLabel:
                id: score1
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p2n
                text: 'Player 2'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p2
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
            BackgroundLabel:
                id: score2
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p3n
                text: 'Player 3'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p3
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
            BackgroundLabel:
                id: score3
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p4n
                text: 'Player 4'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p4
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
            BackgroundLabel:
                id: score4
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p5n
                text: 'Player 5'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p5
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
            BackgroundLabel:
                id: score5
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p6n
                text: 'Player 6'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p6
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
            BackgroundLabel:
                id: score6
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p7n
                text: 'Player 7'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p7
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
            BackgroundLabel:
                id: score7
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p8n
                text: 'Player 8'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p8
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
            BackgroundLabel:
                id: score8
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p9n
                text: 'Player 9'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p9
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
            BackgroundLabel:
                id: score9
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p10n
                text: 'Player 10'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p10
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text)
            BackgroundLabel:
                id: score10
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            Button:
                text: "Main Menu"
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            Button:
                text: "Quick Score"
                on_release:
                    app.root.current = "whichscore"
                    root.manager.transition.direction = "up"
            Button:
                text: "End Game"
                on_release:
                    app.root.current = "rusure"
                    root.manager.transition.direction = "left"
                    
<Name11Window>
    name: "name11"
    GridLayout:
        cols: 1
        GridLayout:
            cols: 2
            Label:
                text: "Player 1"
            TextInput:
                id: p1
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 2"
            TextInput:
                id: p2
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 3"
            TextInput:
                id: p3
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 4"
            TextInput:
                id: p4
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 5"
            TextInput:
                id: p5
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 6"
            TextInput:
                id: p6
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 7"
            TextInput:
                id: p7
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 8"
            TextInput:
                id: p8
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 9"
            TextInput:
                id: p9
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 10"
            TextInput:
                id: p10
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 11"
            TextInput:
                id: p11
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
        GridLayout:
            cols:2
            Button:
                id: next
                disabled: True
                text: "Start Game"
                on_press:
                    root.start_game(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
                    app.root.current = "game11"
                    root.manager.transition.direction = "left"
            Button:
                text: "Back"
                on_press:
                    root.back()
                    app.root.current = "game"
                    root.manager.transition.direction = "right"
                
<Game11PlayerWindow>
    name: "game11"
    GridLayout:
        id: grid
        cols: 1
        Button:
            text: '       PRESS ME to        \\n       setup game.'
            background_color: 0, 1, 0, 1
            on_release: 
                root.setup()
        GridLayout:
            cols: 3
            Button:
                id: back
                text: '<'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, 1)
                    root.update_round(1)
            BackgroundLabel:
                text: 'Round 1'
                id: round
            Button:
                id: next
                text: '>'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, 2)
                    root.update_round(2)
        GridLayout:
            cols: 3
            BackgroundLabel:
                text: 'Names'
                background_color: 1, 0, 0, 0.3
            BackgroundLabel:
                text: 'Score'
                background_color: 1, 0, 1, 0.3
            BackgroundLabel:
                text: 'Totals'
                background_color: 0, 0, 1, 0.45
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p1n
                text: 'Player 1'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ""
                id: p1
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
            BackgroundLabel:
                id: score1
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p2n
                text: 'Player 2'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p2
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
            BackgroundLabel:
                id: score2
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p3n
                text: 'Player 3'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p3
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
            BackgroundLabel:
                id: score3
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p4n
                text: 'Player 4'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p4
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
            BackgroundLabel:
                id: score4
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p5n
                text: 'Player 5'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p5
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
            BackgroundLabel:
                id: score5
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p6n
                text: 'Player 6'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p6
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
            BackgroundLabel:
                id: score6
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p7n
                text: 'Player 7'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p7
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
            BackgroundLabel:
                id: score7
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p8n
                text: 'Player 8'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p8
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
            BackgroundLabel:
                id: score8
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p9n
                text: 'Player 9'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p9
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
            BackgroundLabel:
                id: score9
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p10n
                text: 'Player 10'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p10
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
            BackgroundLabel:
                id: score10
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p11n
                text: 'Player 11'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p11
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text)
            BackgroundLabel:
                id: score11
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            Button:
                text: "Main Menu"
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            Button:
                text: "Quick Score"
                on_release:
                    app.root.current = "whichscore"
                    root.manager.transition.direction = "up"
            Button:
                text: "End Game"
                on_release:
                    app.root.current = "rusure"
                    root.manager.transition.direction = "left"
                
<Name12Window>
    name: "name12"
    GridLayout:
        cols: 1
        GridLayout:
            cols: 2
            Label:
                text: "Player 1"
            TextInput:
                id: p1
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 2"
            TextInput:
                id: p2
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 3"
            TextInput:
                id: p3
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 4"
            TextInput:
                id: p4
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 5"
            TextInput:
                id: p5
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 6"
            TextInput:
                id: p6
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 7"
            TextInput:
                id: p7
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 8"
            TextInput:
                id: p8
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 9"
            TextInput:
                id: p9
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 10"
            TextInput:
                id: p10
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 11"
            TextInput:
                id: p11
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
        GridLayout:
            cols: 2
            Label:
                text: "Player 12"
            TextInput:
                id: p12
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
        GridLayout:
            cols:2
            Button:
                id: next
                disabled: True
                text: "Start Game"
                on_press:
                    root.start_game(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
                    app.root.current = "game12"
                    root.manager.transition.direction = "left"
            Button:
                text: "Back"
                on_press:
                    root.back()
                    app.root.current = "game"
                    root.manager.transition.direction = "right"
                
<Game12PlayerWindow>
    name: "game12"
    GridLayout:
        id: grid
        cols: 1
        Button:
            text: '       PRESS ME to        \\n       setup game.'
            background_color: 0, 1, 0, 1
            on_release: 
                root.setup()
        GridLayout:
            cols: 3
            Button:
                id: back
                text: '<'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text, 1)
                    root.update_round(1)
            BackgroundLabel:
                text: 'Round 1'
                id: round
            Button:
                id: next
                text: '>'
                background_color: 1, 0, 0, 0.6
                disabled: True
                on_release:
                    root.update_score(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text, 2)
                    root.update_round(2)
        GridLayout:
            cols: 3
            BackgroundLabel:
                text: 'Names'
                background_color: 1, 0, 0, 0.3
            BackgroundLabel:
                text: 'Score'
                background_color: 1, 0, 1, 0.3
            BackgroundLabel:
                text: 'Totals'
                background_color: 0, 0, 1, 0.45
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p1n
                text: 'Player 1'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ""
                id: p1
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
            BackgroundLabel:
                id: score1
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p2n
                text: 'Player 2'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p2
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
            BackgroundLabel:
                id: score2
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p3n
                text: 'Player 3'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p3
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
            BackgroundLabel:
                id: score3
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p4n
                text: 'Player 4'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p4
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
            BackgroundLabel:
                id: score4
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p5n
                text: 'Player 5'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p5
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
            BackgroundLabel:
                id: score5
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p6n
                text: 'Player 6'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p6
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
            BackgroundLabel:
                id: score6
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p7n
                text: 'Player 7'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p7
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
            BackgroundLabel:
                id: score7
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p8n
                text: 'Player 8'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p8
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
            BackgroundLabel:
                id: score8
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p9n
                text: 'Player 9'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p9
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
            BackgroundLabel:
                id: score9
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p10n
                text: 'Player 10'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p10
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
            BackgroundLabel:
                id: score10
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p11n
                text: 'Player 11'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p11
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
            BackgroundLabel:
                id: score11
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            BackgroundLabel:
                id: p12n
                text: 'Player 12'
                background_color: 1, 0, 0, 0.35
            TextInput:
                text: ''
                id: p12
                input_filter: 'int'
                on_text: root.check_next(p1.text, p2.text, p3.text, p4.text, p5.text, p6.text, p7.text, p8.text, p9.text, p10.text, p11.text, p12.text)
            BackgroundLabel:
                id: score12
                text: ''
                background_color: 0, 0, 1, 0.5
        GridLayout:
            cols: 3
            Button:
                text: "Main Menu"
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            Button:
                text: "Quick Score"
                on_release:
                    app.root.current = "whichscore"
                    root.manager.transition.direction = "up"
            Button:
                text: "End Game"
                on_release:
                    app.root.current = "rusure"
                    root.manager.transition.direction = "left"

<AreYouSureWindow>
    name: "rusure"
    GridLayout:
        cols: 1
        Label:
            text: "Are you sure you want to end the game?"
        GridLayout:
            cols: 2
            Button:
                text: "Yes"
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
                    root.update_check(2)
                    
            Button:
                id: no
                text: "No"
                on_release:
                    root.update_check(1)
                    if self.text == "No": app.root.current = "game2"
                    elif self.text == " No ": app.root.current = "game3"
                    elif self.text == "  No  ": app.root.current = "game4"
                    elif self.text == "   No   ": app.root.current = "game5"
                    elif self.text == "    No    ": app.root.current = "game6"
                    elif self.text == "     No     ": app.root.current = "game7"
                    elif self.text == "      No      ": app.root.current = "game8"
                    elif self.text == "       No       ": app.root.current = "game9"
                    elif self.text == "        No        ": app.root.current = "game10"
                    elif self.text == "         No         ": app.root.current = "game11"
                    elif self.text == "          No          ": app.root.current = "game12"
                    root.manager.transition.direction = "right"
""")

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()