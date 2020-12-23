
def create(acc_id, token, data, post_data, db):
    name = post_data['name']
    email = post_data['email']
    role_type = post_data['role_type']
    phone_number = post_data['phone_number']
    if len(data) == 0:
        return {'Error': 'invalid voter_id and token'}
    elif data[0]['id'] != acc_id:
        return {'Error': 'invalid registered acc_id'}
    elif data[0]['token'] != token:
        return {'Error': 'invalid registered token'}

    cur = db.cursor()
    try:
        query = "INSERT INTO user (name, email, role_type, phone_number) " \
                    "VALUES ('" + str(name) + "', '" + str(email) + "', " \
                    "'" + str(role_type) + "', '" + str(phone_number) + "')"
        cur.execute(query)
        db.commit()
        return {"User": 'created successfully'}
    except Exception as e:
        return {'Error': str(e).split()[1].replace('\"', '') + " " + str(e).split()[2] + " " + str(e).split()[-1].replace("'crud_table.", "").replace("'", "").replace('\")', '')}


