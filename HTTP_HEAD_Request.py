from http.client import HTTPConnection

#HEAD 메소드 : 리소스의 메타데이터를 취득한다.

url = 'www.example.com'
conn = HTTPConnection(url)
conn.request('HEAD','/')
resp = conn.getresponse()

print(resp.status,resp.reason)
data = resp.read()
print(len(data)) # HEAD는 메타데이터만 읽기 때문에 body부분의 데이터 X
print(data)