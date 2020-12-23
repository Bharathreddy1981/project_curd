
from werkzeug.security import generate_password_hash, check_password_hash


def pass_encrypt(data):
    passwd = data["password"]
    hashed_password = generate_password_hash(passwd, method="sha256")

    return hashed_password



# def pass1_encrypt(data):
#
#     hashed_password = generate_password_hash(data, method="sha256")
#
#     return hashed_password
#



def pass_check(post_data, list_data):
    password = post_data['password']

    if len(list_data) == 0:
        return {'Error': 'email not registered'}
    else:
        fetched_password = list_data[0]['password']
        password_check_final = check_password_hash(fetched_password, password)
        return password_check_final
