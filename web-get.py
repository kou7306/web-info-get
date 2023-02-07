import requests
from bs4 import BeautifulSoup
url = 'https://www.minkou.jp/hischool/ranking/deviation/page={}'
schoolnames = []
schoolvalues = []
for i in range(10): 
    i = i+1
    res = requests.get(url.format(i))
    soup = BeautifulSoup(res.text,'html.parser')
    name = soup.find_all('div',attrs ={'class': 'mod-listRanking-name'})
    value = soup.find_all('dd',attrs ={'class' : 'info-main'})
    for j in name:     
            schoolname =j.find('a')   
            schoolnames.append(schoolname.text)
    for j in value:
            schoolvalue = j.find('a')
            schoolvalues.append(int(schoolvalue.text))
school = dict(zip(schoolnames,schoolvalues))
print(school)
f = open('school.txt', 'w') 
for key,value in school.items():
    f.write('{0} : {1},\n'.format(key, value))
f.close() 