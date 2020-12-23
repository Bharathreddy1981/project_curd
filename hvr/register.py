
def fetch(db, acc_id, token):
    value = acc_id
    cursor = db.cursor()
    query_id = "select * from owner  where id = '" + str(value) + "'"
    cursor.execute(query_id)
    bha = cursor.fetchall()
    login_list = []
    for i in bha:
        k = {"id": i[0], "name": i[1], "email": i[2], "phone": i[3],
                 "password": i[4], "token": i[5]}
        login_list.append(k)

    query = "select * from owner where token = '" + str(token) + "'"
    cursor.execute(query)
    red = cursor.fetchall()
    login_list11 = []
    for i in red:
        k = {"id": i[0], "name": i[1], "email":i[2], "phone": i[3],
                 "password": i[4], "token":i[5]}
        login_list11.append(k)

    if len(login_list) == 0:
        return {'Error': "account id "}
    elif len(login_list11) == 0:
        return {'Error': 'invalid token'}
    else:
        return login_list11





