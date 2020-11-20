word = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def terbilang(x):
    if x < 10:
        return word[x]
    elif x >= 1_000_000_000:
        return terbilang(n // 1_000_000_000) + ' billion ' + (terbilang(x % 1_000_000_000) if x % 1_000_000 != 0 else '')
    elif x >= 1_000_000:
        return terbilang(x // 1_000_000) + ' million ' + (terbilang(x % 1_000_000) if x % 1_000_000 != 0 else '')
    elif x >= 1_000:
        return terbilang(x // 1_000) + ' thousand ' + (terbilang(x % 1_000) if x % 1_000 != 0 else '')
    elif x >= 100:
        return terbilang(x // 100) + ' hundred ' + (terbilang(x % 100) if x % 100 != 0 else '')
    elif x >= 90:
        return ' ninety ' + (terbilang(x % 10) if x % 10 != 0 else '')
    elif x >= 80:
        return ' eighty ' + (terbilang(x % 10) if x % 10 != 0 else '')
    elif x >= 70:
        return ' seventy ' + (terbilang(x % 10) if x % 10 != 0 else '')
    elif x >= 60:
        return ' sixty ' + (terbilang(x % 10) if x % 10 != 0 else '')
    elif x >= 50:
        return ' fifty ' + (terbilang(x % 10) if x % 10 != 0 else '')
    elif x >= 40:
        return 'fourty ' + (terbilang(x % 10) if x % 10 != 0 else '')
    elif x >= 30:
        return 'thirty ' + (terbilang(x % 10) if x % 10 != 0 else '')
    elif x >= 20:
        return 'twenty ' + (terbilang(x % 10) if x % 10 != 0 else '')
    else:
        if x == 10:
            return ' ten'
        elif x == 11:
            return ' eleven'
        elif x == 12:
            return ' twelve'
        elif x == 13:
            return ' thirteen'
        elif x == 15:
            return ' fifteen'
        else:
            return terbilang(x % 10) + 'teen'        


import os
while True:
    os.system('cls')
    print('Membuat Sebuah Angka Menjadi Huruf')
    print('         Selamat Mencoba         ')
    print('==================================')
    try:
        x = int(input('Please Input the Number ? '))
        print(f'{x:,} = {terbilang(x)}')
    except:
        print('Input Data is Incorret !!!')
    os.system('pause')