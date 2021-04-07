# STUDENT: DUSTIN KABAN
# ID: T00663749
# COURSE: COMP 2211, PYTHON, ASSIGNMENT 2
# DATE: APRIL 07, 2021

def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    student_id = input('Enter your student id #: ')
    user_name = get_login_name(first_name,last_name,student_id)
    print('Your username is:', user_name)

    password = input('Enter a password: ')

    while not verifyPassword(password):
        password = input('Enter a password: ')

    print('----------------------')
    print('Login Information is:')
    print('Username:', user_name)
    print('Password:', password)


def get_login_name(first_name,last_name,student_id):
    return first_name[0:3] + last_name[0:3] + student_id[-3:]


def verifyPassword(password):
    if len(password) < 7:
        print('Password must have at least 7 characters')
        return False
    elif not any(char.isupper() for char in password):
        print('Password must have at least 1 uppercase letter')
        return False
    elif not any(char.islower() for char in password):
        print('Password must have at least 1 lowercase letter')
        return False
    elif not any(char.isdigit() for char in password):
        print('Password must have at least 1 digit')
        return False
    else:
        print('Password accepted')
        return True


main()