shifr=shifr={'!':'Q','@':'q','#':'W','$':'w','%':'E','^':'e','&':'R','*':'r','(':'T',')':'t','+':'Y','=':'y','_':'U','{':'u','}':'I','[':'i',']':'O','|':'o','1':'P','2':'p','3':'A','4':'a','5':'S','6':'s','7':'D','8':'d','9':'F','0':'f','я':'G','ч':'g','с':'H','м':'h','и':'J','т':'j','ь':'K','<':'k','>':'L','ф':'l','ы':'Z','в':'z','а':'X',
       'п':'x','р':'C','о':'c','л':'V','д':'v','ж':'B','э':'b','й':'N','ц':'n','у':'M','к':'m',' ':' '}

#Enter encrypted file format:'C:\file.txt,'r'
infile=open()
file=infile.read()
infile.close()
print(file)
fin=[]
f=''
for ch in file:
       if ch in shifr:
              fin.append(shifr[ch])
for ch in fin:
       f+=ch
print(f)
