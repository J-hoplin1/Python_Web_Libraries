from urllib.request import urlopen
from html.parser import HTMLParser

class ImageParser(HTMLParser): # ineirt HTMLParser
    def handle_starttag(self, tag, attrs): # Override handle_starttag
        if tag != 'img':
            return
        if not hasattr(self,'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)

def parse_image(data):
    parser = ImageParser()
    parser.feed(data)
    dataset = set(x for  x in parser.result)
    return dataset

def main():
    url = "http://www.google.co.kr"
    with urlopen(url) as p:
        charset = p.info().get_param('charset')
        data = p.read().decode(charset)

    dataset = parse_image(data)
    print("Images from ", url)
    print('\n'.join(sorted(dataset)))

if __name__ == "__main__":
    main()