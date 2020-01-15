'''
urlopen :urlopen(url, data = None, [timeout])

- url : url안저애 지정한 URL로 연결하고 유사 파일 객체를 반환. url은 문자열 혹은 request클래스의 인스턴스가 올 수 있다.

- 디폴트 요청 방식은 GET이고, 웹 서버에 전달할 파라미터가 있으면 질의 문자열을 url인자에 포함해서 보낸다

- POST로 보내고 싶은 경우 data인자에 질의 문자열을 지정해 주면 된다.
'''

from urllib.request import urlopen

f = urlopen("http://www.example.com")
print(f.read().decode('utf-8'))