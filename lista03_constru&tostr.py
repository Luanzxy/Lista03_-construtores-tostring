class Retângulo:
    def __init__(self):
        self.__b = 0
        self.__h = 0
    def set_b(self,v)
        if v < 1: raise ValueError("A base não pode ser negativa")
        self.__b = v
    def set_h(self,v):
        if v < 0: raise ValueError("A altura não pode ser negativa")
        self.__h = v
    def get_b(self):
        return self.__b
    def get_h(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2 
    def calc_diagonal(self):
        return (self.__h ** 2 + self.__b ** 2) ** 0.5
    