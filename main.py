import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('seaborn')

#index_col=0, header=0,
df = pd.read_excel("travels.xlsx")

#Graphing Miles and minutes
values1 = df.plot.bar(x='Miles', y='Minutes', rot=0)

#Label each bar with the exact yaxis number (which is in minutes)
for bar in values1.patches:
    value = bar.get_height()
    text = f'{value}'
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_y() + value
    plt.text(text_x, text_y, text, ha='center',color='r',size=12.5, rotation=80)

#Title the Graph and label each axis
values1.set_title("Jean Dalmont's Travel Log by Time and Miles")
plt.xlabel("Distance Traveled in Miles")
plt.ylabel("Travel Time in Minutes")
plt.xticks(rotation=50)

############Dataset for Miles traveled each day############
data = {'5/25':88.5, '5/26':88, '5/27':88, '5/28':35.1,
        '5/29':83, '5/30':8.6, '5/31':120.9, '6/1':81.1,
        '6/3':22.7, '6/6':5.2, '6/9':62, '6/11':52.4,
        '6/24':57.2, '6/25':62.4, '6/26':8.9, '6/28':62.6,
        '6/30':5.2, '7/1':47.2, '7/2':456,'7/3':9.5}

dates = list(data.keys())
miles = list(data.values())
fig = plt.figure(figsize = (10, 5))
data1 = plt.bar(dates, miles)

#Label each bar with the exact yaxis number (which is in miles)
for bar in data1.patches:
    value = bar.get_height()
    text = f'{value}'
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_y() + value
    plt.text(text_x, text_y, text, ha='center',color='r',size=12.5)

#Title the Graph and label each axis
plt.suptitle("Jean Dalmont's Travel Log of Miles per Day")
plt.xlabel("Travel Date")
plt.ylabel("Miles Traveled")
plt.xticks(rotation=45)
#plt.show()


############Dataset for time spent traveling each day############
data2 = {'5/25/2022': 131.08, '5/26/2022':115.19, '5/27/2022':144.3,
        '5/28/2022':63.23, '5/29/2022':124.24, '5/30/2022':25.08,
        '5/31/2022':208.15,	'6/1/2022':159.2, '6/3/2022':52.48,
        '6/6/2022':16.29, '6/9/2022':109.11, '6/11/2022':97.41,
        '6/24/2022':109.33, '6/25/2022':90.3, '6/26/2022':31.36,
        '6/28/2022':118.09, '6/30/2022':13.28, '7/1/2022':98.3,
        '7/2/2022':492.16,'7/3/2022':23.42}

dates2 = list(data2.keys())
minutes = list(data2.values())
fig = plt.figure(figsize = (10, 5))
data3 = plt.bar(dates, minutes)

#Label each bar with the exact yaxis number (which is in minutes)
for bar in data3.patches:
    value = bar.get_height()
    text = f'{value}'
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_y() + value
    plt.text(text_x, text_y, text, ha='center',color='r',size=12.5)

#Title the Graph and label each axis
plt.suptitle("Jean Dalmont's Travel Log of Minutes per Day")
plt.xlabel("Travel Date")
plt.ylabel("Minutes Spent Traveling")
plt.xticks(rotation=45)
plt.show()
#plt.savefig("image.png")