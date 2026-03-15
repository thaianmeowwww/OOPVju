#Chờ hiểu bài
class Point: #Lớp điểm A(x, y)
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def printpoint(self):
        print('(%d, %d)' % (self.x, self.y))
        
    def inputpoint(self):
        self.x = int(input('Nhập x: '))
        self.y = int(input('Nhập y: '))

class Circle: #Lớp hình tròn với tâm là điểm A và bán kính r
    def __init__(self):
        self.center = Point()
        self.r = 0

    def printcircle(self):
        print('Tâm: ', end='')
        self.center.printpoint()
        print('Bán kính: %d' % self.r)
    
    def inputcircle(self):
        print('Nhập tâm: ')
        self.center.inputpoint()
        self.r = int(input('Nhập bán kính: '))
    def point_in_circle(self, p):
        input('Nhập điểm cần kiểm tra: ')
        p.inputpoint()
        distance = ((self.center.x - p.x) ** 2 + (self.center.y - p.y) ** 2) ** 0.5
        if distance < self.r:
            print('Điểm nằm trong vòng tròn')
        elif distance == self.r:
            print('Điểm nằm trên đường tròn')
        else:
            print('Điểm nằm ngoài vòng tròn')
class Rectangle: #Lớp hình chữ nhật với góc trên bên trái là điểm A và góc dưới bên phải là điểm B
    def __init__(self):
        self.top_left = Point()
        self.bottom_right = Point()  
    def printrectangle(self):
        print('Góc trên bên trái: ', end='')
        self.top_left.printpoint()
        print('Góc dưới bên phải: ', end='')
        self.bottom_right.printpoint()
    def inputrectangle(self):
        print('Nhập góc trên bên trái: ')
        self.top_left.inputpoint()
        print('Nhập góc dưới bên phải: ')
        self.bottom_right.inputpoint()
    def rest_in_circle(self, c):
        input('Nhập hình chữ nhật cần kiểm tra: ')
        self.inputrectangle()
        corners = [self.top_left, Point(self.bottom_right.x, self.top_left.y), self.bottom_right, Point(self.top_left.x, self.bottom_right.y)]
        for corner in corners:
            distance = ((c.center.x - corner.x) ** 2 + (c.center.y - corner.y) ** 2) ** 0.5
            if distance > c.r:
                print('Hình chữ nhật không nằm trong vòng tròn')
                return
        print('Hình chữ nhật nằm trong vòng tròn')   
    def rest_circle_overlap(self, c):
        input('Nhập hình chữ nhật cần kiểm tra: ')
        self.inputrectangle()
        corners = [self.top_left, Point(self.bottom_right.x, self.top_left.y), self.bottom_right, Point(self.top_left.x, self.bottom_right.y)]
        for corner in corners:
            distance = ((c.center.x - corner.x) ** 2 + (c.center.y - corner.y) ** 2) ** 0.5
            if distance < c.r:
                print('Hình chữ nhật và vòng tròn chồng lấp nhau')
                return
        print('Hình chữ nhật và vòng tròn không chồng lấp nhau')
