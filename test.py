number=int(input('Введите число: '))
total=''
num=' '.join(str(number))
string=num.split()
index=0
while index<len(string):
    if string[index]!='0':
        total+=string[index]+(len(string)-index-1)*'0'+' + '
    index+=1
print(total.rstrip(' + '))
