print('Welkom bij Papi Gelato, wij hebben de juiste smaken!')

aardbei = 0
chocolade = 0
munt = 0
vanille = 0

slagroomPrijs = 0
SprinklesPrijs = 0
CaramelPrijshoorn = 0
CaramelPrijsbakje = 0

aantalLiter = 0
aantalBol = 0
aantalHoorn = 0
aantalBak = 0

literPrijs = 9.80
totaalPrijs = 0
hoornPrijs = 1.25
bakPrijs = 0.75
bolPrijs = 1.10
literPrijs = 9.80
particulier = False
zakelijk = False

def smaken():
    print('AARDBEI - CHOCOLADE - MUNT - VANILLE')
    smaak = str(input(f'Welke smaak wilt u? >>> ')).lower()
    print(f'{smaak} dat is een lekkere smaak!')
    smaakKeuze = str(input('Wil je nog een smaak kiezen? (J/N) >>> ')).lower()
    if smaakKeuze == 'j':
        smaken()
    if smaakKeuze == 'n':
        particulier()
    else:
        sorry()
        smaken()

def toppings():
    toppings = str(input(f'Welke topping wilt u? >>> ')).lower()

def particulier():
    global totaalPrijs, aantalBol, aantalHoorn, aantalBak, totaalbolPrijs, totaalbakPrijs, totaalhoornPrijs
    aantalBol = int(input('Hoeveel bolletjes wilt u? >>> '))
    if aantalBol >= 1 and aantalBol <= 3:
        keuze = str(input(f'Wilt u deze {aantalBol} bolletje(s) in een hoorn of een bak? >>> ')).lower()
        if keuze == 'hoorn':
            aantalHoorn += 1
            print(f'Hier is uw {keuze} met {aantalBol} bolletje(s)')
            bonnetjePa()
        elif keuze == 'bak':
            aantalBak += 1
            print(f'Hier is uw {keuze} met {aantalBol} bolletje(s)')
            bonnetjePa()
        else:
            sorry()
            particulier()
    elif aantalBol >= 4 and aantalBol <= 8:
        aantalBak += 1
        print('Dan krijgt u van mij een bakje met {aantalBol} bolletjes')
        bonnetjePa()
    elif aantalBol >= 9:
        print('Sorry, zulke grote bakken hebben we niet.')
        particulier()
    else:
        sorry()
        particulier()

def zakelijk():
    aantalLiter = int(input('Hoeveel liter wilt u? >>> '))
    i = 1
    while i <= aantalLiter:
        literSmaak = input('Wat voor smaakt wilt u? ' + str(i) + '?\n')
        i += 1
    bonnetjeZa()


def bonnetjePa():
    global totaalPrijs, aantalBol, aantalHoorn, aantalBak, totaalbolPrijs, totaalbakPrijs, totaalhoornPrijs, toppings
    totaalbolPrijs = float(aantalBol * bolPrijs)
    totaalhoornPrijs = float(aantalHoorn * hoornPrijs)
    totaalbakPrijs = float(aantalBak * bakPrijs)
    totaalslagroomPrijs = slagroomPrijs + 0.50
    totaalsprinklesPrijs = aantalBol * 0.30
    totaalcaramelPrijs = aantalBak * 0.90 and aantalHoorn * 0.60
    topping = totaalslagroomPrijs + totaalsprinklesPrijs + totaalcaramelPrijs
    totaalPrijs = float(totaalbolPrijs + totaalhoornPrijs + totaalbakPrijs + topping)
    print('------------------------')
    if aantalBol >= 1: print(f'Bol      ' + str(aantalBol) + ' x ' + str(bolPrijs) + ' euro')
    if aantalHoorn >= 1: print(f'Hoorn    ' + str(aantalHoorn) + ' x ' + str(hoornPrijs) + ' euro')
    if aantalBak >= 1: print(f'Bak      ' + str(aantalBak) + ' x ' + str(bakPrijs) + ' euro')
    if topping >= 1: print(f'Topping      ' + str(topping) + ' euro')
    print('------------------------')
    print(f'{totaalPrijs} euro')
    afrekenen()

def bonnetjeZa():
    global zakelijk, aantalLiter
    totaalPrijs = int(aantalLiter * literPrijs)
    totaalPrijsBelasting = int(totaalPrijs * 0.06)
    print('------------------------')
    if aantalLiter >= 1: print(f'Liter ijs      ' + str(aantalLiter) + ' x ' + str(literPrijs) + ' euro')
    else: print('Er is geen aantal liter aangegeven.')
    print('------------------------')
    print(f'{totaalPrijsBelasting} euro')
    afrekenen()
    
def afrekenen():
    global totaalPrijs, aantalBol, aantalHoorn, aantalBak, totaalbolPrijs, totaalbakPrijs, totaalhoornPrijs
    afrekenen = str(input('Wilt u afrekenen? (J/N) >>> '))
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
                particulier()
            elif afgifte == 'n':
                afrekenen()
    else:
        print('Ik begrijp dit niet...')
        exit()
        
def sorry():
    print('Sorry, dat snap ik niet.')

def paza():
    paza = str(input('Wilt u dit particulier kopen of zakelijk? >>> ')).lower()
    if paza == "particulier":
        particulier()
    if paza == "zakelijk":
        zakelijk()

paza()