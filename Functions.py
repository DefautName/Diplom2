
from pyautocad import APoint

#Функция для работы с размерами. 

# PointST - APoint начальной точки размера
# PointEND - APoint конечнойй точки размера
# TypeSizeLine - Int тип - размера (горизонтальный  0 / вертикальный 1)
# PositionSizeLine - Float отступ - положение размерной линии (<0 - размер идет влево или вниз, >0 вправо или вверх) 


def GetSizePoint (PointST, PointEND, TypeSizeLine, PositionSizeLine):
   rez = APoint(0,0)
   if TypeSizeLine == 0 : 
        rez.x = (PointEND.x - PointST.x)/2 
        if PositionSizeLine < 0:
            rez.y = min(PointST.y, PointEND.y) + PositionSizeLine
        else: rez.y = max(PointST.y, PointEND.y) + PositionSizeLine
   if TypeSizeLine == 1 :
        rez.y = (PointEND.y - PointST.y)/2 
        if PositionSizeLine < 0:
            rez.x = min(PointST.x, PointEND.x) + PositionSizeLine
        else: rez.x = max(PointST.x, PointEND.x) + PositionSizeLine
   return rez

