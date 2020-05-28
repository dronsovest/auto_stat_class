import requests
import json
import datetime

d = datetime.date.today()
result = '[b]Турнирные классы на ' + str(datetime.date.today().strftime("%d.%m.%Y")) + 'г[/b]' + '\n\n' + '[u]Переписка[/u]' + '\n\n'

response = requests.get('https://www.chess-online.com/api/stats/zone-info')

todos = json.loads(response.text)

zones = todos['zones']
main = zones['MAIN']
statsMain = main['stats']
classesMain = statsMain['classes']
maina = zones['MAINA']
statsMaina = maina['stats']
classesMaina = statsMaina['classes']

for i in classesMain:
	result += i['name'] + ' ' + '[b]' + str(i['count']) + '[/b]' + ' ' + 'игрок(а,ов)' +'\n'

result += '\n' + '[u]Адванс[/u]' + '\n\n'

for i in classesMaina:
	result += i['name'] + ' ' + '[b]' + str(i['count']) + '[/b]' + ' ' + 'игрок(а,ов)' +'\n'

print (result)