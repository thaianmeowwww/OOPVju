# ==========================================
# PHẦN 1: CÁC HÀM XÂY DỰNG LƯỚI 2x2
# ==========================================

def print_beam():
    print('+ - - - - ' * 2 + '+')

def print_post():
    print('|         ' * 2 + '|')

def print_four_posts():
    print_post()
    print_post()
    print_post()
    print_post()

def print_row_block():
    print_beam()
    print_four_posts()

def print_grid_2x2():
    print_row_block()
    print_row_block()
    print_beam()

# ==========================================
# PHẦN 2: CÁC HÀM XÂY DỰNG LƯỚI 4x4
# ==========================================

def print_beam_4x4():
    print('+ - - - - ' * 4 + '+')

def print_post_4x4():
    print('|         ' * 4 + '|')

def print_four_posts_4x4():
    print_post_4x4()
    print_post_4x4()
    print_post_4x4()
    print_post_4x4()

def print_row_block_4x4():
    print_beam_4x4()
    print_four_posts_4x4()

def print_grid_4x4():
    print_row_block_4x4()
    print_row_block_4x4()
    print_row_block_4x4()
    print_row_block_4x4()
    print_beam_4x4()

# ==========================================
# PHẦN 3: GỌI HÀM ĐỂ IN RA MÀN HÌNH
# ==========================================

print("--- Grid 2x2 ---")
print_grid_2x2()

print("\n--- Grid 4x4 ---")
print_grid_4x4()