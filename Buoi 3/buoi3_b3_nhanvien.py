class Nhanvien:
    LUONG_MAX=100000000.0
    def __init__(self, name, luongCoBan=0.0,heSoLuong=1.0):
        self._name = name
        self._luongCoBan = luongCoBan
        self._heSoLuong = heSoLuong
    #1. Phương thức tính lương
    def tinhLuong(self):
        return self._luongCoBan * self._heSoLuong
    #2. Phương thức hiển thị thông tin nhân viên
    def hienThiThongTin(self):
        print(f"Tên nhân viên: {self._name}")
        print(f"Lương cơ bản: {self._luongCoBan}")
        print(f"Hệ số lương: {self._heSoLuong}")
        print(f"Lương thực nhận: {self.tinhLuong()}")
    #3. Phương thức tăng lương
    def tangLuong(self, q):
        luongMoi = self._luongCoBan * (self._heSoLuong + q)
        if luongMoi > Nhanvien.LUONG_MAX:
            print("Lương mới vượt quá mức lương tối đa. Không thể tăng lương.")
        else:
            self._luongCoBan = luongMoi
            print(f"Lương đã được tăng lên: {self._luongCoBan}")
# Tạo một đối tượng nhân viên
nv1 = Nhanvien("Nguyen Van A", 5000000.0, 2.0)
# Hiển thị thông tin nhân viên
nv1.hienThiThongTin()
# Tăng lương cho nhân viên
nv1.tangLuong(0.5)
# Hiển thị thông tin nhân viên sau khi tăng lương
nv1.hienThiThongTin()