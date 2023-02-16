import get_data

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    l = []
    for user in data['results']:
        l.append({

            "first_name":user['name']['first'], 
            "last_name":user['name']['last'],
            "phone_number":user['phone']
            
         })
    return l

data = get_data.get_data('randomuser_data.json')
print(get_users_data(data))