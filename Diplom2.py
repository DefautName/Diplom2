from secrets import choice
from tkinter import ROUND #????????
#from pyautocad import Autocad, APoint
from Classes import Wall,Walls
import Functions
import math
import openpyxl
import AutocadWork



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
 
print("Отрисовать виды в Автокад?\n1. ДА \n2. НЕТ")
choice=int(input())
if choice == 1:
    AutocadWork.DrawAutocad(input_datas)
else:
    print("Выход из программы")
