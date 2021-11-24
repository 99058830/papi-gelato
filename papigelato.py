print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')

def top():
    aantal = int(input('Hoeveel bolletjes wilt u? >>> '))
    if aantal >= 1 and aantal <= 3:
        wat = str(input(f'Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? >>> ')).lower()
        if wat == 'hoorntje' or wat == 'bakje':
            print(f'Hier is uw {wat} met {aantal} bolletje(s)')
            end()
    elif aantal >= 4 and aantal <= 8:
        print(f'Dan krijgt u van mij een bakje met {aantal} bolletjes')
        end()
    elif aantal >= 9:
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
        print('Bedankt en tot ziens!')
        exit()
    else:
        print('Ik begrijp dit niet...')
        end()

def sorry():
    print('Sorry, dat snap ik niet.')

top()