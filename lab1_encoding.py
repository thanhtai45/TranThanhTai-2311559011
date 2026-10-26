
# lab1_encoding.py

text_en = "Hello Data"
text_vi = "Xin chào Dữ liệu"

bytes_en = text_en.encode("utf-8")
bytes_vi = text_vi.encode("utf-8")

print("=" * 45)
print(
    f"Chuỗi: '{text_en}' | "
    f"Số ký tự: {len(text_en)} | "
    f"Số byte UTF-8: {len(bytes_en)}"
)
print(
    f"Chuỗi: '{text_vi}' | "
    f"Số ký tự: {len(text_vi)} | "
    f"Số byte UTF-8: {len(bytes_vi)}"
)
print("=" * 45)

char = "A"
print(
    f"Ký tự '{char}': "
    f"Mã ASCII = {ord(char)} | "
    f"Mã nhị phân = {bin(ord(char))}"
)