import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
players = 2
check = 1

class MainWindow(Screen):
    def create_new_number(self, x):
        global wow
        wow = x
    def set_players(self):
        global players
        global check
        try:
            players
        except NameError:
            players = 2
        if check == 1:
            self.ids.resume.text = "Resume Game"
        else:
            self.ids.resume.text = "Resume Game "
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
        else:
            self.ids.gotogame.text = "Game "
    pass

class GameWindow(Screen):
    def reset_game(self):
        global players
        players = 2
        self.ids.players.text = str(players)
        self.ids.player1.text = ""
        self.ids.player2.text = ""
        self.ids.player3.text = ""
        self.ids.player4.text = ""
        self.ids.player5.text = ""
        self.ids.player6.text = ""
        self.ids.player7.text = ""
        self.ids.player8.text = ""
        self.ids.player9.text = ""
        self.ids.player10.text = ""
        self.ids.player11.text = ""
        self.ids.player12.text = ""
        self.ids.player3.readonly = True
        self.ids.player4.readonly = True
        self.ids.player5.readonly = True
        self.ids.player6.readonly = True
        self.ids.player7.readonly = True
        self.ids.player8.readonly = True
        self.ids.player9.readonly = True
        self.ids.player10.readonly = True
        self.ids.player11.readonly = True
        self.ids.player12.readonly = True

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
    def label_add_subtract(self, x):
        global players
        if x == 1:
            if players == 2:
                self.ids.player3.readonly = True
                self.ids.player3.text = ""
            elif players == 3:
                self.ids.player4.readonly = True
                self.ids.player4.text = ""
            elif players == 4:
                self.ids.player5.readonly = True
                self.ids.player5.text = ""
            elif players == 5:
                self.ids.player6.readonly = True
                self.ids.player6.text = ""
            elif players == 6:
                self.ids.player7.readonly = True
                self.ids.player7.text = ""
            elif players == 7:
                self.ids.player8.readonly = True
                self.ids.player8.text = ""
            elif players == 8:
                self.ids.player9.readonly = True
                self.ids.player9.text = ""
            elif players == 9:
                self.ids.player10.readonly = True
                self.ids.player10.text = ""
            elif players == 10:
                self.ids.player11.readonly = True
                self.ids.player11.text = ""
            elif players == 11:
                self.ids.player12.readonly = True
                self.ids.player12.text = ""
        elif x == 2:
            if players == 3:
                self.ids.player3.readonly = False
            elif players == 4:
                self.ids.player4.readonly = False
            elif players == 5:
                self.ids.player5.readonly = False
            elif players == 6:
                self.ids.player6.readonly = False
            elif players == 7:
                self.ids.player7.readonly = False
            elif players == 8:
                self.ids.player8.readonly = False
            elif players == 9:
                self.ids.player9.readonly = False
            elif players == 10:
                self.ids.player10.readonly = False
            elif players == 11:
                self.ids.player11.readonly = False
            elif players == 12:
                self.ids.player12.readonly = False
    def start_game(self, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        global check
        check = 2
    def check_start(self, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, text):
        global players
        if text == "":
            self.ids.start.disabled = True
        global pl
        pl = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
        if players == 12:
            if pl[0] == "" or pl[1] == "" or pl[2] == "" or pl[3] == "" or pl[4] == "" or pl[5] == "" or pl[6] == "" or pl[7] == "" or pl[8] == "" or pl[9] == "" or pl[10] == "" or pl[11] == "":
                self.ids.start.disabled = True
            else:
                self.ids.start.disabled = False
        elif players == 11:
            if pl[0] == "" or pl[1] == "" or pl[2] == "" or pl[3] == "" or pl[4] == "" or pl[5] == "" or pl[6] == "" or pl[7] == "" or \
                    pl[8] == "" or pl[9] == "" or pl[10] == "":
                self.ids.start.disabled = True
            else:
                self.ids.start.disabled = False
        elif players == 10:
            if pl[0] == "" or pl[1] == "" or pl[2] == "" or pl[3] == "" or pl[4] == "" or pl[5] == "" or pl[6] == "" or pl[7] == "" or \
                    pl[8] == "" or pl[9] == "":
                self.ids.start.disabled = True
            else:
                self.ids.start.disabled = False
        elif players == 9:
            if pl[0] == "" or pl[1] == "" or pl[2] == "" or pl[3] == "" or pl[4] == "" or pl[5] == "" or pl[6] == "" or pl[7] == "" or \
                    pl[8] == "":
                self.ids.start.disabled = True
            else:
                self.ids.start.disabled = False
        if players == 8:
            if pl[0] == "" or pl[1] == "" or pl[2] == "" or pl[3] == "" or pl[4] == "" or pl[5] == "" or pl[6] == "" or pl[7] == "":
                self.ids.start.disabled = True
            else:
                self.ids.start.disabled = False
        elif players == 7:
            if pl[0] == "" or  pl[1] == "" or pl[2] == "" or pl[3] == "" or pl[4] == "" or pl[5] == "" or pl[6] == "":
                self.ids.start.disabled = True
            else:
                self.ids.start.disabled = False
        elif players == 6:
            if pl[0] == "" or pl[1] == "" or pl[2] == "" or pl[3] == "" or pl[4] == "" or pl[5] == "":
                self.ids.start.disabled = True
            else:
                self.ids.start.disabled = False
        elif players == 5:
            if pl[0] == "" or pl[1] == "" or pl[2] == "" or pl[3] == "" or pl[4] == "":
                self.ids.start.disabled = True
            else:
                self.ids.start.disabled = False
        if players == 4:
            if pl[0] == "" or pl[1] == "" or pl[2] == "" or pl[3] == "":
                self.ids.start.disabled = True
            else:
                self.ids.start.disabled = False
        elif players == 3:
            if pl[0] == "" or pl[1] == "" or pl[2] == "":
                self.ids.start.disabled = True
            else:
                self.ids.start.disabled = False
        elif players == 2:
            if pl[0] == "" or pl[1] == "":
                self.ids.start.disabled = True
            else:
                self.ids.start.disabled = False
    pass

class Game2Window(Screen):
    def setup(self):
        global pl
        self.ids.p1n.text = pl[0]
        global check
        check = 2
    def update_check(self):
        global check
        check = 2

class AreYouSureWindow(Screen):
    def update_check(self):
        global check
        check = 1

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
    ScoreWindow:
    GameWindow:
    Game2Window:
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
                root.set_players()
                if self.text == "Resume Game": app.root.current = "game"
                elif self.text == "Resume Game ": app.root.current = "game2"
                root.manager.transition.direction = "left" 
        Button:
            text: "Quick Score"
            background_color: 1,1,1,0.5
            on_release:
                root.set_players()
                x = '13'
                root.create_new_number(x)
                app.root.current = "score"
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
                    elif self.text == "Game ": app.root.current = "game2"
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
        BackgroundLabel
            text: 'Number of\\nPlayers:'
            background_color: 1, 1, 1, 0.2
        Button:
            text: 'Quick Score'
            background_color: 1,0,0,1
            on_release:
                app.root.current = "score"
                root.manager.transition.direction = "up"
        Button:
            text: '<'
            background_color: 1,0,0,0.6
            on_release:
                root.update_players(1)
                root.label_add_subtract(1)
                root.check_start(player1.text, player2.text, player3.text, player4.text, player5.text, player6.text, player7.text, player8.text, player9.text, player10.text, player11.text, player12.text, "hi")
        Label:
            id: players
            text: '2'
        Button:
            text: '>'
            background_color: 1,0,0,0.6
            on_release:
                root.update_players(2)
                root.label_add_subtract(2)
                root.check_start(player1.text, player2.text, player3.text, player4.text, player5.text, player6.text, player7.text, player8.text, player9.text, player10.text, player11.text, player12.text, "hi")
        Label:
            text: "Player 1 Name:"
        TextInput:
            id: player1
            on_text: root.check_start(player1.text, player2.text, player3.text, player4.text, player5.text, player6.text, player7.text, player8.text, player9.text, player10.text, player11.text, player12.text, self.text)
        Label:
            text: ""
        Label:
            text: "Player 2 Name:"
        TextInput:
            id: player2
            on_text: root.check_start(player1.text, player2.text, player3.text, player4.text, player5.text, player6.text, player7.text, player8.text, player9.text, player10.text, player11.text, player12.text, self.text)
        Label:
            text: ""
        Label:
            text: "Player 3 Name:"
        TextInput:
            id: player3
            on_text: root.check_start(player1.text, player2.text, player3.text, player4.text, player5.text, player6.text, player7.text, player8.text, player9.text, player10.text, player11.text, player12.text, self.text)
            readonly: True
        Label:
            text: ""
        Label:
            text: "Player 4 Name:"
        TextInput:
            id: player4
            on_text: root.check_start(player1.text, player2.text, player3.text, player4.text, player5.text, player6.text, player7.text, player8.text, player9.text, player10.text, player11.text, player12.text, self.text)
            readonly: True
        Label:
            text: ""
        Label:
            text: "Player 5 Name:"
        TextInput:
            id: player5
            on_text: root.check_start(player1.text, player2.text, player3.text, player4.text, player5.text, player6.text, player7.text, player8.text, player9.text, player10.text, player11.text, player12.text, self.text)
            readonly: True
        Label:
            text: ""
        Label:
            text: "Player 6 Name:"
        TextInput:
            id: player6
            on_text: root.check_start(player1.text, player2.text, player3.text, player4.text, player5.text, player6.text, player7.text, player8.text, player9.text, player10.text, player11.text, player12.text, self.text)
            readonly: True
        Label:
            text: ""
        Label:
            text: "Player 7 Name:"
        TextInput:
            id: player7
            on_text: root.check_start(player1.text, player2.text, player3.text, player4.text, player5.text, player6.text, player7.text, player8.text, player9.text, player10.text, player11.text, player12.text, self.text)
            readonly: True
        Label:
            text: ""
        Label:
            text: "Player 8 Name:"
        TextInput:
            id: player8
            on_text: root.check_start(player1.text, player2.text, player3.text, player4.text, player5.text, player6.text, player7.text, player8.text, player9.text, player10.text, player11.text, player12.text, self.text)
            readonly: True
        Label:
            text: ""
        Label:
            text: "Player 9 Name:"
        TextInput:
            id: player9
            on_text: root.check_start(player1.text, player2.text, player3.text, player4.text, player5.text, player6.text, player7.text, player8.text, player9.text, player10.text, player11.text, player12.text, self.text)
            readonly: True
        Label:
            text: ""
        Label:
            text: "Player 10 Name:"
        TextInput:
            id: player10
            on_text: root.check_start(player1.text, player2.text, player3.text, player4.text, player5.text, player6.text, player7.text, player8.text, player9.text, player10.text, player11.text, player12.text, self.text)
            readonly: True
        Label:
            text: ""
        Label:
            text: "Player 11 Name:"
        TextInput:
            id: player11
            on_text: root.check_start(player1.text, player2.text, player3.text, player4.text, player5.text, player6.text, player7.text, player8.text, player9.text, player10.text, player11.text, player12.text, self.text)
            readonly: True
        Label:
            text: ""
        Label:
            text: "Player 12 Name:"
        TextInput:
            id: player12
            on_text: root.check_start(player1.text, player2.text, player3.text, player4.text, player5.text, player6.text, player7.text, player8.text, player9.text, player10.text, player11.text, player12.text, self.text)
            readonly: True
        Label:
            text: ""
        Button:
            id: start
            text: 'Begin Game'
            background_color: 1,0,0,1
            disabled: True
            on_release: 
                root.start_game(player1.text, player2.text, player3.text, player4.text, player5.text, player6.text, player7.text, player8.text, player9.text, player10.text, player11.text, player12.text)
                app.root.current = "game2"
                root.manager.transition.direction = "left"
        Label:
            text: ""
        Button:
            text: 'Reset'
            background_color: 1,0,0,1
            on_release:
                root.reset_game()
                
<Game2Window>
    name: "game2"
    GridLayout:
        cols: 1
        Label:
            text: 'Please press "Setup" to finish setting up the game.'
        GridLayout:
            cols: 2
            Button:
                id: p1n
                text: "Setup"
                on_release: root.setup()
            Button:
                text: "Main Menu"
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
                    root.update_check()
        GridLayout:
            cols: 2
            Button:
                text: "Quick Score"
                on_release:
                    app.root.current = "score"
                    root.manager.transition.direction = "up"
                    root.update_check()
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
                    root.update_check()
                    
            Button
                text: "No"
                on_release:
                    app.root.current = "game2"
                    root.manager.transition.direction = "right"
                
""")

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()