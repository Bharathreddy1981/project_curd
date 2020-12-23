

def log(json_data, db):

    email = json_data["email"]
    # if json_data != email:
    #     return valid_data

    cur = db.cursor()
    query = "select * from owner where email = ('" + str(email) + "') "
    cur.execute(query)
    fetch_data = cur.fetchall()
    list_data = []
    for data in fetch_data:
        dict_data = {"id": data[0], "name": data[1], "email": data[2], "phone": data[3], "password": data[4]}
        list_data.append(dict_data)
    return list_data
