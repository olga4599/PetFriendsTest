import requests
import json

base_url = 'https://petstore.swagger.io/v2'

#получить список птомцев по статусу
get_url = '/pet/findByStatus'
params_get = {'status': 'available'}
headers_get = {'accept': 'application/json'}

r = requests.get(base_url + get_url, params=params_get, headers=headers_get)
try:
    result = r.json()
except:
    result = r.text
finally:
    print(result)


#POST-method - создать нового питомца
post_url = '/pet'
post_headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
new_pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "dog"
  },
  "name": "Smiley",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "dog"
    }
  ],
  "status": "available"
}
post_data = json.dumps(new_pet)
res = requests.post(base_url + post_url, headers= post_headers, data = post_data)

try:
    result = res.json()
    new_pet_id = result.get('id')
except:
    result = res.text
    new_pet_id = int(result.split(':')[1].split(';')[0])
finally:
    print(result)
print(res.status_code)

#PUT method - поменять данные у питомца
put_url = '/pet'
put_headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
update_pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "parrot"
  },
  "name": "Pirot",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "parrot"
    }
  ],
  "status": "available"
}

put_data = json.dumps(update_pet)
res = requests.post(base_url + put_url, headers= put_headers, data = put_data)

try:
    result = res.json()
except:
    result = res.text
finally:
    print(result)

#DELETE - удалить питомца
del_url = f'/pet/{new_pet_id}'
params_del = {'petId' : new_pet_id}

res = requests.delete(base_url + del_url, params=params_del)
try:
    result = res.json()
except:
    result = res.text
finally:
    print(result)

#проверка удаленного питомца по id
get_url = f'/pet/{new_pet_id}'
params_get = {'petId': new_pet_id}
headers_get = {'accept': 'application/json'}

r = requests.get(base_url + get_url, params=params_get, headers=headers_get)
if r:
    try:
        result = r.json()
    except:
        result = r.text
    finally:
        print(result)
else:
    print('The pet is not found')