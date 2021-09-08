dierenDresseur = input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur (type 0 wanneer geen)? -> ")
jongleren = input("Hoeveel jaar praktijkervaring heeft u met jongleren  (type 0 wanneer geen)? -> ")
acrobatiek = input("Hoeveel jaar praktijkervaring heeft u met acrobatiek  (type 0 wanneer geen)? -> ")
mbo4 = input("Heb je een MBO-4 diploma? -> ")
rijbewijs = input("Heb je een geldig vrachtwagen rijbewijs? -> ")
hogeHoed = input("Heb je een hoge hoed? -> ")
manOfVrouw = input("Bent u een man of vrouw? M/V -> ")

if manOfVrouw.lower() == "m":
    snor = input("Hoe breed is je snoor in cm -> ")
    haar = 0
elif manOfVrouw.lower() == "v":
    haar = input('Hoe lang is je krulhaar? -> ')
    snor = 0

lengte = input("Hoe lang ben je in cm? -> ")
gewicht = input("Hoe zwaar ben je in kg? -> ")
certificaat = input("Heb je een certificaat in overleven met gevaarlijk personeel? -> ")

if int(dierenDresseur) > 4:
    var1 = True
else: 
    var1 = False

if int(jongleren) > 5:
    var2 = True
else: 
    var2 = False

if int(acrobatiek) > 3:
    var3 = True
else:
    var3 = False

if mbo4.lower() == 'ja':
    var4 = True
else:
    var4 = False

if rijbewijs.lower() == 'ja':
    var5 = True
else:
    var5 = False

if hogeHoed.lower() == 'ja':
    var6 = True
else:
    var6 = False

if int(snor) > 10 or int(haar) > 20:
    var7 = True
else:
    var7 = False

if int(lengte) > 150:
    var8 = True
else:
    var8 = False

if int(gewicht) > 90:
    var9 = True
else:
    var9 = False

if certificaat.lower() == "ja":
    var10 = True
else:
    var10 = False

if var1 or var2 or var3:
    # print('var4',var4)
    # print('var5',var5)
    # print('var6',var6)
    # print('var7',var7)
    # print('var8',var8)
    # print('var9',var9)
    # print('var10',var10)

    if var4 and var5 and var6 and var7 and var8 and var9 and var10:
        print("Gefeliciteerd, u bent aangenoment")
    else:
        print("Helaas u bent niet aangenomen")
else:
    print('helaas u bent niet aangenomen')