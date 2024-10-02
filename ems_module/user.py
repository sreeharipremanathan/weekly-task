from admin import*
def view_profile(user):
    print('_'*65)
    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}".format('id','name','age','salary','place','date of birth'))
    print('-'*65)
    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}".format(user['id'],user['name'],user['age'],user['salary'],user['place'],user['date_of_birth']))