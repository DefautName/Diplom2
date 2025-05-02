from tkinter import ROUND
from pyautocad import Autocad, APoint
from Classes import Wall,Walls
import Functions
import math
import openpyxl

# Описание файла и поожения данных для выгрузки в питон
file_Name="DATA_"
add=".xlsm"
sheet_Name="_ПС"
read_row=3 #Стартовая строка
read_column=5 #Стартовый столбец считывания данных по секции
workbook = openpyxl.load_workbook(file_Name+add, data_only=True )
sheet=workbook[sheet_Name]

input_datas=Walls()
input_datas.name=sheet.cell(row=read_row,column=read_column-1)
input_datas.total_count=0
print("Начало считывания данных с Ексель")
while sheet.cell(row=read_row,column=read_column).value != None:#"None"
   # print(sheet.cell(row=read_row,column=read_column).value)
    input_data = Wall()
    input_data.SetData(sheet,read_column)
    print(input_data.name)
    input_datas.total_count += 1
    input_datas.sections.append(input_data)
    read_column+=1
    

#  --\\ОТРИСОВКА\\--
acad= Autocad(create_if_not_exists=False)
print("Необходимо ввести точку вставки, пожалуйста перейдите в AutoCad")
start_point = acad.doc.Utility.GetPoint(APoint(0, 0), "Введите точку вставки: ")# ввод от пользователя точки вставки картинки в автокад

Line_distance = 85000 #расстояние между двух видовых рамок секций
View_l1 = 5000 #расстояние между фасадом и сечением 1-1 (по горизонтали)
View_l2 = 5000 #расстояние сечением 1-1 и сечением 2-2 (по горизонтали)
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

# Создание маcсива топологии для отрисовки размерных линий
# Все размеры создаются строго слева направо или снозу вверх!!!    
# [[x,y,Тип размера, Величина отступа]]   
 
SizeTopology=[]

#Размеры видов в масштабе 1:100
SizeStyle1 = 'LINE100'

SizeTopology.append([1, 5, math.pi/2, 1000,SizeStyle1])
SizeTopology.append([4, 6, 3*math.pi/2, 1000,SizeStyle1])

SizeTopology.append([23, 24, math.pi/2, 500,SizeStyle1])
SizeTopology.append([23, 26, 0, 1000,SizeStyle1])

#Размеры сечений в масштабе 1:50
SizeStyle2 = 'LINE50'

SizeTopology.append([7, 10, math.pi/2, 500,SizeStyle2])
SizeTopology.append([7, 14, 0, 1000,SizeStyle2])

SizeTopology.append([15, 18, math.pi/2, 500,SizeStyle2])
SizeTopology.append([15, 22, 0, 500,SizeStyle2])

 

#Отрисовка видов
for SECTION_Coor in input_datas.sections_coors:
    #Выставление необходимого слоя
    acad.doc.ActiveLayer = acad.doc.Layers.Item("Contur")#установка слоя для отрисовки
    for item in Topology:
        start_point=APoint(SECTION_Coor[item[0]].x,SECTION_Coor[item[0]].y)
        end_point=APoint(SECTION_Coor[item[1]].x,SECTION_Coor[item[1]].y)
        acad.model.AddLine(start_point,end_point)
        
    acad.doc.ActiveLayer = acad.doc.Layers.Item("Size") #установка слоя для отрисовки 

    #Отрисовка размерных линий
    for item in SizeTopology:
        start_point = APoint(SECTION_Coor[item[0]].x, SECTION_Coor[item[0]].y )
        end_point = APoint(SECTION_Coor[item[1]].x, SECTION_Coor[item[1]].y )
        dim_position = Functions.GetSizePoint(start_point,end_point,item[2],item[3])
        dim_obj = acad.model.AddDimRotated(start_point, end_point, dim_position,item[2])
    
    # Создание таблицы ведомости объемов работ
    acad.doc.ActiveLayer = acad.doc.Layers.Item("T_Border") #установка слоя для отрисовки 

    # Apoint (точка вставки, кол-во строк, кол-во столбцов, высота строки, ширина столбца) - таблица автоматически создается с объединенной 1-й строкой -типа название таблицы

    table = acad.model.AddTable(APoint(SECTION_Coor[19].x + 15000, SECTION_Coor[19].y + 5000),4,3,1000,1000) 

    #table.SetTextHeight(5) #высота текста 3 - задается для всей таблицы
    # Задать сразу правильные размеры столбцов и строк - нельзя. Поэтому изменяем их после создания таблицы другим методом:#
    #table.SetAligment(1+4)
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
    table.SetText (2, 0 , 'Ростверк подпорных стен монолитный железобетонный \n - бетон В30 F₁200 W8 ГОСТ 26633-2015')
    table.SetText (3, 0 , 'Тело подпорных стен монолитное железобетонное \n - бетон В30 F₁300 W8 ГОСТ 26633-2015')
    table.SetText (1, 1 , 'Ед.изм.')
    table.SetText (1, 2 , 'Кол.')
    table.SetText (2, 1 , 'м3')
    table.SetText (3, 1 , 'м3')
    #table.SetText (2, 2, round(input_data.V1 , 1))
    #table.SetText (3, 2, round(input_data.V2 , 1))