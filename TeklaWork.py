#Подключение бибилиотек Tekla
import clr 
from Classes import Wall,Walls

tekla_path = r"C:/Program Files/Tekla Structures/2020.0/nt/bin/plugins/"  # Укажите ваш путь
clr.AddReference(tekla_path + "Tekla.Structures.dll")
clr.AddReference(tekla_path + "Tekla.Structures.Model.dll")
clr.AddReference(tekla_path + "Tekla.Structures.Drawing.dll")
#clr.AddReference("Tekla.Structures.Model")
from Tekla.Structures.Model import Model,Component, Beam,Position,CutPlane,Plane,BooleanPart
from Tekla.Structures.Geometry3d import Point,Vector
from Tekla.Structures.Model import *
#from Tekla.Structures import Position

def InputIKomponent(input_datas):
    model = Model()
    if not model.GetConnectionStatus():
        print("Не удалось подключиться к модели Tekla")
        exit()

    x_pos=0.0 # Точко вставки компонентов
    cons_inter=20 # Величина зазора между конструкциями
    for wall in input_datas.sections:
        beam = Beam() # Будет создавать компонент подпорной стенки
        beam.StartPoint = Point(wall.tek_start_x, wall.tek_start_y, wall.foundation_base)# Стартовая точка компонента
        x_pos+=wall.leght
        beam.EndPoint = Point(wall.tek_end_x, wall.tek_end_y, wall.foundation_base)# Конечная точка компонента
        #Здесь будут заполняться атрибуты компонента
        beam.Profile.ProfileString = f"RCRW{max(wall.height_start,wall.height_end)}*{wall.foundation_width}-{wall.top_wall_width}*{wall.edge_distance}-{wall.bottom_wall_width}-{wall.t1}*{wall.t2}-{wall.t3}*{wall.t4}" # HEA300
        beam.Material.MaterialString = "Сoncrete"
        beam.Class = "3"

        #Установка положения балки по глубине в позицию "Спереди"
        position = getattr(Position.DepthEnum, 'FRONT')#
        
        beam.Position.Depth = position 

        if beam.Insert():
            print(wall.name_wall + " успешно создана")
            model.CommitChanges()  # Сохраняем изменения в модели
            #return beam
        else:
            print("Ошибка при создании " + wall.name_wall)
            return None
        print(wall.foundation_base)
        # cut_beam=Beam()
        # cut_beam.StartPoint=Point(beam.StartPoint.X,beam.StartPoint.Y+wall.foundation_width/2-wall.edge_distance,beam.StartPoint.Z+wall.height_start)
        # cut_beam.EndPoint=Point(beam.EndPoint.X,beam.EndPoint.Y+wall.foundation_width/2-wall.edge_distance,beam.EndPoint.Z+wall.height_end)
        # cut_beam.Profile.ProfileString=f"{1000}*{1000}"
        # cut_beam.Position.Depth = getattr(Position.DepthEnum, 'FRONT')
        # cut_beam.Insert()

        x_pos+=cons_inter#Зазор между секциями

 
    
   
    


    
