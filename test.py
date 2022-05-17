#Разбивает числа на десяиые, сотые, тысячные и т.д
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
#Возвращает строкой
string=input('Введите строку: ')
string+='.'
total=''
for ch in range(len(string)-1):
    total+=string[ch]
    if string[ch+1].isupper():
        total+=" "
print(total[0].upper()+total[1:].lower())
print('Good')

