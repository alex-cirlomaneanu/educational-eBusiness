# import tkinter as tk
#
# root = tk.Tk()
# canvas1 = tk.Canvas(root, width = 700, height = 500)
# canvas1.pack()
#
# def reguli():
#     label1 = tk.Label(root, text = 'Reguli:\nStabiliți legături între fiecare categorie! \n Aveți grijă la numele enumerate. \n Have fun :)', fg='green', font=('helvetica', 12, 'bold'))
#     canvas1.create_window(350, 100, window=label1)
# button1 = tk.Button(text = '- Salut!', command = reguli)
# canvas1.create_window(350, 50, window=button1)
#
# def program():
print("\n  Salut! Azi vom descoperi ce legături sunt între următoarele entități enumerate.\n\tPentru asta priviți listele de mai jos.")
autoritati = ["Guvern", "Primarie", "Fisc", "Parlament", "Minister", "Liceu"]
business = ["Amazon", "Kaufland", "Emag", "Google", "Dacia", "Danone", "Vodafone", "Carrefour", "Microsoft"]
clienti = ["Eu", "Gigel", "Marcel", "Maria", "Ioana", "Vecinul", "Bunica"]
print("\t- Acestea sunt autoritățile: \n", autoritati)
print("\t- Acestea sunt business-urile: \n", business)
print("\t- Acestia sunt clienții: \n", clienti)
print("\n\t Regulile jocului:")
print("\t1. Stabiliți legături între fiecare categorie.")
print("\t2. Veți introduce câte două nume, iar în funcție de apartența lor la mulțimile de mai sus,\nse va afișa relația între cei doi termeni.")
print("\t3. Aveți grijă să folosiți termenii enumerați (fără ghilimele), după ce tastați numele lor apăsați enter.\nCând vreți să opriți jocul, tastați 'stop' în dreptul primului nume și 'la fel' în dreptul celui de al doilea. Spor!")
print("\t4. Have fun :)")
print("\n\tStart")
while True:
    comanda_1 = input("\tIntrodu primul nume: ")
    if comanda_1.capitalize() == "Stop":
        print("\tO zi buna!")
    comanda_2 = input("\tIntrodu al doilea nume: ")
    if comanda_2.capitalize() == "La fel":
        quit()
    if comanda_1.capitalize() in autoritati and comanda_2.capitalize() in autoritati:
        print("\t", comanda_1.capitalize(), "și", comanda_2.capitalize(), "sunt în relație de : A2A (authority to authority)")

    elif comanda_1.capitalize() in autoritati and comanda_2.capitalize() in clienti:
        print("\t", comanda_1.capitalize(), "și", comanda_2.capitalize(), "sunt în relație de : A2C (authority to client)")

    elif comanda_1.capitalize() in autoritati and comanda_2.capitalize() in business:
        print("\t", comanda_1.capitalize(), "și", comanda_2.capitalize(), "sunt în relație de: A2B (authority to business)")


    elif comanda_1.capitalize() in business and comanda_2.capitalize() in business:
        print("\t", comanda_1.capitalize(), "și", comanda_2.capitalize(), "sunt în relație de: B2B (business to business)")
    elif comanda_1.capitalize() in business and comanda_2.capitalize() in autoritati:
        print("\t", comanda_1.capitalize(), "și", comanda_2.capitalize(), "sunt în relație de: B2A (business to authority)")
    elif comanda_1.capitalize() in business and comanda_2.capitalize() in clienti:
        print("\t", comanda_1.capitalize(), "și", comanda_2.capitalize(), "sunt în relație de: B2C (business to client)")


    elif comanda_1.capitalize() in clienti and comanda_2.capitalize() in clienti:
        print("\t", comanda_1.capitalize(), "și", comanda_2.capitalize(), "sunt în relație de: C2C (client to client)")
    elif comanda_1.capitalize() in clienti and comanda_2.capitalize() in autoritati:
        print("\t", comanda_1.capitalize(), "și", comanda_2.capitalize(), "sunt în relație de: C2A (client to authority)")
    elif comanda_1.capitalize() in clienti and comanda_2.capitalize() in business:
        print("\t", comanda_1.capitalize(), "și", comanda_2.capitalize(), "sunt în relație de: C2B (client to business)")

    else:
        print("\tNu cunosc (încearcă să scrii numele corect)")

# button2 = tk.Button(text = 'Start', command = program)
# root.mainloop()
