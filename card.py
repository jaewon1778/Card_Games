import random

class card_output():
    '''
    @ (int)card_num = 0 - 카드 리스트 길이
    @ (list[card])card_li = [] - 카드 리스트
    @ 카드 출력의 class
    '''
    card_num = 0
    card_li = []
    def __init__(self,card_num,card_li):
        self.card_num = card_num
        self.card_li = card_li
    def card_num_output(self,num):
        cno =["┏━┓┣━┫┃ ┃","┏━┓┏━┛┗━━","┏━┓ ━┫┗━┛","┃ ┃┗━╋  ┃",
            "┏━━┗━┓┗━┛","┏━┓┣━┓┗━┛","┏━┓  ┃  ┃","┏━┓┣━┫┗━┛",
            "┏━┓┗━┫┗━┛","┓┏┓┃┃┃┻┗┛","━━┳  ┃┗━┛","┏━┓┃ ┃┗━╋","┃┏┛┣┻┓┃ ┃"]
        return cno[num-1]
    def card_mark_output(self,mark):
        cmo = ["♠","♦","♥","♣"]
        if mark == "s": return cmo[0]
        if mark == "d": return cmo[1]
        if mark == "h": return cmo[2]
        if mark == "c": return cmo[3]
    def get_card_output(self):
        output = ["","","","","","",""]
        for i in self.card_li:
            if i.getback():
                output[0] += "┏━┳━┳━┳━┳━┓"
                output[1] += "┃╋ ╋ ╋ ╋ ╋┃"
                output[2] += "┣ ╋ ╋ ╋ ╋ ┫"
                output[3] += "┃╋ ╋ ╋ ╋ ╋┃"
                output[4] += "┣ ╋ ╋ ╋ ╋ ┫"
                output[5] += "┃╋ ╋ ╋ ╋ ╋┃"
                output[6] += "┗━┻━┻━┻━┻━┛"
                continue
            m=self.card_mark_output(i.getmark())
            n=self.card_num_output(i.getnum())
            output[0] += "┏━━━━━━━━━┓"
            output[1] += "┃       "+m+" ┃"
            output[2] += "┃   "+n[:3]+"   ┃"
            output[3] += "┃   "+n[3:6]+"   ┃"
            output[4] += "┃   "+n[6:]+"   ┃"
            output[5] += "┃ "+m+"       ┃"
            output[6] += "┗━━━━━━━━━┛"
        return output
        

class card():
    '''
    @ (string)mark - 카드의 문양 "s", "d", "h", "c" 중 하나
    @ (int)num = - 카드의 숫자 1 ~ 13 중 하나
    @ (bool)back = False - 카드의 앞뒷면(기본 앞면)
    @ card 한 장의 class
    '''
    back = False
    mark = ""
    num = 0
    def __init__(self,mark,num,back=False):
        self.mark = mark
        self.num = num
        self.back = back
    def __eq__(self, other):
        return self.mark == other.mark and self.num == other.num
    def getmark(self):
        return self.mark
    def getnum(self):
        return self.num
    def getback(self):
        return self.back
    def setback(self,backis):
        self.back = backis

class deck():
    '''
    @ (int)deck_num = 52 - 덱의 카드 개수
    @ (list[card])deck = [52 cards] - 덱의 카드 리스트
    @ 52장 카드 덱
    '''
    deck_num = 52
    deck = []
    def __init__(self):
        self.deck_num = 52
        for mark in ["s","d","h","c"]:
            for num in range(1,14):
                self.deck.append(card(mark,num))
    def getdeck_num(self):
        return self.deck_num
    def draw_rand_card(self):
        self.deck_num -= 1
        return self.deck.pop(random.randint(0,self.deck_num))
    def draw_rand_back_card(self):
        self.deck_num -= 1
        popcard = self.deck.pop(random.randint(0,self.deck_num))
        popcard.setback(True)
        return popcard
    def dealing(self,onehand,num):
        for _ in range(num):
            onehand.plus_card(self.draw_rand_card())
    def draw_the_card(self, thecard):
        for i in range(self.deck_num):
            if self.deck[i] == thecard:
                self.deck_num -= 1
                return self.deck.pop(i)
        return card()

class hand():
    '''
    @ (int)hand_num = 0 - 패의 카드 수
    @ (list[card])card_li = [] - 패의 카드 리스트
    @ player의 패
    '''
    hand_num = 0
    card_li = []
    def __init__(self,hand_num=0,card_li=[]):
        self.hand_num = hand_num
        self.card_li = card_li
    def get_card_li(self):
        return self.card_li
    def print_hand(self):
        output = card_output(self.hand_num,self.card_li).get_card_output()
        print(output[0])
        print(output[1])
        print(output[2])
        print(output[3])
        print(output[4])
        print(output[5])
        print(output[6])
    def print_hand_with_row(self, row):
        col = self.hand_num//row
        rem = self.hand_num%row
        for i in range(col):
            output = card_output(i*row,self.card_li[row*i:row*(i+1)]).get_card_output()
            print(output[0])
            print(output[1])
            print(output[2])
            print(output[3])
            print(output[4])
            print(output[5])
            print(output[6])
        if rem != 0:
            output = card_output(rem,self.card_li[col*row:]).get_card_output()
            print(output[0])
            print(output[1])
            print(output[2])
            print(output[3])
            print(output[4])
            print(output[5])
            print(output[6])
    def plus_card(self,newcard):
        self.card_li.append(newcard)
        self.hand_num += 1
    def minus_card(self,card_id):
        self.card_li.pop(card_id)
        self.hand_num -= 1
    def all_card_front(self):
        for eachcard in self.card_li:
            eachcard.setback(False)
    def all_card_back(self):
        for eachcard in self.card_li:
            eachcard.setback(True)
    def select_card_front(self, card_id):
        self.card_li[card_id].setback(False)
    def select_card_back(self, card_id):
        self.card_li[card_id].setback(True)
    def get_card_with_mark_num(self, mark, num):
        for eachcard in self.card_li:
            if eachcard.getmark() == mark and eachcard.getnum() == num:
                return eachcard
        return card()
    def get_card_with_id(self, card_id):
        return self.card_li[card_id]
    def get_card_id_with_mark_num(self, mark, num):
        for i in range(self.hand_num):
            if self.card_li[i].getmark() == mark and self.card_li[i].getnum() == num:
                return i
        return -1
    def get_card_id_with_card(self, acard):
        for i in range(self.hand_num):
            if self.card_li[i] == acard:
                return i
        return -1




