from http.client import HTTPConnection

host = 'www.example.com'
#연결 객체 생성
conn = HTTPConnection(host)
#요청보내기
conn.request('GET','/')
#응답 객체 생성
resp = conn.getresponse()

#순서대로 상태 코드, 상태 메세지
print(resp.status,resp.reason)
data1 = resp.read() # 데이터를 전체 읽어야 추후 다시 request()를 했을떄 오류 발생 X
print(data1)
