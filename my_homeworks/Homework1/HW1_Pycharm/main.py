file = open('/home/dmytriii/Desktop/Cursor/linux_lecture/homework.sh', 'w')

for number in range(1, 11):
    file.write(f'{number}\n')

file.close()

