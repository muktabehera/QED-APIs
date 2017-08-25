from bravado.requests_client import RequestsClient
from bravado.client import SwaggerClient

http_client = RequestsClient()
url = 'http://172.30.3.174/content/apidocs/index.html'
token = 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiZGVsaXZlcnlAdG9rZW4uY29tIiwiYXVkIjoicWVkOmRlZmF1bHQiLCJxZWRwIjpbImQiLCJnIiwiYyIsInMiLCJtIiwiYSIsInAiXSwiZXhwIjoxNTY3MTk5ODQ4fQ.SLo2AoCFsj9awqYxG7u5UwC6QZD4S9IlE1XMOuOKNGo'
# header1 = {
# "Accept": "application/json,application/vnd.qumu.qed+json,application/vnd.qumu.qed.v1+json" ,
# "Authorization": "Bearer "+token+""
# }

http_client.set_api_key(
    'url',
    'token'
)
client = SwaggerClient.from_url('http://172.30.3.174/services/apidocs/qed.json', http_client=http_client)
AuthorizationSystemsByID = client.AuthorizationSystems.authorizationSystemsById(authorizationSystemsid= 'default').result()

# from bravado.requests_client import RequestsClient
# from bravado.client import SwaggerClient
#
# http_client = RequestsClient()
# http_client.set_api_key(
#     'http://petstore.swagger.io', 'special-key'
# )
# client = SwaggerClient.from_url(
#     'http://petstore.swagger.io/v2/swagger.json',
#     http_client=http_client,
# )
# pet = client.pet.getPetById(petId=42).result()
# print pet