import openpyxl

from Classes import Wall
from Classes import Coor
#import pyautocad

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

input_data.name=sheet.cell(row=read_row,column=read_column).value
input_data.name_founding=sheet.cell(row=read_row+1,column=read_column).value
input_data.name_wall=sheet.cell(row=read_row+3,column=read_column).value
input_data.count=sheet.cell(row=read_row+5,column=read_column).value
input_data.foundation_base=sheet.cell(row=read_row+6,column=read_column).value
input_data.leght=sheet.cell(row=read_row+7,column=read_column).value
input_data.height_start=sheet.cell(row=read_row+8,column=read_column).value
input_data.height_end=sheet.cell(row=read_row+9,column=read_column).value
input_data.foundation_width=sheet.cell(row=read_row+10,column=read_column).value
input_data.top_wall_width=sheet.cell(row=read_row+11,column=read_column).value
input_data.edge_distance=sheet.cell(row=read_row+12,column=read_column).value
input_data.bottom_wall_width=sheet.cell(row=read_row+13,column=read_column).value
input_data.t1=sheet.cell(row=read_row+14,column=read_column).value
input_data.t2=sheet.cell(row=read_row+15,column=read_column).value
input_data.t3=sheet.cell(row=read_row+16,column=read_column).value
input_data.t4=sheet.cell(row=read_row+17,column=read_column).value
input_data.V1=sheet.cell(row=read_row+18,column=read_column).value
input_data.V2=sheet.cell(row=read_row+18,column=read_column).value


input_data.ShowAll()


#--\\ОТРИСОВКА\\--

incert_point=Coor(0,input_data.foundation_base)#Точка вставки - левый нижний угол фасада подпорной стены
incert_point.X = 0 #функция ввода из автокада (пользователь делает тык) <------
incert_point.Y = input_data.foundation_base

View_l1 = 5000 #расстояние между фасадом и сечением 1-1 (по горизонтали)
View_l2 = 5000 #расстояние сечением 1-1 и сечением 2-2 (по горизонтали)
View_l3 = 10000 #расстояние между фасадом и планом (по вертикали)
Line_distance = 15000 #расстояние между двух видовых рамок секций

SECTION_Coor = [] #список всех координат видов в одной секции стенки

SECTION_Coor.append(Coor(0,0)) #0 - фиктивная точка 00 для начала нумерации нормальных точек с единицы
SECTION_Coor.append(incert_point)#1
#Фасад
SECTION_Coor.append(Coor(incert_point.X, incert_point.Y + input_data.t2))#2
SECTION_Coor.append(Coor(incert_point.X + input_data.leght, incert_point.Y + input_data.t2))#3
SECTION_Coor.append(Coor(incert_point.X + input_data.leght, incert_point.Y))#4
SECTION_Coor.append(Coor(incert_point.X, incert_point.Y + input_data.height_start))#5
SECTION_Coor.append(Coor(incert_point.X + input_data.leght, incert_point.Y + input_data.height_end))#6

#Вид 1-1
#Задаем точку НК чтобы каждый вид считать от 0.0 а не прибавлять все расстояния в каждой точке
start_coordinates = Coor(incert_point.X + input_data.leght + View_l1, incert_point.Y) 
print("start coordinate: " + str(start_coordinates.X) +" " + str(start_coordinates.Y))

SECTION_Coor.append(Coor(start_coordinates.X, start_coordinates.Y))#7
SECTION_Coor.append(Coor(start_coordinates.X, start_coordinates.Y + input_data.t2))#8
SECTION_Coor.append(Coor(start_coordinates.X + input_data.edge_distance , start_coordinates.Y + input_data.t1))#9
SECTION_Coor.append(Coor(start_coordinates.X + input_data.edge_distance , start_coordinates.Y + input_data.height_start))#10
SECTION_Coor.append(Coor(start_coordinates.X + input_data.edge_distance + input_data.top_wall_width, start_coordinates.Y + input_data.height_start))#11
SECTION_Coor.append(Coor(start_coordinates.X + input_data.edge_distance + input_data.bottom_wall_width, start_coordinates.Y + input_data.t3))#12
SECTION_Coor.append(Coor(start_coordinates.X + input_data.foundation_width, start_coordinates.Y + input_data.t4))#13
SECTION_Coor.append(Coor(start_coordinates.X + input_data.foundation_width, start_coordinates.Y))#14

#Вид 2-2
#Задаем точку НК чтобы каждый вид считать от 0.0 а не прибавлять все расстояния в каждой точке
start_coordinates = Coor(incert_point.X + input_data.leght + View_l1, incert_point.Y) 
print("start coordinate: " + str(start_coordinates.X) +" " + str(start_coordinates.Y))


#print(SECTION_Coor)
for item in SECTION_Coor:
    print(item.X)
    print(str(item.Y)+"\n")

