import json

# Danh sách các file cần gộp
input_files = [
    "file1.jsonl",
    "file2.jsonl",
    "file3.jsonl",
    "file4.jsonl"
]

# Tên file output sau khi gộp
output_file = "merged_output.jsonl"

with open(output_file, "w", encoding="utf-8") as outfile:
    for file_path in input_files:
        with open(file_path, "r", encoding="utf-8") as infile:
            for line in infile:
                try:
                    record = json.loads(line)  # Đảm bảo dòng hợp lệ
                    json.dump(record, outfile)
                    outfile.write("\n")
                except json.JSONDecodeError:
                    continue  # Bỏ qua dòng lỗi nếu có
