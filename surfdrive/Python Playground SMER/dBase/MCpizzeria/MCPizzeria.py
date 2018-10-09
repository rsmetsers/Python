# Vul hier jullie namen in:
#
#
# Vul hier de naam van je programma in:
# Programmanaam
#

### --------- Importeren bibliotheken -----------------
import sqlite3
#maak een database en geef deze een verkorte naam 'db'
with sqlite3.connect("MCPizzeriaTest.db") as db:
    #maak een cursor waarmee je data uit de database kan halen
    cursor = db.cursor()


def maakNieuweTabellen():
    # Maak een nieuwe tabel met 3 kolommen: id, naam, prijs
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_pizzas(
        gerechtID INTEGER PRIMARY KEY AUTOINCREMENT,
        gerechtNaam TEXT,
        gerechtPrijs DOUBLE,
        gerechtFoto TEXT);""")
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

# def getPizzaLink(gerechtID):
#     cursor.execute("SELECT gerechtFoto FROM tbl_pizzas WHERE gerechtID = ? ",(gerechtID,))
#     gerechtFoto = cursor.fetchall()
#     print("Foto link:", gerechtFoto)
#     return gerechtFoto
# def getSelectedPizzaLink():
#     #where gelijk aan geselecteerde pizza
#     cursor.execute("SELECT gerechtFoto FROM tbl_pizzas WHERE gerechtID = ? ",(gerechtID,))
#     gerechtFoto = cursor.fetchall()
#     print("Foto link:", gerechtFoto)
#     return gerechtFoto


def printWinkelWagenTabel():
    cursor.execute("SELECT tbl_pizzas.gerechtNaam, aantal FROM tbl_winkelWagen, tbl_pizzas WHERE tbl_winkelWagen.gerechtID = tbl_pizzas.gerechtID")
    rows = cursor.fetchall()
    print("Tabel tbl_pizzas:", rows)
    return rows



def voegNieuwPizzaToe(gerechtNaam, gerechtPrijs, gerechtFoto):
        #the NULL parameter is for the auto-incremented id
    cursor.execute("INSERT INTO tbl_pizzas VALUES(NULL, ?, ?, ? )", (gerechtNaam, gerechtPrijs, gerechtFoto))
    print("Gerecht toegevoegd aan 'tbl_pizzas':" + gerechtNaam + " " + str(gerechtPrijs) + " " + gerechtFoto )


def voegToeAanWinkelWagen(pizzaRij, pizzaAantal):
    #Pizzarij is een tuple van drie waarden, pizza_id is daarvan de eerste
    eerste_rij = pizzaRij[0]#eerste pizza selecteren uit de lijst van pizzas
    toeTeVoegenGerechtID = eerste_rij[0]#eerste element in de tuple is gerechtID

    cursor.execute("SELECT aantal FROM tbl_winkelWagen WHERE gerechtID = ?", (toeTeVoegenGerechtID,))
    rows = cursor.fetchone()
    if not rows == None:
        aantalVanGerechtAlInWinkelWagen = rows[0]
        print("al gevonden:", rows[0])
        #print("aantal al gevonden, pizza soort", pizzaAlGevondenInRij[1])
       # print("aantal al gevonden, pizza aantal", pizzaAlGevondenInRij[2])
        nieuw_aantal = aantalVanGerechtAlInWinkelWagen + pizzaAantal
        #update winkelwagen tabel met nieuwe aantal
        cursor.execute("UPDATE tbl_winkelWagen SET aantal = ? WHERE gerechtID = ?", (pizzaAantal, toeTeVoegenGerechtID,))
    else:#pizza soort zit nog niet in wandelwagen
        toeTeVoegenaantal = pizzaAantal

        cursor.execute("INSERT INTO tbl_winkelWagen VALUES(NULL, ?, ?)", (toeTeVoegenGerechtID, toeTeVoegenaantal,))
    printTabel("tbl_winkelWagen")

def verwijderPizza(gerechtID):
    cursor.execute("DELETE FROM tbl_pizzas WHERE gerechtID = ?", (gerechtID,))
    print("Gerecht verwijderd uit 'tbl_pizzas':" + str(gerechtID) )

def voegPizzasToe():
    printTabel("tbl_pizzas")
    voegNieuwPizzaToe("Hawaii", 12.25, "Hawaii.png")
    voegNieuwPizzaToe("Salami", 10.00, "Salami.png")
    voegNieuwPizzaToe("Margarita", 8.75, "Margarita.png")
    voegNieuwPizzaToe("Doner", 9.50, "Doner.png")
    voegNieuwPizzaToe("TuttiFrutti", 10.00, "Mozarella.png")
    voegNieuwPizzaToe("AlFormaggio", 10.25, "4Cheese.png")
    voegNieuwPizzaToe("Verkeer", 10.75, "Mozarella.png")
    voegNieuwPizzaToe("NEC", 12.00, "Rucula.png")
    voegNieuwPizzaToe("Pepperoni", 11.00, "fotoPepperoni.png")
    voegNieuwPizzaToe("Vegetarisch", 9.55, "Veggie.png")
    voegNieuwPizzaToe("Tonno", 9.25, "Mozarella.png")
    voegNieuwPizzaToe("Diablo", 9.75, "Diablo.png")
    voegNieuwPizzaToe("QuattroStagioni", 8.75, "Mozarella.png")
    printTabel("tbl_pizzas")

#Zoek een pizza dat begint met de ingevoerde waarde
def zoekPizza(deelVanPizzaNaam):
    print("looking for pizza")
    cursor.execute("SELECT * FROM tbl_pizzas WHERE gerechtNaam LIKE ?", ( '%'+deelVanPizzaNaam+'%', ) )
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

def berekenTotaalPrijs():
    totaalPrijs = 0.00
    cursor.execute("SELECT * FROM tbl_winkelwagen" )
    rows = cursor.fetchall()
    for bestelde_item in rows:
        print("gerechtID:", bestelde_item[1])
        aantal =  bestelde_item[2]

        cursor.execute("SELECT tbl_pizzas.gerechtPrijs FROM tbl_pizzas, tbl_winkelWagen WHERE tbl_pizzas.gerechtID = tbl_winkelWagen.gerechtID" )
        prijs = cursor.fetchone()#eeen Select levert altijd een tabel op, in dit geval een tabel met 1 rij
        totaalPrijs += (prijs[0] * aantal) #de prijs is de eerste waarde in mijn rij

    return totaalPrijs

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
print("bereken")
berekenTotaalPrijs()
#verwijderPizza(1)
#printTabel("tbl_pizzas")

#schrijf aanpassingen naar het database bestand
#c.commit()


#verbreek verbinding met het database bestand
#c.close()


