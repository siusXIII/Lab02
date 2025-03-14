class Dictionary:

    def __init__(self):
        self._diz = {}

    def addWord(self, alieno, italiano):
        if alieno.lower() in self._diz:
            prevVal = self._diz.get(alieno.lower())
            if isinstance(prevVal, str):
                currentVal = []
                currentVal.append(prevVal)
            else:
                currentVal = self._diz.get(alieno.lower())
            print(currentVal)
            self._diz[alieno.lower()] = [*currentVal, italiano.lower()]
            print(self._diz[alieno.lower()])
        else:
            self._diz[alieno.lower()] = italiano.lower()

    def translate(self, alieno):
        return self._diz.get(alieno.lower(), [])

    def translateWordWildCard(self, txt):
        trovate = []
        parts = txt.split("?")
        for d in self._diz.keys():
            if len(txt) == len(d):
                if parts[0] == d[0:len(parts[0])] and parts[1] == d[len(parts[0])+1:len(d)]:
                    trovate.append(d)
        return trovate

    def loadDictionary(self):
        with open("dictionary.txt", "r", encoding="utf-8") as file:
            #righe = file.readlines()
            for riga in file:
                [key, value] = riga.strip("\n").split(" ")
                self._diz[key] = value

    def printAll(self):
        for key, value in self._diz.items():
            # Assuming getAlienWord and getTranslations are methods to access object properties
            alienWord = key
            translations = value
            print(f"Alien Word: {alienWord}, Translations: {translations}\n")
