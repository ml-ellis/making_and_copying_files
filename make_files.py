target_1 = open('file_1.txt', 'w')
target_2 = open('file_2.txt', 'w')

print('Write to file 1:')
str_1 = input()

target_1.write(str_1)

print('Write to file 2:')
str_2 = input()

target_2.write(str_2)

target_1.close
target_2.close
