import translator as tr

t = tr.Translator("dictionary.txt")


while(True):

    t.printMenu()

    dizionario = t.loadDictionary()

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print()
        txtIn = input("Ok, quale parola devo aggiungere:\n")
        t.handleAdd(txtIn)
    elif int(txtIn) == 2:
        txtIn = input("Ok, quale parola devo tradurre:\n")
        print(f"La traduzione di {txtIn} è: {t.handleTranslate(txtIn)}")
    elif int(txtIn) == 3:
        txtIn = input("Ok, quale wildCard devo tradurre:\n")
        for p in t.handleWildCard(txtIn):
            print(f"La traduzione di {p} è: {t.handleTranslate(p)}")
        pass
    elif int(txtIn) == 4:
        print(t.loadDictionary())
    elif int(txtIn) == 5:
        break