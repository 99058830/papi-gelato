print('Welkom bij Papi Gelato, wij hebben de juiste smaken!')

aardbei = 0
chocolade = 0
munt = 0
vanille = 0

aantalGeen = 0
aantalslagroom = 0
aantalSprinkles = 0
aantalCaramelhoorn = 0
aantalCaramelbakje = 0

aantalLiters = 0
aantalBol = 0
aantalHoorn = 0
aantalBak = 0
literPrijs = 9.80
totaalPrijs = 0
totaalPrijsBelasting = 0
hoornPrijs = 1.25
bakPrijs = 0.75
bolPrijs = 1.10
literPrijs = 9.80

def paza():
    global paofza
    paofza = str(input('Wilt u dit particulier kopen of zakelijk? >>> ')).lower()
    if paofza == "particulier":
        particulier()
    if paofza == "zakelijk":
        zakelijk()
    else:
        sorry()
        exit()

def particulier():
    global totaalPrijs, aantalBol, aantalHoorn, aantalBak, aardbei, chocolade, munt, vanille, keuze, toppings
    aantalBol = int(input('Hoeveel bolletjes wilt u? >>> '))
    if aantalBol >= 9:
        print('Sorry, zulke grote bakken hebben we niet.')
        particulier()
    i = 1
    while i <= aantalBol:
        print('AARDBEI - CHOCOLADE - MUNT - VANILLE')
        bolSmaak = input('Wat voor smaakt wilt u? ' + str(i) + '\n').lower()
        i += 1
        if bolSmaak == 'aardbei':
            aardbei += 1
        elif bolSmaak == 'chocolade':
            chocolade += 1
        elif bolSmaak == 'munt':
            munt += 1
        elif bolSmaak == 'vanille':
            vanille += 1
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
        else:
            sorry()
            particulier()
    elif aantalBol >= 4 and aantalBol <= 8:
        aantalBak += 1
        print('Dan krijgt u van mij een bakje met {aantalBol} bolletjes')
        toppings()

def zakelijk():
    global aantalLiters, aardbei, chocolade, munt, vanille
    aantalLiters = int(input('Hoeveel liter wilt u? >>> '))
    i = 1
    while i <= aantalLiters:
        print('AARDBEI - CHOCOLADE - MUNT - VANILLE')
        literSmaak = input('Wat voor smaakt wilt u? ' + str(i) + '\n').lower()
        i += 1
        if literSmaak == 'aardbei':
            aardbei += 1
        elif literSmaak == 'chocolade':
            chocolade += 1
        elif literSmaak == 'munt':
            munt += 1
        elif literSmaak == 'vanille':
            vanille += 1
        else:
            sorry()
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
        sorry()

def bonnetjePa():
    global totaalPrijs, aantalBol, aantalHoorn, aantalBak, topping, totaalcaramelPrijsBak, totaalcaramelPrijsHoorn, totaalslagroomPrijs, totaalsprinklesPrijs
    totaalbolPrijs = float(aantalBol * bolPrijs)
    totaalhoornPrijs = float(aantalHoorn * hoornPrijs)
    totaalbakPrijs = float(aantalBak * bakPrijs)
    totaalslagroomPrijs = 0.50
    totaalsprinklesPrijs = aantalBol * 0.30
    totaalcaramelPrijsBak = aantalBak * 0.90
    totaalcaramelPrijsHoorn = aantalHoorn * 0.60
    topping = totaalslagroomPrijs + totaalsprinklesPrijs
    totaalPrijs = float(totaalbolPrijs + totaalhoornPrijs + totaalbakPrijs + topping)
    print('------------------------')
    if aantalBol >= 1: print(f'Bol      ' + str(aantalBol) + ' x ' + str(bolPrijs) + ' euro')
    if aantalHoorn >= 1: print(f'Hoorn    ' + str(aantalHoorn) + ' x ' + str(hoornPrijs) + ' euro')
    if aantalBak >= 1: print(f'Bak      ' + str(aantalBak) + ' x ' + str(bakPrijs) + ' euro')
    if aantalslagroom >= 1: print(f'Toppings      ' + str(totaalslagroomPrijs) + ' euro')
    if aantalSprinkles >= 1: print(f'Toppings      ' + str(totaalsprinklesPrijs) + ' euro')
    if aantalCaramelbakje >= 1: print(f'Toppings      ' + str() + ' euro')
    if aantalCaramelhoorn >= 1: print(f'Toppings      ' + str(totaalslagroomPrijs) + ' euro')
    print('------------------------')
    print(f'{totaalPrijs:.2f} euro')
    afrekenen()

def bonnetjeZa():
    global zakelijk, aantalLiters, totaalPrijsBelasting, aardbei, chocolade, munt, vanille
    totaalPrijsBelasting = float(aantalLiters * literPrijs)
    print('------------------------')
    if aantalLiters >= 1: print(f'Liter ijs      ' + str(aantalLiters) + ' x ' + str(literPrijs) + ' euro')
    print('------------')
    if aardbei >= 1: print(f'Aardbei      {aardbei} liter')
    if chocolade >= 1: print(f'Chocolade      {chocolade} liter')
    if munt >= 1: print(f'Munt            {munt} liter')
    if vanille >= 1: print(f'Vanille      {vanille} liter')
    print('------------------------')
    print(f'{totaalPrijsBelasting} euro')
    afrekenen()
    
def afrekenen():
    global totaalPrijs, totaalPrijsBelasting, aantalBol, aantalHoorn, aantalBak
    afrekening = str(input('Wilt u afrekenen? (J/N) >>> '))
    if afrekening == 'j':
        print(f'Resterend bedrag om te betalen is {totaalPrijs or totaalPrijsBelasting:.2f} euro')
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

def sorry():
    print('Sorry, dat snap ik niet.')

paza()