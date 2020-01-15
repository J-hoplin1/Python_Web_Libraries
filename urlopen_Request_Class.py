from urllib.request import urlopen, Request
from urllib.parse import urlencode

url = "http://127.0.0.1:8000"

data = {
    'name':'A',
    'email':'example.com',
    'url':'www.a.b'
}

encData = urlencode(data)
postData = bytes(encData,encoding='utf-8')
req = Request(url,data=postData)
req.add_header('Content-Type','application/x-www-form-urlencoded')
f = urlopen(req)
print(f.info())
print(f.read().decode('utf-8'))

'''
요청헤더를 지정해서 보내고 싶은 경우에는 URL을 지정하는 방식을 변경하면 된다. urlopen의 url인자에 문자열 대신 Request객체를 지정해 주면 된다. Request객체를 생성하고 add_header()를 통해서 헤더를 추가하여 웹 서버로 요청을 보내면 된다.
POST요청을 보내기 위해서는 urlopen()함수와 마찬가지로 data인자를 지정해주면된다(동일하게 바이트 스트링 타입으로)
'''