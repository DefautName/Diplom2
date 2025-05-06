
import math
from pyautocad import APoint

#Функция для работы с размерами. 

# PointST - APoint начальной точки размера
# PointEND - APoint конечнойй точки размера
# TypeSizeLine - Int тип - размера (горизонтальный  0 / вертикальный 1)
# PositionSizeLine - Float отступ - положение размерной линии (<0 - размер идет влево или вниз, >0 вправо или вверх) 

 
def GetSizePoint (PointST, PointEND, TypeSizeLine, PositionSizeLine):
   rez = APoint(0,0)
   if TypeSizeLine == 0  or TypeSizeLine == math.pi: 
        rez.x = (PointEND.x - PointST.x)/2 
        if TypeSizeLine == 0:
            rez.y = min(PointST.y, PointEND.y) - PositionSizeLine
        else: rez.y = max(PointST.y, PointEND.y) + PositionSizeLine
   if TypeSizeLine == math.pi/2 or TypeSizeLine == 3*math.pi/2:
        rez.y = (PointEND.y - PointST.y)/2 
        if TypeSizeLine == math.pi/2:
            rez.x = min(PointST.x, PointEND.x) - PositionSizeLine
        else: rez.x = max(PointST.x, PointEND.x) + PositionSizeLine
   return rez

# Функция расчета параметров рамки

def GetRecSize(incert_point, max_width, max_height):
    vertical_otstyp = 15000
    horizontal_otstyp_left = 10000  
    horizontal_otstyp_right = horizontal_otstyp_left * 3
    H = max_height + vertical_otstyp * 2
    B  = max_width + horizontal_otstyp_left + horizontal_otstyp_right
    Point = APoint(incert_point.x - horizontal_otstyp_left, incert_point.y - max_height -  vertical_otstyp )
    rez = [Point, H, B]
    return rez
    
#

def ConvertAdress(input_adress):
    print("Convert adress")
    
def GetStringPoint(point1, point2,up_dist):
    rez=APoint(0,0)
    rez.x=point1.x+(point2.x-point1.x)/4
    rez.y=max(point1.y,point2.y)+up_dist
    return rez

