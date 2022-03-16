import re

with open('bloomberg_article.txt', 'r', encoding='utf-8') as f:
    out = f.read()
    
abbrvs = ['Inc.', 'E.g.', 'e.g.', 'Ltd.']

out = re.sub('\s*\n', '\n', out)
out = re.sub('(?<![."”?!])\s*\n', ' ', out)
out = re.sub('\*\*\*\*\*\s*', '\n', out)
out = out.replace("(Bloomberg) -- ", "\n")
for a in abbrvs:
    out = out.replace(a+'\n', a+' ')
out = out.replace('\n', '\n\n')
with open('bloomberg_article_formatted.txt', 'w', encoding='utf-8') as f:
    f.write(out)