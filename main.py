
from hvr import database, register, validations,total, update, delete, fetch, insert
from flask import Flask, jsonify, request
from package import package_register, login, validation, password, token
from package_csv import download, upload

main = Flask(__name__)
@main.route("/package_register", methods=['POST'])
def pack_reg():
    json_data = request.get_json()
    db = database.base()
    encrypted_password = password.pass_encrypt(json_data)
    valid_data = validation.valid(json_data)
    value = package_register.inserted(db, json_data, valid_data, encrypted_password)
    return jsonify(value)

@main.route("/package_login", methods=['POST'])
def pack_login():
    json_data = request.get_json()
    #valid_data = validation.valid(json_data)
    db = database.base()
    list_data = login.log(json_data, db)
    password_chek = password.pass_check(json_data, list_data)
    tok = token.log_token(db, json_data, list_data, password_chek)
    return jsonify(tok)




@main.route("/register_data/acc_id=<acc_id>", methods=['POST'])
def reg(acc_id):
    token = request.headers['token']
    json_data = request.get_json()
    db = database.base()
    data = register.fetch( db, acc_id, token,)
    value = insert.create(acc_id, token, data, json_data, db)

    return jsonify(value)

@main.route("/total_data/acc_id=<acc_id>", methods=['GET'])
def list_user(acc_id):
    token = request.headers['token']
    #json_data = request.get_json()
    db = database.base()
    data = register.fetch(db, acc_id, token, )
    value = total.total_info(acc_id, token, data,  db)
    return jsonify(value)




@main.route("/update_data/acc_id=<acc_id>", methods=['POST'])
def edit_user(acc_id):
    token = request.headers['token']
    json_data = request.get_json()
    db = database.base()
    data = register.fetch(db, acc_id, token)
    value = update.update_info(acc_id, json_data , token, data, db)
    return jsonify(value)



@main.route("/delete_data/acc_id=<acc_id>", methods=['POST'])
def delete_user(acc_id):
    token = request.headers['token']
    json_data = request.get_json()
    db = database.base()
    data = register.fetch(db, acc_id, token)
    value = delete.delete_info(acc_id, json_data, token, data, db)
    return jsonify(value)





@main.route("/download/user_id=<user_id>", methods=['GET'])
def download_data(user_id):
    token = request.headers['token']
    db = database.base()
    data = register.fetch(db, user_id, token)
    file_name = 'operation.package_csv'
    info = download.download_csv(user_id, token, data, db, file_name)

    return jsonify(info)


@main.route("/upload/acc_id=<acc_id>", methods=['GET'])
def upload_data(acc_id):
    token = request.headers['token']
    db = database.base()
    list_data = register.fetch(db, acc_id, token)
    file_name = 'python.csv'
    info = upload.upload_csv(acc_id, token, list_data, db, file_name)

    return jsonify(info)





if(__name__ == "__main__"):
   main.run(debug=True)
