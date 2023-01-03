import requests
import json

# Запрос GET
status = 'available'
res_g = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}',
                    headers={'accept': 'application/json'})
print('Результат запроса GET\n', res_g.status_code)
print(res_g.json())

# Запрос POST добавляем нового питомца
param = {"id": 1822, "category": {"id": 1822, "name": "dogs"},
 "name": "Chaplin", "photoUrls": ["string"], "tags": [{"id": 1822, "name": "shepherds"}], "status": "available"}
json_param = json.dumps(param)
res_p = requests.post('https://petstore.swagger.io/v2/pet',
headers={'accept': 'application/json', 'Content-Type': 'application/json'},
data=json_param)
print('\nРезультат запроса POST\n', res_p.status_code)
print(res_p.text)

# Запро GET поиск питомца по petId
petId = 1822
res_id = requests.get(f'https://petstore.swagger.io/v2/pet/{petId}', headers={'accept': 'application/json'})
print('\nРезультат поиска питомца\n', res_id.status_code)
print(res_id.json())

# Запрос PUT обновление данных питомца (изменение имени)
param = {'id': 1822, 'category': {'id': 1822, 'name': 'dogs'}, 'name': 'Charlie Chaplin', 'photoUrls': ['string'],
        'tags': [{'id': 1822, 'name': 'shepherds'}], 'status': 'available'}
json_param = json.dumps(param)
res_put = requests.put('https://petstore.swagger.io/v2/pet', headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                      data=json_param)
print('\nРезультат изменения питомца\n', res_put.status_code)
print(res_put.json())

# Запрос DELETE удаление нашего питомца
res_del = requests.delete(f'https://petstore.swagger.io/v2/pet/{petId}', headers={'accept': 'application/json'})
print('\nРезультат удаления\n', res_del.status_code)
print(res_del.json())