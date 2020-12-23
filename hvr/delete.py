
def delete_info(acc_id, json_data, token, data, db):
    if len(data) == 0:
        return {'Error': 'invalid voter_id and token'}
    elif data[0]['id'] != acc_id:
        return {'Error': 'invalid registered acc_id'}
    elif data[0]['token'] != token:
        return {'Error': 'invalid registered token'}

    email = json_data['email']
    cursor = db.cursor()

    query11 = "select * from user where  email ='" + str(email) + "'"
    cursor.execute(query11)
    db.commit()
    red = cursor.fetchall()
    login_list11 = []
    for i in red:
        k = {"name": i[0], "email": i[1], "role_type": i[2], "phone": i[3]}
        login_list11.append(k)
    if len(login_list11) == 0:
        return {"email": "The email does not exists to update the values"}

    try:
        query = "DELETE FROM user WHERE email = ('" + str(email) + "')"
        cursor.execute(query)
        db.commit()

    except Exception as e:
        return {'Error': str(e)}

    return {"User": 'deleted User successfully'}


