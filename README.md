# QA

## Thông tin cá nhân
Họ và tên: Huỳnh Nguyên Phúc
MSSV: 2110451

## Các file trong thư mục Models
* **scanner.py**: Thực hiện phân đoạn từ, nhận input từ file input.txt và trả về kết quả trong file lexicon.txt
* **dependency_parser.py**: Thực hiện phân tích cú pháp theo văn phạm phụ thuộc, nhận input từ file lexicon.txt và trả về kết quả trong file dependencies.txt
* **grammatical_relation.py**: Tạo các quan hệ văn phạm, nhận input từ file dependencies.txt và trả về kết quả trong file grammatical_relation.txt
* **logical_form.py**: Tạo dạng logical form, nhận input từ file grammatical_relation.txt và trả về kết quả trong file logical_form.txt
* **procedural_semantic.py**: Tạo dạng ngữ nghĩa thủ tục, nhận input từ file logical_form.txt và trả về kết quả trong file procedural_semantic.txt
* **database.py**: Thực hiện truy xuất database và trả về kết quả, nhận input từ file procedural_semantic.txt và trả về kết quả trong file answer.txt

## Chạy project
Chạy hàm main.py