
import pandas as pd



def download_csv(user_id, token, list_data, db, file_name):
    if len(list_data) == 0:
        return {'Error': 'invalid voter_id and token'}
    elif list_data[0]['id'] != user_id:
        return {'Error': 'invalid registered user_id'}
    elif list_data[0]['token'] != token:
        return {'Error': 'invalid registered token'}

    df = pd.read_sql_query("select * from user", con=db)
    df.to_csv(file_name, index=False)
    return {'file_name': file_name}


