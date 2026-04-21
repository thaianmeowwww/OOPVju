import csv
import json
import os

# --- 1. ĐỊNH NGHĨA ĐỐI TƯỢNG ---
class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    def to_dict(self):
        """Chuyển đối tượng thành dict để lưu JSON"""
        d = self.__dict__.copy()
        d["loai"] = type(self).__name__
        return d

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh = nganh

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

# --- 2. HỆ THỐNG QUẢN LÝ ---
class QuanLyCanBo:
    def __init__(self):
        self.csv_file = "canbo.csv"
        self.json_file = "canbo.json"
        self.ds_dict = {} # Key là tên
        self.load_du_lieu()

    # --- XỬ LÝ FILE ---
    def load_du_lieu(self):
        """Ưu tiên JSON, nếu không có thì tìm CSV"""
        if os.path.exists(self.json_file):
            self.load_json()
        elif os.path.exists(self.csv_file):
            self.load_csv()

    def load_json(self):
        try:
            with open(self.json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for d in data:
                    loai = d.pop("loai")
                    if loai == "CongNhan": cb = CongNhan(**d)
                    elif loai == "KySu": cb = KySu(**d)
                    else: cb = NhanVien(**d)
                    self.ds_dict[cb.ho_ten] = cb
            print("[OK] Đã tải dữ liệu từ JSON")
        except Exception as e: print(f"[!] Lỗi JSON: {e}")

    def load_csv(self):
        try:
            with open(self.csv_file, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    ten, tuoi, gt, dc, loai, extra = row
                    if loai == "CongNhan": cb = CongNhan(ten, int(tuoi), gt, dc, int(extra))
                    elif loai == "KySu": cb = KySu(ten, int(tuoi), gt, dc, extra)
                    else: cb = NhanVien(ten, int(tuoi), gt, dc, extra)
                    self.ds_dict[ten] = cb
            print("[OK] Đã tải dữ liệu từ CSV")
        except Exception as e: print(f"[!] Lỗi CSV: {e}")

    def save_all(self):
        """Lưu đồng thời cả 2 file để đồng bộ"""
        try:
            # Lưu JSON
            list_data = [cb.to_dict() for cb in self.ds_dict.values()]
            with open(self.json_file, "w", encoding="utf-8") as f:
                json.dump(list_data, f, ensure_ascii=False, indent=2)
            
            # Lưu CSV
            with open(self.csv_file, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                for cb in self.ds_dict.values():
                    loai = type(cb).__name__
                    extra = cb.bac if loai == "CongNhan" else (cb.nganh if loai == "KySu" else cb.cong_viec)
                    writer.writerow([cb.ho_ten, cb.tuoi, cb.gioi_tinh, cb.dia_chi, loai, extra])
            print("[OK] Đã lưu dữ liệu vào cả JSON và CSV")
        except Exception as e: print(f"[!] Lỗi khi lưu: {e}")

    # --- CHỨC NĂNG ---
    def menu(self):
        while True:
            print("\n" + "-"*30 + "\n1. Thêm | 2. Hiện | 3. Lưu | 0. Thoát")
            chon = input("Chọn: ")
            try:
                if chon == "1":
                    ten = input("Tên: ")
                    loai = input("1.Công Nhân / 2.Kỹ Sư: ")
                    if loai == "1":
                        bac = int(input("Bậc: "))
                        self.ds_dict[ten] = CongNhan(ten, 20, "Nam", "HN", bac)
                    elif loai == "2":
                        nganh = input("Ngành: ")
                        self.ds_dict[ten] = KySu(ten, 22, "Nữ", "HCM", nganh)
                elif chon == "2":
                    for cb in self.ds_dict.values():
                        print(f"{type(cb).__name__}: {cb.ho_ten} - {cb.dia_chi}")
                elif chon == "3":
                    self.save_all()
                elif chon == "0": break
            except Exception as e:
                print(f"[!] Lỗi thao tác: {e}")

if __name__ == "__main__":
    app = QuanLyCanBo()
    app.menu()