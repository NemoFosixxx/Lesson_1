homework_list = []

for i in range (1, 1001, 2):
    homework_list.append(i ** 3)

final_sum = 0
for num in homework_list:
    chek_sum = 0
    for chek_num in str(final_sum):
        chek_sum += int(chek_num)
    if chek_sum % 7 == 0:
        final_sum += num
print(final_sum)  

final_sum = 0
for num in homework_list:
    num += 17
    chek_sum = 0
    for chek_num in str(final_sum):
        chek_sum += int(chek_num)
    if chek_sum % 7 == 0:
        final_sum += num
print(final_sum)  