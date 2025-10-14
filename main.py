# 初始化各类字符计数为 0
letter_count = 0
digit_count = 0
space_count = 0
other_count = 0

# 获取输入（注意：自动测试可能要求输入后无多余操作，直接处理）
input_str = input()

# 遍历每个字符进行统计
for char in input_str:
    # 判断英文字符（严格匹配 a - z 或 A - Z）
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        letter_count += 1
    # 判断数字（0 - 9）
    elif char.isdigit():
        digit_count += 1
    # 判断空格（仅普通空格 ' '）
    elif char == ' ':
        space_count += 1
    # 其他字符
    else:
        other_count += 1

# 按要求格式输出，确保与测试用例的预期输出完全一致
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
