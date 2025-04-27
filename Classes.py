class coor(object):
    #pass
    X:float
    Y:float

class Wall(object):
    name: str # Имя секции
    leght: float # Длина секции, м - L
    height_end: float
    height_end: float # 
    foundation_width: float
    top_wall_width: float
    edge_distance: float
    bottom_wall_width: float
    t1: float
    t2: float
    t3: float
    t4: float

class Walls(object):
    name: str
    total_count: int
    sections: List[Wall]





