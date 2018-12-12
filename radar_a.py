# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:21:27 2018

@author: Rune
"""
import start as s
import time
import random
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

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


# Set data
grader = 90
maalinger = 12
deviation = 0.1
#startdisp = 315
m_g = grader / maalinger
full_deg_mes = int(360 / m_g)
oldstamp = "kk"
while True:
    time.sleep(9)
    list_n, timest = s.run_s()
    #print(timest, "new")
    #print(oldstamp, "old")
    #if oldstamp != timest:
        #print(timest)
        
        #print(oldstamp)
    nd = pd.DataFrame({'group': [1, 1]})
    try:
        test = list_one
        firstrun = 0
    except:
        list_one = []
        list_avg = []
        firstrun = 1
    
        print(firstrun)
    
    for a in range(full_deg_mes):
        #rand_n = random.randint(20,250)
        if a <= 1 or a < 13:
            #avg = 
            number = int(list_n[a])
            s1 = pd.Series([number, 1], name=a*7.5)
        else:
            s1 = pd.Series([1, 1], name=a*7.5)
            
        nd = pd.concat([nd, s1], axis=1)
    
    if firstrun == 1:
        df = nd
        #graphic(df)
    else:
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
            print(cha_msg)
            #speak.Speak(cha_msg) 

    graphic(df)
    
    
#    ax.clear()
#    categories=list(df)[1:]
#    N = len(categories)
#    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
#    angles = [n / float(N) * 2 * pi for n in range(N)]
#    angles += angles[:1]
#    # Initialise the spider plot
#    ax = plt.subplot(111, polar=True)
#    # If you want the first axis to be on top:
#    ax.set_theta_offset(pi / 2)
#    ax.set_theta_direction(-1)
#    # Draw one axe per variable + add labels labels yet
#    plt.xticks(angles[0:48], categories, color="red", size=5)
#    # Draw ylabels
#    ax.set_rlabel_position(0)
#    plt.yticks([20,50,100,200], ["20cm","50cm","100cm","200cm"], color="blue", size=6)
#    plt.ylim(0,250)
#    # Ind1
#    values=df.loc[0].drop('group').values.flatten().tolist()
#    values += values[:1]
#    
#    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Current")
#    ax.fill(angles, values, 'b', alpha=0.1)
#    # Ind2
#    values=df.loc[1].drop('group').values.flatten().tolist()
#    values += values[:1]
#    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Average")
#    ax.fill(angles, values, 'r', alpha=0.1)
#    # Add legend
#    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
#    plt.savefig('foo.png', bbox_inches='tight', dpi=150)
        #print("tetst")
        #oldstamp = timest
    
