import itertools
from datetime import datetime

def set_password():
    while True:
        password = input("Set an 8-character password (for educational purposes): ")
        if len(password) == 8:
            return password
        else:
            print("Password must be exactly 8 characters.")

def brute_force_cracker(target_password):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-!$#@ '
    password_length = 8

    start_time = datetime.now()

    for length in range(password_length, password_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            current_attempt = ''.join(attempt)
            print(f"Trying: {current_attempt}")

            if current_attempt == target_password:
                end_time = datetime.now()
                time_taken = end_time - start_time
                print(f"\nPassword found: {current_attempt}")
                print(f"Time taken: {time_taken}")
                return 

    print("\nPassword not found.")

def password_strength_checker(password):
    bools=[]
    for elements in password:
        if elements.islower()==True:
            bools.append(True)
            break
    for elements_2 in password:
        if elements_2.isupper()==True:
            bools.append(True)
            break
    for elements_3 in password:
        if elements_3=='_' or elements_3=='-' or elements_3=='#' or elements_3=='@' or elements_3=='$' or elements_3==' ' or elements_3=='!':
            bools.append(True)
            break
    for elements_4 in password:
        if elements_4=='6' or elements_4=='7'or elements_4=='8'or elements_4=='9'or elements_4=='5' or elements_4=='4' or elements_4=='3' or elements_4=='2' or elements_4=='1' or elements_4=='0':
            bools.append(True)
            break
    if len(bools)==3 or len(bools)==4:
        return "strong"
    elif len(bools)==2:
        return "medium"
    elif len(bools)==1:
        return "weak"

def main():
    user_password = set_password()
    brute_force_cracker(user_password)

    strength_result = password_strength_checker(user_password)
    print(f"\nPassword strength: {strength_result}")

if __name__ == "__main__":
    main()