product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]

def parse_product(product_str):
    if not product_str:
        print("-> Bỏ qua sản phẩm do chuỗi dữ liệu rỗng.")
        return None
        
    parts = product_str.split('-')
    
    if len(parts) < 4:
        ma_tam = parts[0] if len(parts) > 0 else "Unknown"
        print(f"-> Bỏ qua sản phẩm [{ma_tam}] do sai cấu trúc dữ liệu.")
        return None
        
    ma_sp = parts[0]
    ten_sp = parts[1]
    gia_str = parts[2]
    rating_str = parts[3]
    
    clean_gia_str = "".join([c for c in gia_str if '0' <= c <= '9'])
            
    if not clean_gia_str: 
        print(f"-> Bỏ qua sản phẩm [{ma_sp}] do giá không chứa chữ số hợp lệ.")
        return None
        
    try:
        gia = int(clean_gia_str)
        rating = float(rating_str)
        
        return {
            "ma": ma_sp,
            "ten": ten_sp,
            "gia": gia,
            "rating": rating
        }
    except ValueError:
        print(f"-> Bỏ qua sản phẩm [{ma_sp}] do lỗi ép kiểu dữ liệu.")
        return None

def chuc_nang_1():
    print("\n--- DANH SÁCH TEM NHÃN ---")
    
    for item in product_list:
        p_dict = parse_product(item)
        if p_dict:
            print(f"Mã: {p_dict['ma']:<10} | Tên: {p_dict['ten']:<20} | Giá: {p_dict['gia']:,} VND | Rating: {p_dict['rating']}*")

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
        
    tong_gia_tri = sum(prices)
    print(f"Tổng giá trị các mặt hàng hiện tại là: {tong_gia_tri:,} VND.")
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
