from abc import ABC, abstractmethod

class GiaKhongHopLe(Exception): 
    def __init__(self, gia):
        self.gia = gia
        super().__init__(f'Giá {gia} không hợp lệ')

class MaHangTrungLap(Exception):
    def __init__(self, ma):
        self.ma = ma
        super().__init__(f'Mã hàng {ma} đã bị trùng lặp')

class HangHoa(ABC):
    # Tạo một biến cấp class (Class Attribute) để lưu các mã đã dùng
    danh_sach_ma_da_dung = []

    def __init__(self, ma, ten, nsx, gia):
        self.__ten = ten
        self.__nsx = nsx
        self.ma_hang = ma 
        self.gia = gia

    @property
    def gia(self):
        return self.__gia

    @gia.setter
    def gia(self, v):
        if v < 0:
            raise GiaKhongHopLe(v)
        self.__gia = v

    @property
    def ma_hang(self):
        return self.__ma

    @ma_hang.setter
    def ma_hang(self, m): 
        if m in HangHoa.danh_sach_ma_da_dung:
            raise MaHangTrungLap(m)
        HangHoa.danh_sach_ma_da_dung.append(m)
        self.__ma = m
    @abstractmethod
    #Lớp con phải ghi đè
    def loai_hang(self):
        pass
    #Bất cứ ai muốn làm con của HangHoa thì đều phải tự khai báo mình là loại hàng gì!
    def inTTin(self):
        return (f"[{self.loai_hang()}] {self.__ma}" 
                f" | {self.__ten} |Nhà sản xuất: {self.__nsx} | {self.__gia:,.0f}đ")
        #self.loai_hang(): Đợi ghi đè khi tạo class con
    def __str__(self): #Khi in ra đối tượng, sẽ tự động gọi hàm này
            return self.inTTin() 
    def __eq__(self,o): #So sánh 2 đối tượng có bằng nhau hay không, dựa vào mã hàng
        return self.__ma==o.__ma 
    def __lt__(self,o): #So sánh 2 đối tượng, dựa vào giá
        return self.__gia<o.__gia 
    def __hash__(self): #Tạo mã băm cho đối tượng, dựa vào mã hàng
        return hash(self.__ma)
class HangDienMay(HangHoa):
    def __init__(self,ma,ten,nsx,gia,bh,dien,congsuat):
        super().__init__(ma,ten,nsx,gia)
        self.__bh=bh
        self.__dien=dien
        self.__congsuat=congsuat
    def loai_hang(self):
        return "Điện máy "
    def inTTin(self):
       return (f"{super().inTTin()}" 
               f" | BH:{self.__bh} tháng" 
               f" | {self.__dien}V | {self.__congsuat} W")
class HangSanhSu(HangHoa):
    def __init__(self,ma,ten,nsx,gia,loai_nguyenlieu):
        super().__init__(ma,ten,nsx,gia)
        self.__loai_nguyenlieu=loai_nguyenlieu
    def loai_hang(self):
        return "Sành sứ"
    def inTTin(self):
       return (f"{super().inTTin()}" 
               f" | Chất liệu: {self.__loai_nguyenlieu}")
class HangThucPham(HangHoa):
    def __init__(self,ma,ten,nsx,gia,ng_sanxuat,hsd):
        super().__init__(ma,ten,nsx,gia)
        self.__ng_sanxuat=ng_sanxuat
        self.__hsd=hsd
    def loai_hang(self):
        return "Thực phẩm"
    def inTTin(self):
        return (f"{super().inTTin()}" 
               f" | NSX: {self.__ng_sanxuat} -- HSD: {self.__hsd}")
ds=[HangDienMay("TL01","Tủ lạnh", "Samsung",12000000,36,220,300), HangThucPham("MILK01","Sữa chua","Vinamilk",30000,"08/04/2026","30/04/2026")]

for sp in sorted(ds):
    print(sp) #Phi từ print ra

with open("kho.txt","w") as f:
    for sp in ds:
        f.write(repr(sp)+ "\n")