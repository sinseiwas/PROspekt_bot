import pandas as pd


cmd_list = "Список команд:\n1)/hello\n2)/bosses\n3)/bot_founder\n4)/in_development\n5)/info\n6)/am_i_alone"


prospekt_bosses = "КУРАТОРЫ НАПРАВЛЕНИЙ — те, к кому вы можете обратиться по любым вопросам:\n\
<b><i>Режиссёры</i></b>: Анастасия Переверзева\n\
<b><i>Организаторы, художники по костюмам, сценографы</i></b>: Олеся Крыжановская\n\
<b><i>Дизайнеры афиш и постов соцсетей</i></b>: Алина Шушкова\n\
<b><i>СММ</i></b>: Дарья Гостева\n\
<b><i>Куратор актёров</i></b>: Ася Панина\n\
<b><i>Куратор Командообразования</i></b>: Иван Зазулин"


file_path = 'file.xlsx'
data = pd.read_excel(file_path)
content_plan = []


for i in range(len(data['name'])):
    content_plan.append([str(data['date'][i]), str(data['name'][i]), str(data['text'][i]), str(data['picture'][i])])
