try:
    file1 = open(r'C:\Users\panka\Tutedude\Assignment\Assignment_4\sample.txt','r',encoding = 'utf-8')
    reading_file = file1.readlines()
    i = 0
    while i < len(reading_file):
        print('Line no.',i + 1,':',reading_file[i])
        i = i + 1    
    file1.close()
    
except FileNotFoundError:
    print('The file "sample.txt" was not found.')