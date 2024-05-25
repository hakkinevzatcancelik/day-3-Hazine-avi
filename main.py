print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Hazine Avına Hoş Geldiniz.")
print("Göreviniz Hazineye Ulaşmak.") 

choice1 = input('Yol ayrımındasınız. Gitmek istediğiniz yönü yazın. "Sağ" veya "Sol".').lower()

if choice1 == "sol":
          choice2 = input('Göle geldiniz."Yüz" veya Sala binmek için "Bin" yaz.').lower()
          if choice2 == "bin":
                    choice3 = input('Gölün karşısına başarı ile geldiniz. Bir kapı seçiniz. Kırmızı için "K", Mavi için "M", Yeşil için "Y".').lower()
                    if choice3 == "k":
                              print("Başarı ile hazineye ulaştınız.")
                    elif choice3 == "m":
                              print("Hazineyi ararken lanetlendiniz. Kaybettiniz.")
                    elif choice3 == "y":
                              print("Yılanlarla dolu bir odaya düştünüz. Oyunu kaybettiniz.")
                    else:
                              print("Oyunun kurallarına uymayan cezalandırılır. Evinizi bulucam.")
          elif choice2 == "yüz":
                    print("Donarak öldünüz. Oyunu kaybettiniz.")
          else:
                    print("Oyunun kurallarına uymayan cezalandırılır. Evinizi bulucam.")
elif choice1 == "sağ":
          print("Ormanda kayboldunuz ve kurtlar sizi yedi. Kaybettiniz.")
else:
          print("Oyunun kurallarına uymayan cezalandırılır. Evinizi bulucam.")
