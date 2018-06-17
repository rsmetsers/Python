from tkinter import *
import MCPizzeria
#from PIL import ImageTk, Image
#import TkTreectrl as treectrl
#from pip._vendor.appdirs import unicode


def drawGUI(window):
    window.wm_title("MC Pizzeria")

    labelIntro = Label(window, text="Zoek een pizza op naam of kies uit de lijst")
    labelIntro.grid(row=0, column=0, columnspan=3, sticky="W")# sticky="W" zorgt dat tekst links uitgelijnd wordt)

    labelPizza = Label(window, text="Pizzanaam:")
    labelPizza.grid(row=1, column=0, sticky="W")# sticky="W" zorgt dat tekst links uitgelijnd wordt

    pizzaNaam_text = StringVar()
    invoerveldPizzanaam = Entry(window, textvariable=pizzaNaam_text)
    invoerveldPizzanaam.grid(row=1, column=1, columnspan=2, sticky="W")



    labellistboxMenu = Label(window, text="Mogelijkheden:")
    labellistboxMenu.grid(row=2, column=0, sticky="W")# sticky="W" zorgt dat tekst links uitgelijnd wordt


    def search_pizza():
        listboxMenu.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
        listboxMenu.insert(0, "ID \t Gerecht \t \t Prijs")
        gezochte_pizzas = MCPizzeria.zoekPizza( pizzaNaam_text.get() )
        for row in gezochte_pizzas:
            listboxMenu.insert(END, row)

    knopZoekOpPizzaNaam = Button(window, text="Zoek pizza", width=12, command=search_pizza)
    knopZoekOpPizzaNaam.grid(row=1, column=4)


    listboxMenu = Listbox(window, height=6, width=35)
    listboxMenu.grid(row=2, column=1, rowspan=6, columnspan=2, sticky="W")

    ### functie voor het selecteren van een rij uit de listbox en in een andere veld plaatsen
    def get_selected_row(event):
        geselecteerdeRegelInLijst = listboxMenu.curselection()[0] #haal regel waar op geklikt is
        geselecteerdeTekst = listboxMenu.get(geselecteerdeRegelInLijst)  #haal tekst
        invoerveldGeselecteerdePizza.delete(0, 35) #verwijder tekst uit veld (max 35 tekens), voor het geval er al iets staat
        invoerveldGeselecteerdePizza.insert(0, geselecteerdeTekst) #zet tekst in veld

    listboxMenu.bind('<<ListboxSelect>>', get_selected_row)



   # mlb.focus_set()
   #  mlb.configure(selectcmd=select_cmd, selectmode='extended')
   #  mlb.config(columns=('Column 1', 'Column 2'))
   #  cursor.execute('SELECT * from foo')
   #  for row in cursor.fetchall():
   #      mlb.insert('end',*map(unicode,row))



    # now we need to attach a scrollbar to the listbox, and the other direction,too
    scrollbarlistboxMenu = Scrollbar(window)
    scrollbarlistboxMenu.grid(row=2, column=2, rowspan=6)
    listboxMenu.config(yscrollcommand=scrollbarlistboxMenu.set)#, takefocus=0)#, columns=('A', 'B', 'C'))
    scrollbarlistboxMenu.config(command=listboxMenu.yview)


    def toonMenuInListboxMenu():
        listboxMenu.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
        listboxMenu.insert(0, "ID \t Gerecht \t \t Prijs")
        for row in MCPizzeria.printPizzaTabel():
            listboxMenu.config(yscrollcommand=scrollbarlistboxMenu.set)#, takefocus=1)#, columns=('A', 'B', 'C'))
            listboxMenu.insert(END, row)# *map(unicode,row))


    knopToonPizzas = Button(window, text="Toon alle pizza's", width=12, command=toonMenuInListboxMenu)
    knopToonPizzas.grid(row=2, column=4)

### TOON WELKE PIZZA GESELECTEERD IS OM AAN BESTELLING TOE TE VOEGEN
    labelinvoerveldSelecteerdePizza = Label(window, text="Gekozen pizza:")
    labelinvoerveldSelecteerdePizza.grid(row=9, column=0, sticky="W")

 #   invoerveldSelecteerdePizza = Listbox(window, height=1, width=35)
 #   invoerveldSelecteerdePizza.grid(row=9, column=1, rowspan=1, columnspan=2, sticky="W")
    geselecteerdePizza= StringVar()
    invoerveldGeselecteerdePizza = Entry(window, textvariable=geselecteerdePizza)
    invoerveldGeselecteerdePizza.grid(row=9, column=1, columnspan=2, sticky="W")


 #    def get_geselecteerde_pizza(event):
 # #       listboxMenu.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
 #  #      for row in MCPizzeria.printPizzaTabel():
 # #           listboxMenu.insert(END, row)
 #
 #    invoerveldSelecteerdePizza.bind('<<ListboxSelect>>', get_geselecteerde_pizza)#dubbel klik op selectie


### KIES AANTAL VAN DE GESELECTEERDE PIZZA
    labelAantalGeselecteerd = Label(window, text="Aantal:")
    labelAantalGeselecteerd.grid(row=10, column=0, sticky="W")

    aantalGeslecteerdePizza = IntVar()
    aantalGeslecteerdePizza.set(1) #initiele waarde
    optionMenuPizzaAantal = OptionMenu(window, aantalGeslecteerdePizza, 0, 1,2,3,4,5,6,7,8)
    optionMenuPizzaAantal.grid(row=10, column=1, sticky="W")


## GETTING PIZZA DOESNT WORK

    # # #Voegt gewenste aantallen van een pizza toe aan bestelling lijst.
    # # #TODO: als al een van de pizzas in listboxWinkelwagen staan, dan aantal omhogen met gewenst aantal
    # def viewBestelling_command():
    #     #print(invoerveldSelecteerdePizza)
    #     keuze = invoerveldSelecteerdePizza.get()[0]
    #     print("Keuze was", keuze)
    #     print("Geselecteerde pizza was:", invoerveldSelecteerdePizza)
    #     print("Aantal geslecteerd:", invoerPizzaAantal)
    #     #TODO: dit nog aanpassen, doet nu natuurlijk nog niks
    #     #listboxMenu.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
    #     for row in MCPizzeria.printPizzaTabel():
    #         listboxMenu.insert(END, row) #voeg aan het einde toe
    #

    def berekenEnToonPrijs():
        berekendeTotaalPrijs = MCPizzeria.berekenTotaalPrijs()
        print(berekendeTotaalPrijs)
        totaalPrijs.delete(0, 35) #verwijder tekst uit veld (max 35 tekens), voor het geval er al iets staat
        totaalPrijs.insert(0, berekendeTotaalPrijs) #zet tekst in veld


    #invoerveldSelecteerdePizzaNaam_text, aantalGeslecteerdePizza
    def voegToeAanWinkelWagen_command():
        MCPizzeria.voegToeAanWinkelWagen(geselecteerdePizza.get(), aantalGeslecteerdePizza.get() )
        listboxWinkelwagen.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
        listboxWinkelwagen.insert(0, "# \t \t Gerecht")
        for row in MCPizzeria.printWinkelWagenTabel():
            listboxWinkelwagen.insert(END, str(row[1])+"\t \t \t"+ row[0])
        berekenEnToonPrijs()


    # Wat je eigenlijk wil is dat hij uit de gegevens haalt: tbl_pizzaWinkelWagen
    knopVoegToeAanWinkelWagen = Button(window, text="Kies", width=12, command=voegToeAanWinkelWagen_command)
    knopVoegToeAanWinkelWagen.grid(row=10, column=4)


    labellistboxWinkelwagen = Label(window, text="Bestelling:")
    labellistboxWinkelwagen.grid(row=11, column=0, sticky="W")# zorgt dat tekst links uitgelijnd wordt




    listboxWinkelwagen = Listbox(window, height=6, width=35)
    listboxWinkelwagen.grid(row=11, column=1, rowspan=4, columnspan=2, sticky="W")

    listboxWinkelwagen.bind('<<ListboxSelect>>')#, get_selected_row)

    # now we need to attach a scrollbar to the listbox, and the other direction,too
    scrollbarlistboxWinkelwagen = Scrollbar(window)
    scrollbarlistboxWinkelwagen.grid(row=10, column=2, rowspan=6)
    listboxWinkelwagen.config(yscrollcommand=scrollbarlistboxWinkelwagen.set)
    scrollbarlistboxWinkelwagen.config(command=listboxWinkelwagen.yview)




    labelPrijs = Label(window, text="Totaal Prijs:")
    labelPrijs.grid(row=15, column=0, sticky="W")

    totaalPrijs = Listbox(window, height=1, width=35)
    totaalPrijs.grid(row=15, column=1, rowspan=1, columnspan=1)




    # b2 = Button(window, text="Search entry", width=12, command=search_command)
    # b2.grid(row=3, column=3)
    #
    # b3 = Button(window, text="Add entry", width=12, command=add_command)
    # b3.grid(row=4, column=3)
    #
    # b4 = Button(window, text="Update selected", width=12, command=update_command)
    # b4.grid(row=5, column=3)
    #
    # b5 = Button(window, text="Delete selected", width=12, command=delete_command)
    # b5.grid(row=6, column=3)

    knopSluit = Button(window, text="Sluiten", width=12, command=window.destroy)
    knopSluit.grid(row=16, column=4)

    icoontjeR = PhotoImage(file="R_icon.png")
    icoon_knop = Button(window, text="fsd", image=icoontjeR, height=50, width=150)
    icoon_knop.grid(row=17, column=1)

#code for the GUI (front end)
window = Tk()
drawGUI(window)

window.mainloop()
