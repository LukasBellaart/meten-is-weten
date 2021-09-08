isGeel = input('Is de kaas geel? -> ')

if isGeel.lower() == "ja":
    zijnGaten = input("Zitten er gaten in? -> ")
    if zijnGaten.lower() == "ja":
        isDuur = input("Is de kaas belachelijk duur? -> ")
        if isDuur.lower() == "ja":
            print("De kaas is Emmenthaler")
        elif isDuur.lower() == 'nee':
            print("De kaas is Leerdammer")
    elif zijnGaten.lower() == "nee":
        isHard = input("Is de kaas hard als steen? -> ")
        if isHard.lower() == "ja":
            print("De kaas is pammigiano reggiano")
        elif isHard.lower() == 'nee':
            print('De kaas is goudse kaas')
elif isGeel.lower() == "nee":
    heeftSchimmels = input("Heeft de kaas blauwe schimmels? -> ")
    if heeftSchimmels.lower() == "ja":
        heeftKorst = input("Heeft de kaas een korst? -> ")
        if heeftKorst.lower() == "ja":
            print("De kaas is bleu de rochbaron")
        elif heeftKorst.lower() == 'nee':
            print('de kaas is foumme d\'ambert')
    elif heeftSchimmels.lower() == 'nee':
        heeftKorst = input("Heeft de kaas een korst? -> ")
        if heeftKorst.lower() == "ja":
            print("De kaas is bleu de Camembert")
        elif heeftKorst.lower() == 'nee':
            print('de kaas is foumme d\'mozzerella')