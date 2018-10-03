### --------- Importeren bibliotheken -----------------
from tkinter import *
import backendMCPizzaVoorVerslag


#fotoPad = "fotoPepperoni.png"
fotoPad = ""
#fotoPath = "R_icon.png"

def search_pizza():
    listboxMenu.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
    listboxMenu.insert(0, "ID \t Gerecht \t \t Prijs")
    gezochte_pizzas = backendMCPizzaVoorVerslag.zoekPizza( pizzaNaam_text.get() )
    for row in gezochte_pizzas:
        listboxMenu.insert(END, row)


### functie voor het selecteren van een rij uit de listbox en in een andere veld plaatsen
def getGeselecteerdeRij(event):
    geselecteerdeRegelInLijst = listboxMenu.curselection()[0] #haal regelnummer waar op geklikt is
    geselecteerdeTekst = listboxMenu.get(geselecteerdeRegelInLijst)  #haal tekst uit regel
    invoerveldGeselecteerdePizza.delete(0, 50) #verwijder tekst uit veld (max 35 tekens), voor het geval er al iets staat
    invoerveldGeselecteerdePizza.insert(0, geselecteerdeTekst) #zet tekst in veld

    #pizzaLink = MCPizzeria.getPizzaLink(gerechtID)
    # for row in MCPizzeria.printWinkelWagenTabel():
    #     listboxWinkelwagen.insert(END, str(row[1])+"\t \t \t"+ row[0])
    regel = listboxMenu.get(geselecteerdeTekst[0])
    global fotoPad
    fotoPad = regel[3] #positie 3 in tabel is link naar plaatje
    #update foto
    nieuwPhotoPad = PhotoImage(file=fotoPad)
    #nieuwPhotoPad = nieuwPhotoPad.subsample(5)
    fotoPizza.configure(image=nieuwPhotoPad)
    fotoPizza.image = nieuwPhotoPad




def toonMenuInListboxMenu():
    listboxMenu.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
    listboxMenu.insert(0, "ID \t Gerecht \t \t Prijs \t FotoLink")
    for row in MCPizzeria.printPizzaTabel():
        listboxMenu.config(yscrollcommand=scrollbarlistboxMenu.set)#, takefocus=1)#, columns=('A', 'B', 'C'))
        listboxMenu.insert(END, row)# *map(unicode,row))

def berekenEnToonPrijs():
    berekendeTotaalPrijs = MCPizzeria.berekenTotaalPrijs()
    print(berekendeTotaalPrijs)
    totaalPrijs.delete(0, 50) #verwijder tekst uit veld (max 35 tekens), voor het geval er al iets staat
    totaalPrijs.insert(0, berekendeTotaalPrijs) #zet tekst in veld


#invoerveldSelecteerdePizzaNaam_text, aantalGeslecteerdePizza
def voegToeAanWinkelWagen_command():
    backendMCPizzaVoorVerslag.voegToeAanWinkelWagen(geselecteerdePizza.get(), aantalGeslecteerdePizza.get() )
    listboxWinkelwagen.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
    listboxWinkelwagen.insert(0, "# \t \t Gerecht")
    for row in backendMCPizzaVoorVerslag.printWinkelWagenTabel():
        listboxWinkelwagen.insert(END, str(row[1])+"\t \t \t"+ row[0])
    berekenEnToonPrijs()


#code for the GUI (front end)
venster = Tk()
venster.iconbitmap("MC_icon.ico")
venster.wm_title("MC Pizzeria")

labelIntro = Label(venster, text="Zoek een pizza op naam of kies uit de lijst")
labelIntro.grid(row=0, column=0, columnspan=3, sticky="W")# sticky="W" zorgt dat tekst links uitgelijnd wordt)

labelPizza = Label(venster, text="Pizzanaam:")
labelPizza.grid(row=1, column=0, sticky="W")# sticky="W" zorgt dat tekst links uitgelijnd wordt

pizzaNaam_text = StringVar()
invoerveldPizzanaam = Entry(venster, textvariable=pizzaNaam_text)
invoerveldPizzanaam.grid(row=1, column=1, columnspan=2, sticky="W")

labellistboxMenu = Label(venster, text="Mogelijkheden:")
labellistboxMenu.grid(row=2, column=0, sticky="W")# sticky="W" zorgt dat tekst links uitgelijnd wordt

knopZoekOpPizzaNaam = Button(venster, text="Zoek pizza", width=12, command=search_pizza)
knopZoekOpPizzaNaam.grid(row=1, column=4)

listboxMenu = Listbox(venster, height=6, width=50)
listboxMenu.grid(row=2, column=1, rowspan=6, columnspan=2, sticky="W")

listboxMenu.bind('<<ListboxSelect>>', getGeselecteerdeRij)

# now we need to attach a scrollbar to the listbox, and the other direction,too
scrollbarlistboxMenu = Scrollbar(venster)
scrollbarlistboxMenu.grid(row=2, column=2, rowspan=6)
listboxMenu.config(yscrollcommand=scrollbarlistboxMenu.set)#, takefocus=0)#, columns=('A', 'B', 'C'))
scrollbarlistboxMenu.config(command=listboxMenu.yview)

knopToonPizzas = Button(venster, text="Toon alle pizza's", width=12, command=toonMenuInListboxMenu)
knopToonPizzas.grid(row=2, column=4)

### TOON WELKE PIZZA GESELECTEERD IS OM AAN BESTELLING TOE TE VOEGEN
labelinvoerveldSelecteerdePizza = Label(venster, text="Gekozen pizza:")
labelinvoerveldSelecteerdePizza.grid(row=9, column=0, sticky="W")

geselecteerdePizza= StringVar()
invoerveldGeselecteerdePizza = Entry(venster, textvariable=geselecteerdePizza)
invoerveldGeselecteerdePizza.grid(row=9, column=1, columnspan=2, sticky="W")


padFotoGeselecteerdePizza = PhotoImage(file=fotoPad)
fotoPizza = Label(venster, width=100, height=100, image=padFotoGeselecteerdePizza)
fotoPizza.grid(row=9, column=2, columnspan=2, sticky="W")



### KIES AANTAL VAN DE GESELECTEERDE PIZZA
labelAantalGeselecteerd = Label(venster, text="Aantal:")
labelAantalGeselecteerd.grid(row=10, column=0, sticky="W")

aantalGeslecteerdePizza = IntVar()
aantalGeslecteerdePizza.set(1) #initiele waarde
optionMenuPizzaAantal = OptionMenu(venster, aantalGeslecteerdePizza, 0, 1,2,3,4,5,6,7,8)
optionMenuPizzaAantal.grid(row=10, column=1, sticky="W")





# Wat je eigenlijk wil is dat hij uit de gegevens haalt: tbl_pizzaWinkelWagen
knopVoegToeAanWinkelWagen = Button(venster, text="Kies", width=12, command=voegToeAanWinkelWagen_command)
knopVoegToeAanWinkelWagen.grid(row=10, column=4)


labellistboxWinkelwagen = Label(venster, text="Bestelling:")
labellistboxWinkelwagen.grid(row=11, column=0, sticky="W")# zorgt dat tekst links uitgelijnd wordt


listboxWinkelwagen = Listbox(venster, height=6, width=35)
listboxWinkelwagen.grid(row=11, column=1, rowspan=4, columnspan=2, sticky="W")

listboxWinkelwagen.bind('<<ListboxSelect>>')#, get_selected_row)

# now we need to attach a scrollbar to the listbox, and the other direction,too
scrollbarlistboxWinkelwagen = Scrollbar(venster)
scrollbarlistboxWinkelwagen.grid(row=10, column=2, rowspan=6)
listboxWinkelwagen.config(yscrollcommand=scrollbarlistboxWinkelwagen.set)
scrollbarlistboxWinkelwagen.config(command=listboxWinkelwagen.yview)




labelPrijs = Label(venster, text="Totaal Prijs:")
labelPrijs.grid(row=15, column=0, sticky="W")

totaalPrijs = Listbox(venster, height=1, width=35)
totaalPrijs.grid(row=15, column=1, rowspan=1, columnspan=1)




# b2 = Button(venster, text="Search entry", width=12, command=search_command)
# b2.grid(row=3, column=3)
#
# b3 = Button(venster, text="Add entry", width=12, command=add_command)
# b3.grid(row=4, column=3)
#
# b4 = Button(venster, text="Update selected", width=12, command=update_command)
# b4.grid(row=5, column=3)
#
# b5 = Button(venster, text="Delete selected", width=12, command=delete_command)
# b5.grid(row=6, column=3)

knopSluit = Button(venster, text="Sluiten", width=12, command=venster.destroy)
knopSluit.grid(row=16, column=4)

venster.mainloop()
