import re

with open('bloomberg_article.txt', 'r', encoding='utf-8') as f:
    out = f.read()
    
abbrvs = ['Inc.', 'E.g.', 'e.g.', 'Ltd.', 'St.', 'Ave.', 'Blvd.', 'Corp.', 'Mr.', 'Mrs.', 'U.S.', 'U.S.A.', 'U.K.', 'Dr.']
leads = ["(Bloomberg) -- ", "(Bloomberg Opinion) -- ", "(Bloomberg Businessweek) -- ", "(Dow Jones) -- "]

datestamp = '\d+-\d+-\d+\s'
timestamp = '\d+:\d+:\d+.\d+\sGMT'

out = out.replace('\n\n', '+++++')
out = re.sub('(?<![."”?!])\s*\n', ' ', out)
out = re.sub(timestamp, '', out)

p = re.compile(datestamp) 
dates = p.findall(out)

for a in abbrvs:
    out = out.replace(a+'\n', a+' ')
for l in leads:
    out = out.replace(l, '\n')
for d in dates:
    out = out.replace(d, '\n'+d)

out = out.replace('+++++', '\n')

with open('bloomberg_article_formatted.txt', 'w', encoding='utf-8') as f:
    f.write(out)

with open('bloomberg_article_formatted.txt', 'r', encoding='utf-8') as f:
    contents = f.readlines()

b = [i.lstrip() for i in contents]
new_contents = "".join(b)
new_contents = new_contents.replace('\n', '\n\n')

with open('bloomberg_article_formatted.txt', 'w', encoding='utf-8') as f:
    f.write(new_contents)