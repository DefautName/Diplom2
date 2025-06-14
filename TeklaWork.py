try:
    #Подключение бибилиотек Tekla
    from pathlib import Path # Библиотека для указания пути к текущей папке
    import clr 
    from Classes import Wall,Walls

    # tekla_path = r"C:/Program Files/Tekla Structures/2020.0/nt/bin/plugins/"  # Укажите ваш путь
    tekla_path = Path.cwd() # Узнаем путь к папке, где лежит приложение
    clr.AddReference(str(tekla_path) + "/Tekla.Structures.dll") # отвечает за работу геометрии в текле
    clr.AddReference(str(tekla_path) + "/Tekla.Structures.Model.dll") # отвечает за работу с балками и прочими компонентами
    clr.AddReference(str(tekla_path) + "/Tekla.Structures.Drawing.dll") #  отвечает за работу с чертежом

    from Tekla.Structures.Model import Model, Beam,Position,BooleanPart
    from Tekla.Structures.Geometry3d import Point
    from Tekla.Structures.Model import *


    def InputIKomponent(input_datas):
        model = Model()
        if not model.GetConnectionStatus():
            print("Не удалось подключиться к модели Tekla")
            exit()

        for wall in input_datas.sections:
            beam = Beam()
            beam.StartPoint = Point(wall.tek_start_x, wall.tek_start_y, wall.foundation_base)# Стартовая точка подпорной стенки
            beam.EndPoint = Point(wall.tek_end_x, wall.tek_end_y, wall.foundation_base)# Конечная точка подпорной стенки
            beam.Profile.ProfileString = f"RCRW{max(wall.height_start,wall.height_end)}*{wall.foundation_width}-{wall.top_wall_width}*{wall.edge_distance}-{wall.bottom_wall_width}-{wall.t1}*{wall.t2}-{wall.t3}*{wall.t4}"
            # Материал Подпорной стенки
            beam.Material.MaterialString = "Сoncrete"
            beam.Class="3" # Задает цвет конструкциции (3 - зеленый)

            #Установка положения балки по глубине в позицию "Спереди"
            position = getattr(Position.DepthEnum, 'FRONT')
            beam.Position.Depth = position 

            if beam.Insert():# Вставляем объект и проверяем: создался или нет
                print(wall.name_wall + " успешно создана")
                model.CommitChanges()
            else:
                print("Ошибка при создании " + wall.name_wall)
                return None

            cut_beam = Beam()
            cut_beam.StartPoint = Point(wall.tek_start_x, wall.tek_start_y, wall.foundation_base+wall.height_start)# Стартовая точка подпорной стенки
            cut_beam.EndPoint = Point(wall.tek_end_x, wall.tek_end_y, wall.foundation_base+wall.height_end)# Конечная точка подпорной стенки
            cut_beam.Profile.ProfileString = f"{wall.foundation_width*2}*{wall.foundation_width*2}"
            cut_beam.Class=BooleanPart.BooleanOperativeClassName
            cut_beam.Position.Depth = position
            cut_beam.Insert()

            boolean_part = BooleanPart()
            boolean_part.Father = beam
            boolean_part.SetOperativePart(cut_beam)
            boolean_part.Type = BooleanPart.BooleanTypeEnum.BOOLEAN_CUT
            boolean_part.Insert()

            model.CommitChanges()
            model.GetModelObjectSelector().GetAllObjects().SelectInstances = False

            cut_beam.Delete()
            model.CommitChanges();
except Exception as e:
     print(e)
 
    
   
    


    
