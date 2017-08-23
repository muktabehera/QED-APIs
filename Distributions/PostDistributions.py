import requests

test_case = 'PostDistributions'
url = 'http://172.30.3.174/distributions'
Token = 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiZGVsaXZlcnlAdG9rZW4uY29tIiwiYXVkIjoicWVkOmRlZmF1bHQiLCJxZWRwIjpbImQiLCJnIiwiYyIsInMiLCJtIiwiYSIsInAiXSwiZXhwIjoxNTY3MTk5ODQ4fQ.SLo2AoCFsj9awqYxG7u5UwC6QZD4S9IlE1XMOuOKNGo'
header = {
"Accept": "application/json,application/vnd.qumu.qed+json,application/vnd.qumu.qed.v1+json" ,
"Authorization": "Bearer "+Token+""
}
payload = {
  "id": "contentM2",
  "name": "contentM2",
  "creationDate": "2017-08-23T12:32:11Z",
  "modificationDate": "2017-08-23T12:32:11Z",
  "activationDate": "2017-06-20T07:42:55Z",
  "expirationDate": None,
  "distributionPolicy": "REQUIRED",
  "files": [
    {
      "id": "cont27",
      "sourceUrl": "qedorigin://Content_storage/mediaLarge6.mp4",
      "streamMetadata": {
        "bitrateKbps": 100,
        "width": 10,
        "height": 5,
        "codecs": None,
        "mimeType": "video/wmv",
        "lang": None,
        "tags": {}
      },
      "auxiliaryFiles": [],
      "status": "PUSH_COMPLETE",
      "statusDetails": []
    }
  ],
  "targetAudiences": [
    {
      "id": "cache_eviction_audi",
      "name": "cache_eviction_audi"
    }
  ],
  "tags": None,
  "status": "PUSH_COMPLETE"
}
#print header
#print data
response = requests.post(url, data=payload, headers=header)
# print response.status_code
print response.text

if response.status_code == 200:
    print 'Test Case '+test_case+': Pass'
else:
    print 'Test Case ' + test_case + ': Fail'

#
