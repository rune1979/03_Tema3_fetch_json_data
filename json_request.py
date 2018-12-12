# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 07:56:01 2018

@author: Rune
"""
import matplotlib.pyplot as plt
import json
import requests
import numpy as np


def urget2(ch, api, rs="results=20"):
    url = 'https://api.thingspeak.com/channels/'+ str(ch) +'/feeds.json?api_key='+ str(api) + '&' + str(rs)
    r = requests.get(url)
    print("Status: ", r.status_code)
    return r.json()

def urget(ch, api, rs="results=30"):
    url = 'https://api.thingspeak.com/channels/'+ str(ch) +'/feeds.json?api_key='+ str(api) + '&' + str(rs)
    r = requests.get(url)
    print("Status: ", r.status_code)
    return r.json()

def savefile(filname, todump):
    with open(filname, 'w') as towrite:
        json.dump(todump, towrite, indent=4)
        
def openfile(filname):
    with open(filname, 'r') as toread:
        return json.load(toread)

#3(a): Hent de nyeste 10 målinger og gem dem i en dictionary. Gem derefter dictionary’en i en JSON fil (bestem selv navnet)

def ca():
    res = urget("results=30")
    savefile('import json/mynewdump30.json', res)
    
#
#3(b): Hent alle målinger mellem 16/11-2018 kl.9:00 og 17/11-2018 kl.9:00 og gem dem i en dictionary og gem denne dictionary i en JSON fil (bestem selv navnet).
#
def cb():
    res = urget("start=2018-11-16%2009:00:00&end=2018-11-16%2013:00:00")
    savefile('import json/mynewdump_datesorted2.json', res)

#3(c): Plot målingerne fra opgave 3(a) i et linjediagram
#
def cc(myload):
    #myload = openfile("import json/mynewdump.json")
    vallist = []; tidlist = []
    for a in myload["feeds"]:
        vallist.append(float(a["field2"]))
        tid = a["created_at"]; tid = tid.split('T', 1); tid = tid[1]
        tidlist.append(tid)

    plt.plot(tidlist, vallist, 5)
    plt.title('10 Målinger'); plt.xlabel('Tid'); plt.ylabel("Måling")
    plt.show()
    
#3(d): Plot målingerne fra opgave 3(b) i et linjediagram
#
def cd(myload):
    myload = openfile("import json/mynewdump_datesorted.json")
    vallist = []; tidlist = []
    for a in myload["feeds"]:
        short = round(float(a["field2"]), 2)
        vallist.append(short)
        tid = a["created_at"]; #tid = tid.split('T', 1); tid = tid[1]
        tidlist.append(tid)

    plt.plot(tidlist, vallist)
    plt.title('Et Døgn'); plt.xlabel('Tid'); plt.ylabel("Måling")
    plt.show()

#3(e): Beregn gennemsnitstemperaturen fra målingerne i opgave 3(a)
#
def ce(fil="import json/mynewdump30.json"):
    myload = openfile(fil) # GETTING 30 RESULTS
    vallist = []; tidlist = []; avglist = []; avgtemp = 0; acum = 0; counter = 0 
    for a in myload["feeds"]:
        temp = round(float(a["field2"]), 2); counter +=1
        acum = acum + temp
        avgtemp = acum/counter
        avglist.append(round(avgtemp, 2))
        vallist.append(float(a["field2"]))
        tid = a["created_at"]; tid = tid.split('T', 1); tid = tid[1]
        tidlist.append(tid)
    print("GENNEMSNIT OVER ALLE ITERATIONER:" + str(round(avgtemp, 2)))
    plt.plot(tidlist, vallist, tidlist, avglist)
    plt.title('30 Målinger'); plt.xlabel('Tid'); plt.ylabel("Måling")
    plt.show()
#3(f): Beregn gennemsnitstemperaturen fra målingerne i opgave 3(b)
#
def cf():
    ce("import json/mynewdump_datesorted2.json")
        
#3(g): Hvad sker hvis du prøver at downloade data fra en kanal som ikke findes/er tilgængelig
#
def cg():
    url = 'https://api.thingspeak.com/channels/9jd78552s622826hh3/feeds.json?results=30'
    r = requests.get(url)
    print("Status: ", r.status_code)
    print(r.json())

#3(h): Lav et program som beder brugeren om et antal målinger (max. 8000) fra kanal 9. Programmet skal gemme målingerne i en dictionary og lave to plots/diagrammer: Et over temperatur og et over lysniveau.
def ch():
    inp = input("Hvor mange målinger vil du have? (max. 8000): ")
    retj = urget("results=" + str(inp)); retj = retj["feeds"]; fulllist = []
    #myarr = np.zeros((int(inp),3))#print(retj)
    print(retj)
    for a in retj:
        fulllist.append([int(a["field1"]), float(a["field2"]), a["created_at"]])
        print(a)
        #myarr = np.append([[int(a["field1"])], [float(a["field2"])], [a["created_at"]]], axis=0)
    tubber = tuple(fulllist)
    print(tubber[:])
        
        
    
    


func_dict = {"3a":ca,"3b":cb,"3c":cc,"3d":cd,"3e":ce,"3f":cf,"3g":cg,"3h":ch}
if __name__ == "__main__":
    command = input("Hvilken opgave skal køres?: ")
    #command = input(">")
    func_dict[command]()
