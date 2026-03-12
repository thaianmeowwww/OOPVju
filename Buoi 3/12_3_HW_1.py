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