import math
print("=== BÀI TẬP 2.2 - THINK PYTHON ===")
print("\n--- Bài 1: Thể tích hình cầu ---")
r = 5
V = (4 / 3) * math.pi * (r ** 3)
print("Thể tích của hình cầu có bán kính bằng 5 là: " + str(V))

print("\n--- Bài 2: Chi phí bán buôn sách ---")
gia_bia = 24.95
chiet_khau = 0.40
so_luong = 60

# Tính toán giá sách và phí vận chuyển
gia_sau_chiet_khau = gia_bia * (1 - chiet_khau)
tong_tien_sach = gia_sau_chiet_khau * so_luong
phi_van_chuyen = 3.00 + 0.75 * (so_luong - 1)
tong_chi_phi = tong_tien_sach + phi_van_chuyen

print("Tổng chi phí bán buôn cho 60 cuốn sách là: $" + str(tong_chi_phi))

print("\n--- Bài 3: Thời gian chạy bộ về nhà ---")

# Đổi thời gian xuất phát ra giây 
start_hours = 6
start_minutes = 52
start_time_seconds = (start_hours * 3600) + (start_minutes * 60)

# Đổi Pace (tốc độ) ra giây
# "Easy pace" là chạy chậm, "Tempo pace" là chạy nhịp độ cao
easy_pace_seconds = (8 * 60) + 15 
tempo_pace_seconds = (7 * 60) + 12

# Tính tổng thời gian chạy (giây) cho 2 dặm chậm và 3 dặm nhanh
total_run_seconds = (easy_pace_seconds * 2) + (tempo_pace_seconds * 3)

# Thời gian lúc về đến nhà (giây)
home_time_seconds = start_time_seconds + total_run_seconds

# Đóng gói lại thành Giờ, Phút, Giây
home_hours = home_time_seconds // 3600
seconds_remaining = home_time_seconds % 3600

home_minutes = seconds_remaining // 60
home_seconds = seconds_remaining % 60

# Định dạng chuỗi có 2 chữ số
str_hours = str(home_hours).zfill(2)
str_minutes = str(home_minutes).zfill(2)
str_seconds = str(home_seconds).zfill(2)

print("Thời gian về đến nhà để ăn sáng là: " + str_hours + ":" + str_minutes + ":" + str_seconds + " sáng.")
print("==================================")