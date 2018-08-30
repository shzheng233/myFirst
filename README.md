# myFirst
python爬虫练手实例

利用**request**与**bs4**的特性打磨出来的爬小说的实例

**request获取网页源代码**

``` python
url = 'url'

res = requests.get(url)
content = res.text

```
**bs4解析网页代码**

``` python
soup = BeautifulSoup(content)
manager = soup.findAll('td')
#更多方法请仔细百度
```
**谢谢观看**
