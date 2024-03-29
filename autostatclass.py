import datetime
import json
import pyperclip
import requests
import tkinter as tk


def format_players(players_count):
    if players_count == 1:
        return 'игрок'
    elif 2 <= players_count <= 4:
        return 'игрока'
    else:
        return 'игроков'


result = ('[b]Турнирные классы на ' +
          str(datetime.date.today().strftime("%d.%m.%Y")) + 'г[/b]' + '\n\n' +
          '[u]Переписка[/u]' + '\n\n')

response = requests.get('https://www.chess-online.com/api/stats/zone-info')

todos = json.loads(response.text)

zones = todos['zones']
main = zones['MAIN']
stats_main = main['stats']
classes_main = stats_main['classes']

for i in classes_main:
    if i['name'] == 'Класс F':
        result += 'Класс F \n'
    else:
        result += (i['name'] + ' ' + '[b]' + str(i['count']) + '[/b]' + ' ' +
                   format_players(i['count'] % 10) + '\n')

result += ('\n[color=red][size=9]Класс F скрыт, так как данные неинформативны.'
           '\nТуда попадают все, кто сыграл 20 партий по переписке.[/size]'
           '[/color]')

result_gui = result.replace('[b]', '').replace('[/b]', '').replace('[u]' , '').replace('[/u]', '')

window = tk.Tk()
window.title('Chotcher 1.0')
window.geometry('600x500+650+300')
label = tk.Label(
    text=result_gui,
    width=70,
    height=20,
)
label.pack()
button = tk.Button(
    master=window, 
    text='Скопировать в буфер обмена',
    command=pyperclip.copy(result),
    )
button.pack()
button2 = tk.Button(
    master=window, 
    text='Закрыть',
    command=window.destroy,
    )
button2.pack()
window.mainloop()
