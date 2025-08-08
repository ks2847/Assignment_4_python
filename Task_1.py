
try:
    file1 = open(r'C:\Users\panka\Tutedude\Assignment\Assignment_4\sample.txt','r',encoding = 'utf-8')
    reading_file = file1.readline()
    print(reading_file)
    reading_file = file1.readline()
    print(reading_file)
    file1.close()
except FileNotFoundError:
    print('The file "sample.txt" was not found.')

# reading_file = file1.readline()
# print(reading_file)
# reading_file = file1.readline()
# print(reading_file)
# file1.close()



