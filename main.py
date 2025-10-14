letter_count = 0
digit_count = 0
space_count = 0
other_count = 0
input_str = input()
for char in input_str:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1
    else:
        other_count += 1
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
