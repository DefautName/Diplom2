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
    foundation_base:float # Отметка подошвы 
    leght: float # Длина секции, м - L
    height_end: float
    height_start: float # Привет
    foundation_width: float
    top_wall_width: float
    edge_distance: float
    bottom_wall_width: float
    t1: float
    t2: float
    t3: float
    t4: float
    V1: float
    V2: float

    def ShowAll(self):
        print("Имя секции: "+self.name)
        print("Имя ростверка: "+self.name_founding)
        print("Имя стенки: "+self.name_wall)
        print("Отметка подошвы: "+str(self.foundation_base))
        print("Число: "+str(self.count))
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





