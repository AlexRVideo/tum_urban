my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

a = 0

while a < len(my_list):
    current_value = my_list[a]
    if current_value > 0:
        print(current_value)
    elif current_value == 0:
        a += 1
        continue
    else:
        break
    a += 1