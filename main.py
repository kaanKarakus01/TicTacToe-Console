import random
import time
#Oyun Sınıfı
class TicTacToe:
    def __init__(self):
        self.hamle=0
        self.finish=False
        #Platformda yazacak numaralar
        self.platformN=["1","2","3","4","5","6","7","8","9"]
        self.platform()
    #Oyuncu 1 için özellikler
    def player1(self):
        #Oyuncu 1 kazanma durumu
        self.p1Win=False
        if self.p1Win:
            self.gameFinish()
        else:
            while True:
                if self.hamle==9:
                    print("BERABERE BİTTİ!")
                    self.gameFinish()
                    break
                option_3=int(input("Hangi satıra yazmak istiyorsunuz ? : "))
                if self.platformN.count(str(option_3))==1:
                    self.platformN[option_3-1]="X"
                    self.hamle+=1
                    self.platform()
                else:
                    print("Satır dolu!")
                    continue
                if (self.platformN[0]=="X" and self.platformN[1]=="X" and self.platformN[2]=="X") or (self.platformN[3]=="X" and self.platformN[4]=="X" and self.platformN[5]=="X") or (self.platformN[6]=="X" and self.platformN[7]=="X" and self.platformN[8]=="X"):
                    self.p1Win=True
                    print("PLAYER 1 KAZANDI!")
                    self.gameFinish()
                elif (self.platformN[0]=="X" and self.platformN[4]=="X" and self.platformN[8]=="X") or (self.platformN[2]=="X" and self.platformN[4]=="X" and self.platformN[6]=="X") or (self.platformN[0]=="X" and self.platformN[3]=="X" and self.platformN[6]=="X") or (self.platformN[1]=="X" and self.platformN[4]=="X" and self.platformN[7]=="X") or (self.platformN[2]=="X" and self.platformN[5]=="X" and self.platformN[8]=="X"):
                    self.p1Win=True
                    print("PLAYER 1 KAZANDI!")
                    self.gameFinish()
                break     
    #Oyuncu 2 için özellikler
    def player2(self):
        #Oyuncu 2 nin kazanma durumu
        self.p2Win=False
        if self.p2Win:
            self.gameFinish()
        else:
            while True:
                if self.hamle==9:
                    print("BERABERE BİTTİ!")
                    self.gameFinish()
                    break
                option_3=int(input("Hangi satıra yazmak istiyorsunuz ? : "))
                if self.platformN.count(str(option_3))==1:
                    self.platformN[option_3-1]="O"
                    self.hamle+=1
                    self.platform()
                else:
                    print("Satır dolu!")
                    continue
                if (self.platformN[0]=="O" and self.platformN[1]=="O" and self.platformN[2]=="O") or (self.platformN[3]=="O" and self.platformN[4]=="O" and self.platformN[5]=="O") or (self.platformN[6]=="O" and self.platformN[7]=="O" and self.platformN[8]=="O"):
                    self.p2Win=True
                    print("PLAYER 2 KAZANDI!")
                    self.gameFinish()
                elif (self.platformN[0]=="O" and self.platformN[4]=="O" and self.platformN[8]=="O") or (self.platformN[2]=="O" and self.platformN[4]=="O" and self.platformN[6]=="O") or (self.platformN[0]=="O" and self.platformN[3]=="O" and self.platformN[6]=="O") or (self.platformN[1]=="O" and self.platformN[4]=="O" and self.platformN[7]=="O") or (self.platformN[2]=="O" and self.platformN[5]=="O" and self.platformN[8]=="O"):
                    self.p2Win=True
                    print("PLAYER 2 KAZANDI!")
                    self.gameFinish()
                break     
    #Oyun bittiği zaman çalışacak
    def gameFinish(self):
        self.finish=True
        print("Oyun bitti!")
        time.sleep(1)
        option_4=input("1-Tekrar oyna\n2-Çıkış\n:")
        if option_4=="1":   
            time.sleep(2)
        elif option_4=="2":
            global y
            y=False
    
    def platform(self):
        #Oyun Platformu
        print(f"{self.platformN[0]}  | {self.platformN[1]} | {self.platformN[2]} ")
        print(f"---+---+---")
        print(f"{self.platformN[3]}  | {self.platformN[4]} | {self.platformN[5]} ")
        print(f"---+---+---")
        print(f"{self.platformN[6]}  | {self.platformN[7]} | {self.platformN[8]} ")
#Bu sınıf arkadaşıyla oynamak istediği zaman çalışacak
class Friend(TicTacToe):
    def __init__(self):
        self.sira=0
        self.p1="X"
        self.p2="O"
        super().__init__()
        self.game()
    def game(self):
        while True:
            if self.finish==False:
                if self.sira==0:
                    print("Player 1 Sırası")
                    self.player1()
                    self.sira+=1
                elif self.sira==1:
                    print("Player 2 Sırası!")
                    self.player2()
                    self.sira-=1
            else:
                self.sira=0
                self.hamle=0
                break

class Computer(TicTacToe):
    def __init__(self):
        print("Yapım aşamasındadır!")
        global y
        y=False
y=True
while True:
    if y==False:
        break
    else:
        print("***Çıkış Yapmak için 3 tuşuna basınız!***")
        print("TicTacToe Oyununa Hoşgeldiniz!\n1-Player 1 : X\n2-Player 2 : O")
        option=input(" : ")
        if option=="3":
            break
        else:
            pass
        print("1-Bilgisayara karşı\n2-Arkadaşınla oyna")
        option_2=input(" : ")
        if option_2=="1":
            p2=Computer()
        elif option_2=="2":
            p1=TicTacToe
            x=random.randint(0,1)
            p3=Friend()
        else:
            print("Hatalı tuşlama yaptınız!")



