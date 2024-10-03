from admin import*
# from main import*
def login():
    uname=input('enter your username: ')
    password=input('enter your passwrod: ')
    f=0
    user=''
    if uname=='admin' and password=='admin':
        f=1
    if uname.isdigit():
        uname=int(uname)
    for i in emp:
        # user lo
                # print(type(uname))

        if i['id']==uname and i['password']==password:
            f=2
            user=i
    # for i in emp:
    #     if i['id']==uname and i['password']==password:
    #         f=2
    #         user=i
    return f,user