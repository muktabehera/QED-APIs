from bravado.requests_client import RequestsClient
from bravado.client import SwaggerClient

http_client = RequestsClient()
url = 'http://172.30.4.216/content/apidocs/index.html'
token = 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiYWRtaW5AMTcyLjMwLjQuMjE2LmNvbSIsImF1ZCI6InFlZDpkZWZhdWx0IiwicWVkcCI6WyJzIiwiYyIsImciLCJwIiwiZCIsIm0iLCJhIl19.3NzYb3lS8W3WMNBDRS0q5Zoh3pZJxWRUaXjvyszEsvs'
header1 = {
"Accept": "application/json,application/vnd.qumu.qed+json,application/vnd.qumu.qed.v1+json" ,
"Authorization": "Bearer "+token+""
}

http_client.set_api_key(
    'url',
    'token', param_in='header1'
)
client = SwaggerClient.from_url('http://172.30.4.216/services/apidocs/qed.json', http_client=http_client)
# AuthorizationSystemsByID = client.AuthorizationSystems.authorizationSystemsById(authorizationSystemsid= 'default').result()
print header1