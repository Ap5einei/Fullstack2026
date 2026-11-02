# never stop the madness

from abc import ABC, abstractmethod

class Ajoneuvo(ABC):
    @abstractmethod
    def liikkuu(self):
        pass
    def meluaa(self):
        print("ajoneuvo meluaa")

class Bussi(Ajoneuvo):
    def __init__(self) -> None:
        super().__init__()
        self.bussimatkustaja = 50
    def liikkuu(self):
        print("bussi liikkuu")

class Juna(Ajoneuvo):
    pass

#mytesti = Ajoneuvo()
#mytesti.meluaa()

mybussi = Bussi()
mybussi.meluaa()
mybussi.liikkuu()
