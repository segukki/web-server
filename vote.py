import cgi
import json


def save_to_file(ques, answer):
    """Создаём начальный файл, если он не создан"""
    try:
        with open("cgi-bin/vote.json", 'r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        with open("cgi-bin/vote.json", 'w', encoding='utf-8') as f:
            json.dump({}, f)
    """Запись текста"""
    with open("cgi-bin/vote.json", 'r', encoding='utf-8') as f:
        vote = json.load(f)
    vote[ques] = answer
    with open("cgi-bin/vote.json", 'w', encoding='utf-8') as f:
        json.dump(vote, f)


form = cgi.FieldStorage()

ques = form.getfirst("ques", "")
answer = form.getfirst("answer", "")
save_to_file(ques, answer)

q = 'page' + str(int(ques)+1) + '.html'
if int(ques) == 15:
    q = 'cgi-bin/end_page_sct.py'
print('Content-type: text/html\n')
print('<meta http-equiv="Refresh" content="0; url=http://localhost:8000/' + q + '" />')
