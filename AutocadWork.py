try:
    from pyautocad import Autocad, APoint
    from Classes import Wall,Walls
    import math
    import Functions

    def DrawAutocad(input_datas):
        #  --\\ОТРИСОВКА\\--
        acad= Autocad(create_if_not_exists=False)
        print("Необходимо ввести точку вставки, пожалуйста перейдите в AutoCad")
        start_point = acad.doc.Utility.GetPoint(APoint(0, 0), "Введите точку вставки: ")# ввод от пользователя точки вставки картинки в автокад

        Line_distance = 85000 #расстояние между двух видовых рамок секций
        View_l1 = 5000 #расстояние между фасадом и сечением 1-1 (по горизонтали)
        View_l2 = 3000 #расстояние сечением 1-1 и сечением 2-2 (по горизонтали)
        View_l3 =  10000 #расстояние между фасадом и планом (по вертикали)
        i=0
        for input_data in input_datas.sections:
            incert_point=APoint(start_point[0]+Line_distance*i,input_data.foundation_base)#Точка вставки - левый нижний угол фасада подпорной стены
            i+=1
            SECTION_Coor = [] #список всех координат видов в одной секции стенки

            SECTION_Coor.append(APoint(0,0)) #0 - фиктивная точка 00 для начала нумерации нормальных точек с единицы
            SECTION_Coor.append(incert_point)#1
            #Фасад
            SECTION_Coor.append(APoint(incert_point.x, incert_point.y + input_data.t2))#2
            SECTION_Coor.append(APoint(SECTION_Coor[2].x + input_data.leght, SECTION_Coor[2].y))#3
            SECTION_Coor.append(APoint(SECTION_Coor[1].x + input_data.leght, SECTION_Coor[1].y))#4
            SECTION_Coor.append(APoint(incert_point.x, incert_point.y + input_data.height_start))#5
            SECTION_Coor.append(APoint(incert_point.x + input_data.leght, incert_point.y + input_data.height_end))#6

            #Вид 1-1
            #Задаем точку НК чтобы каждый вид считать от 0.0 а не прибавлять все расстояния в каждой точке
            start_coordinates = APoint(incert_point.x + input_data.leght + View_l1, incert_point.y) 
            print("start coordinate: " + str(start_coordinates.x) +" " + str(start_coordinates.y))

            SECTION_Coor.append(APoint(start_coordinates.x, start_coordinates.y))#7
            SECTION_Coor.append(APoint(start_coordinates.x, start_coordinates.y + input_data.t2))#8
            SECTION_Coor.append(APoint(start_coordinates.x + input_data.edge_distance , start_coordinates.y + input_data.t1))#9
            SECTION_Coor.append(APoint(start_coordinates.x + input_data.edge_distance , start_coordinates.y + input_data.height_start))#10
            SECTION_Coor.append(APoint(start_coordinates.x + input_data.edge_distance + input_data.top_wall_width, start_coordinates.y + input_data.height_start))#11
            SECTION_Coor.append(APoint(start_coordinates.x + input_data.edge_distance + input_data.bottom_wall_width, start_coordinates.y + input_data.t3))#12
            SECTION_Coor.append(APoint(start_coordinates.x + input_data.foundation_width, start_coordinates.y + input_data.t4))#13
            SECTION_Coor.append(APoint(start_coordinates.x + input_data.foundation_width, start_coordinates.y))#14

            #Вид 2-2
            #Задаем точку НК чтобы каждый вид считать от 0.0 а не прибавлять все расстояния в каждой точке
            start_coordinates = APoint(incert_point.x + input_data.leght + View_l1+ View_l2+ input_data.foundation_width, incert_point.y) 
            #print("start coordinate: " + str(start_coordinates.x) +" " + str(start_coordinates.y))

            SECTION_Coor.append(APoint(start_coordinates.x, start_coordinates.y))#15
            SECTION_Coor.append(APoint(start_coordinates.x, start_coordinates.y + input_data.t2))#16
            SECTION_Coor.append(APoint(start_coordinates.x + input_data.edge_distance , start_coordinates.y + input_data.t1))#17
            SECTION_Coor.append(APoint(start_coordinates.x + input_data.edge_distance , start_coordinates.y + input_data.height_end))#18
            SECTION_Coor.append(APoint(start_coordinates.x + input_data.edge_distance + input_data.top_wall_width, start_coordinates.y + input_data.height_end))#19
            SECTION_Coor.append(APoint(start_coordinates.x + input_data.edge_distance + input_data.bottom_wall_width, start_coordinates.y + input_data.t3))#20
            SECTION_Coor.append(APoint(start_coordinates.x + input_data.foundation_width, start_coordinates.y + input_data.t4))#21
            SECTION_Coor.append(APoint(start_coordinates.x + input_data.foundation_width, start_coordinates.y))#22

            #План 
            start_coordinates = APoint(incert_point.x, incert_point.y - View_l3)

            SECTION_Coor.append(APoint(start_coordinates.x, start_coordinates.y))#23
            SECTION_Coor.append(APoint(start_coordinates.x, start_coordinates.y + input_data.foundation_width))#24
            SECTION_Coor.append(APoint(SECTION_Coor[24].x+input_data.leght, SECTION_Coor[24].y))#25
            SECTION_Coor.append(APoint(SECTION_Coor[23].x+input_data.leght, SECTION_Coor[23].y))#26
            SECTION_Coor.append(APoint(start_coordinates.x, start_coordinates.y+input_data.edge_distance))#27
            SECTION_Coor.append(APoint(start_coordinates.x, start_coordinates.y+input_data.edge_distance+input_data.bottom_wall_width))#28
            SECTION_Coor.append(APoint(SECTION_Coor[28].x + input_data.leght, SECTION_Coor[28].y))#29
            SECTION_Coor.append(APoint(SECTION_Coor[27].x + input_data.leght, SECTION_Coor[27].y))#30
            SECTION_Coor.append(APoint(start_coordinates.x, start_coordinates.y+input_data.edge_distance+input_data.top_wall_width))#31
            SECTION_Coor.append(APoint(SECTION_Coor[31].x+input_data.leght, SECTION_Coor[31].y))#32
    
            input_datas.sections_coors.append(SECTION_Coor)


            #Массив топологии видов стенок
            #Отрисовка ведется отрезками.Заполняем список мини-спиками - в которых записано начало и конец отрезка

            Topology=[]

            #Фасад

            Topology.append([1,4])
            Topology.append([2,3])
            Topology.append([5,6])
            Topology.append([1,5])
            Topology.append([4,6])

            #Вид 1-1
            Topology.append([7,8])
            Topology.append([8,9])
            Topology.append([9,10])
            Topology.append([10,11])
            Topology.append([11,12])
            Topology.append([12,13])
            Topology.append([13,14])
            Topology.append([14,7])
        


            #Вид 2-2
            Topology.append([15,16])
            Topology.append([16,17])
            Topology.append([17,18])
            Topology.append([18,19])
            Topology.append([19,20])
            Topology.append([20,21])
            Topology.append([21,22])
            Topology.append([22,15])

            #План
            Topology.append([23,24])
            Topology.append([24,25])
            Topology.append([25,26])
            Topology.append([26,23])
            Topology.append([28,29])
            Topology.append([27,30])
            Topology.append([31,32])
        
            #Линии границы ф-та и стены на 1-1 и 2-2
            Topology.append([9,12])
            Topology.append([17,20])

            # Создание маcсива топологии для отрисовки размерных линий
            # Все размеры создаются строго слева направо или снизу вверх!!!    
            # [[x,y,Тип размера, Величина отступа]]   
 
            SizeTopology=[]

            #Размеры видов в масштабе 1:100
            SizeStyle1 = 'LIN100'

            SizeTopology.append([1, 5, math.pi/2, 1000,SizeStyle1])
            SizeTopology.append([4, 6, 3*math.pi/2, 1000,SizeStyle1])
            SizeTopology.append([23, 26, 0, 1000,SizeStyle1])

            SizeTopology.append([23, 24, math.pi/2, 1200,SizeStyle1])
            SizeTopology.append([23, 27, math.pi/2, 500,SizeStyle1])
            SizeTopology.append([27, 28, math.pi/2, 500,SizeStyle1])
            SizeTopology.append([28, 24, math.pi/2, 500,SizeStyle1])

            #Размеры сечений в масштабе 1:50
            SizeStyle2 = 'LIN50'

            SizeTopology.append([7, 10, math.pi/2, 500,SizeStyle2])
            SizeTopology.append([7, 14, 0, 500,SizeStyle2])

            SizeTopology.append([15, 18, math.pi/2, 500,SizeStyle2])
        
            SizeTopology.append([7, 10, math.pi/2, 1000,SizeStyle2])
            SizeTopology.append([7, 8, math.pi/2, 500,SizeStyle2])
            SizeTopology.append([10, 11, math.pi, 300,SizeStyle2])
            SizeTopology.append([11, 12, math.pi, 300,SizeStyle2])
            SizeTopology.append([14, 13,math.pi*1.5, 500,SizeStyle2])

            SizeTopology.append([15, 18, math.pi/2, 1000,SizeStyle2])
            SizeTopology.append([15, 16, math.pi/2, 500,SizeStyle2])
            SizeTopology.append([15, 22, 0, 500,SizeStyle2])
            SizeTopology.append([18, 19, math.pi, 300,SizeStyle2])
            SizeTopology.append([19, 20, math.pi, 300,SizeStyle2])
            SizeTopology.append([22, 21,math.pi*1.5, 500,SizeStyle2])




        #Отрисовка видов
        index = 0 # Индекс для обращения к параметрам секции
        for SECTION_Coor in input_datas.sections_coors:
    
            acad.doc.ActiveLayer = acad.doc.Layers.Item("Notes")
            rec_size=Functions.GetRecSize(SECTION_Coor[1],(SECTION_Coor[22].x-SECTION_Coor[1].x),(SECTION_Coor[6].y-SECTION_Coor[26].y))
  
            #command = f"_-RECTANG _non {rec_size[0].x},{rec_size[0].y} _non {rec_size[0].x + rec_size[2]},{rec_size[0].y + rec_size[1]}\n"
            #acad.doc.SendCommand(command)
            points = [
            APoint(rec_size[0].x, rec_size[0].y),
            APoint(rec_size[0].x + rec_size[2], rec_size[0].y),
            APoint(rec_size[0].x + rec_size[2], rec_size[0].y + rec_size[1]),
            APoint(rec_size[0].x, rec_size[0].y + rec_size[1]),
            APoint(rec_size[0].x, rec_size[0].y)  # замыкаем прямоугольник
            ]
            for it in range(1,len(points)):
                acad.model.AddLine(points[it-1],points[it])    # Создание полилинии (прямоугольника)

            acad.doc.ActiveLayer = acad.doc.Layers.Item("Contur")#установка слоя для отрисовки
            for item in Topology:
                start_point=APoint(SECTION_Coor[item[0]].x,SECTION_Coor[item[0]].y)
                end_point=APoint(SECTION_Coor[item[1]].x,SECTION_Coor[item[1]].y)
                acad.model.AddLine(start_point,end_point)
        
            #Отрисовка размерных линий
            acad.doc.ActiveLayer = acad.doc.Layers.Item("Size") #установка слоя для отрисовки 

            for item in SizeTopology:
                acad.doc.ActiveDimStyle = acad.doc.DimStyles.Item(item[4]) # Выставление необходимого размерного стиля 
                start_point = APoint(SECTION_Coor[item[0]].x, SECTION_Coor[item[0]].y )
                end_point = APoint(SECTION_Coor[item[1]].x, SECTION_Coor[item[1]].y )
                dim_position = Functions.GetSizePoint(start_point,end_point,item[2],item[3])
                dim_obj = acad.model.AddDimRotated(start_point, end_point, dim_position,item[2])
            
            # Вставка блока отметки
        
            acad.model.InsertBlock(
                APoint(SECTION_Coor[1].x+(SECTION_Coor[4].x- SECTION_Coor[1].x)/2  , input_datas.sections[index].foundation_base), #Точка вставки - SECTION_Coor[4].x)/2
                'Otmetka', #Имя блока
                1, #Масштаб по Х
                1, #Y
                1, #Z
                0) #Угол поворота
        
            acad.model.InsertBlock(
                SECTION_Coor[6], 
                'Otmetka', 
                1, 
                1, 
                1, 
                0)
        
            acad.model.InsertBlock(
                SECTION_Coor[5], 
                'Otmetka', 
                1, 
                1, 
                1, 
                0)
      
                    
            #Вывод названий видов
        
            acad.doc.ActiveLayer = acad.doc.Layers.Item("Text_B")
            text_style = acad.doc.TextStyles.Item("RS0.7") 
            acad.doc.ActiveTextStyle=text_style
            to_view_dis = 2500 # Расстояние от вида до его текста

            text_fas=acad.model.AddMText(Functions.GetStringPoint(SECTION_Coor[5],SECTION_Coor[6],to_view_dis),0,"Фасад " + input_datas.sections[index].name +"\n (1 : 100)")
            text_fas.Height = 400
        
            text_fas.AttachmentPoint = 5#ACAttachmentPoint.MiddleCenter Выравнивание текста по центру  
            text_plan=acad.model.AddMText(Functions.GetStringPoint(SECTION_Coor[24],SECTION_Coor[25],to_view_dis),0,"План (1 : 100)")
            text_plan.Height=400
            text_1_1=acad.model.AddMText(Functions.GetStringPoint(SECTION_Coor[10],SECTION_Coor[11],to_view_dis/2),0,"1 - 1 (1 : 50)")
            text_1_1.Height=200
            text_2_2=acad.model.AddMText(Functions.GetStringPoint(SECTION_Coor[18],SECTION_Coor[19],to_view_dis/2),0,"2 - 2 (1 : 50)")
            text_2_2.Height=200
        
        
              # Создание таблицы ведомости объемов работ
            acad.doc.ActiveLayer = acad.doc.Layers.Item("T_Border") #установка слоя для отрисовки 

            # Apoint (точка вставки, кол-во строк, кол-во столбцов, высота строки, ширина столбца) - таблица автоматически создается с объединенной 1-й строкой -типа название таблицы

            table = acad.model.AddTable(APoint(points[2].x - 18500, points[2].y),4,3,1000,1000) 

            #table.SetTextHeight(5) #высота текста 3 - задается для всей таблицы
            # Задать сразу правильные размеры столбцов и строк - нельзя. Поэтому изменяем их после создания таблицы другим методом:#
    
            table.SetColumnWidth (0, 14500) # 1й столбец ширина = 145000
            table.SetColumnWidth (1, 1500)
            table.SetColumnWidth (2, 2500)

            table.SetRowHeight (0, 1500)
            table.SetRowHeight (1, 1500)
            table.SetRowHeight (2, 1300)
            table.SetRowHeight (3, 1300)

            #Заполнение текстом

            table.SetText (0, 0 , 'Ведомость основных объемов работ') # 1 строка 1 столбец " заголовок"
            table.SetText (1, 0 , 'Наименование работ')
            table.SetText (2, 0 , 'Ростверк подпорных стен монолитный железобетонный \n - бетон В30 F{\\S1^;}200 W8 ГОСТ 26633-2015')
            table.SetText (3, 0 , 'Тело подпорных стен монолитное железобетонное \n - бетон В30 F{\\S1^;}300 W8 ГОСТ 26633-2015')
            table.SetText (1, 1 , 'Ед.изм.')
            table.SetText (1, 2 , 'Кол.')
            table.SetText (2, 1 , 'м3')
            table.SetText (3, 1 , 'м3')
            table.SetText (2, 2, round(input_datas.sections[index].V1 , 1))
            table.SetText (3, 2, round(input_datas.sections[index].V2 , 1))
        
            # Редактирование высоты и стиля текста в таблице
            table_text_height=350
            for row in range(table.Rows):
                for col in range(table.Columns):
                    table.SetCellTextStyle(row, col, "RS0.7")
                    table.SetCellAlignment(row, col,5)
                    table.SetCellTextHeight(row, col, table_text_height)

            index+=1 #Итератор смены секции
except Exception as e:
    print(e)
