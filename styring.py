# -*- coding: utf-8 -*-
"""

"""
import pygame
import os
from time import sleep
import socket

host = "192.168.43.77"
port = 3002
skt = socket.socket()
skt.connect((host,port))

def sokkerne():
    """Denne funktion blive kørt hver gang der bliver foretaget et godtaget tastetryk. 
    Funktionen sender 'kører variablerne' til hovedprogammet på Raspberry pi"""
    global turnON
    global forward
    global back
    global left
    global right
    
    #Den næste kommando sammensætter en fælles string over alle variablerne    
    dataListe = str(turnON) + str("-") + str(forward) + str("-") + str(back) + str("-") + str(left) + str("-") + str(right)
    BdataListe = dataListe.encode("UTF-8")
    skt.sendall(BdataListe)

turnON = 0 #Variabel for forvidt motoren er tændt
forward = 0 #Variabel for forvidt piRobert kører frem
back = 0 #Variabel for forvidt piRobert kører tilbage
left = 0 #Variabel for forvidt piRobert drejer til venstre
right = 0 #Variabel for forvidt piRobert drejer til højre
styringLoop = True

pygame.init()
screen = pygame.display.set_mode((600,200))

#Clear skærmen
os.system('cls' if os.name == 'nt' else 'clear')

#Hovedloop til at lytte efter tastetryk 
while styringLoop == True:
    #Starter for motoren ved at trykke på t. Resten af loopet er afhænget af at motoren er startet
    sleep(0.2)
    pygame.display.set_caption("Styringsenhed til piRobert - Motoren er slukket. Tryk på 't' for at starte den")
    ONOFF = pygame.event.get()
    for event in ONOFF:
        #Starter styringsloppet hvis man trykker t
        if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            if turnON == 0:
                turnON = 1
                print("Motoren er startet")
                #sokkerne()
        #Lukker programmet hvis den ikke er tændt (turON == 0)
        if event.type == pygame.QUIT:
                styringLoop = False
                break
                
    #Selve styrigen. Venter på at motoren er startet ved at trykke på det
    while turnON == 1:
        sleep(0.05)
        pygame.display.set_caption("Styringsenhed til piRobert - Motoren er tændt")
        events = pygame.event.get()
        for event in events:
            #Hvis man trykker exit
            if event.type == pygame.QUIT:
                turnON = 0
                #sokkerne()
                styringLoop = False
                break
            #Forward hvor den kontrollerer om den kører tilbage /Hvis den gør, skal den ikke gøre noget
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                if back == 0:
                    forward = 1
                    sokkerne()
            if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                forward = 0
                sokkerne()
            #Left
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                left = 1
                sokkerne()
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                left = 0
                sokkerne()
            #Right
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                right = 1
                sokkerne()
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                right = 0
                sokkerne()
            #Back hvor den kontrollerer om den kører frem /Hvis den gør, skal den ikke gøre noget
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                if forward == 0:
                    back = 1
                    sokkerne()
            if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                back = 0
                sokkerne()
                
            #Sluk for motoren ved at trykke på t
            if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                turnON = 0
                forward = 0
                back = 0
                left = 0
                right = 0
                
                sokkerne()
                break
            
            #Print status i konsol
            os.system('cls' if os.name == 'nt' else 'clear') #Clear consollen
            if forward == 1:
                print("\nPiRobert kører frem")
            if left == 1:
                print("\nPiRobert drejer til venstre")
            if right == 1:
                print("\nPiRobert drejer til højre")
            if back == 1:
                print("\nPiRobert kører tilbage")
    
    pygame.display.flip()
