
from uuid import uuid4

def inserted(db, post_data, validations_data,encrypted):
    if post_data != validations_data:
        return validations_data
    else:
        name = post_data['name']
        phone = post_data['phone']
        email = post_data['email']
        #password = post_data['password']
        cursor = db.cursor()

    try:
        query = "INSERT INTO owner (id, name, email,  phone, password) " \
                "VALUES ( '" + str(uuid4()) + "', '" + str(name) + "', '" + str(email) + "',  '" + str(phone) + "', '" + str(encrypted) + "')"
        cursor.execute(query)
        db.commit()
    except Exception as e:
        return {
            'Error': str(e).split()[1].replace('\"', '') + " " + str(e).split()[2] + " " + str(e).split()[-1].replace(
                "'register_table.", "").replace("'", "").replace('\")', '').replace('user.', '')}

    return {"User": 'Add User successfully'}

