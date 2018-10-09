# #wat wordt er op het scherm geprint na uitvoer van deze code?
# x = 4
# while x < 7:
#     print("A")
#
#    #ANTWOORD: oneindig veel A
#
#
#
# #Zijn de volgende twee stukken code hetzelfde? J/N. Licht je antwoord kort toe.
# x = 4
# while x < 7:
#     print("A")
#     x += 1
#
# x = 4
# while x <= 6:
#     print("A")
#     x = x + 1
#
#     #ANTWOORD: ja, want <7 is zelfde als <=6 EN x=x+1 is zelfde als x+=1
#

# # WAT WORDT ER IN DE CONSOLE AFGEDRUKT?
# # x=3
# # for getal in range(4):
# #     x += 2
# #
# # print(x, getal)
# #
# # #ANTWOORD: 11 3
# # #MOEILIJKHEDEN: print met een ,
# #
# # #WAT WORDT ER IN DE CONSOLE AFGEDRUKT?
# # x=8
# # for getal in range(3):
# #     getal -= 2
# #
# # print(x)
# # print(getal)
# # #ANTWOORD 8 0
# # #MOEILIJKHEDEN: getal in loop ipv x, -=

#Wat wordt er in de console afgedrukt?
# getallenLijst = [3,6,9]
# getallenLijst.append(-1)
# print(getallenLijst)
# #ANTWOORD: [3,6,9,-1]

# #hoeveel stoelen zijn er na afloop? en hoeveel tafels?
# stoelen = 2
# tafels = 3
# for i in range (3):
#     stoelen = stoelen + stoelen
# tafels = tafels + tafels
#
# #ANTWOORD: 16 stoelen en 6 tafels
# #print("Aantal stoelen is:", stoelen, "en aantal tafels is:", tafels)



# #hoeveel stoelen zijn er na afloop? en hoeveel tafels?
# stoelen = 2
# tafels = 3
# for i in range (3):
#     stoelen = stoelen + stoelen
#     if stoelen >=4:
#         tafels += 1
# tafels = tafels + tafels
#
# #ANTWOORD: Aantal stoelen is: 16 en aantal tafels is: 12
# #print("Aantal stoelen is:", stoelen, "en aantal tafels is:", tafels)


#######################################################################

#### VOORBEELD TOETS VRAGEN
# #Hoeveel elementen zitten er na afloop in de lijst?
# getallen = [3, 6, 9, -1]
# for i in range (3):
#     getallen += [4]
#
## print(getallen)
#ANTWOORD: 7, dit is namelijk de lijst: [3, 6, 9, -1, 4, 4, 4]

# getallen = [3, 6, 9, -1]
# for i in range (3):
#     if len(getallen) <= 5:
#         getallen += [4]
#
# print(getallen)
# #ANTOORD: 6, nl [3, 6, 9, -1, 4, 4]

#Wat wordt in de console afgedrukt?
# getallen = [3, 6, 9, -1]
# for i in range (3):
#     if len(getallen) <= 5:
#         i + 4
#
# print(getallen)
# print(i)
# ANTWOORD:
# [3, 6, 9, -1]
# 2

# Wat is het type van getallen?
# ANTWOORD: lijst

#
# #Hoeveel elementen zitten er na afloop in de lijst?
# getallen = [3, 6, 9, -1]
# for i in range (3):
#     getallen += [4]
# getallen += [2]
# print(getallen)
# #ANTWOORD: 8, nl. [3, 6, 9, -1, 4, 4, 4, 2]

#####################################
# Geef aan wat de type is van:
# a)	De parameter
# b)	Wat er opgeleverd wordt
# c)	Wat er afgedrukt wordt
#
# def piep ( a ):
#     b = "Hallo"
#     print( b )
#     if a > 4:
#         return True
#     else:
#         return False
#
#
# piep(6.2)

#
# def blaf ( a ):
#     b = "Hallo"
#     while a >= 4:
#         print("a")
#         a-=1
#
# blaf(6)
# print(b)

################
# Opgave: Ik wil een programma schrijven dat onder elkaar het volgende afdrukt
# 6 7 8 9 3
# Kun jij mijn programma verbeteren zodat dat gebeurt?
#
# def blaf ( a ):
#     b = 3
#     while a<10:
#         print(a)
#         a+=1
#
# blaf(6)
# print(b)


# def drukWatAf( a ):
#     b = 3
#     while a > b:
#         print(a)
#         a = a - 1
#
# drukWatAf(6)


# # Opgave: Als ik met de volgende programma op Run druk krijg ik een foutmelding.
# # Leg uit waarom ik een foutmelding krijg.
# a = 4
# def doeIets():
#     c = 6
#     print( a , b, c )
#
# b = 3
# doeIets()
# print( a, b, c )


#OPGAVE: We willen een programma schrijven dat een gebruiker om getallen vraagt en deze bij elkaar optelt. Het programma stopt als de gebruiker een 0 ingeeft.
#Geef aan welke van de volgende instructies nodig zijn, en in welke volgorde.
# totaal = 0
# invoer = int( input ("Voer een getal in: ") )
# while not invoer==0:
#     # totaal = totaal + invoer
#     # print(totaal)
#
#     # invoer = int( input ("Voer een getal in: ") )
#     # totaal = totaal + invoer
#     # print(totaal)
#
#     totaal = totaal + invoer
#     invoer = int( input ("Voer een getal in: ") )
#     print(totaal)



# totaal = 0
# invoer = int( input ("Voer een getal in: ") )
# totaal = totaal + invoer
# while not invoer==0:
#     print(totaal)

#     # print(totaal)
#
#     # invoer = int( input ("Voer een getal in: ") )
#     # totaal = totaal + invoer
#
#     totaal = totaal + invoer
#     invoer = int( input ("Voer een getal in: ") )
#     print(totaal)

# #Hoe vaak worden deze loops uitgevoerd?
# teller = 0
# for x in range(3,7):
#     teller +=1
#     print (teller)
# #
# x = 8
# while x >= 5:
#     x-=1
#     print (x)

## Hoe vaak wordt deze loop uitgevoerd? ANTWOORD: 3x
# for x in range(3, 9, 2):
#     print(x)

#wat doet deze code? ANTWOORD: 4 cirkles naast elkaar
# import turtle
#
# turtle.pendown()
# for x in range(4):
#     for y in range (360):
#         turtle.forward(1)
#         turtle.right(1)
#     turtle.penup()
#     turtle.forward(100)
#     turtle.pendown()

# for i in range (0,5):
#     print(2*i)

# getallenLijst = [3, 5, -1, 9]
# getal = getallenLijst[1]
# print( getal )

# for i in range(3):
#     print(i)
#
# i=0
# while i < 3:
#     print(i)
#     i+=1

# for i in range (0, 5):
#     print( 2 * i )
# print(i)


# x = 1
# if x < 3:
#     if x < 1:
#         x = 2
#     x = x + 5
#
# print(x)

# FOR LOOP ALWAYS TERMINATES! Not true range(1,7,-1) should not terminate
# for i in range(5):
#     print(i)
#     i+=4
#     print(i)

# Voorbeeld toetsvraag
# list = [3,6,9]
# a = 0
# b = 0
# while b < len(list):
#     a += b
#     b += 2
# print(a)

# # tel de getallen 1 t/m 4 op
# sum = 0
# for i in range(1,5):
#     sum = sum + i
#
# print(sum)
#
#
# for i in range(1,5):
#     sum = 0
#     sum = sum + i
