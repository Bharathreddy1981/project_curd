
import csv


def upload_csv(user_id, token, list_data, db, file_name):
    if len(list_data) == 0:
        return {'Error': 'invalid voter_id and token'}
    elif list_data[0]['id'] != user_id:
        return {'Error': 'invalid registered user_id'}
    elif list_data[0]['token'] != token:
        return {'Error': 'invalid registered token'}

    cur = db.cursor()
    csv_data = csv.reader(open(file_name))
    next(csv_data)
    for row in csv_data:
        cur.execute('INSERT INTO user (name, email, role_type, phone_number) VALUES(%s, %s, %s, %s) '
                        'ON DUPLICATE KEY UPDATE name = ("' + str(row[0]) + '"), email = ("' + str(row[1]) + '"), '
                    'role_type = ("' + str(row[2]) + '"), phone_number = ("' + str(row[3]) + '")', row)
    try:
        db.commit()
        cur.close()
    except Exception as e:
        return {'Error': str(e).split()[1].replace('\"', '') + " " + str(e).split()[2] + " " + str(e).split()[
               -1].replace("'crud_table.", "").replace("'", "").replace('\")', '')}
    return {'csv_file': 'successfully upload'}
