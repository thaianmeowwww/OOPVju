# Cài số hàng và cột
Rows = 4
Columns = 4

# Vòng lặp duyệt qua từng hàng của lưới
for i in range(Rows): # i chạy từ 0 đến 1 (tổng cộng 2 lần, tương ứng với 2 hàng)
    
    # 1. In ĐƯỜNG NGANG trên cùng của hàng đó
    # Dùng phép nhân chuỗi: lặp lại cụm '+ - - - - ' theo số cột, rồi cộng thêm dấu '+' ở cuối
    print('+ - - - - ' * Columns + '+')
    
    # 2. In PHẦN THÂN dọc (gồm 4 dòng)
    for j in range(4): # j chạy từ 0 đến 3 (tổng cộng 4 lần, tương ứng với 4 dòng của phần thân)
        print('|         ' * Columns + '|') 

# 3. In ĐƯỜNG NGANG chốt lại ở dưới cùng sau khi đã vẽ xong hết các hàng
print('+ - - - - ' * Columns + '+')