class NhanVien:
    LUONG_MAX = 100000000.0

    def __init__(self, tenNhanVien, luongCoBan=0.0, heSoLuong=1.0):
        self._tenNhanVien = tenNhanVien
        self._luongCoBan = float(luongCoBan)
        self._heSoLuong = float(heSoLuong)
    def get_tenNhanVien(self):
        return self._tenNhanVien
    def set_tenNhanVien(self, value):
        self._tenNhanVien = value
    def get_luongCoBan(self):
        return self._luongCoBan
    def set_luongCoBan(self, value):
        self._luongCoBan = value
    def get_heSoLuong(self):
        return self._heSoLuong
    def set_heSoLuong(self, value):
        self._heSoLuong = value
    def tinhLuong(self):
        return self._luongCoBan * self._heSoLuong

    def inTTin(self):
        print(f"Tên nhân viên: {self._tenNhanVien}")
        print(f"Lương cơ bản: {self._luongCoBan:,.0f}")
        print(f"Hệ số lương: {self._heSoLuong}")
        print(f"Lương thực nhận: {self.tinhLuong():,.0f}")

    def tangLuong(self, delta):
        luong_moi = self._luongCoBan * (self._heSoLuong + delta)
        
        if luong_moi > NhanVien.LUONG_MAX:
            print("-> Lương mới vượt quá lương lớn nhất. Không thể tăng lương.")
            return False
        else:
            self._heSoLuong += delta
            print(f"-> Tăng lương thành công! Lương thực nhận mới: {self.tinhLuong():,.0f}")
            return True


nv1 = NhanVien("Thái An", 5000000.0, 2.0)
nv1.inTTin()

print("\nTĂNG LƯƠNG LẦN 1 ")
ket_qua_1 = nv1.tangLuong(0.5)
print(f"Kết quả trả về của hàm: {ket_qua_1}")

print("\n TĂNG LƯƠNG LẦN 2 ")
ket_qua_2 = nv1.tangLuong(20.0)
print(f"Kết quả trả về của hàm: {ket_qua_2}")