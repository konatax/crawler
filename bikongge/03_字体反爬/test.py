from lxml import etree

with open('./test.html','r',encoding='utf-8') as f:
    html = f.read()
print(html)
tree = etree.HTML(html)
t = tree.xpath('//h/p/text()')
print(t)
print(0x9476)