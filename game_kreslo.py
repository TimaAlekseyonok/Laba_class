from stul import Stul
from kreslo import Kreslo


class Game_kreslo(Stul, Kreslo):
    def __init__(self, name, mats, dementions, back, mat_lining, kol):
        Stul.__init__(self, name, mats, dementions, back)
        Kreslo.__init__(self, name, mats, dementions, mat_lining)
        self.kol = kol

    def get_kol(self):
        for kol1, kol2 in self.kol.items():
            if kol1 == '+':
                print(f'Колёсики имеются в количестве {kol2} штук')
            else:
                print(f'Колёсики отсутствуют')

    def get_all_info(self):
        self.get_name()
        self.get_mats()
        self.get_dementions()
        self.get_mat_lining()
        self.get_back()
        self.get_kol()