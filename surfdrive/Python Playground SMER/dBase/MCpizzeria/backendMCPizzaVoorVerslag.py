import sqlite3
#maak verbinding met het database bestand
#c = sqlite3.connect(DBASE_FILE).cursor()
#DBASE_FILE = 'my_trial_db.sqlite'

with sqlite3.connect("MCPizzeria.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen



def maakNieuweTabellen():
    # Maak een nieuwe tabel met 3 kolommen: id, naam, prijs
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_pizzas(
        pizzaNr INTEGER PRIMARY KEY AUTOINCREMENT,
        pizzaNaam VARCHAR(20),
        pizzaPrijs FLOAT);""") #uiteindelijk uitbreiden met een foto
    print("Tabel 'tbl_pizzas' aangemaakt.")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_klanten(
        klantNr INTEGER PRIMARY KEY AUTOINCREMENT,
        naam VARCHAR(20),
        adres VARCHAR(30),
        postcode VARCHAR(6),
        telNr VARCHAR(10));""")
    print("Tabel 'tbl_klanten' aangemaakt.")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_bestelling(
        bestelNr INTEGER PRIMARY KEY AUTOINCREMENT,
        datum VARCHAR(6),
        klantNr INTEGER,
        betaald VARCHAR(1),
        FOREIGN KEY (klantNr) REFERENCES tbl_klanten(klantNr) );""")#UITBREIDEN MET BEREKENING TOTAAL PRIJS
    print("Tabel 'tbl_bestelling' aangemaakt.")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_pizzaBestelling(
            bestelNr INTEGER PRIMARY KEY,
            pizzaNaam VARCHAR(20),
            aantal INTEGER NOT NULL,
            FOREIGN KEY (pizzaNaam) REFERENCES tbl_pizzas(pizzaNaam)
        );""")
    print("Tabel 'tbl_pizzaBestelling' aangemaakt.")

    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS tbl_pizzaBestelling(
    #         bestelNr INTEGER PRIMARY KEY,
    #         pizzaNaam VARCHAR(20),
    #         aantal INTEGER NOT NULL,
    #         #FOREIGN KEY (bestelNr) REFERENCES tbl_bestelling(bestelNr),
    #         FOREIGN KEY (pizzaNaam) REFERENCES tbl_pizzas(pizzaNaam)
    #     );""")
    # print("Tabel 'tbl_pizzaBestelling' aangemaakt.")

def printTabel(tabel_naam):
    cursor.execute("SELECT * FROM " + tabel_naam)
    opgehaalde_gegevens = cursor.fetchall()
    print("Tabel" + tabel_naam + ":", opgehaalde_gegevens)
    return opgehaalde_gegevens


def printPracticeTabel():
    cursor.execute("SELECT * "
                   "FROM tbl_pizzas")
    opgehaalde_gegevens = cursor.fetchall()
    print("Tabel tbl_pizzas:", opgehaalde_gegevens)
    return opgehaalde_gegevens




def vulPizzaTabel():
        #the NULL parameter is for the auto-incremented id
    cursor.execute("INSERT INTO tbl_pizzas "
                   " VALUES(NULL, ?, ? )",
                   ("Hawaii", 12.25))
    cursor.execute("INSERT INTO tbl_pizzas "
                   " VALUES(NULL, ?, ? )",
                   ("Salami", 10.00))
    cursor.execute("INSERT INTO tbl_pizzas "
                   " VALUES(NULL, ?, ? )",
                   ("Margarita", 8.75))
    db.commit()

def voegNieuwePizzaToe(gerechtNaam, gerechtPrijs):
    cursor.execute("INSERT INTO tbl_pizzas VALUES(NULL, ?, ? )", (gerechtNaam, gerechtPrijs))
    db.commit()
#    print("Gerecht toegevoegd aan 'tbl_pizzas':" + gerechtNaam + " " + str(gerechtPrijs) )

def vulKlantenTabel():
    cursor.execute("INSERT INTO tbl_klanten VALUES(NULL, ?, ?, ?, ? )", ("klantnaam1", "straat 123", "1234AB", "0612345678"))
    cursor.execute("INSERT INTO tbl_klanten VALUES(NULL, ?, ?, ?, ? )", ("klantnaam2", "straat 45", "4567XY", "0622224444"))


def vulBestellingTabel():
   cursor.execute("INSERT INTO tbl_bestelling VALUES(NULL, ?, ?, ? )", ("01022018", 1, "N"))

    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS tbl_bestelling(
    #     bestelNr INTEGER PRIMARY KEY AUTOINCREMENT,
    #     datum VARCHAR(6),
    #     klantNr INTEGER NOT NULL,
    #     betaald VARCHAR(1),
    #     FOREIGN KEY (klantNr) REFERENCES tbl_klanten(klantNr) );""")#UITBREIDEN MET PRIJS
    # print("Tabel 'tbl_bestelling' aangemaakt.")

def verwijderPizza(gerechtID):
    cursor.execute("DELETE FROM tbl_pizzas "
                   "WHERE gerechtID = ?",
                   (gerechtID,))
    print("Gerecht verwijderd uit 'tbl_pizzas':" + str(gerechtID) )



# #Zoek een pizza dat begint met de ingevoerde waarde
# def zoekPizza(deelVanPizzaNaam):
#     print("looking for pizza")
#     cursor.execute("SELECT * "
#                    "FROM tbl_pizzas "
#                    "WHERE pizzaNaam LIKE ?", ( '%'+deelVanPizzaNaam+'%', ) )
#     rows = cursor.fetchall()
#     if rows == []:
#         print("Helaas, geen match gevonden met "+ deelVanPizzaNaam)
#     else:
#         print("De volgende pizza's zoals "+deelVanPizzaNaam+" gevonden:", rows)
#     return rows

#Zoek een pizza dat begint met de ingevoerde waarde
def zoekPizza(gezochte_pizzanaam):
    print("looking for pizza...")
    cursor.execute("SELECT * "
                   "FROM tbl_pizzas "
                   "WHERE pizzaNaam = ?", ( gezochte_pizzanaam, ) )
    query_resultaat  = cursor.fetchall()
    if query_resultaat  == []:
        print("Helaas, geen match gevonden met "+ gezochte_pizzanaam)
    else:
        print("De volgende pizza's zoals "+gezochte_pizzanaam+" gevonden:", query_resultaat )
    return query_resultaat

def printPizzaTabel():
#    c = sqlite3.connect(DBASE_FILE).cursor()
    cursor.execute("SELECT * FROM tbl_pizzas")
    rows = cursor.fetchall()
    print("Tabel tbl_pizzas:", rows)
    return rows
#    c.close()


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

##OPSTARTEN


### HOOFDPROGRAMMA
#verwijder bestaande tabellen
cursor.execute("DROP TABLE tbl_pizzas")
cursor.execute("DROP TABLE tbl_klanten")

maakNieuweTabellen()
vulPizzaTabel()
vulKlantenTabel()
vulBestellingTabel()

printTabel("tbl_pizzas")
printTabel("tbl_klanten")
printTabel("tbl_bestelling")

printPracticeTabel()
cursor.execute("DELETE FROM tbl_pizzas "
               "WHERE pizzaNaam = ?",
               ("Hawaii",))
#print("removed hawaii pizza")

cursor.execute("UPDATE tbl_pizzas"
               " SET pizzaNaam = ?, pizzaPrijs = ?"
               " WHERE pizzaNr = ?",
               ('Hawaii', 19.25, 1,))


printPracticeTabel()

#verwijderPizza(1)
#printTabel("tbl_pizzas")

#schrijf aanpassingen naar het database bestand
#c.commit()


#verbreek verbinding met het database bestand
#cursor.close()


#####EXTRA CODE IDEAS#######
# class Database:
#     def __init__(self,db):
#         self.conn = sqlite3.connect(db)
#         self.cur = self.conn.cursor()
#         self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, "
#                     "author TEXT, year INTEGER, isbn INTEGER)")
#         self.conn.commit()
#
#     def insert(self,title, author, year, isbn):
#         #the NULL parameter is for the auto-incremented id
#         self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title,author,year,isbn))
#         self.conn.commit()
#
#
#     def view(self):
#         self.cur.execute("SELECT * FROM book")
#         rows = self.cur.fetchall()
#
#         return rows
#
#     def search(self,title="", author="", year="", isbn=""):
#         self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? "
#                     "OR isbn = ?", (title, author, year, isbn))
#         rows = self.cur.fetchall()
#         #conn.close()
#         return rows
#
#     def delete(self,id):
#         self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
#         self.conn.commit()
#         #conn.close()
#
#     def update(self,id, title, author, year, isbn):
#         self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
#         self.conn.commit()
#
#     #destructor-->now we close the connection to our database here
#     def __del__(self):
#         self.conn.close()
