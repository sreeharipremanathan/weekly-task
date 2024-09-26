def login():
    uname=input('enter your username: ')
    password=input('enter your passwrod: ')
    f=0
    if uname=='admin' and password=='admin':
        f=1
    return f