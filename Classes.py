from turtle import position


class Coor(object):
    #pass
    X:float
    Y:float
    def __init__(self):
        self.X=0
        self.Y=0

    def __init__(self,x,y):
        self.X=x
        self.Y=y

class Wall(object):
    name: str # Имя стенки
    name_wall:str
    name_founding:str
    count:int
    foundation_base:float # Отметка подошвы фундамента
    leght: float # Длина секции, м - L
    height_end: float # Высота в конце стенки - H_кон
    height_start: float # Высота в начале стенки - H_нач
    foundation_width: float #Ширина ф-та - В
    top_wall_width: float #ширина стены наерху - в2
    edge_distance: float #расстояние от стены до края - в3
    bottom_wall_width: float #ширина стены внизу - в4
    t1: float #толщина перекрытия 1 у стены 
    t2: float #толщина перекрытия 1 у насыпи
    t3: float #толщина перекрытия 2 у стены
    t4: float #олщина перекрытия 2 у насыпи
    V1: float #объем ростверка подпорной стены, м3
    V2: float #объем стеновой части подпорной стены, м3

    def ShowAll(self):
        print("Имя секции: "+self.name)
        print("Имя ростверка: "+self.name_founding)
        print("Имя стенки: "+self.name_wall)
        print("Отметка подошвы: "+str(self.foundation_base))
        print("Колличество секций: "+str(self.count))
        print("Длина: "+str(self.leght))
        print("Общая высота (нач): "+str(self.height_start))
        print("Общая высота (кон): "+str(self.height_end))
        print("Ширина фундамента: "+str(self.foundation_width))
        print("Ширина стены сверху : "+str(self.top_wall_width))
        print("Расстояние от стены до края: "+str(self.edge_distance))
        print("Ширина стены внизу: "+str(self.bottom_wall_width))
        print("Толщина перекрытия 1 у стены: "+str(self.t1))
        print("Толщина перекрытия 1 у насыпи: "+str(self.t2))
        print("Толщина перекрытия 2 у стены: "+str(self.t3))
        print("Толщина перекрытия 2 у насыпи: "+str(self.t4))
        print("Объем ростверка подпорной стены, м3: "+str(self.V1))
        print("Объем тела подпорной стены, м3: "+str(self.V2))

        

class Walls(object):
    name: str
    total_count: int
  #  sections: List[Wall]





