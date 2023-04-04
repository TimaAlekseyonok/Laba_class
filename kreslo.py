from mebel import Mebel


class Kreslo(Mebel):
    def __init__(self, name, mats, dementions, mat_lining):
        Mebel.__init__(self, name, mats, dementions)
        self.mat_lining = mat_lining

    def get_mat_lining(self):
        print(f'Материал обшивки: {self.mat_lining}')

    def get_all_info(self):
        super().get_all_info()
        self.get_mat_lining()