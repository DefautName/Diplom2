#Подключение бибилиотек Tekla
import clr 
#import tekla.structures.model as ts_model

tekla_path = r"C:/Program Files/Tekla Structures/2020.0/nt/bin/plugins/"  # Укажите ваш путь
clr.AddReference(tekla_path + "Tekla.Structures.dll")
clr.AddReference(tekla_path + "Tekla.Structures.Model.dll")
#clr.AddReference(tekla_path + "Tekla.Structures.Model.UI.dll")
clr.AddReference(tekla_path + "Tekla.Structures.Drawing.dll")

from Tekla.Structures.Model import Model,Component, Beam
from Tekla.Structures.Geometry3d import Point
#from Tekla.Structures.Model.UI import *

def InputIKomponent(input_datas,komponent_name):
    model = Model()
    if not model.GetConnectionStatus():
        print("Не удалось подключиться к модели Tekla")
        exit()

    beam = Beam()
    beam.StartPoint = Point(0, 0, 0)
    beam.EndPoint = Point(0, 0, 5000)
    beam.Profile.ProfileString = "HEA300"
    beam.Material.MaterialString = "S235JR"
    beam.Class = "3"
    
      # Вставляем балку в модель
    if beam.Insert():
        print(f"Балка успешно создана")
        model.CommitChanges()  # Сохраняем изменения в модели
        return beam
    else:
        print("Ошибка при создании балки")
        return None
    
   
    


    
