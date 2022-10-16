


class team:
    def __init__(self, nev, projekt, szerep):
        self._nev = nev
        self._projekt = projekt
        self._szerep = szerep
        
    @property
    def projekt(self):
        return self._projekt

    @projekt.setter
    def projekt(self, job):
        self._projekt = job

    def __str__(self):
        return self._nev + " a " + self._projekt + "-en dolgozik " + self._szerep + " szerepkörben."

    def __eq__(self, another_worker):
        return self._nev != another_worker._nev and self._projekt == another_worker._projekt
 
worker1 = team("Ricsi", "SolArch", "Frontend")
worker2 = team("Angéla", "ZerTeng", "Tesztelő")
worker3 = team("Peti", "KefERP", "Backend")
worker4 = team("Éva", "KefERP", "Frontend")

print("-- Developer létrehozva. --")
print(worker1)

print("-- Developer létrehozva. --")
print(worker2)

print("-- Developer létrehozva. --")
print(worker3)

print("-- Developer létrehozva. --")
print(worker4)

osszehas = (worker3 == worker4)
if osszehas == True:

    print(worker3._nev + " és " + worker4._nev + " dolgoznak egy projekten.")
