from mebel import Mebel


class Stul(Mebel):
    def __init__(self, name, mats, dementions, back):
        Mebel.__init__(self, name, mats, dementions)
        self.back = back

    def get_back(self):
        print(f'Материал спинки: {self.back}')

    def get_all_info(self):
        super().get_all_info()
        self.get_back()