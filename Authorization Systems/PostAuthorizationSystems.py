import requests

test_case = 'GetAuthorizationSystems'
url = 'http://172.30.3.174/authorizationSystems'
Token = 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiZGVsaXZlcnlAdG9rZW4uY29tIiwiYXVkIjoicWVkOmRlZmF1bHQiLCJxZWRwIjpbImQiLCJnIiwiYyIsInMiLCJtIiwiYSIsInAiXSwiZXhwIjoxNTY3MTk5ODQ4fQ.SLo2AoCFsj9awqYxG7u5UwC6QZD4S9IlE1XMOuOKNGo'
header = {
"Accept": "application/json,application/vnd.qumu.qed+json,application/vnd.qumu.qed.v1+json" ,
"Authorization": "Bearer "+Token+""
}
payload = {
  "visibleInAllConfigurations": 'true',
  "configAdminCanEdit": 'true',
  "configurations": [],
  "id": "667",
  "name": "23AugustAuthorizationSystem",
  "macKey": "11111111111111111111111111111111",
  "grantablePermissions": ["manageSystem","matchAny","provision","match","distribute","generate","manageConfiguration"]
}
#print header
response = requests.post(url, data=payload, headers=header)
# print response.status_code
# print response.text
#print payload

if response.status_code == 200:
    print 'Test Case '+test_case+': Pass'
else:
    print 'Test Case ' + test_case + ': Fail'