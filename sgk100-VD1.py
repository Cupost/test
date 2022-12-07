print('nhap so giay') 
a = int(input())
# Nhập số giây từ bàn phím 

ngay = a//86400
gio = a//3600 - ngay*24
phut =a//60 - 60*24*ngay - gio*60
giay = a - ngay*24*60*60 - gio*60*60 - phut*60
# Quy đổi 

print(ngay,'ngày',gio,'giờ',phut,'phút',giay,'giây')
# In ra màn hình 

