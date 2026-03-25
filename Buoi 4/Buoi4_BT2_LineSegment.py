import copy
#Bổ sung cách chỉnh định dạng đẹp(str)
class Point: 
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'({self.x}, {self.y})'

class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        elif len(args) == 2:
            if isinstance(args[0], Point) and isinstance(args[1], Point):
                self.__d1 = args[0]
                self.__d2 = args[1]
        elif len(args) == 4:
                self.__d1 = Point(args[0], args[1])
                self.__d2 = Point(args[2], args[3])
        elif len(args) == 1:
            if isinstance(args[0], LineSegment):
                self.__d1 = copy.deepcopy(args[0].__d1)
                self.__d2 = copy.deepcopy(args[0].__d2)
                
    def getD1(self):
        return self.__d1
        
    def getD2(self):
        return self.__d2

    def __str__(self):
        return f'{self.__d1} và {self.__d2}'


# --- PHẦN CHẠY THỬ (MAIN) CHỈ CÒN 1 DÒNG DUY NHẤT CHO MỖI ĐỐI TƯỢNG ---

l1 = LineSegment()
print(f'Đoạn thẳng l1 có điểm đầu và cuối lần lượt là: {l1}')

l2 = LineSegment(Point(3, 4), Point(5, 6))
print(f'Đoạn thẳng l2 có điểm đầu và cuối lần lượt là: {l2}')

l3 = LineSegment(7, 8, 9, 10)
print(f'Đoạn thẳng l3 có điểm đầu và cuối lần lượt là: {l3}')

l4 = LineSegment(l2)
print(f'Đoạn thẳng l4 có điểm đầu và cuối lần lượt là: {l4}')