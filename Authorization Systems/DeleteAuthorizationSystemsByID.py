import requests

test_case = 'DeleteAuthorizationSystemsByID'
url = 'http://172.30.3.174/authorizationSystems/667'
Token = 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiZGVsaXZlcnlAdG9rZW4uY29tIiwiYXVkIjoicWVkOmRlZmF1bHQiLCJxZWRwIjpbImQiLCJnIiwiYyIsInMiLCJtIiwiYSIsInAiXSwiZXhwIjoxNTY3MTk5ODQ4fQ.SLo2AoCFsj9awqYxG7u5UwC6QZD4S9IlE1XMOuOKNGo'
header = {
"Accept": "application/json,application/vnd.qumu.qed+json,application/vnd.qumu.qed.v1+json" ,
"Authorization": "Bearer "+Token+""
}
#print header
response1 = requests.delete(url,headers=header)
response2 = requests.get(url,headers=header)
# print response.status_code
#print response.text


if response1.status_code == 200 and response2.status_code == 404 :
    print 'Test Case '+test_case+': Pass'
else:
    print 'Test Case ' + test_case + ': Fail'