def total_info(acc_id, token, data,  db):
    if len(data) == 0:
        return {'Error': 'invalid voter_id and token'}
    elif data[0]['id'] != acc_id:
        return {'Error': 'invalid registered acc_id'}
    elif data[0]['token'] != token:
        return {'Error': 'invalid registered token'}

    cur = db.cursor()
    try:
        query = "select * from user"
        cur.execute(query)
        red = cur.fetchall()
        login_list11 = []
        for i in red:
            k = { "name": i[0], "email": i[1], "role_type": i[2],
                  "phone_number": i[3]}
            login_list11.append(k)
        db.commit()
        return login_list11
    except Exception as e:
        return {'Error': str(e).split()[1].replace('\"', '') + " " + str(e).split()[2] + " " + str(e).split()[-1].replace(
                "'crud_table.", "").replace("'", "").replace('\")', '')}

