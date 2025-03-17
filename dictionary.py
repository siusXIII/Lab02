class Dictionary:

    dizionario = {}

    def __init__(self, diz):
        with open(diz, "r", encoding="utf-8") as file:
            righe = file.readlines()
            for riga in righe:
                [key, value] = riga.strip("\n").split(" ")
                if key in self.dizionario:
                    self.dizionario[key].append(value)
                else:
                    self.dizionario[key] = [value]
                #self.dizionario[key] = [value]

    def addWord(self, alieno, italiano):
        if alieno.lower() in self.dizionario:
            self.dizionario[alieno.lower()].append(italiano.lower())
        else:
            self.dizionario[alieno.lower()] = [italiano.lower()]

    def translate(self, alieno):
        return self.dizionario.get(alieno.lower(), [])

    def translateWordWildCard(self, txt):
        trovate =[]
        parts = txt.split("?")
        for d in self.dizionario.keys():
            if len(txt) == len(d):
                if parts[0] == d[0:len(parts[0])] and parts[1] == d[len(parts[0])+1:len(d)]:
                    trovate.append(d)
        return trovate