# Có try/except → chương trình không crash
try:
    diem = int("abc")   # thử chạy dòng này
    print(diem)
except:
    print("Lỗi! Dữ liệu không hợp lệ")  # nếu lỗi → chạy dòng này

print("Chương trình vẫn tiếp tục chạy!")