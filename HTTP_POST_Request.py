from http.client import HTTPConnection
from urllib.parse import urlencode

url = '127.0.0.1:8000'

#POST요청으로 보낼 Parameters

params = urlencode({
    'language' : 'python',
    'name' : 'Hoplin',
    'email' : 'a@b'
})

print(params)

# Headers

headers = {
    'Content-Type' :'application/x-www-form-urlencoded',
    'Accept' : 'text/plain'
}

conn = HTTPConnection(url)
conn.request('PUT','',params,headers) #request(method,URL,body,headers) 순서의 매개변수를 가지고 있다.
resp = conn.getresponse()
print(resp.status,resp.reason)

data = resp.read()
print(data.decode('utf-8'))

conn.close()