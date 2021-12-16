print('Welkom bij Papi Gelato, wij hebben de juiste smaken!')

aardbei = False
chocolade = False
vanille = False

aantalGeen = 0
aantalslagroom = 0
aantalSprinkles = 0
aantalCaramelhoorn = 0
aantalCaramelbakje = 0

bollen = 0
aantalLiters = 0
aantalBol = 0
aantalHoorn = 0
aantalBak = 0
literPrijs = 9.80
totaalPrijs = 0
totaalAlles = 0
totaalPrijsBelasting = 0
hoornPrijs = 1.25
bakPrijs = 0.75
bolPrijs = 0.95
literPrijs = 9.80

def paza():
    global paofza
    paofza = str(input('Wilt u dit particulier kopen of zakelijk? >>> ')).lower()
    if paofza == "particulier":
        particulier()
    if paofza == "zakelijk":
        zakelijk()
    else:
        exit()

def particulier():
    global totaalPrijs, aantalBol, aantalHoorn, aantalBak, aardbei, chocolade, vanille, keuze, toppings, bollen
    aantalBol = int(input('Hoeveel bolletjes wilt u? >>> '))
    bollen += aantalBol
    if aantalBol >= 9:
        print('Sorry, zulke grote bakken hebben we niet.')
        particulier()
    i = 1
    while i <= aantalBol:
        print('AARDBEI - CHOCOLADE - VANILLE')
        bolSmaak = input('Wat voor smaakt wilt u? ' + str(i) + '\n').lower()
        i += 1
        if bolSmaak == 'aardbei':
            aardbei += True
        elif bolSmaak == 'chocolade':
            chocolade += True
        elif bolSmaak == 'vanille':
            vanille += True
        else:
            i = 1
    if aantalBol >= 1 and aantalBol <= 3:
        keuze = str(input(f'Wilt u deze {aantalBol} bolletje(s) in een hoorn of een bak? >>> ')).lower()
        if keuze == 'hoorn':
            aantalHoorn += 1
            print(f'Hier is uw {keuze} met {aantalBol} bolletje(s)')
            toppings()
        elif keuze == 'bak':
            aantalBak += 1
            print(f'Hier is uw {keuze} met {aantalBol} bolletje(s)')
            toppings()
    elif aantalBol >= 4 and aantalBol <= 8:
        aantalBak += 1
        print(f'Dan krijgt u van mij een bakje met {aantalBol} bolletjes')
        toppings()
    else:
        print('Sorry dat is geen optie die we aanbieden...')
        particulier()

def zakelijk():
    global aantalLiters, aardbei, chocolade, vanille
    aantalLiters = int(input('Hoeveel liter wilt u? >>> '))
    i = 1
    while i <= aantalLiters:
        print('AARDBEI - CHOCOLADE - VANILLE')
        literSmaak = input('Wat voor smaakt wilt u? ' + str(i) + '\n').lower()
        i += 1
        if literSmaak == 'aardbei':
            aardbei += 1
        elif literSmaak == 'chocolade':
            chocolade += 1
        elif literSmaak == 'vanille':
            vanille += 1
        else:
            print('Sorry dat is geen optie die we aanbieden...')
            i = 1
    bonnetjeZa()

def toppings():
    global topping, aantalGeen, aantalslagroom, aantalCaramelbakje, aantalCaramelhoorn, aantalSprinkles, keuze
    print('GEEN - SLAGROOM - SPRINKLES - CARAMELSAUS')
    topping = str(input(f'Welke topping wilt u? >>> ')).lower()
    if topping == 'geen':
        aantalGeen += 1
    elif topping == 'slagroom':
        aantalslagroom += 1
    elif topping == 'sprinkles':
        aantalSprinkles += 1
    elif topping == 'caramelsaus':
        if keuze == 'bakje':
            aantalCaramelbakje += 1
        elif keuze == 'hoorn':
            aantalCaramelhoorn += 1
    if paofza == 'particulier':
        bonnetjePa()
    else:
        print('Sorry dat is geen optie die we aanbieden...')

def bonnetjePa():
    global totaalPrijs, aantalBol, aantalHoorn, aantalBak, topping, totaalcaramelPrijsBak, totaalcaramelPrijsHoorn, totaalslagroomPrijs, totaalsprinklesPrijs
    totaalbolPrijs = float(bollen * bolPrijs)
    totaalhoornPrijs = float(aantalHoorn * hoornPrijs)
    totaalbakPrijs = float(aantalBak * bakPrijs)
    totaalslagroomPrijs = 0.50
    totaalsprinklesPrijs = aantalBol * 0.30
    totaalcaramelPrijsBak = aantalBak * 0.90
    totaalcaramelPrijsHoorn = aantalHoorn * 0.60
    topping = totaalslagroomPrijs + totaalsprinklesPrijs
    totaalPrijs = float(totaalbolPrijs + totaalhoornPrijs + totaalbakPrijs + topping)
    print('------------------------')
    if aantalBol >= 1: print(f'Bol      ' + str(bollen) + ' x ' + str(bolPrijs) + ' euro')
    if aantalHoorn >= 1: print(f'Hoorn    ' + str(aantalHoorn) + ' x ' + str(hoornPrijs) + ' euro')
    if aantalBak >= 1: print(f'Bak      ' + str(aantalBak) + ' x ' + str(bakPrijs) + ' euro')
    if aantalslagroom >= 1: print(f'Toppings      ' + str(totaalslagroomPrijs) + ' euro')
    if aantalSprinkles >= 1: print(f'Toppings      ' + str(totaalsprinklesPrijs) + ' euro')
    if aantalCaramelbakje >= 1: print(f'Toppings      ' + str(totaalcaramelPrijsBak) + ' euro')
    if aantalCaramelhoorn >= 1: print(f'Toppings      ' + str(totaalcaramelPrijsHoorn) + ' euro')
    print('------------------------')
    print(f'{totaalPrijs:.2f} euro')
    afrekenen()

def bonnetjeZa():
    global zakelijk, aantalLiters, totaalPrijsBelasting, totaalAlles, aardbei, chocolade, vanille
    totaalPrijsBelasting = float(aantalLiters * literPrijs)
    totaalBelasting = (totaalPrijsBelasting * 0.06)
    totaalAlles = (totaalBelasting + totaalPrijsBelasting)
    print('------------------------')
    if aantalLiters >= 1: print(f'Liter ijs      ' + str(aantalLiters) + ' x ' + str(literPrijs) + ' euro')
    print('------------')
    if aardbei >= 1: print(f'Aardbei      {aardbei} liter')
    if chocolade >= 1: print(f'Chocolade      {chocolade} liter')
    if vanille >= 1: print(f'Vanille      {vanille} liter')
    print('------------------------')
    print(f'{totaalBelasting:.2f} BTW')
    print(f'{totaalAlles:.2f} euro')
    afrekenen()
    
def afrekenen():
    global totaalPrijs, totaalPrijsBelastings, aantalBol, aantalHoorn, aantalBak, totaalAlles
    afrekening = str(input('Wilt u afrekenen? (J/N) >>> '))
    if afrekening == 'j':
        print(f'Resterend bedrag om te betalen is {totaalPrijs or totaalAlles:.2f} euro')
        bedragbetalen = float(input('Typ het volledige bedrag in >>> '))
        if bedragbetalen == bedragbetalen:
            print('Bedankt voor de betaling, hier is uw ijs. Fijne dag verder')
        else:
            print('Je moet wel geld betalen!')
            (exit)
    elif afrekening == 'n':
            afgifte = str(input('Wilt u nog meer bestellen? (J/N) >>> ')).lower()
            if afgifte == 'j':
                afgifteVraag = str(input(f'Is dit zakelijk of particulier? >>> ')).lower()
                if afgifteVraag == 'particulier':
                    particulier()
                elif afgifteVraag == 'zakelijk':
                    zakelijk()
            elif afgifte == 'n':
                stop = str(input(f'Wil je de bestelling stoppen? (J/N) >>> '))
                if stop == 'j':
                    exit()
                elif stop == 'n':
                    afrekenen()

paza()