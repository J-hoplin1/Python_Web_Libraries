from http.client import HTTPConnection
from urllib.parse import urlencode

url = '127.0.0.1:8000'
'''
urlencode를 통해 URL을 인코딩 하는 이유

URL인코딩이란 문자나 특수문자를 웹서버와 브라우저에서 보편적으로 허용되는 방식으로 변화시키는 매커니즘을 의미한다. URL은 ASCII문자 집합으로만 인터넷에 전송할 수 있는데
URL에서는 가끔씩 ASCII집합 이외의 문자들도 포함시키다 보니, URL은 유효한 ASCII형식으로 변환시켜 주어야 하는것이다.이말은 즉슨 아스키 문자 이외의 문자는 모두 인코딩 된다는 것이다.
'''

params = urlencode({
    'language' : 'python',
    'name' : 'Hoplin',
    'email' : 'a@b'
})

print(params)
# Result : language=python&name=Hoplin&email=a%40b

# Headers

headers = {
    'Content-Type' :'application/x-www-form-urlencoded',
    'Accept' : 'text/plain'
}

#연결 객체
conn = HTTPConnection(url)
# PUT방식 명시 POST방식과 동일
conn.request('PUT','',params,headers)

resp = conn.getresponse()
print(resp.status,resp.reason)

data = resp.read()
print(data.decode('utf-8'))

conn.close()
