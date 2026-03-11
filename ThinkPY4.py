# Cài số hàng và cột
Rows = 2
Columns = 2

# Vòng lặp duyệt qua từng hàng của lưới
for i in range(Rows): # Duyệt qua từng hàng (từ 0 đến Rows-1- quy ước bắt đầu từ 0)
    # 1. In ĐƯỜNG NGANG trên cùng của hàng đó
    print('+ - - - - ' * Columns + '+')
    
    # 2. In PHẦN THÂN dọc (chiều cao gồm 4 dòng)
    for j in range(4): 
        print('|         ' * Columns + '|') 

# 3. In ĐƯỜNG NGANG chốt lại ở dưới cùng sau khi đã vẽ xong hết các hàng
print('+ - - - - ' * Columns + '+')


