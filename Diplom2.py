import openpyxl
#import pyautocad
# Создаем новый Excel-файл и активный лист

fileName="DATA_"
add=".xlsm"
sheetName="_ПС"
workbook = openpyxl.load_workbook(fileName+add, data_only=True )

sheet=workbook[sheetName]

startPoint='D3'

value=sheet.cell(row=3,column=4).value





print(value)
