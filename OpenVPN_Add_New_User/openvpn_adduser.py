import requests

firstName = input("Please enter First Name: ")
lastName = input("Please enter Last Name: ")

devGroupId = "1d11f604-6d36-46b4-8c7f-425895b39504"
qaGroupId = "0272a3be-5262-4f24-b94c-3bac064b714b"
prodGrouId = "61eecf44-73f7-4101-8843-faf2032f5133"

groupIds = {'dev': devGroupId, 'qa': qaGroupId, 'prod': prodGrouId}


def selectFromDict(awsEnv, env):
    index = 0
    indexValidList = []
    print('Select a ' + env + ':')
    for optionName in awsEnv:
        index = index + 1
        indexValidList.extend([awsEnv[optionName]])
        print(str(index) + ') ' + optionName)
    inputValid = False
    while not inputValid:
        inputRaw = input(env + ': ')
        inputNo = int(inputRaw) - 1
        if -1 < inputNo < len(indexValidList):
            selected = indexValidList[inputNo]
            print('Selected ' + env + ': ' + selected)
            break
        else:
            print('Please select a valid ' + env + ' number')
    return selected


awsEnv = {'Dev': 'dev', 'QA': 'QA', 'Prod': 'Prod'}

# Let user select an Env
environment = selectFromDict(awsEnv, 'Environment')
print(environment)
print(groupIds[environment])

headers = {
    'accept': 'application/json',
    'authorization': '',
    'Content-Type': 'application/json',

}

json_data = {
    'devices': [
        {
            'description': 'string',
            'name': 'string',
        },
    ],
    'firstName': firstName,
    'groupId': groupIds[environment],
    'lastName': lastName,
    'username': firstName[0] + lastName + '-' + environment
}

response = requests.post('https://sureco.api.openvpn.com/api/beta/users', headers=headers, json=json_data)

print(response.status_code)
print(response.text)
