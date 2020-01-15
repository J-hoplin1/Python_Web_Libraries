from urllib.parse import urlparse

result = urlparse("http://www.python.org:80/guido/python.html;philosophy?overall=3#n10")

print(result)

'''
urlparse : urllib.parse 모듈은 URL의 분헤, 조립, 변경 및 URL 문자 인코딩, 디코딩 등을 처리하는 함수를 제공해 준다. 

urlparse()함수는

ParseResult(scheme='http', netloc='www.python.org:80', path='/guido/python.html', params='philosophy', query='overall=3', fragment='n10')

scheme : URL에 사용된 프로토콜을 의미한다.

netloc : 네트워크 위치

path : 파일 및 애플리케이션의 경로

params : 애플리케이션에 전달되는 매개변수

query : 질의 문자열 또는 매개변수. (쿼리 스트링을 의미한다)

fragment : 문서 내의 Anchor조각을 의미

'''