print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')

aantalBol = 0
aantalBol2 =+ aantalBol
aantalHoorn = 0
aantalBak = 0
hoornPrijs = 1.25
bakPrijs = 0.75
bolPrijs = 1.10

def prijs():
    global totaalPrijs, aantalBol, aantalHoorn, aantalBak, totaalbolPrijs, totaalbakPrijs, totaalhoornPrijs
    totaalbolPrijs = float(aantalBol * bolPrijs)
    totaalhoornPrijs = float(aantalHoorn * hoornPrijs)
    totaalbakPrijs = float(aantalBak * bakPrijs)
    totaalPrijs = float(totaalbolPrijs + totaalhoornPrijs + totaalbakPrijs)
    print(f'Bol      ' + str(aantalBol) + ' x ' + str(bolPrijs) + ' euro')
    print(f'Hoorn    ' + str(aantalHoorn) + ' x ' + str(hoornPrijs) + ' euro')
    print(f'Bak      ' + str(aantalBak) + ' x ' + str(bakPrijs) + ' euro')
    print('------------------------')
    print(f'{totaalPrijs} euro')
    afrekenen()
    
def afrekenen():
    global totaalPrijs, aantalBol, aantalHoorn, aantalBak, totaalbolPrijs, totaalbakPrijs, totaalhoornPrijs
    afrekenen = str(input('Wil je afrekenen? (J/N) >>> '))
    if afrekenen == 'j':
        print(f'Resterend bedrag om te betalen is {totaalPrijs} euro')
        bedragbetalen = float(input('Typ het volledige bedrag in >>> '))
        if bedragbetalen == totaalPrijs:
            print('Bedankt voor de betaling, hier is uw ijs. Fijne dag verder')
        else:
            print('No money?')
            (exit)
    elif afrekenen == 'n':
            afgifte = str(input('Wilt u nog meer bestellen? (J/N) >>> ')).lower()
            if afgifte == 'j':
                top()
            elif afgifte == 'n':
                afrekenen()
    else:
        print('Ik begrijp dit niet...')
        exit()

def top():
    global totaalPrijs, aantalBol, aantalBol2, aantalHoorn, aantalBak, totaalbolPrijs, totaalbakPrijs, totaalhoornPrijs
    aantalBol = aantalBol2 = int(input('Hoeveel bolletjes wilt u? >>> '))
    aantalBol + aantalBol2
    if aantalBol >= 1 and aantalBol <= 3:
        keuze = str(input(f'Wilt u deze {aantalBol} bolletje(s) in een hoorn of een bak? >>> ')).lower()
        if keuze == 'hoorn':
            aantalHoorn += 1
            print(f'Hier is uw {keuze} met {aantalBol} bolletje(s)')
            prijs()
        elif keuze == 'bak':
            aantalBak += 1
            print(f'Hier is uw {keuze} met {aantalBol} bolletje(s)')
            prijs()
        else:
            sorry()
            top()
    elif aantalBol >= 4 and aantalBol <= 8:
        aantalBol2 =+ aantalBol
        print(f'Dan krijgt u van mij een bakje met {aantalBol} bolletjes')
        prijs()
    elif aantalBol >= 9:
        print('Sorry, zulke grote bakken hebben we niet.')
        top()
    else:
        sorry()
        top()

def sorry():
    print('Sorry, dat snap ik niet.')

top()