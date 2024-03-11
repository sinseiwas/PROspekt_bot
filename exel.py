import pandas as pd


file_path = 'file.xlsx'
data = pd.read_excel(file_path)
content_plan = []


for i in range(len(data['name'])):
    content_plan.append([str(data['date'][i]), str(data['name'][i]), str(data['text'][i]), str(data['picture'][i])])
