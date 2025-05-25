#Подключение бибилиотек Tekla
import clr 
from Classes import Wall,Walls

tekla_path = r"C:/Program Files/Tekla Structures/2020.0/nt/bin/plugins/"  # Укажите ваш путь
clr.AddReference(tekla_path + "Tekla.Structures.dll")
clr.AddReference(tekla_path + "Tekla.Structures.Model.dll")
clr.AddReference(tekla_path + "Tekla.Structures.Drawing.dll")

from Tekla.Structures.Model import Model,Component, Beam
from Tekla.Structures.Geometry3d import Point

def InputIKomponent(input_datas,komponent_name):
    model = Model()
    if not model.GetConnectionStatus():
        print("Не удалось подключиться к модели Tekla")
        exit()

    x_pos=0.0 # Точко вставки компонентов
    cons_inter=20 # Величина зазора между конструкциями
    for wall in input_datas.sections:
        beam = Beam() # Будет создавать компонент подпорной стенки
        beam.StartPoint = Point(x_pos, 0, wall.foundation_base)# Стартовая точка компонента
        x_pos+=wall.leght
        beam.EndPoint = Point(x_pos, 0, wall.foundation_base)# Конечная точка компонента
        #Здесь будут заполняться атрибуты компонента
        beam.Profile.ProfileString = "HEA300"
        beam.Material.MaterialString = "S235JR"
        beam.Class = "3"

        if beam.Insert():
            print(wall.name_wall + " успешно создана")
            model.CommitChanges()  # Сохраняем изменения в модели
            #return beam
        else:
            print("Ошибка при создании " + wall.name_wall)
            return None
        x_pos+=cons_inter#Зазор между секциями

 
    
   
    


    
