emp=[{'id':1, 'name': 'hari', 'age': 22, 'salary': 35000, 'place': 'tsr', 'dob': '2002', 'password': '2002'}]
def add_emp():
    id=int(input('enter the id: '))
    f=0
    for i in emp:
        if i['id']==id:
            f=1
            print('existing id..!!!')
            add_emp()
    if f==0:
        name=input('enter the name: ')
        age=int(input('enter the age: '))
        salary=int(input('enter the salary: '))
        place=input('enter the place: ')
        dob=input('enter the dob: ')
        password=dob
        emp.append({'id':id,'name':name,'age':age,'salary':salary,'place':place,'dob':dob,'password':password})
        print('employee added successfully......')
        print(emp)

def admin_update():
    print(emp)
    id=int(input('enter your id: '))
    f=0
    for i in emp:
        if i['id']==id:
            f=1
            name=input('enter your name: ')
            age=int(input('enter your age: '))
            salary=int(input('enter your salary: '))
            place=(input('enter your place: '))
            dob=(input('enter your date of birth: '))
            i['name']=name
            i['age']=age
            i['salary']=salary
            i['place']=place
            i['dob']=dob
            print('updated successfully')
    if f==0:
        print('invalid id!!!')

def admin_delete():
    id=int(input('enter your id: '))
    f3=0
    for i in emp:
        if i['id']==id:
            f3=1
            emp.remove(i)
            print('REMOVED!!!')
    if f3==0:
        print('invalid id!!!')
#     id=str(input('enter thre id: '))
#     f=0
#     for i in emp:
#         if i['id']==id:
#             f=1
#             emp.remove(i)
#             print('REMOVED...!!!')
#     if f==0:
#         print('invalid id!!!')

def admin_display():
    print('_'*65)
    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}".format('id','name','age','salary','place','dob'))
    print('-'*65)
    for i in emp:
            print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}".format(i['id'],i['name'],i['age'],i['salary'],i['place'],i['dob']))