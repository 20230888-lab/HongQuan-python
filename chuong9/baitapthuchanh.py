class HocVien:
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    def show_info(self):
        print("=== Thông tin học viên ===")
        print("Họ tên:", self.ho_ten)
        print("Ngày sinh:", self.ngay_sinh)
        print("Email:", self.email)
        print("Điện thoại:", self.dien_thoai)
        print("Địa chỉ:", self.dia_chi)
        print("Lớp:", self.lop)

    def change_info(self, dia_chi="Hà Nội", lop="DCCNTT14.2"):
        self.dia_chi = dia_chi
        self.lop = lop


if __name__ == "__main__":
    hv1 = HocVien(
        "Lê Hồng Quân",
        "22/01/2005",
        "20230888@eaut.edu.vn",
        "0123456789",   # bạn có thể sửa lại số thật
        "Hà Nội",       # địa chỉ ban đầu
        "IT10"          # lớp ban đầu
    )

    print("=== Trước khi thay đổi ===")
    hv1.show_info()

    print("\n=== Sau khi thay đổi ===")
    hv1.change_info()  # dùng mặc định: Hà Nội, IT12.x
    hv1.show_info()