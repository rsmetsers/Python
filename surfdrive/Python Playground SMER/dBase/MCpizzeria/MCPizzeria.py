### WORKS!
# NO OO needed, ugly def in a method though

#from tkinter import *
import sqlite3
with sqlite3.connect("MCPizzeria.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen


def maakNieuweTabellen():
    # Maak een nieuwe tabel met 3 kolommen: id, naam, prijs
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_pizzas(
        gerechtID INTEGER PRIMARY KEY AUTOINCREMENT,
        gerechtNaam TEXT,
        gerechtPrijs FLOAT);""")
    print("Tabel 'tbl_pizzas' aangemaakt.")


    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS tbl_toppings(
    #     toppingID INTEGER PRIMARY KEY AUTOINCREMENT,
    #     toppingNaam TEXT,
    #     toppingPrijs DECIMAL(6,2) NOT NULL);""")
    #
    # print("Tabel 'tbl_toppings' aangemaakt.")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_klanten(
        klantID INTEGER PRIMARY KEY AUTOINCREMENT,
        klantAchternaam TEXT,
        klantTel TEXT);""")
    print("Tabel 'tbl_klanten' aangemaakt.")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_bestellingAfrekening(
        bestelNr INTEGER PRIMARY KEY AUTOINCREMENT,
        datum VARCHAR(6),
        klantNr INTEGER,
        betaald VARCHAR(1),
        FOREIGN KEY (klantNr) REFERENCES tbl_klanten(klantNr) );""")#UITBREIDEN MET BEREKENING TOTAAL PRIJS
    print("Tabel 'tbl_bestellingAfrekening' aangemaakt.")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_winkelWagen(
        bestelNr INTEGER PRIMARY KEY,
        gerechtID INTEGER,
        aantal INTEGER NOT NULL,
        FOREIGN KEY (bestelNr) REFERENCES tbl_bestellingAfrekening(bestelNr),
        FOREIGN KEY (gerechtID) REFERENCES tbl_pizzas(gerechtID)
        );""")
    print("Tabel 'tbl_winkelWagen' aangemaakt.")




def printTabel(tabel_naam):
#    c = sqlite3.connect(DBASE_FILE).cursor()
    cursor.execute("SELECT * FROM "+tabel_naam)
    rows = cursor.fetchall()
    print("Tabel" + tabel_naam + ":", rows)
#    c.close()


def printPizzaTabel():
#    c = sqlite3.connect(DBASE_FILE).cursor()
    cursor.execute("SELECT * FROM tbl_pizzas")
    rows = cursor.fetchall()
    print("Tabel tbl_pizzas:", rows)
    return rows
#    c.close()

def printWinkelWagenTabel():
    cursor.execute("SELECT tbl_pizzas.gerechtNaam, aantal FROM tbl_winkelWagen, tbl_pizzas WHERE tbl_winkelWagen.gerechtID = tbl_pizzas.gerechtID")
    #rows = [("Gerecht \t \t Aantal")]
    rows = cursor.fetchall()
    print("Tabel tbl_pizzas:", rows)
    return rows




def voegNieuwPizzaToe(gerechtNaam, gerechtPrijs):
        #the NULL parameter is for the auto-incremented id
    cursor.execute("INSERT INTO tbl_pizzas VALUES(NULL, ?, ? )", (gerechtNaam, gerechtPrijs))
    print("Gerecht toegevoegd aan 'tbl_pizzas':" + gerechtNaam + " " + str(gerechtPrijs) )


def voegToeAanWinkelWagen(pizzaRij, pizzaAantal):
    #Pizzarij is een tuple van drie waarden, pizza_id is daarvan de eerste
    print("ik wil wat aan mijn bestelling toevoegen")

    eerste_rij = pizzaRij[0]#eerste pizza selecteren uit de lijst van pizzas
    gerechtID = eerste_rij[0]#eerste element in de tuple is gerechtID
    aantal = pizzaAantal

 #   print("Ik wil toevoegen " + str(gerechtID) )
    print("Ik wil toevoegen "+ str(aantal) +" maal " + gerechtID)
 #   print("Ik wil toevoegen "+ str(aantal) +" maal " + gerechtID)
#     c.execute("INSERT INTO tbl_pizzas VALUES(NULL, ?, ? )", (gerechtNaam, gerechtPrijs))
    cursor.execute("INSERT INTO tbl_winkelWagen VALUES(NULL, ?, ?)", (gerechtID, aantal,))
    printTabel("tbl_winkelWagen")

def verwijderPizza(gerechtID):
    cursor.execute("DELETE FROM tbl_pizzas WHERE gerechtID = ?", (gerechtID,))
    print("Gerecht verwijderd uit 'tbl_pizzas':" + str(gerechtID) )

def voegPizzasToe():
    printTabel("tbl_pizzas")
    voegNieuwPizzaToe("Hawaii", 12.25)
    voegNieuwPizzaToe("Salami", 10.00)
    voegNieuwPizzaToe("Margarita", 8.75)
    voegNieuwPizzaToe("Doner", 9.50)
    voegNieuwPizzaToe("Tutti Frutti", 10.00)
    voegNieuwPizzaToe("Al Formaggio", 10.25)
    voegNieuwPizzaToe("Verkeer", 10.75)
    voegNieuwPizzaToe("NEC", 12.00)
    voegNieuwPizzaToe("Pepperoni", 11.00)
    voegNieuwPizzaToe("Vegetarisch", 9.55)
    voegNieuwPizzaToe("Tonno", 9.25)
    voegNieuwPizzaToe("Pollo", 9.75)
    voegNieuwPizzaToe("Quattro Stagioni", 8.75)
    printTabel("tbl_pizzas")

#Zoek een pizza dat begint met de ingevoerde waarde
def zoekPizza(deelVanPizzaNaam):
    print("looking for pizza")
    cursor.execute("SELECT * FROM tbl_pizzas WHERE gerechtNaam LIKE ?", ( '%'+deelVanPizzaNaam+'%', ) )
#    c.execute("SELECT * FROM tbl_pizzas WHERE gerechtNaam LIKE ?", ( '%'+deelVanPizzaNaam+'%', )) #WERKT NIET?!?!?
    rows = cursor.fetchall()
    if rows == []:
        print("Helaas, geen match gevonden met "+ deelVanPizzaNaam)
    else:
        print("De volgende pizza's zoals "+deelVanPizzaNaam+" gevonden:", rows)
    return rows

def verwijderEvtOudeTabellen():
    cursor.execute("DROP TABLE IF EXISTS tbl_pizzas")
    cursor.execute("DROP TABLE IF EXISTS tbl_klanten")
#    cursor.execute("DROP TABLE IF EXISTS tbl_toppings")
    cursor.execute("DROP TABLE IF EXISTS tbl_bestellingAfrekening")
    cursor.execute("DROP TABLE IF EXISTS tbl_winkelWagen")

##OPSTARTEN
#maak verbinding met het database bestand



### HOOFDPROGRAMMA
verwijderEvtOudeTabellen()
maakNieuweTabellen()
voegPizzasToe()
# zoekPizza("Hawaii")
# zoekPizza("Haw")
# zoekPizza("waii")
#gezochte_pizza = zoekPizza("Hawaii")
#voegPizzaToeAanBestelling(gezochte_pizza)

#verwijderPizza(1)
#printTabel("tbl_pizzas")

#schrijf aanpassingen naar het database bestand
#c.commit()





#verbreek verbinding met het database bestand
#c.close()


