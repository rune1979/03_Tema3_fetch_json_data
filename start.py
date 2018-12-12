# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:45:40 2018

@author: Rune
"""
#import json_request as a
import time
import requests
#GET https://api.thingspeak.com/channels/638714/feeds.json?api_key=SHM8B3NMWV23AQHZ&results=2
#channel = "638714"
#api_key = "SHM8B3NMWV23AQHZ"
def urget(ch, api, rs="results=30"):
    url = 'https://api.thingspeak.com/channels/'+ str(ch) +'/feeds.json?api_key='+ str(api) + '&' + str(rs)
    r = requests.get(url)
    print("Status: ", r.status_code)
    return r.json()

#API KEY: ANJWFUJKQ85EI4NR
#Channel: 633219
#Field2: Data
#Field3: Grader
#Field4: DATO
global lasttime
api_key = "IHKIXT6UK0F8STZC"
channel = "645235"
degree = 90
#url = "https://thingspeak.com/channels/437741/feed.json"
action = 'live' # test or live
#if action == 'test':
#    topr = a.urget(channel, api_key, "results=130")
#if action == 'live':
topr = urget(channel, api_key, "results=13")

def run_s(action=action, topr=topr):
    if action == 'test':
        inputs_check = []
        begining = []
        global checklist
        for a in topr['feeds']:
            time_st = a['created_at']
            deg = a['field2']
            distance = float(a['field1'])
            distance = int(distance)
            uid = a['entry_id']
            if deg == '0' and uid not in begining:
                begining.append(uid) 
                zero_found = 1
        for i in begining:
            if i not in checklist:
                checklist.append(i)
                for a in topr['feeds']:
                    time_st = a['created_at']
                    deg = a['field2']
                    distance = float(a['field1'])
                    distance = int(distance)
                    uid = a['entry_id']
                    
        
                
        #print(b)
    elif action == "live":
        newlist = []
        
        for a in topr['feeds']:
            
            newtime = a['created_at']
            deg = a['field2']
            #print(deg)
            distance = float(a['field1'])
            distance = int(distance)
            newlist.append(distance)
        return newlist, newtime
#        try:
#            if newtime == lasttime:
#                #return 'non'
#                return newlist
#            
#            else:
#                lasttime = newtime
#                return newlist 
#                
#                               
#        except:
#            lasttime = newtime 
        
        #topr = a.urget(channel, api_key, "results=13")
    
#list_n, timest = run_s()
#print(timest)
#print(list_n)
   
if action == 'test':
    begining = run_s(action, topr)
    #for a in sorted(begining, reverse=True):
    #print(begining)
    for a in begining:
        #print(a, "a-loop")
        for b in topr['feeds']:
            uid = b['entry_id']
            #print(uid, "b-loop")
            if uid >= a and uid <= a + 12:
                print(b['field2'], b['field1'], b['created_at'])
                
                #print(b['field1'])
                #print(b['entry_id'])                 
                
#topr = a.urget(channel, api_key)
#print(topr)
#a = 'feeds'
#for a in topr.keys():
#    print(a)
#print(topr['feeds'])
#for key, value in topr.items() :
 #   print(key, value)
#print(topr('feeds'))
#a.savefile("datapull.json", topr)
#top = a.openfile("datapull.json")
#a.cc(top)