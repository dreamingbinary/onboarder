import requests

firstName = input("Please enter a new Username: ")
lastName = input("Please enter a new Username: ")

#todo add the following to list for selection, currently hardcoded in json_data
devGroupId = "1d11f604-6d36-46b4-8c7f-425895b39504"
qaGroupId = "0272a3be-5262-4f24-b94c-3bac064b714b"
prodGrouId = "61eecf44-73f7-4101-8843-faf2032f5133"


headers = {
    'accept': 'application/json',
    'authorization': 'add auth bearer here'
}

json_data = {
    'devices': [
        {
            'description': 'string',
            'name': 'string',
        },
    ],
    'firstName': firstName,
    'groupId': '1d11f604-6d36-46b4-8c7f-425895b39504',
    'lastName': lastName,
    'username': firstName[0] + lastName + "-" + "dev"
}

response = requests.post('https://sureco.api.openvpn.com/api/beta/users', headers=headers, json=json_data)