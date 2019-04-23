# 正则表达式
import re

pattern1 = 'cat'
pattern2 = 'muse'
str1 = 'cat and dog run and ran '

# 简单匹配
print(pattern1 in str1)
print(pattern2 in str1)

# 正则表达式匹配
print(re.search(pattern1, str1))
print(re.search(pattern2, str1))

ptn = r'r[au]n'
print(re.search(ptn, str1))

pattern3 = r'^I'
text = 'sjs' \
       'I am xxx'
print(re.search(pattern3, text))

print(re.findall(r'r[au]n', str1))