from mebel import Mebel
from stul import Stul
from kreslo import Kreslo
from game_kreslo import Game_kreslo


primer1 = Mebel('Элемент мебели', ['дерево', 'ткань'], {'x': '1200', 'y': '200', 'z': '600'})
primer1.get_all_info()
print(f'\n_________________\n')

primer2 = Stul('Стул', ['дерево',], {'x': '1200', 'y': '200', 'z': '600'}, 'дерево')
primer2.get_all_info()
print(f'\n_________________\n')

primer3 = Kreslo('Кресло', ['дерево', 'металл, ткань'], {'x': '1600', 'y': '900', 'z': '900'}, 'велюр')
primer3.get_all_info()
print(f'\n_________________\n')

primer4 = Game_kreslo('Игровое кресло', ['пластик', 'металл', 'кожа', 'экокожа'], {'x': '1600', 'y': '850', 'z': '850'}, 'экокожа', 'кожа', {'+': 5})
primer4.get_all_info()