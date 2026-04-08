from abc import ABC, abstractmethod

class TuoiKhongHopLe(Exception):
    def __init__(self, tuoi):
        super().__init__(f'Tuổi {tuoi} không hợp lệ (phải từ 18 đến 65)')

class BacKhongHopLe(Exception):
    def __init__(self, bac):
        super().__init__(f"Bậc {bac} không hợp lệ (Công nhân chỉ từ bậc 1 đến 10)")

class CanBo(ABC): 
    def __init__(self, hoten, tuoi, gen, diachi):
        self.__hoten = hoten
        self.__gen = gen
        self.__diachi = diachi
        self.tuoi = tuoi

    @property
    def hoten(self):
        return self.__hoten

    @property
    def tuoi(self):
        return self.__tuoi

    @tuoi.setter
    def tuoi(self, v):
        if (v < 18) or (v > 65):
            raise TuoiKhongHopLe(v)
        self.__tuoi = v

    @abstractmethod
    def mo_ta(self):
        pass

    def inTTin(self):
        return f"[{self.mo_ta()}] {self.__hoten} | {self.__tuoi} tuổi | {self.__gen} | {self.__diachi}"

    def __str__(self):
        return self.inTTin()

    def __repr__(self):
        return self.inTTin()

    def __lt__(self, o):
        return self.__hoten < o.hoten 

class CongNhan(CanBo):
    def __init__(self, hoten, tuoi, gen, diachi, bac):
        super().__init__(hoten, tuoi, gen, diachi)
        self.bac = bac
        
    @property
    def bac(self):
        return self.__bac
        
    @bac.setter
    def bac(self, v):
        if v < 1 or v > 10:
            raise BacKhongHopLe(v)
        self.__bac = v

    def mo_ta(self):
        return f"Công nhân bậc {self.bac}"

class KySu(CanBo):
    def __init__(self, hoten, tuoi, gen, diachi, nganh):
        super().__init__(hoten, tuoi, gen, diachi)
        self.__nganh = nganh
        
    def mo_ta(self):
        return f"Kỹ sư {self.__nganh}"

class NhanVien(CanBo):
    def __init__(self, hoten, tuoi, gen, diachi, cong_viec):
        super().__init__(hoten, tuoi, gen, diachi)
        self.__cong_viec = cong_viec
        
    def mo_ta(self):
        return f"Nhân viên {self.__cong_viec}"

if __name__ == "__main__":
    try:
        ds = [
            CongNhan("Độ Mixi", 30, "Nam", "Thanh Hóa", 5),
            KySu("Trần Chi Mai", 28, "Nữ", "Đà Nẵng", "CNTT"),
            NhanVien("Lê Đình Tạ", 35, "Nam", "Gia Lai", "Kế toán")
        ]

        for cb in sorted(ds):
            print(cb)
            
    except Exception as e:
        print("Lỗi hệ thống:", e)