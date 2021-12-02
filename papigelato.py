print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')

aantalBol = 0
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
    print(totaalPrijs)
    afrekenen()
    
def afrekenen():
    global totaalPrijs, aantalBol, aantalHoorn, aantalBak, totaalbolPrijs, totaalbakPrijs, totaalhoornPrijs
    afrekenen = str(input('Wil je afrekenen? ja of nee >>> '))
    if afrekenen == 'ja':
        print(f'Resterend bedrag om te betalen {totaalPrijs} euro')
        bedragbetalen = float(input('Typ het volledige bedrag in >>> '))
        if bedragbetalen == totaalPrijs:
            print('Bedankt voor de betaling, hier is uw ijs. Fijne dag verder')
        else:
            print('No money?')
            end()
    elif afrekenen == 'nee':
        wissen = str(input('Wil je de vorige bestelling wissen? ja of nee >>> '))
        if wissen == 'ja':
            aantalBol = 0
            aantalHoorn = 0
            aantalBak = 0
            top()
        elif wissen == 'nee':
            top()

def top():
    global totaalPrijs, aantalBol, aantalHoorn, aantalBak, totaalbolPrijs, totaalbakPrijs, totaalhoornPrijs
    aantalBol = int(input('Hoeveel bolletjes wilt u? >>> '))
    if aantalBol >= 1 and aantalBol <= 3:
        keuze = str(input(f'Wilt u deze {aantalBol} bolletje(s) in een hoorn of een bak? >>> ')).lower()
        if keuze == 'hoorn': 
            aantalHoorn = 1
            print(f'Hier is uw {keuze} met {aantalBol} bolletje(s)')
            prijs()
        elif keuze == 'bak':
            aantalBak = 1
            print(f'Hier is uw {keuze} met {aantalBol} bolletje(s)')
            prijs()
        else:
            sorry()
            top()
    elif aantalBol >= 4 and aantalBol <= 8:
        print(f'Dan krijgt u van mij een bakje met {aantalBol} bolletjes')
        prijs()
    elif aantalBol >= 9:
        print('Sorry, zulke grote bakken hebben we niet.')
        top()
    else:
        sorry()
        top()

def end():
    afgifte = str(input('Wilt u nog meer bestellen? (J/N)')).lower()
    if afgifte == 'j':
        top()
    elif afgifte == 'n':
        prijs()
        exit()
    else:
        print('Ik begrijp dit niet...')
        end()

def sorry():
    print('Sorry, dat snap ik niet.')

top()