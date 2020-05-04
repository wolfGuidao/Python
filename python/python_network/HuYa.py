from urllib import request
import re


class Spider():
    url = "https://www.huya.com/g/lol"
    root_pattren = '<span class="txt"([\s\S]*?)</span>'
    # name_pattern = '</i>([\s\S]*?)</span>'
    # number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattren, htmls)
        print(root_html)
    #     anctors = []
    #     for html in root_html:
    #         name = re.findall(Spider.name_pattern, html)
    #         number = re.findall(Spider.number_pattern, html)
    #         anctor = {'name': name, 'number': number}
    #         anctors.append(anctor)
    #     return anctors

    # def __refine(self, anctors):
    #     lam = lambda anctor: {
    #         'name': anctor['name'][0].strip(),
    #         'number': anctor['number'][0]
    #         }
    #     return map(lam, anctors)

    # def __sort_seed(self, anctor):
    #     r = re.findall('\d*', anctor['name'])
    #     number = float(r[0])
    #     if '万' in anctor['number']:
    #         number = number * 10000
    #     return number

    # def __sort(self, anctors):
    #     anctors = sorted(anctors, key=self.__sort_seed, reversed=True)
    #     return anctors

    # def __show(self, anctors):
    #     for rank in range(0, len(anctors)):
    #         print('rank' + str(rank + 1) + ': ' + anctors[rank]['name'] + '  ' + anctors[rank]['number'])

    def go(self):
        htmls = self.__fetch_content()
        print(htmls)
        self.__analysis(htmls)
    #    anctors = self.__analysis(htmls)
    #     anctors = list(self.__refine(anctors))
    #     anctors = self.__sort(anctors)
    #     self.__show(anctors)

spider = Spider()

spider.go()
