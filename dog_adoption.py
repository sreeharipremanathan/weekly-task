# dogs=[{'id':101,'breed':'lab','age':2,'gender':'male'},{'id':102,'breed':'germanshprd','age':1,'gender':'male'},{'id':101,'breed':'lab','age':3,'gender':'female'}]
dogs=[]
while True:
    print('''
        1.register dog
        2.view all
        3.update
        4.remove
        5.search by breed
        6.view available for adoption
        7.exit
''')
    choice=int(input('enter your choice: '))
    if len(dogs)==0:
        id=101
    else:
        id=dogs[-1]['id']+1
    if choice==1:
        breed=input('enter the breed: ')
        age=int(input('enter the age: '))
        gender=input('male or female: ')
        adop_sts=input('available or unavailable for adoption: ')
        dogs.append({'id':id,'breed':breed,'age':age,'gender':gender,'adoption_status':adop_sts})
        print('registration completed...')
    elif choice==2:
        print('_'*40)
        print("{:<10}{:<15}{:<10}{:<10}".format('id','breed','age','gender'))
        print('-'*40)
        for i in dogs:
            print("{:<10}{:<15}{:<10}{:<10}".format(i['id'],i['breed'],i['age'],i['gender']))
    elif choice==3:
        id=int(input('enter the id: '))
        f=0
        for i in dogs:
            if i['id']==id:
                f=1
                while True:
                    print('''
                        1.update age
                        2.update adoption status
                        3.exit
''')
                    sub_ch=int(input('enter your choice: '))
                    if sub_ch==1:
                        age=input('enter udated age: ')
                        i['age']=age
                    elif sub_ch==2:
                        adop_sts=input('available or unavailable: ')
                        i['adoption_status']=adop_sts
                    elif sub_ch==3:
                        break
                    else:
                        print('invalid choice!!!')
        if f==0:
            print('invalid choice')
    elif choice==4:
        id=int(input('enter the id to be deleted: '))
        f=0
        for i in dogs:
            if i['id']==id:
                f=1
                dogs.remove(i)
        if f==0:
            print('invalid choice')
    elif choice==5:
        breed_srch=input('enter the breed you want: ')
        print('_'*60)
        print("{:<10}{:<15}{:<10}{:<10}{:<15}".format('id','breed','age','gender','adoption_status'))
        print('-'*60)
        for i in dogs:
            if i['breed']==breed_srch:
                print("{:<10}{:<15}{:<10}{:<10}{:<15}".format(i['id'],i['breed'],i['age'],i['gender'],i['adoption_status']))
            else:
                print('not found!!!')
    elif choice==6:
        print('_'*60)
        print("{:<10}{:<15}{:<10}{:<10}{:<15}".format('id','breed','age','gender','adoption_status'))
        print('-'*60)
        for i in dogs:
            if i['adoption_status']=='available':
                print("{:<10}{:<15}{:<10}{:<10}{:<15}".format(i['id'],i['breed'],i['age'],i['gender'],i['adoption_status']))
               
    elif choice==7:
        break
    else:
        print('invalid....!!!')