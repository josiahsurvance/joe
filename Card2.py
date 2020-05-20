import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.base import runTouchApp
players = 2
check = 1
skd = 0
wow = ""

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

class Game2PlayerWindow(Screen):
    def setup(self):
        global check
        if check == 1:
            self.ids.pa1.text = ""
            self.ids.pa2.text = ""
            self.ids.pa3.text = ""
            self.ids.pa4.text = ""
            self.ids.pa5.text = ""
            self.ids.pa6.text = ""
            self.ids.pa7.text = ""
            self.ids.pa8.text = ""
            self.ids.pa9.text = ""
            self.ids.pa10.text = ""
            self.ids.pa11.text = ""
            self.ids.pa12.text = ""
            self.ids.pa13.text = ""
            self.ids.pa14.text = ""
            self.ids.pa15.text = ""
            self.ids.pa16.text = ""
            self.ids.pa17.text = ""
            self.ids.pa18.text = ""
            self.ids.pa19.text = ""
            self.ids.pa20.text = ""

            self.ids.pb1.text = ""
            self.ids.pb2.text = ""
            self.ids.pb3.text = ""
            self.ids.pb4.text = ""
            self.ids.pb5.text = ""
            self.ids.pb6.text = ""
            self.ids.pb7.text = ""
            self.ids.pb8.text = ""
            self.ids.pb9.text = ""
            self.ids.pb10.text = ""
            self.ids.pb11.text = ""
            self.ids.pb12.text = ""
            self.ids.pb13.text = ""
            self.ids.pb14.text = ""
            self.ids.pb15.text = ""
            self.ids.pb16.text = ""
            self.ids.pb17.text = ""
            self.ids.pb18.text = ""
            self.ids.pb19.text = ""
            self.ids.pb20.text = ""

            self.ids.pc1.text = ""
            self.ids.pc2.text = ""
            self.ids.pc3.text = ""
            self.ids.pc4.text = ""
            self.ids.pc5.text = ""
            self.ids.pc6.text = ""
            self.ids.pc7.text = ""
            self.ids.pc8.text = ""
            self.ids.pc9.text = ""
            self.ids.pc10.text = ""
            self.ids.pc11.text = ""
            self.ids.pc12.text = ""
            self.ids.pc13.text = ""
            self.ids.pc14.text = ""
            self.ids.pc15.text = ""
            self.ids.pc16.text = ""
            self.ids.pc17.text = ""
            self.ids.pc18.text = ""
            self.ids.pc19.text = ""
            self.ids.pc20.text = ""

            self.ids.pd1.text = ""
            self.ids.pd2.text = ""
            self.ids.pd3.text = ""
            self.ids.pd4.text = ""
            self.ids.pd5.text = ""
            self.ids.pd6.text = ""
            self.ids.pd7.text = ""
            self.ids.pd8.text = ""
            self.ids.pd9.text = ""
            self.ids.pd10.text = ""
            self.ids.pd11.text = ""
            self.ids.pd12.text = ""
            self.ids.pd13.text = ""
            self.ids.pd14.text = ""
            self.ids.pd15.text = ""
            self.ids.pd16.text = ""
            self.ids.pd17.text = ""
            self.ids.pd18.text = ""
            self.ids.pd19.text = ""
            self.ids.pd20.text = ""

            self.ids.pe1.text = ""
            self.ids.pe2.text = ""
            self.ids.pe3.text = ""
            self.ids.pe4.text = ""
            self.ids.pe5.text = ""
            self.ids.pe6.text = ""
            self.ids.pe7.text = ""
            self.ids.pe8.text = ""
            self.ids.pe9.text = ""
            self.ids.pe10.text = ""
            self.ids.pe11.text = ""
            self.ids.pe12.text = ""
            self.ids.pe13.text = ""
            self.ids.pe14.text = ""
            self.ids.pe15.text = ""
            self.ids.pe16.text = ""
            self.ids.pe17.text = ""
            self.ids.pe18.text = ""
            self.ids.pe19.text = ""
            self.ids.pe20.text = ""

            self.ids.pf1.text = ""
            self.ids.pf2.text = ""
            self.ids.pf3.text = ""
            self.ids.pf4.text = ""
            self.ids.pd5.text = ""
            self.ids.pf6.text = ""
            self.ids.pf7.text = ""
            self.ids.pf8.text = ""
            self.ids.pf9.text = ""
            self.ids.pf10.text = ""
            self.ids.pf11.text = ""
            self.ids.pf12.text = ""
            self.ids.pf13.text = ""
            self.ids.pf14.text = ""
            self.ids.pf15.text = ""
            self.ids.pf16.text = ""
            self.ids.pf17.text = ""
            self.ids.pf18.text = ""
            self.ids.pf19.text = ""
            self.ids.pf20.text = ""

            self.ids.pg1.text = ""
            self.ids.pg2.text = ""
            self.ids.pg3.text = ""
            self.ids.pg4.text = ""
            self.ids.pg5.text = ""
            self.ids.pg6.text = ""
            self.ids.pg7.text = ""
            self.ids.pg8.text = ""
            self.ids.pg9.text = ""
            self.ids.pg10.text = ""
            self.ids.pg11.text = ""
            self.ids.pg12.text = ""
            self.ids.pg13.text = ""
            self.ids.pg14.text = ""
            self.ids.pg15.text = ""
            self.ids.pg16.text = ""
            self.ids.pg17.text = ""
            self.ids.pg18.text = ""
            self.ids.pg19.text = ""
            self.ids.pg20.text = ""

            self.ids.ph1.text = ""
            self.ids.ph2.text = ""
            self.ids.ph3.text = ""
            self.ids.ph4.text = ""
            self.ids.ph5.text = ""
            self.ids.ph6.text = ""
            self.ids.ph7.text = ""
            self.ids.ph8.text = ""
            self.ids.ph9.text = ""
            self.ids.ph10.text = ""
            self.ids.ph11.text = ""
            self.ids.ph12.text = ""
            self.ids.ph13.text = ""
            self.ids.ph14.text = ""
            self.ids.ph15.text = ""
            self.ids.ph16.text = ""
            self.ids.ph17.text = ""
            self.ids.ph18.text = ""
            self.ids.ph19.text = ""
            self.ids.ph20.text = ""

            self.ids.pi1.text = ""
            self.ids.pi2.text = ""
            self.ids.pi3.text = ""
            self.ids.pi4.text = ""
            self.ids.pi5.text = ""
            self.ids.pi6.text = ""
            self.ids.pi7.text = ""
            self.ids.pi8.text = ""
            self.ids.pi9.text = ""
            self.ids.pi10.text = ""
            self.ids.pi11.text = ""
            self.ids.pi12.text = ""
            self.ids.pi13.text = ""
            self.ids.pi14.text = ""
            self.ids.pi15.text = ""
            self.ids.pi16.text = ""
            self.ids.pi17.text = ""
            self.ids.pi18.text = ""
            self.ids.pi19.text = ""
            self.ids.pi20.text = ""

            self.ids.pj1.text = ""
            self.ids.pj2.text = ""
            self.ids.pj3.text = ""
            self.ids.pj4.text = ""
            self.ids.pj5.text = ""
            self.ids.pj6.text = ""
            self.ids.pj7.text = ""
            self.ids.pj8.text = ""
            self.ids.pj9.text = ""
            self.ids.pj10.text = ""
            self.ids.pj11.text = ""
            self.ids.pj12.text = ""
            self.ids.pj13.text = ""
            self.ids.pj14.text = ""
            self.ids.pj15.text = ""
            self.ids.pj16.text = ""
            self.ids.pj17.text = ""
            self.ids.pj18.text = ""
            self.ids.pj19.text = ""
            self.ids.pj20.text = ""

            self.ids.pk1.text = ""
            self.ids.pk2.text = ""
            self.ids.pk3.text = ""
            self.ids.pk4.text = ""
            self.ids.pk5.text = ""
            self.ids.pk6.text = ""
            self.ids.pk7.text = ""
            self.ids.pk8.text = ""
            self.ids.pk9.text = ""
            self.ids.pk10.text = ""
            self.ids.pk11.text = ""
            self.ids.pk12.text = ""
            self.ids.pk13.text = ""
            self.ids.pk14.text = ""
            self.ids.pk15.text = ""
            self.ids.pk16.text = ""
            self.ids.pk17.text = ""
            self.ids.pk18.text = ""
            self.ids.pk19.text = ""
            self.ids.pk20.text = ""

            self.ids.pl1.text = ""
            self.ids.pl2.text = ""
            self.ids.pl3.text = ""
            self.ids.pl4.text = ""
            self.ids.pl5.text = ""
            self.ids.pl6.text = ""
            self.ids.pl7.text = ""
            self.ids.pl8.text = ""
            self.ids.pl9.text = ""
            self.ids.pl10.text = ""
            self.ids.pl11.text = ""
            self.ids.pl12.text = ""
            self.ids.pl13.text = ""
            self.ids.pl14.text = ""
            self.ids.pl15.text = ""
            self.ids.pl16.text = ""
            self.ids.pl17.text = ""
            self.ids.pl18.text = ""
            self.ids.pl19.text = ""
            self.ids.pl20.text = ""

            self.ids.pas.text = ""
            self.ids.pbs.text = ""
            self.ids.pcs.text = ""
            self.ids.pds.text = ""
            self.ids.pes.text = ""
            self.ids.pfs.text = ""
            self.ids.pgs.text = ""
            self.ids.phs.text = ""
            self.ids.pis.text = ""
            self.ids.pjs.text = ""
            self.ids.pks.text = ""
            self.ids.pls.text = ""

            self.ids.pas2.text = ""
            self.ids.pbs2.text = ""
            self.ids.pcs2.text = ""
            self.ids.pds2.text = ""
            self.ids.pes2.text = ""
            self.ids.pfs2.text = ""
            self.ids.pgs2.text = ""
            self.ids.phs2.text = ""
            self.ids.pis2.text = ""
            self.ids.pjs2.text = ""
            self.ids.pks2.text = ""
            self.ids.pls2.text = ""
        check = 2
        global pl
        self.ids.p1n.text = pl[0]
        self.ids.p2n.text = pl[1]
        self.ids.p3n.text = pl[2]
        self.ids.p4n.text = pl[3]
        self.ids.p5n.text = pl[4]
        self.ids.p6n.text = pl[5]
        self.ids.p7n.text = pl[6]
        self.ids.p8n.text = pl[7]
        self.ids.p9n.text = pl[8]
        self.ids.p10n.text = pl[9]
        self.ids.p11n.text = pl[10]
        self.ids.p12n.text = pl[11]
        self.ids.p1n2.text = pl[0]
        self.ids.p2n2.text = pl[1]
        self.ids.p3n2.text = pl[2]
        self.ids.p4n2.text = pl[3]
        self.ids.p5n2.text = pl[4]
        self.ids.p6n2.text = pl[5]
        self.ids.p7n2.text = pl[6]
        self.ids.p8n2.text = pl[7]
        self.ids.p9n2.text = pl[8]
        self.ids.p10n2.text = pl[9]
        self.ids.p11n2.text = pl[10]
        self.ids.p12n2.text = pl[11]
        if players == 2 or players == 3 or players == 4 or players == 5 or players == 6 or players == 7 or players == 8 or players == 9 or players == 10 or players == 11:
            self.ids.pl1.readonly = True
            self.ids.pl2.readonly = True
            self.ids.pl3.readonly = True
            self.ids.pl4.readonly = True
            self.ids.pl5.readonly = True
            self.ids.pl6.readonly = True
            self.ids.pl7.readonly = True
            self.ids.pl8.readonly = True
            self.ids.pl9.readonly = True
            self.ids.pl10.readonly = True
            self.ids.pl11.readonly = True
            self.ids.pl12.readonly = True
            self.ids.pl13.readonly = True
            self.ids.pl14.readonly = True
            self.ids.pl15.readonly = True
            self.ids.pl16.readonly = True
            self.ids.pl17.readonly = True
            self.ids.pl18.readonly = True
            self.ids.pl19.readonly = True
            self.ids.pl20.readonly = True
        if players == 2 or players == 3 or players == 4 or players == 5 or players == 6 or players == 7 or players == 8 or players == 9 or players == 10:
            self.ids.pk1.readonly = True
            self.ids.pk2.readonly = True
            self.ids.pk3.readonly = True
            self.ids.pk4.readonly = True
            self.ids.pk5.readonly = True
            self.ids.pk6.readonly = True
            self.ids.pk7.readonly = True
            self.ids.pk8.readonly = True
            self.ids.pk9.readonly = True
            self.ids.pk10.readonly = True
            self.ids.pk11.readonly = True
            self.ids.pk12.readonly = True
            self.ids.pk13.readonly = True
            self.ids.pk14.readonly = True
            self.ids.pk15.readonly = True
            self.ids.pk16.readonly = True
            self.ids.pk17.readonly = True
            self.ids.pk18.readonly = True
            self.ids.pk19.readonly = True
            self.ids.pk20.readonly = True
        if players == 2 or players == 3 or players == 4 or players == 5 or players == 6 or players == 7 or players == 8 or players == 9:
            self.ids.pj1.readonly = True
            self.ids.pj2.readonly = True
            self.ids.pj3.readonly = True
            self.ids.pj4.readonly = True
            self.ids.pj5.readonly = True
            self.ids.pj6.readonly = True
            self.ids.pj7.readonly = True
            self.ids.pj8.readonly = True
            self.ids.pj9.readonly = True
            self.ids.pj10.readonly = True
            self.ids.pj11.readonly = True
            self.ids.pj12.readonly = True
            self.ids.pj13.readonly = True
            self.ids.pj14.readonly = True
            self.ids.pj15.readonly = True
            self.ids.pj16.readonly = True
            self.ids.pj17.readonly = True
            self.ids.pj18.readonly = True
            self.ids.pj19.readonly = True
            self.ids.pj20.readonly = True
        if players == 2 or players == 3 or players == 4 or players == 5 or players == 6 or players == 7 or players == 8:
            self.ids.pi1.readonly = True
            self.ids.pi2.readonly = True
            self.ids.pi3.readonly = True
            self.ids.pi4.readonly = True
            self.ids.pi5.readonly = True
            self.ids.pi6.readonly = True
            self.ids.pi7.readonly = True
            self.ids.pi8.readonly = True
            self.ids.pi9.readonly = True
            self.ids.pi10.readonly = True
            self.ids.pi11.readonly = True
            self.ids.pi12.readonly = True
            self.ids.pi13.readonly = True
            self.ids.pi14.readonly = True
            self.ids.pi15.readonly = True
            self.ids.pi16.readonly = True
            self.ids.pi17.readonly = True
            self.ids.pi18.readonly = True
            self.ids.pi19.readonly = True
            self.ids.pi20.readonly = True
        if players == 2 or players == 3 or players == 4 or players == 5 or players == 6 or players == 7:
            self.ids.ph1.readonly = True
            self.ids.ph2.readonly = True
            self.ids.ph3.readonly = True
            self.ids.ph4.readonly = True
            self.ids.ph5.readonly = True
            self.ids.ph6.readonly = True
            self.ids.ph7.readonly = True
            self.ids.ph8.readonly = True
            self.ids.ph9.readonly = True
            self.ids.ph10.readonly = True
            self.ids.ph11.readonly = True
            self.ids.ph12.readonly = True
            self.ids.ph13.readonly = True
            self.ids.ph14.readonly = True
            self.ids.ph15.readonly = True
            self.ids.ph16.readonly = True
            self.ids.ph17.readonly = True
            self.ids.ph18.readonly = True
            self.ids.ph19.readonly = True
            self.ids.ph20.readonly = True
        if players == 2 or players == 3 or players == 4 or players == 5 or players == 6:
            self.ids.pg1.readonly = True
            self.ids.pg2.readonly = True
            self.ids.pg3.readonly = True
            self.ids.pg4.readonly = True
            self.ids.pg5.readonly = True
            self.ids.pg6.readonly = True
            self.ids.pg7.readonly = True
            self.ids.pg8.readonly = True
            self.ids.pg9.readonly = True
            self.ids.pg10.readonly = True
            self.ids.pg11.readonly = True
            self.ids.pg12.readonly = True
            self.ids.pg13.readonly = True
            self.ids.pg14.readonly = True
            self.ids.pg15.readonly = True
            self.ids.pg16.readonly = True
            self.ids.pg17.readonly = True
            self.ids.pg18.readonly = True
            self.ids.pg19.readonly = True
            self.ids.pg20.readonly = True
        if players == 2 or players == 3 or players == 4 or players == 5:
            self.ids.pf1.readonly = True
            self.ids.pf2.readonly = True
            self.ids.pf3.readonly = True
            self.ids.pf4.readonly = True
            self.ids.pf5.readonly = True
            self.ids.pf6.readonly = True
            self.ids.pf7.readonly = True
            self.ids.pf8.readonly = True
            self.ids.pf9.readonly = True
            self.ids.pf10.readonly = True
            self.ids.pf11.readonly = True
            self.ids.pf12.readonly = True
            self.ids.pf13.readonly = True
            self.ids.pf14.readonly = True
            self.ids.pf15.readonly = True
            self.ids.pf16.readonly = True
            self.ids.pf17.readonly = True
            self.ids.pf18.readonly = True
            self.ids.pf19.readonly = True
            self.ids.pf20.readonly = True
        if players == 2 or players == 3 or players == 4:
            self.ids.pe1.readonly = True
            self.ids.pe2.readonly = True
            self.ids.pe3.readonly = True
            self.ids.pe4.readonly = True
            self.ids.pe5.readonly = True
            self.ids.pe6.readonly = True
            self.ids.pe7.readonly = True
            self.ids.pe8.readonly = True
            self.ids.pe9.readonly = True
            self.ids.pe10.readonly = True
            self.ids.pe11.readonly = True
            self.ids.pe12.readonly = True
            self.ids.pe13.readonly = True
            self.ids.pe14.readonly = True
            self.ids.pe15.readonly = True
            self.ids.pe16.readonly = True
            self.ids.pe17.readonly = True
            self.ids.pe18.readonly = True
            self.ids.pe19.readonly = True
            self.ids.pe20.readonly = True
        if players == 2 or players == 3:
            self.ids.pd1.readonly = True
            self.ids.pd2.readonly = True
            self.ids.pd3.readonly = True
            self.ids.pd4.readonly = True
            self.ids.pd5.readonly = True
            self.ids.pd6.readonly = True
            self.ids.pd7.readonly = True
            self.ids.pd8.readonly = True
            self.ids.pd9.readonly = True
            self.ids.pd10.readonly = True
            self.ids.pd11.readonly = True
            self.ids.pd12.readonly = True
            self.ids.pd13.readonly = True
            self.ids.pd14.readonly = True
            self.ids.pd15.readonly = True
            self.ids.pd16.readonly = True
            self.ids.pd17.readonly = True
            self.ids.pd18.readonly = True
            self.ids.pd19.readonly = True
            self.ids.pd20.readonly = True
        if players == 2:
            self.ids.pc1.readonly = True
            self.ids.pc2.readonly = True
            self.ids.pc3.readonly = True
            self.ids.pc4.readonly = True
            self.ids.pc5.readonly = True
            self.ids.pc6.readonly = True
            self.ids.pc7.readonly = True
            self.ids.pc8.readonly = True
            self.ids.pc9.readonly = True
            self.ids.pc10.readonly = True
            self.ids.pc11.readonly = True
            self.ids.pc12.readonly = True
            self.ids.pc13.readonly = True
            self.ids.pc14.readonly = True
            self.ids.pc15.readonly = True
            self.ids.pc16.readonly = True
            self.ids.pc17.readonly = True
            self.ids.pc18.readonly = True
            self.ids.pc19.readonly = True
            self.ids.pc20.readonly = True
        if players == 3 or players == 4 or players == 5 or players == 6 or players == 7 or players == 8 or players == 9 or players == 10 or players == 11 or players == 12:
            self.ids.pc1.readonly = False
            self.ids.pc2.readonly = False
            self.ids.pc3.readonly = False
            self.ids.pc4.readonly = False
            self.ids.pc5.readonly = False
            self.ids.pc6.readonly = False
            self.ids.pc7.readonly = False
            self.ids.pc8.readonly = False
            self.ids.pc9.readonly = False
            self.ids.pc10.readonly = False
            self.ids.pc11.readonly = False
            self.ids.pc12.readonly = False
            self.ids.pc13.readonly = False
            self.ids.pc14.readonly = False
            self.ids.pc15.readonly = False
            self.ids.pc16.readonly = False
            self.ids.pc17.readonly = False
            self.ids.pc18.readonly = False
            self.ids.pc19.readonly = False
            self.ids.pc20.readonly = False
        if players == 4 or players == 5 or players == 6 or players == 7 or players == 8 or players == 9 or players == 10 or players == 11 or players == 12:
            self.ids.pd1.readonly = False
            self.ids.pd2.readonly = False
            self.ids.pd3.readonly = False
            self.ids.pd4.readonly = False
            self.ids.pd5.readonly = False
            self.ids.pd6.readonly = False
            self.ids.pd7.readonly = False
            self.ids.pd8.readonly = False
            self.ids.pd9.readonly = False
            self.ids.pd10.readonly = False
            self.ids.pd11.readonly = False
            self.ids.pd12.readonly = False
            self.ids.pd13.readonly = False
            self.ids.pd14.readonly = False
            self.ids.pd15.readonly = False
            self.ids.pd16.readonly = False
            self.ids.pd17.readonly = False
            self.ids.pd18.readonly = False
            self.ids.pd19.readonly = False
            self.ids.pd20.readonly = False
        if players == 5 or players == 6 or players == 7 or players == 8 or players == 9 or players == 10 or players == 11 or players == 12:
            self.ids.pe1.readonly = False
            self.ids.pe2.readonly = False
            self.ids.pe3.readonly = False
            self.ids.pe4.readonly = False
            self.ids.pe5.readonly = False
            self.ids.pe6.readonly = False
            self.ids.pe7.readonly = False
            self.ids.pe8.readonly = False
            self.ids.pe9.readonly = False
            self.ids.pe10.readonly = False
            self.ids.pe11.readonly = False
            self.ids.pe12.readonly = False
            self.ids.pe13.readonly = False
            self.ids.pe14.readonly = False
            self.ids.pe15.readonly = False
            self.ids.pe16.readonly = False
            self.ids.pe17.readonly = False
            self.ids.pe18.readonly = False
            self.ids.pe19.readonly = False
            self.ids.pe20.readonly = False
        if players == 6 or players == 7 or players == 8 or players == 9 or players == 10 or players == 11 or players == 12:
            self.ids.pf1.readonly = False
            self.ids.pf2.readonly = False
            self.ids.pf3.readonly = False
            self.ids.pf4.readonly = False
            self.ids.pf5.readonly = False
            self.ids.pf6.readonly = False
            self.ids.pf7.readonly = False
            self.ids.pf8.readonly = False
            self.ids.pf9.readonly = False
            self.ids.pf10.readonly = False
            self.ids.pf11.readonly = False
            self.ids.pf12.readonly = False
            self.ids.pf13.readonly = False
            self.ids.pf14.readonly = False
            self.ids.pf15.readonly = False
            self.ids.pf16.readonly = False
            self.ids.pf17.readonly = False
            self.ids.pf18.readonly = False
            self.ids.pf19.readonly = False
            self.ids.pf20.readonly = False
        if players == 7 or players == 8 or players == 9 or players == 10 or players == 11 or players == 12:
            self.ids.pg1.readonly = False
            self.ids.pg2.readonly = False
            self.ids.pg3.readonly = False
            self.ids.pg4.readonly = False
            self.ids.pg5.readonly = False
            self.ids.pg6.readonly = False
            self.ids.pg7.readonly = False
            self.ids.pg8.readonly = False
            self.ids.pg9.readonly = False
            self.ids.pg10.readonly = False
            self.ids.pg11.readonly = False
            self.ids.pg12.readonly = False
            self.ids.pg13.readonly = False
            self.ids.pg14.readonly = False
            self.ids.pg15.readonly = False
            self.ids.pg16.readonly = False
            self.ids.pg17.readonly = False
            self.ids.pg18.readonly = False
            self.ids.pg19.readonly = False
            self.ids.pg20.readonly = False
        if players == 8 or players == 9 or players == 10 or players == 11 or players == 12:
            self.ids.ph1.readonly = False
            self.ids.ph2.readonly = False
            self.ids.ph3.readonly = False
            self.ids.ph4.readonly = False
            self.ids.ph5.readonly = False
            self.ids.ph6.readonly = False
            self.ids.ph7.readonly = False
            self.ids.ph8.readonly = False
            self.ids.ph9.readonly = False
            self.ids.ph10.readonly = False
            self.ids.ph11.readonly = False
            self.ids.ph12.readonly = False
            self.ids.ph13.readonly = False
            self.ids.ph14.readonly = False
            self.ids.ph15.readonly = False
            self.ids.ph16.readonly = False
            self.ids.ph17.readonly = False
            self.ids.ph18.readonly = False
            self.ids.ph19.readonly = False
            self.ids.ph20.readonly = False
        if players == 9 or players == 10 or players == 11 or players == 12:
            self.ids.pi1.readonly = False
            self.ids.pi2.readonly = False
            self.ids.pi3.readonly = False
            self.ids.pi4.readonly = False
            self.ids.pi5.readonly = False
            self.ids.pi6.readonly = False
            self.ids.pi7.readonly = False
            self.ids.pi8.readonly = False
            self.ids.pi9.readonly = False
            self.ids.pi10.readonly = False
            self.ids.pi11.readonly = False
            self.ids.pi12.readonly = False
            self.ids.pi13.readonly = False
            self.ids.pi14.readonly = False
            self.ids.pi15.readonly = False
            self.ids.pi16.readonly = False
            self.ids.pi17.readonly = False
            self.ids.pi18.readonly = False
            self.ids.pi19.readonly = False
            self.ids.pi20.readonly = False
        if players == 10 or players == 11 or players == 12:
            self.ids.pj1.readonly = False
            self.ids.pj2.readonly = False
            self.ids.pj3.readonly = False
            self.ids.pj4.readonly = False
            self.ids.pj5.readonly = False
            self.ids.pj6.readonly = False
            self.ids.pj7.readonly = False
            self.ids.pj8.readonly = False
            self.ids.pj9.readonly = False
            self.ids.pj10.readonly = False
            self.ids.pj11.readonly = False
            self.ids.pj12.readonly = False
            self.ids.pj13.readonly = False
            self.ids.pj14.readonly = False
            self.ids.pj15.readonly = False
            self.ids.pj16.readonly = False
            self.ids.pj17.readonly = False
            self.ids.pj18.readonly = False
            self.ids.pj19.readonly = False
            self.ids.pj20.readonly = False
        if players == 11 or players == 12:
            self.ids.pk1.readonly = False
            self.ids.pk2.readonly = False
            self.ids.pk3.readonly = False
            self.ids.pk4.readonly = False
            self.ids.pk5.readonly = False
            self.ids.pk6.readonly = False
            self.ids.pk7.readonly = False
            self.ids.pk8.readonly = False
            self.ids.pk9.readonly = False
            self.ids.pk10.readonly = False
            self.ids.pk11.readonly = False
            self.ids.pk12.readonly = False
            self.ids.pk13.readonly = False
            self.ids.pk14.readonly = False
            self.ids.pk15.readonly = False
            self.ids.pk16.readonly = False
            self.ids.pk17.readonly = False
            self.ids.pk18.readonly = False
            self.ids.pk19.readonly = False
            self.ids.pk20.readonly = False
        if players == 12:
            self.ids.pl1.readonly = False
            self.ids.pl2.readonly = False
            self.ids.pl3.readonly = False
            self.ids.pl4.readonly = False
            self.ids.pl5.readonly = False
            self.ids.pl6.readonly = False
            self.ids.pl7.readonly = False
            self.ids.pl8.readonly = False
            self.ids.pl9.readonly = False
            self.ids.pl10.readonly = False
            self.ids.pl11.readonly = False
            self.ids.pl12.readonly = False
            self.ids.pl13.readonly = False
            self.ids.pl14.readonly = False
            self.ids.pl15.readonly = False
            self.ids.pl16.readonly = False
            self.ids.pl17.readonly = False
            self.ids.pl18.readonly = False
            self.ids.pl19.readonly = False
            self.ids.pl20.readonly = False
    def update_check(self):
        global check
        check = 2
    def update(self, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, x):
        s = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20]
        global score
        score = 0
        if x == 1:
            for n in list(range(20)):
                if s[n] == "":
                    return
                elif s[n] != "":
                    score += int(s[n])
                    self.ids.pas.text = str(score)
                    self.ids.pas2.text = str(score)
        elif x == 2:
            for n in list(range(20)):
                if s[n] == "":
                    return
                elif s[n] != "":
                    score += int(s[n])
                    self.ids.pbs.text = str(score)
                    self.ids.pbs2.text = str(score)
        elif x == 3:
            for n in list(range(20)):
                if s[n] == "":
                    return
                elif s[n] != "":
                    score += int(s[n])
                    self.ids.pcs.text = str(score)
                    self.ids.pcs2.text = str(score)
        elif x == 4:
            for n in list(range(20)):
                if s[n] == "":
                    return
                elif s[n] != "":
                    score += int(s[n])
                    self.ids.pds.text = str(score)
                    self.ids.pds2.text = str(score)
        elif x == 5:
            for n in list(range(20)):
                if s[n] == "":
                    return
                elif s[n] != "":
                    score += int(s[n])
                    self.ids.pes.text = str(score)
                    self.ids.pes2.text = str(score)
        elif x == 6:
            for n in list(range(20)):
                if s[n] == "":
                    return
                elif s[n] != "":
                    score += int(s[n])
                    self.ids.pfs.text = str(score)
                    self.ids.pfs2.text = str(score)
        elif x == 7:
            for n in list(range(20)):
                if s[n] == "":
                    return
                elif s[n] != "":
                    score += int(s[n])
                    self.ids.pgs.text = str(score)
                    self.ids.pgs2.text = str(score)
        elif x == 8:
            for n in list(range(20)):
                if s[n] == "":
                    return
                elif s[n] != "":
                    score += int(s[n])
                    self.ids.phs.text = str(score)
                    self.ids.phs2.text = str(score)
        if x == 9:
            for n in list(range(20)):
                if s[n] == "":
                    return
                elif s[n] != "":
                    score += int(s[n])
                    self.ids.pis.text = str(score)
                    self.ids.pis2.text = str(score)
        elif x == 10:
            for n in list(range(20)):
                if s[n] == "":
                    return
                elif s[n] != "":
                    score += int(s[n])
                    self.ids.pjs.text = str(score)
                    self.ids.pjs2.text = str(score)
        elif x == 11:
            for n in list(range(20)):
                if s[n] == "":
                    return
                elif s[n] != "":
                    score += int(s[n])
                    self.ids.pks.text = str(score)
                    self.ids.pks2.text = str(score)
        elif x == 12:
            for n in list(range(20)):
                if s[n] == "":
                    return
                elif s[n] != "":
                    score += int(s[n])
                    self.ids.pls.text = str(score)
                    self.ids.pls2.text = str(score)
        pass

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
    Game2PlayerWindow:
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
        Button:
            text: "Exit App"
            background_color: 1,1,1,0.5
            on_release: app.stop()
                
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
        BackgroundLabel:
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
                app.root.current = "game2"
                root.manager.transition.direction = "left"
        Label:
            text: ""
        Button:
            text: 'Reset'
            background_color: 1,0,0,1
            on_release:
                root.reset_game()
                
<Game2PlayerWindow>
    name: "game2"
    ScrollView:
        GridLayout:
            id: grid
            cols: 24
            spacing: 10
            size_hint_x: None
            height: 50
            
            width: self.minimum_width
            height: self.minimum_height
            Button:
                text: '       PRESS ME to        \\n       setup game.'
                font_size: 12
                size_hint_x: None
                height: 50
                height: 50
                width: self.texture_size[0]
                background_color: 0, 1, 0, 1
                on_release: root.setup()
            BackgroundLabel:
                text: '           Totals           '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 0.5
            BackgroundLabel:
                text: '         Round 1         '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.1
            BackgroundLabel:
                text: '         Round 2         '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.125
            BackgroundLabel:
                text: '         Round 3         '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.15
            BackgroundLabel:
                text: '         Round 4         '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.175
            BackgroundLabel:
                text: '         Round 5         '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.2
            BackgroundLabel:
                text: '         Round 6         '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.225
            BackgroundLabel:
                text: '         Round 7         '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.25
            BackgroundLabel:
                text: '         Round 8         '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.275
            BackgroundLabel:
                text: '         Round 9         '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.3
            BackgroundLabel:
                text: '        Round 10        '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.325
            BackgroundLabel:
                text: '        Round 11        '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.35
            BackgroundLabel:
                text: '        Round 12        '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.375
            BackgroundLabel:
                text: '        Round 13        '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.4
            BackgroundLabel:
                text: '        Round 14        '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.425
            BackgroundLabel:
                text: '        Round 15        '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.45
            BackgroundLabel:
                text: '        Round 16        '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.475
            BackgroundLabel:
                text: '        Round 17        '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.5
            BackgroundLabel:
                text: '        Round 18        '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.525
            BackgroundLabel:
                text: '        Round 19        '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.55
            BackgroundLabel:
                text: '        Round 20        '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 1, 1, 1, 0.575
            BackgroundLabel:
                text: '           Totals           '
                font_size: 12
                size_hint_x: None
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 0.5
            Label:
                text: '                            '
                size_hint_x: None
                height: 50
            BackgroundLabel:
                id: p1n
                text: 'Player 1'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: pas
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            TextInput:
                txt: "0"
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa1
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa2
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa3
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa4
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa5
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa6
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa7
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa8
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa9
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa10
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa11
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa12
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa13
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa14
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa15
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa16
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa17
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa18
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa19
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pa20
                input_filter: 'int'
                on_text: root.update(pa1.text, pa2.text, pa3.text, pa4.text, pa5.text, pa6.text, pa7.text, pa8.text, pa9.text, pa10.text, pa11.text, pa12.text, pa13.text, pa14.text, pa15.text, pa16.text, pa17.text, pa18.text, pa19.text, pa20.text, 1)                
                readonly: False
            BackgroundLabel:
                id: pas2
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            BackgroundLabel:
                id: p1n2
                text: '        Player 1        '
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: p2n
                text: 'Player 2'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: pbs
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            TextInput:
                txt: "0"
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb1
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                txt: ""
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb2
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb3
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb4
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb5
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb6
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb7
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb8
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb9
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb10
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb11
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb12
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb13
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb14
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb15
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb16
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb17
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb18
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb19
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            TextInput:
                font_size: 12
                size_hint_x: None
                height: 50
                id: pb20
                input_filter: 'int'
                on_text: root.update(pb1.text, pb2.text, pb3.text, pb4.text, pb5.text, pb6.text, pb7.text, pb8.text, pb9.text, pb10.text, pb11.text, pb12.text, pb13.text, pb14.text, pb15.text, pb16.text, pb17.text, pb18.text, pb19.text, pb20.text, 2)
                readonly: False
            BackgroundLabel:
                id: pbs2
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            BackgroundLabel:
                id: p2n2
                text: 'Player 2'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: p3n
                text: 'Player 3'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: pcs
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            TextInput:
                txt: "0"
                font_size: 12
                size_hint_x: None
                id: pc1
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                txt: ""
                font_size: 12
                size_hint_x: None
                id: pc2
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc3
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc4
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc5
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc6
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc7
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc8
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc9
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc10
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc11
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc12
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc13
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc14
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc15
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc16
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc17
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc18
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc19
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pc20
                input_filter: 'int'
                on_text: root.update(pc1.text, pc2.text, pc3.text, pc4.text, pc5.text, pc6.text, pc7.text, pc8.text, pc9.text, pc10.text, pc11.text, pc12.text, pc13.text, pc14.text, pc15.text, pc16.text, pc17.text, pc18.text, pc19.text, pc20.text, 3)
                readonly: True
            BackgroundLabel:
                id: pcs2
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            BackgroundLabel:
                id: p3n2
                text: 'Player 3'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: p4n
                text: 'Player 4'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: pds
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            TextInput:
                txt: "0"
                font_size: 12
                size_hint_x: None
                id: pd1
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                txt: ""
                font_size: 12
                size_hint_x: None
                id: pd2
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd3
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd4
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd5
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd6
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd7
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd8
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd9
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd10
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd11
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd12
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd13
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd14
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd15
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd16
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd17
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd18
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd19
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pd20
                input_filter: 'int'
                on_text: root.update(pd1.text, pd2.text, pd3.text, pd4.text, pd5.text, pd6.text, pd7.text, pd8.text, pd9.text, pd10.text, pd11.text, pd12.text, pd13.text, pd14.text, pd15.text, pd16.text, pd17.text, pd18.text, pd19.text, pd20.text, 4)
                readonly: True
            BackgroundLabel:
                id: pds2
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            BackgroundLabel:
                id: p4n2
                text: 'Player 4'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: p5n
                text: 'Player 5'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: pes
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            TextInput:
                txt: "0"
                font_size: 12
                size_hint_x: None
                id: pe1
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                txt: ""
                font_size: 12
                size_hint_x: None
                id: pe2
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe3
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe4
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe5
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe6
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe7
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe8
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe9
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe10
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe11
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe12
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe13
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe14
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe15
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe16
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe17
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe18
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe19
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pe20
                input_filter: 'int'
                on_text: root.update(pe1.text, pe2.text, pe3.text, pe4.text, pe5.text, pe6.text, pe7.text, pe8.text, pe9.text, pe10.text, pe11.text, pe12.text, pe13.text, pe14.text, pe15.text, pe16.text, pe17.text, pe18.text, pe19.text, pe20.text, 5)
                readonly: True
            BackgroundLabel:
                id: pes2
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            BackgroundLabel:
                id: p5n2
                text: 'Player 5'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: p6n
                text: 'Player 6'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: pfs
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            TextInput:
                txt: "0"
                font_size: 12
                size_hint_x: None
                id: pf1
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                txt: ""
                font_size: 12
                size_hint_x: None
                id: pf2
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf3
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf4
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf5
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf6
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf7
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf8
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf9
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf10
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf11
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf12
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf13
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf14
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf15
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf16
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf17
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf18
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf19
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pf20
                input_filter: 'int'
                on_text: root.update(pf1.text, pf2.text, pf3.text, pf4.text, pf5.text, pf6.text, pf7.text, pf8.text, pf9.text, pf10.text, pf11.text, pf12.text, pf13.text, pf14.text, pf15.text, pf16.text, pf17.text, pf18.text, pf19.text, pf20.text, 6)
                readonly: True
            BackgroundLabel:
                id: pfs2
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            BackgroundLabel:
                id: p6n2
                text: 'Player 6'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: p7n
                text: 'Player 7'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: pgs
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            TextInput:
                txt: "0"
                font_size: 12
                size_hint_x: None
                id: pg1
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                txt: ""
                font_size: 12
                size_hint_x: None
                id: pg2
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg3
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg4
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg5
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg6
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg7
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg8
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg9
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg10
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg11
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg12
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg13
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg14
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg15
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg16
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg17
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg18
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg19
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pg20
                input_filter: 'int'
                on_text: root.update(pg1.text, pg2.text, pg3.text, pg4.text, pg5.text, pg6.text, pg7.text, pg8.text, pg9.text, pg10.text, pg11.text, pg12.text, pg13.text, pg14.text, pg15.text, pg16.text, pg17.text, pg18.text, pg19.text, pg20.text, 7)
                readonly: True
            BackgroundLabel:
                id: pgs2
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            BackgroundLabel:
                id: p7n2
                text: 'Player 7'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: p8n
                text: 'Player 8'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: phs
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            TextInput:
                txt: "0"
                font_size: 12
                size_hint_x: None
                id: ph1
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                txt: ""
                font_size: 12
                size_hint_x: None
                id: ph2
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph3
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph4
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph5
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph6
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph7
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph8
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph9
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph10
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph11
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph12
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph13
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph14
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph15
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph16
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph17
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph18
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph19
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: ph20
                input_filter: 'int'
                on_text: root.update(ph1.text, ph2.text, ph3.text, ph4.text, ph5.text, ph6.text, ph7.text, ph8.text, ph9.text, ph10.text, ph11.text, ph12.text, ph13.text, ph14.text, ph15.text, ph16.text, ph17.text, ph18.text, ph19.text, ph20.text, 8)
                readonly: True
            BackgroundLabel:
                id: phs2
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            BackgroundLabel:
                id: p8n2
                text: 'Player 8'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: p9n
                text: 'Player 9'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: pis
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            TextInput:
                txt: "0"
                font_size: 12
                size_hint_x: None
                id: pi1
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                txt: ""
                font_size: 12
                size_hint_x: None
                id: pi2
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi3
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi4
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi5
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi6
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi7
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi8
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi9
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi10
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi11
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi12
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi13
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi14
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi15
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi16
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi17
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi18
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi19
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pi20
                input_filter: 'int'
                on_text: root.update(pi1.text, pi2.text, pi3.text, pi4.text, pi5.text, pi6.text, pi7.text, pi8.text, pi9.text, pi10.text, pi11.text, pi12.text, pi13.text, pi14.text, pi15.text, pi16.text, pi17.text, pi18.text, pi19.text, pi20.text, 9)
                readonly: True
            BackgroundLabel:
                id: pis2
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            BackgroundLabel:
                id: p9n2
                text: 'Player 9'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: p10n
                text: 'Player 10'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: pjs
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            TextInput:
                txt: "0"
                font_size: 12
                size_hint_x: None
                id: pj1
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                txt: ""
                font_size: 12
                size_hint_x: None
                id: pj2
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj3
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj4
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj5
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj6
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj7
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj8
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj9
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj10
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj11
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj12
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj13
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj14
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj15
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj16
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj17
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj18
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj19
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pj20
                input_filter: 'int'
                on_text: root.update(pj1.text, pj2.text, pj3.text, pj4.text, pj5.text, pj6.text, pj7.text, pj8.text, pj9.text, pj10.text, pj11.text, pj12.text, pj13.text, pj14.text, pj15.text, pj16.text, pj17.text, pj18.text, pj19.text, pj20.text, 10)
                readonly: True
            BackgroundLabel:
                id: pjs2
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            BackgroundLabel:
                id: p10n2
                text: 'Player 10'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: p11n
                text: 'Player 11'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: pks
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            TextInput:
                txt: "0"
                font_size: 12
                size_hint_x: None
                id: pk1
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                txt: ""
                font_size: 12
                size_hint_x: None
                id: pk2
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk3
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk4
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk5
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk6
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk7
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk8
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk9
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk10
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk11
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk12
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk13
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk14
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk15
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk16
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk17
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk18
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk19
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pk20
                input_filter: 'int'
                on_text: root.update(pk1.text, pk2.text, pk3.text, pk4.text, pk5.text, pk6.text, pk7.text, pk8.text, pk9.text, pk10.text, pk11.text, pk12.text, pk13.text, pk14.text, pk15.text, pk16.text, pk17.text, pk18.text, pk19.text, pk20.text, 11)
                readonly: True
            BackgroundLabel:
                id: pks2
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            BackgroundLabel:
                id: p11n2
                text: 'Player 11'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: p12n
                text: 'Player 12'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            BackgroundLabel:
                id: pls
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            TextInput:
                txt: "0"
                font_size: 12
                size_hint_x: None
                id: pl1
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                txt: ""
                font_size: 12
                size_hint_x: None
                id: pl2
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl3
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl4
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl5
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl6
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl7
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl8
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl9
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl10
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl11
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl12
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl13
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl14
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl15
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl16
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl17
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl18
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl19
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            TextInput:
                font_size: 12
                size_hint_x: None
                id: pl20
                input_filter: 'int'
                on_text: root.update(pl1.text, pl2.text, pl3.text, pl4.text, pl5.text, pl6.text, pl7.text, pl8.text, pl9.text, pl10.text, pl11.text, pl12.text, pl13.text, pl14.text, pl15.text, pl16.text, pl17.text, pl18.text, pl19.text, pl20.text, 12)
                readonly: True
            BackgroundLabel:
                id: pls2
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 0, 0, 1, 1
            BackgroundLabel:
                id: p12n2
                text: 'Player 12'
                font_size: 12
                size_hint_x: 100
                height: 50
                width: self.texture_size[0]
                background_color: 1, 0, 0, 0.35
            Button:
                text: "Main Menu"
                font_size: 12
                size_hint_x: 100
                height: 50
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            Button:
                text: "Quick Score"
                font_size: 12
                size_hint_x: 100
                on_release:
                    app.root.current = "score"
                    root.manager.transition.direction = "up"
            Button:
                text: "End Game"
                font_size: 12
                size_hint_x: 100
                on_release:
                    app.root.current = "rusure"
                    root.manager.transition.direction = "left"
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Label:
                text: '                            '
                size_hint_x: None
            Button:
                text: "Main Menu"
                font_size: 12
                size_hint_x: 100
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            Button:
                text: "Quick Score"
                font_size: 12
                size_hint_x: 100
                on_release:
                    app.root.current = "score"
                    root.manager.transition.direction = "up"
            Button:
                text: "End Game"
                font_size: 12
                size_hint_x: 100
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