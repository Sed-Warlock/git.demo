import pickle
def main():
    print('If you want to open a file for writing, click Y\nIf you want to read an existing file N:',end='')
    man=input('')
    if man.upper()=='Y':

        #Enter where the file should be located in the format "C :\ File.dat, "ab"

        infile=open()

        email={}

        menu=0

        while menu!=6:
            menu=menu_mail(menu)
            if menu==1:
                search(email)
            elif menu==2:
                add(email)
            elif menu==3:
                change(email)
            elif menu==4:
                delete(email)
            elif menu==5:
                all_list(email)
        pickle.dump(email,infile)
        infile.close()
    elif man.upper()=='N':

        #Enter the hosted file to open in the format "C :\ File.dat, "rb"

        outfile=open()
        finish=pickle.load(outfile)
        outfile.close()
        print('Name        email')
        print('-----------------')
        for ch in finish:
            print(ch,'--->',finish[ch])

def menu_mail(menu):
    print('Choose an item from the menu')
    print('---------------------')
    print('1. Search for an e-mail address by name')
    print('2.Add a new name and address')
    print('3.Change address')
    print('4.Delete address')
    print('5.Listing all available mails')
    print('6.Exit')

    menu=int(input('Go to:'))
    while menu<0 or menu>=6:
        return 6
    return menu

def search(email):
    print()
    print('Search for an e-mail address by name')
    print('----------------------------')
    name=input('Enter name: ')
    search=email.get(name,'Name not found')
    print(search)

def add(email):
    print()
    print('2.Add a new name and address')
    print('----------------------------')
    name=input('Enter name: ')
    if name not in email:
        mail=input('Enter email: ')
        email[name]=mail

def change(email):
    print()
    print('Change address')
    print('---------------')
    name=input('Enter name: ')
    if name in email:
        new_email=input('Add new email: ')
        email[name]=new_email

def delete(email):
    print()
    print('Delete address')
    print('-------------')
    name=input('Enter name:')
    if name in email:
        del email[name]

def all_list(email):
    print()
    print('Listing all available mails')
    print('--------------------------------')
    for ch in email:
        print(ch,'--->',email[ch])
main()
