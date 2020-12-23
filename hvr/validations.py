


def valid(post_data):
    name = post_data['name']
    phone = post_data['phone']
    email = post_data["email"]
    role = post_data["role_name"]
    if 4 > len(name) or len(name) > 15:
        return {'Error': 'user_name range between 4-15'}
    elif 14 > len(email) or len(email) > 30:
        return {'Error': 'email range between 13-30'}

    return post_data
