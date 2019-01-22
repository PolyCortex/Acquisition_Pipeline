
class Filter:

    def __init__(self, outQueue):
        self._outQueue = outQueue   # Output des donnees, donnee a la construction
        self._rawData        # Une queue qui contient les donnees non filtrees
        self._filteredData          # Une queue qui contient les donnees filtrees

    # Fonction lancee par le Reader pour ajouter une nouvelle donnee pour feeder le filtre
    def feedNewData(self, newData):
        a = 1
        # TODO: prendre la nouvelle donnee et l'ajouter dans les raw data
        # TODO: si la queue est pleine (?pas sur de ca) aappliquer le filtre
        # TODO: pop la donnee la plus recente dans le _outQueue
