import openpyxl
#import pyautocad
# Создаем новый Excel-файл и активный лист
workbook = openpyxl.Workbook()
sheet = workbook.active
#Привет!!!!!
# Записываем данные в ячейки
sheet['A1'] = 'Имя'
sheet['B1'] = 'Возраст'
sheet['A2'] = 'Алексей'
sheet['B2'] = 25
sheet['A3'] = 'Мария'
sheet['B3'] = 30

# Сохраняем файл
workbook.save('example.xlsx')

print("Файл 'example.xlsx' успешно создан!")
