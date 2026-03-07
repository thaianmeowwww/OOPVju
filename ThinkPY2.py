'''Viết một đoạn mã (script) đọc thời gian hiện tại và chuyển đổi nó thành thời gian trong ngày
bao gồm giờ, phút, giây, cộng với số ngày đã trôi qua kể từ mốc kỷ nguyên đó.'''
import time
total_seconds = time.time()
secperday = 24 * 60 * 60
secperhrs = 60 * 60
secpermin = 60

#Số ngày trôi qua kể từ 1/1/1970
days = int(total_seconds // secperday) 

# Số giây còn lại trong ngày hiện tại
seconds_left_today = total_seconds % secperday #

# Số giờ trôi qua trong ngày hiện tại
hours = int(seconds_left_today // secperhrs)

# Số giây trôi qua trong giờ hiện tại
seconds_left_for_minutes = seconds_left_today % secperhrs
minutes = int(seconds_left_for_minutes // secpermin)

# Số giây trôi qua trong phút hiện tại
seconds = int(seconds_left_for_minutes % secpermin)

# Ép kiểu dữ liệu số thành chuỗi bằng str() 
print("Số ngày trôi qua kể từ 1/1/1970: " + str(days) + " ngày.")

# Dùng hàm .zfill(2) lên các chuỗi để đảm bảo giờ, phút, giây luôn hiển thị dưới dạng 2 chữ số 
str_hours = str(hours).zfill(2)
str_minutes = str(minutes).zfill(2)
str_seconds = str(seconds).zfill(2)

print("Thời gian hiện tại (giờ GMT): " + str_hours + ":" + str_minutes + ":" + str_seconds)