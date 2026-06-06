product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]

def parse_product(product_str):
    try:
        parts = product_str.split('-')
        if len(parts) < 4:
            raise IndexError
            
        ma_sp = parts[0]
        ten_sp = parts[1]
        gia_str = parts[2]
        rating_str = parts[3]
        
        clean_gia_str = ""
        for c in gia_str:
            if '0' <= c <= '9':
                clean_gia_str += c
                
        if not clean_gia_str: 
            raise ValueError
            
        gia = int(clean_gia_str)
        rating = float(rating_str)
        
        return {
            "ma": ma_sp,
            "ten": ten_sp,
            "gia": gia,
            "rating": rating
        }
        
    except IndexError:
        ma_tam = product_str.split('-')[0] if product_str else "Unknown"
        print(f"-> Bỏ qua sản phẩm [{ma_tam}] do sai cấu trúc dữ liệu.")
        return None
    except ValueError:
        ma_tam = product_str.split('-')[0] if product_str else "Unknown"
        print(f"-> Bỏ qua sản phẩm [{ma_tam}] do lỗi ép kiểu dữ liệu.")
        return None

def dinh_dang_tien(so_tien):
    chuoi_so = str(so_tien)
    ket_qua = ""
    dem = 0
    for i in range(len(chuoi_so) - 1, -1, -1):
        dem += 1
        ket_qua = chuoi_so[i] + ket_qua
        if dem % 3 == 0 and i != 0:
            ket_qua = ',' + ket_qua
    return ket_qua

def chuc_nang_1():
    print("\n--- DANH SÁCH TEM NHÃN ---")
    template = "Mã: {ma:<10} | Tên: {ten:<20} | Giá: {gia_format} VND | Rating: {rating}*"
    
    for item in product_list:
        p_dict = parse_product(item)
        if p_dict:
            p_dict["gia_format"] = dinh_dang_tien(p_dict["gia"])
            print(template.format_map(p_dict))

def chuc_nang_2():
    print("\n--- SẮP XẾP SẢN PHẨM ---")
    
    def sort_key(product_str):
        p_dict = parse_product(product_str)
        if p_dict is None:
            return (-999.0, 999999999)
        return (-p_dict["rating"], p_dict["gia"])
    
    product_list.sort(key=sort_key)
    print("Đã sắp xếp thành công! Cập nhật danh sách:")
    
    for idx, item in enumerate(product_list, 1):
        note = ""
        if "550000" in item and "4.5" in item:
            note = "  (Cùng 4.5* nhưng giá rẻ hơn)"
        print(f"{idx}. {item}{note}")

def tu_viet_reduce(danh_sach):
    if not danh_sach:
        return 0
    tich_luy = danh_sach[0]
    for i in range(1, len(danh_sach)):
        tich_luy = tich_luy + danh_sach[i]
    return tich_luy

def chuc_nang_3():
    print("\n--- TỔNG GIÁ TRỊ KHO ---")
    
    prices = []
    for item in product_list:
        p_dict = parse_product(item)
        if p_dict:
            prices.append(p_dict["gia"])
            
    if not prices:
        print("Không có sản phẩm hợp lệ để tính tổng.")
        return 0
        
    tong_gia_tri = tu_viet_reduce(prices)
    print(f"Tổng giá trị các mặt hàng hiện tại là: {dinh_dang_tien(tong_gia_tri)} VND.")
    return tong_gia_tri

def main():
    while True:
        print("\n============ E-COMMERCE ANALYTICS ============")
        print("1. Hiển thị tem nhãn sản phẩm (format_map & F-String)")
        print("2. Sắp xếp sản phẩm thông minh (sort key)")
        print("3. Tính tổng giá trị kho hàng (reduce tự viết)")
        print("4. Đóng hệ thống")
        print("==============================================")
        
        choice = input("Chọn chức năng (1-4): ").strip()
        
        if choice == '1':
            chuc_nang_1()
        elif choice == '2':
            chuc_nang_2()
        elif choice == '3':
            chuc_nang_3()
        elif choice == '4':
            print("Đang đóng hệ thống... Tạm biệt!")
            break
        else:
            print("Chức năng không hợp lệ, vui lòng chọn lại từ 1 đến 4.")

if __name__ == "__main__":
    main()