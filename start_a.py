# -*- coding: utf-8 -*-
import time; import requests; import matplotlib.pyplot as plt; import pandas as pd; from math import pi
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

grader = 90; maalinger = 12; deviation = 0.1
m_g = grader / maalinger
full_deg_mes = int(360 / m_g)
firstrun = 0
api_key = "IHKIXT6UK0F8STZC"
channel = "645235"
res = "results=13"

def urget(ch, api, rs="results=30"):
    url = 'https://api.thingspeak.com/channels/'+ str(ch) +'/feeds.json?api_key='+ str(api) + '&' + str(rs)
    r = requests.get(url)
    return r.json()

def graphic(df):
    # number of variable
    categories=list(df)[1:]
    N = len(categories)
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)
    ax.clear()
    ax = plt.subplot(111, polar=True)
    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[0:48], categories, color="red", size=5)
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([20,50,100,200], ["20cm","50cm","100cm","200cm"], color="blue", size=6)
    plt.ylim(0,250)
    # Ind1
    values=df.loc[0].drop('group').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Current")
    ax.fill(angles, values, 'b', alpha=0.1)
    # Ind2
    values=df.loc[1].drop('group').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Average")
    ax.fill(angles, values, 'r', alpha=0.1)
    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    plt.savefig('foo.png', bbox_inches='tight', dpi=150)

def data_struc():
    list_n = run_s()
    nd = pd.DataFrame({'group': [1, 1]})
    global firstrun
    global df
    #global speak
    for a in range(full_deg_mes):
        if a <= 1 or a < 13:
            number = int(list_n[a])
            s1 = pd.Series([number, 1], name=a*7.5)
        else:
            s1 = pd.Series([1, 1], name=a*7.5)
        nd = pd.concat([nd, s1], axis=1)   
    if firstrun == 1:
        cha_msg = "Alert, deviation detected at, "
        setalert = 0
        for column in nd:
            updev = 1 + deviation
            lowdev = 1 - deviation
            cur_val = nd[column][0]#df1.ix[:,1]
            old_avg = df[column][1]
            if cur_val * updev < old_avg or cur_val * lowdev > old_avg:
                setalert = 1
                cha_msg = cha_msg + str(column) + ", "
            avg_five = old_avg * 4 + cur_val; avg_five = float(avg_five) / 5
            df[column][1] = avg_five; df[column][0] = cur_val
        cha_msg = cha_msg, "degrees!"
        if setalert == 1:
            speak.Speak(cha_msg)
            print(cha_msg)
    else:
        df = nd
        for column in nd:
            df[column][1] = nd[column][0]; df[column][0] = nd[column][0]  
    firstrun = 1
    graphic(df)       

topr = urget(channel, api_key, res)        
def run_s(topr=topr):
    newlist = []
    for a in topr['feeds']:
        distance = float(a['field1'])
        distance = int(distance)
        newlist.append(distance)
    return newlist

while True:
    time.sleep(9)
    data_struc()