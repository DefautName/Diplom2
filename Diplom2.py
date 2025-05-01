from pyautocad import Autocad, APoint
import openpyxl
from Classes import Wall
import Functions

file_Name="DATA_"
add=".xlsm"
sheet_Name="_ПС"
workbook = openpyxl.load_workbook(file_Name+add, data_only=True )

sheet=workbook[sheet_Name]

start_Point='D3'
read_row=3
read_column=5
value=sheet.cell(row=read_row,column=read_column).value

input_data=Wall()

input_data.name=sheet.cell(row=read_row,column=read_column).value#имя секции
input_data.name_founding=sheet.cell(row=read_row+1,column=read_column).value
input_data.name_wall=sheet.cell(row=read_row+3,column=read_column).value
input_data.count=sheet.cell(row=read_row+5,column=read_column).value
input_data.foundation_base=sheet.cell(row=read_row+6,column=read_column).value
input_data.leght=sheet.cell(row=read_row+7,column=read_column).value*1000
input_data.height_start=sheet.cell(row=read_row+8,column=read_column).value*1000
input_data.height_end=sheet.cell(row=read_row+9,column=read_column).value*1000
input_data.foundation_width=sheet.cell(row=read_row+10,column=read_column).value*1000
input_data.top_wall_width=sheet.cell(row=read_row+11,column=read_column).value*1000
input_data.edge_distance=sheet.cell(row=read_row+12,column=read_column).value*1000
input_data.bottom_wall_width=sheet.cell(row=read_row+13,column=read_column).value*1000
input_data.t1=sheet.cell(row=read_row+14,column=read_column).value*1000
input_data.t2=sheet.cell(row=read_row+15,column=read_column).value*1000
input_data.t3=sheet.cell(row=read_row+16,column=read_column).value*1000
input_data.t4=sheet.cell(row=read_row+17,column=read_column).value*1000
input_data.V1=sheet.cell(row=read_row+18,column=read_column).value
input_data.V2=sheet.cell(row=read_row+18,column=read_column).value


input_data.ShowAll()


#--\\ОТРИСОВКА\\--
acad= Autocad(create_if_not_exists=False)
print("Необходимо ввести точку вставки, поржалуйста перейдите в AutoCad")
start_point = acad.doc.Utility.GetPoint(APoint(0, 0), "Введите точку вставки: ")# ввод от пользователя точки вставки картинки в автокад

incert_point=APoint(start_point[0],input_data.foundation_base)#Точка вставки - левый нижний угол фасада подпорной стены


View_l1 = 5000 #расстояние между фасадом и сечением 1-1 (по горизонтали)
View_l2 = 5000 #расстояние сечением 1-1 и сечением 2-2 (по горизонтали)
View_l3 = 10000 #расстояние между фасадом и планом (по вертикали)
Line_distance = 15000 #расстояние между двух видовых рамок секций

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

#Выставление необходимого слоя
acad.doc.ActiveLayer = acad.doc.Layers.Item("Contur")#установка слоя для отрисовки 

#Отрисовка
for item in Topology:
    start_point=APoint(SECTION_Coor[item[0]].x,SECTION_Coor[item[0]].y)
    end_point=APoint(SECTION_Coor[item[1]].x,SECTION_Coor[item[1]].y)
    acad.model.AddLine(start_point,end_point)
    
# Создание маасива топологии для отрисовки размерных линий
# Все размеры создаются строго слева направо или снозу вверх!!!    
# [[x,y,Тип размера, Величина отступа]]   
 
SizeTopology=[]

#Размеры видов в масштабе 1:100
SizeStyle1 = 'LINE100'

SizeTopology.append([1, 5, 1, -1000])
SizeTopology.append([4, 6, 1, -1000])

SizeTopology.append([23, 24, 1, -500])
SizeTopology.append([23, 26, 0, -1000])

#Размеры сечений в масштабе 1:50
SizeStyle1 = 'LINE50'

SizeTopology.append([7, 10, 1, -500])
SizeTopology.append([7, 14, 0, -1000])

SizeTopology.append([15, 18, 1, -500])
SizeTopology.append([15, 22, 0, -500])


acad.doc.ActiveLayer = acad.doc.Layers.Item("Size") #установка слоя для отрисовки 
#Отрисовка
for item in SizeTopology:
    start_point = APoint(SECTION_Coor[item[0]].x, SECTION_Coor[item[0]].y )
    end_point = APoint(SECTION_Coor[item[1]].x, SECTION_Coor[item[1]].y )
    dim_position = Functions.GetSizePoint(start_point,end_point,item[2],item[3])
    dim_obj = acad.model.AddDimRotated(start_point, end_point, dim_position,0)
    