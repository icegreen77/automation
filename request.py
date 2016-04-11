#!/usr/bin/env python
# coding=utf-8
import urllib2
import urllib
import json

if __name__ == '__main__':
    # url_heweather = 'https://api.heweather.com/x3/weather?cityid=CN101210101&key=5d3398e76e2d4e84bd115c011cf816ad'
    # info = urllib.urlopen(url_heweather)
    # content = json.dumps(json.loads(info.read()), encoding='utf-8', ensure_ascii=False)

    url_apistore = 'http://apis.baidu.com/apistore/iplookupservice/iplookup?ip=222.46.16.69'
    req = urllib2.Request(url_apistore)
    req.add_header('apikey', 'cb7dde77706b83f859b647dcf81978a8')
    resp = urllib2.urlopen(req)
    content = json.dumps(json.loads(resp.read()), indent=4, encoding='utf-8', ensure_ascii=False)
    print content

    # post方式，get方式使用urllib2.open
    url_win007 = 'http://ios.win007.com/phone/sbodds.aspx?'
    data = {'scheid': '1136996', 'apiversion': '1', 'from': '2'}
    body = urllib.urlencode(data)
    req007 = urllib2.Request(url_win007, body)
    resp007 = urllib2.urlopen(req007)
    content007 = json.dumps(json.loads(resp007.read()), indent=4, encoding='utf-8')
    print content007
    print resp007.code  # 获取http请求状态码

    # reqHttp = httplib.HTTPConnection('http://ios.win007.com/phone/sbodds.aspx?scheid=1136996&apiversion=1&from=2', 80)
    # reqHttp.request('POST', 'http://ios.win007.com/phone/sbodds.aspx?scheid=1136996&apiversion=1&from=2')
    # respHttp = reqHttp.getresponse()
    # print respHttp
    pass
