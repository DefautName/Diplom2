import openpyxl
#import pyautocad
# Создаем новый Excel-файл и активный лист

fileName="DATA_"
add=".xlsm"
sheetName="_ПС"
workbook = openpyxl.load_workbook(fileName+add)

sheet=workbook[sheetName]

value=sheet['D5'].value

print(value)
