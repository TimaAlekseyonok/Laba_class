class Mebel:
    def __init__(self, name, mats, dementions):
        self.name = name
        self.mats = mats
        self.dementions = dementions

    def get_name(self):
        print(f'Название изделия: {self.name}')

    def get_mats(self):
        print(f'Материалы: ')
        for material in self.mats:
            print(material)

    def get_dementions(self):
        print(f'Размеры: ')
        for os, razmer in self.dementions.items():
            print(f'{os}: {razmer} mm')

    def get_all_info(self):
        self.get_name()
        self.get_mats()
        self.get_dementions()