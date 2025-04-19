import os
import json
import random

# Đường dẫn file jsonl đầu vào
input_file = "data/all_data.jsonl"

# Thư mục output
output_dir = "data/splits"
os.makedirs(output_dir, exist_ok=True)

# Tỷ lệ chia (7:1.5:1.5 → 70% - 15% - 15%)
train_ratio = 0.7
valid_ratio = 0.15
test_ratio = 0.15

# Đọc toàn bộ dữ liệu
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Shuffle để đảm bảo phân phối ngẫu nhiên
random.shuffle(lines)

# Tính chỉ số chia
total = len(lines)
train_end = int(total * train_ratio)
valid_end = train_end + int(total * valid_ratio)

# Chia dữ liệu
train_lines = lines[:train_end]
valid_lines = lines[train_end:valid_end]
test_lines = lines[valid_end:]

# Hàm ghi ra file
def write_jsonl(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        for line in data:
            f.write(line.strip() + "\n")

# Ghi từng phần vào file
write_jsonl(os.path.join(output_dir, "train.jsonl"), train_lines)
write_jsonl(os.path.join(output_dir, "valid.jsonl"), valid_lines)
write_jsonl(os.path.join(output_dir, "test.jsonl"), test_lines)

print(f"✅ Split hoàn tất. Đã lưu vào: {output_dir}")
print(f"Train: {len(train_lines)}, Valid: {len(valid_lines)}, Test: {len(test_lines)}")
