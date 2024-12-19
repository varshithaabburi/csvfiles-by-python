
csv='application.csv'
#add details into the csv file
def addcontacts():
    n=int(input('Enter how many details you want to insert'))
    for i in range(1,n+1):
        print('Enter',i,'details:')
        details=input('Enter name,phno,email with space:').split(' ')
        with open(csv) as r:
            d=r.readlines()
            for j in d:
                info=j.split(',')
                if info[1]==details[1] or info[2]==details[2]:
                    print("This details already exist in file")
                    return
        with open(csv,'a') as a:
            a.write(details[0]+','+details[1]+','+details[2]+'\n')
            print(details[0],'inserted successfully')
#print all details in csv file
def printall():
    with open(csv) as r:
        data=r.readlines()
        for i in data:
            s=i.split(',')
            print('Name:',s[0],'\nPhoneno:',s[1],'\nEmail:',s[2])
#searching the csvfile using name
def search():
    n=input('Enter name:')
    with open(csv) as r:
        data=r.readlines()
        c=0
        for i in data:
            s=i.split(',')
            if n==s[0]:
                print('Name:',s[0],'\nPhoneno:',s[1],'\nEmail:',s[2])
                return data.index(i)
            else:
                c=c+1
        if c==len(data):
            print(n,'is not found')
#to delete the deltails using name
def delete(ind):
    with open(csv) as r:
        data=r.readlines()          
        with open(csv,'w') as w:
            for i in data:
                if ind!=data.index(i):
                    w.write(i)
                else:
                    print('Deleted successfully')
#to update phno or email using name
def update(index):
    newp,newe=input('Enter new phno,email to update with spaces:').split(' ')
    with open(csv) as r:
        data=r.readlines()
        upd=data[index].split(',')
        upd[1]=newp
        upd[2]=newe+'\n'
        with open(csv,'w') as w:
            for i in data:
                if index!=data.index(i):
                    w.write(i)
                else:
                    str=upd[0]+','+upd[1]+','+upd[2]
                    w.write(str)
while True:
    print('1.Addcontact\n2.View all contact\n3.Search for contact\n4.Delete the contact\n5.Update the contact\n6.Exit')
    op=int(input('Enter your option'))
    if op==1:
        addcontacts()
    elif op==2:
        printall()
    elif op==3:
        search()
    elif op==4:
        ind='null'
        ind=search()
        if ind!='null':
            delete(ind)
    elif op==5:
        ind='null'
        ind=search()
        if ind!='null':
            update(ind)
    elif op==6:
        break
    else:
        print('Enter a valid option')
        
