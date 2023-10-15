import json

async def init():
    listObj = []
    with open('database.json', 'w') as json_file:
        json.dump(listObj, json_file,
                  indent=4,
                  separators=(',', ': '))


async def read():
    with open('database.json', mode='r') as f:

        data = json.load(f)
    return data


async def write(to_json):
    listObj = await read()
    print(type(listObj))


    listObj.append(to_json)

    # Verify updated list
    print(listObj)

    with open('database.json', 'w') as json_file:
        json.dump(listObj, json_file,
                  indent=4,
                  separators=(',', ': '))

    print('Successfully appended to the JSON file')

