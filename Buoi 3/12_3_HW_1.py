class Concho:
    def __init__(self, name,colour,Giong, emotion):
        self.name = name
        self.colour = colour
        self.Giong = Giong
        self.emotion = emotion
    def __str__(self):
        return f"Con chó tên {self.name}, màu {self.colour}, giống {self.Giong}, cảm xúc {self.emotion}"
    def bark(self):
        return "Gâu gâu!"
    def eat(self, food):
        return f"{self.name} đang ăn {food}."
    def vayduoi(self):
        return f"{self.name} đang vẫy đuôi."
    
concho1 = Concho("Do", "Đen", "Mực", "xì khói")
print(concho1)
print(concho1.bark())
print(concho1.eat("xương"))
concho2=Concho("Mèo", "Vàng", "Cao Bằng", "vui vẻ")
print(concho2)
print(concho2.vayduoi())

class Car:
    def __init__(self, brand, size, color, price):
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
    def __str__(self):
        return f"Xe {self.brand} có kích thước {self.size}, màu {self.color}, giá {self.price}." 
    def speedup(self):
        return f"{self.brand} đang tăng tốc."
    def brake(self):
        return f"{self.brand} đang phanh."
    def dam(self):
        return f"{self.brand} đang đâm vào vật cản."
car1 = Car("Toyota", "Lớn", "Đỏ", 50000000)
print(car1)
print(car1.speedup())
print(car1.brake())
print(car1.dam())

class Account:
 def __init__(self, account_number, name, brand, balance):
        self.account_number = account_number
        self.name = name
        self.brand = brand
        self.balance = balance
def __str__(self):
        return f"Tài khoản {self.account_number} thuộc về {self.name}, ngân hàng {self.brand}, số dư {self.balance}."
def rut_tien(self, amount):
        if amount > self.balance:
            return "Số dư không đủ để rút tiền."
        else:
            self.balance -= amount # Số dư = Số dư - Số tiền rút( -= = Số dư - Số tiền rút)
            return f"Bạn đã rút {amount}. Số dư còn lại: {self.balance}."   
def gui_tien(self, amount):
        self.balance += amount # Số dư = Số dư + Số tiền gửi( += = Số dư + Số tiền gửi)
        return f"Bạn đã gửi {amount}. Số dư còn lại: {self.balance}."       
def check_balance(self):
        return f"Số dư hiện tại của bạn là: {self.balance}."
