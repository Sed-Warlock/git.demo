shifr={'Q':'!','q':'@','W':'#','w':'$','E':'%','e':'^','R':'&','r':'*','T':'(','t':')','Y':'+','y':'=','U':'_','u':'{','I':'}','i':'[','O':']','o':'|','P':'1','p':'2','A':'3','a':'4','S':'5','s':'6','D':'7','d':'8','F':'9','f':'0','G':'я','g':'ч','H':'с','h':'м','J':'и','j':'т','K':'ь','k':'<','L':'>','l':'ф','Z':'ы','z':'в','X':'а',
       'x':'п','C':'р','c':'о','V':'л','v':'д','B':'ж','b':'э','N':'й','n':'ц','M':'у','m':'к',' ':' '}

new_str=[]
finish=''
wat=[]

#Create a txt file where you will store the message
infile=open()
#In open, specify the path to the file in this format:'C:\file.txt,'r'

watch=infile.readlines()
infile.close()

for ch in watch:
       wat.append(ch.rstrip('\n'))

for ch in wat:
       for c in ch:
              if c in shifr:
                     new_str.append(shifr[c])
for ch in new_str:
       finish+=ch

#Specify where you would like to save the file, format:'C\new_file.txt,'w'
outfile=open()
last=outfile.write(finish)
outfile.close()
