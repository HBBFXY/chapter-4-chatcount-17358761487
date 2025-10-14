letter_count = 0
digit_count = 0
space_count = 0
other_count = 0
input_str = input().strip()  # 去除输入两端可能的多余空白（若测试用例要求严格）

for char in input_str:
    # 严格判断英文字符（仅a - z、A - Z）
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char == ' ':  # 明确判断单个空格（避免isspace()对换行等空白的兼容问题）
        space_count += 1
    else:
        other_count += 1

# 确保输出格式与测试用例完全一致（比如“英文字符: X”，无多余空格）
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
