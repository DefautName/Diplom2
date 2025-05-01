
from Classes import Coor

#Функция для работы с размерами. 

# PointST - Coor начальной точки размера
# PointEND - Coor конечнойй точки размера
# TypeSizeLine - Int тип - размера (горизонтальный  0 / вертикальный 1)
# PositionSizeLine - Float отступ - положение размерной линии (<0 - размер идет влево или вниз, >0 вправо или вверх) 


def GetSizePoint (PointST, PointEND, TypeSizeLine, PositionSizeLine):
   rez = Coor(0,0)
   if TypeSizeLine == 0 : 
        rez.X = (PointEND.X - PointST.X)/2 
        if PositionSizeLine < 0:
            rez.Y = min(PointST.Y, PointEND.Y) + PositionSizeLine
        else: rez.Y = max(PointST.Y, PointEND.Y) + PositionSizeLine
   if TypeSizeLine == 1 :
        rez.Y = (PointEND.Y - PointST.Y)/2 
        if PositionSizeLine < 0:
            rez.X = min(PointST.X, PointEND.X) + PositionSizeLine
        else: rez.X = max(PointST.X, PointEND.X) + PositionSizeLine
   return rez

