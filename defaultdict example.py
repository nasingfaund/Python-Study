from collections import defaultdict

# ЗАДАЧА: вывести топ-3 частоиспользуемых слова в тексте
s = "abba com mother bill mother com abba dog abba mother com"

words = s.split(' ')

# упростим этот кусок кода с помощью defaultdict
# d = dict()

# for word in words:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1

d = defaultdict(int)

for word in words:
    d[word] += 1

print(d)
print(list(d.keys())[:3])
