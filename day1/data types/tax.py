#uzytkownik wprowadza kwote netto
#uzytkownik wprowadza stawke podatku
#uzytkownik podaje imie
#program oblicza podatek i kwote brutto
#Hello <imie>, you will pay <brutto> PLN, that includes <tax> PLN in taxes

netto = int(input('Podaj kwote netto: '))
tax = netto*0.23
brutto = netto + tax
print(f'You will pay {brutto} PLN, that includes {tax} PLN in taxes')

# netto = float(input("Podaj kwtotę netto: "))
# podatek_procent = int(input("Podaj stawkę podatku w %: "))
# podatek = (podatek_procent / 100) * netto
# imię = input("Wprowadź imię: ")
# brutto = netto + podatek
# print(f'Hello {imię}, you will pay {brutto} PLN, that includes {podatek} PLN in taxes')