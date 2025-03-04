from dictionary import Dictionary

class Translator:

    def __init__(self,diz):
        self.d = Dictionary(diz)

    def printMenu(self):
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")


    def loadDictionary(self):
        return self.d.dizionario


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parts = entry.split(" ")
        alieno = parts[0]
        italiano = parts[1:]
        for trad in italiano:
            self.d.addWord(alieno, trad)


    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        return self.d.translate(query)

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        return self.d.translateWordWildCard(query)
