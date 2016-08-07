#!/usr/bin/python2.6
# -*- coding : utf-8 -*
# Ecrivez un programe qui convertisse en metres par seconde et en km/h une vitesse 
# fourni par l'utilisateur
vitesse = raw_input("fournisser une vitesse en miles/heure :")
vitesse = float(vitesse)
vitesse_m_seconde = (vitesse * 1609) / 3600
vitesse_km_h = vitesse * 1.609 

print ("la vitesse en metres par seconde est: ",vitesse_m_seconde, "m/s")
print ("la vitesse en Kilometres par heure est: ",vitesse_km_h, "km/h")

