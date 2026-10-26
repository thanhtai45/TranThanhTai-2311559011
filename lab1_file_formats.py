
# lab1_file_formats.py

import json

students = [
    {
        "id": 1,
        "name": "Nguyen Van A",
        "age": 20,
        "major": "Computer Science",
        "gpa": 3.4
    },
    {
        "id": 2,
        "name": "Tran Thi B",
        "age": 21,
        "major": "Data Science",
        "gpa": 3.8
    },
    {
        "id": 3,
        "name": "Le Van C",
        "age": 22,
        "major": "Information Technology",
        "gpa": 3.1
    }
]

# 1. Tạo file TXT
with open("students.txt", "w", encoding="utf-8") as f:
    f.write("DANH SÁCH SINH VIÊN\n")
    for s in students:
        f.write(
            f"ID: {s['id']} | {s['name']} | "
            f"Tuổi: {s['age']} | Ngành: {s['major']} | "
            f"GPA: {s['gpa']}\n"
        )

# 2. Tạo file CSV
with open("students.csv", "w", encoding="utf-8") as f:
    f.write("id,name,age,major,gpa\n")
    for s in students:
        f.write(
            f"{s['id']},{s['name']},{s['age']},"
            f"{s['major']},{s['gpa']}\n"
        )

# 3. Tạo file JSON
with open("students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=2)

print("Đã tạo thành công 3 file dữ liệu!")
