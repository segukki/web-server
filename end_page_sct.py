import json


with open('cgi-bin/vote.json', 'r', encoding='utf-8') as f:
    vote = json.load(f)

with open('cgi-bin/answers.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

q = open('end_page.html', 'r', encoding='utf8', errors="ignore")

pattern = q.read()

pub = ''
i = 0
if answers is not None:
    for key, value in answers.items():
        pub += '<tr><td>Вопрос ' + str(key) + ': ' + str(value) + '</td>'
        pub += '<td>Вопрос ' + str(key) + ': ' + str(vote.get(key)) + '</td></tr>'
        if str(value) == str(vote.get(key)):
            i += 1


print('Content-type: text/html\n')

print(pattern.format(result=pub, itog=i))
