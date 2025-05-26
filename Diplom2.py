from Classes import Wall,Walls
import Functions
import openpyxl
import AutocadWork
#import TeklaWork


# Описание файла и поожения данных для выгрузки в питон
file_Name="DATA_.xlsm" #"C:/Users/Ponka/Desktop/Диплом/Diplom2/DATA_.xlsm"
sheet_Name="_ПС"
#file_name = input("Введите имя фалла без расширения")# стоит проверить как он работает с путем к файлу и сделать два варианта воода имени файла
#sheet_Name = input("Введите имя листа с которого будет считываться информация о секциях")
read_row=3 #Стартовая строка
read_column=5 #Стартовый столбец считывания данных по секции
workbook = openpyxl.load_workbook(file_Name, data_only=True )
sheet=workbook[sheet_Name]

input_datas=Walls()
input_datas.name=sheet.cell(row=read_row,column=read_column-1)
input_datas.total_count=0
print("Начало считывания данных с Ексель")
while sheet.cell(row=read_row,column=read_column).value != None:#"None"
   # print(sheet.cell(row=read_row,column=read_column).value)
    input_data = Wall()
    input_data.SetData(sheet,read_column)
    #print(input_data.name)
    input_datas.total_count += 1
    input_datas.sections.append(input_data)
    read_column+=1
 
print("Отрисовать виды в Автокад?\n1. ДА \n2. НЕТ")
# Нужно ли здесь зацикливание?, зачем два раза отрисовывать? 
#choice=int(input())
#if choice == 1:

AutocadWork.DrawAutocad(input_datas)
komp_name="test"#"Подпст1"
#TeklaWork.InputIKomponent(input_datas,komp_name)
#else:
#    print("Выход из программы")
