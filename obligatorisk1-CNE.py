# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:53:22 2024

@author: Christer N Elvsaas
"""
###############################################################################
# Obligatorisk oppgaven # 1
# 
# Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, og du ønsker å 
# sammenlikne de årlige kostnadene ved elbil sammenliknet med bensinbil.
# 
# Lag et Python-program som beregner og presenterer (i konsollen) de 
# a) årlige totalkostnadene for elbil og for bensinbil 
#
# b) samt årlig kostnadsdifferanse basert på informasjonen gitt nedenfor. 
# 
# Du kan her for enkelhets skyld se 
# bort fra kostnader som renter på billån og verditap (du har da egentlig 
# antatt at slike kostnader er like for elbil og bensinbil).
# 
#
# Nedenfor er informasjon som programmet skal baseres på 
# 
#
#   Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. 
#   Ev. (hvis du ikke har bil) kan du anta 10.000 km.
#   Forsikring: Elbil: 5000 kr/år. 
#               Bensinbil: 7500 kr/år.
#   Trafikkforsikringsavgift: 8,38 kr/dag (El & Bensin)
#   Drivstoffbruk:
#       Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. 
#       Bensinbil: 1,0 kr/km.
#       Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.
###############################################################################


# Lag oversikt for totalkostnader elbil vs bensinbil

#Variabler-fra-tekstoppgave:
ForsikringElbil = 5000  # kr per år
ForsikringBensinbil = 7500  # kr per år
Trafikkforsikringsavgift = 8.38  # kr per dag for begge biler
Stroempris = 2.00  # kr per kWh
Bensin_pr_km = 1.0  # kr per km for bensinbil
KWH_pr_km = 0.2  # kWh per km for elbil
BomavgiftElbil = 0.1  # kr per km
BomavgiftBensinbil = 0.3  # kr per km
DageriAaret = 365

print("Utregning kostnader knyttet til bruk av Elbil og Bensinbil \n")
# Kjørelengde
Antall_km_kjort = int(input("Oppgi antall kjørte kilometer per år (default er 10.000 km):") or "10000 \n")
print("") #Blank linje

# Felles - beregninger:
print("Felleskostnader begge modeller:") #Skriver feltoverskrift

#Trafikkforsikring
TrafikkforskringPrAar =  Trafikkforsikringsavgift * DageriAaret #Regner ut årsavgift trafikkforskring
print(f"Trafikkforskring pr år begge modeller: {TrafikkforskringPrAar:.2f} kr") #Skriver trafikkforsikring resultatet
print("")#Blank linje

#Forsikringer
print("Forsikringer pr modell:") #Skriver feltoverskrift
print(f"Forsikring Elbil pr år: {ForsikringElbil:.2f} kr") #Skriver variabel for Elbil forsikring
print(f"Forsikring Bensinbil pr år: {ForsikringBensinbil:.2f} kr") #Skriver variabel for Bensinbil forsikring
print("") #Blank linje


# Elbil-kostnader ############################################################

## Drivstoff
print("Kostnader Elbil:")
DrivstoffKostElbil = Antall_km_kjort * (KWH_pr_km * Stroempris) # Regner ut Drivstoffkostnad
print(f"Drivstoffkostnad Elbil pr år: {DrivstoffKostElbil:.2f} kr") #Skriver variabel for Elbil drivstoffkostnad

## Bomkost Elbil
BomKostElbil = Antall_km_kjort * BomavgiftElbil  # Regner ut Bomkostnad Elbil
print(f"Bomkostnad Elbil pr år: {BomKostElbil:.2f} kr") #Skriver variabel for Elbil Bomkostnad

## Årskostnad Elbil
TotalkostElbil = DrivstoffKostElbil + BomKostElbil + TrafikkforskringPrAar + ForsikringElbil
print(f"Totalkostnad Elbil pr år: {TotalkostElbil:.2f} kr \n") #Skriver Totalkostnad Elbil

# Bensinbil-kostnader ########################################################

## Drivstoff
print("Kostnader Bensinbil:")
DrivstoffKostBensinbil = Antall_km_kjort * Bensin_pr_km # Regner ut Drivstoffkostnad
print(f"Drivstoffkostnad Bensinbil pr år: {DrivstoffKostBensinbil:.2f} kr") #Skriver variabel for Bensinbil drivstoffkostnad

## Bomkost Bensinbil
BomKostBensinbil = Antall_km_kjort * BomavgiftBensinbil  # Regner ut Bomkostnad Bensinbil
print(f"Bomkostnad Bensinbil pr år: {BomKostBensinbil:.2f} kr") #Skriver variabel for Bensinbil Bomkostnad

## Årskostnad Bensinbil
TotalkostBensinbil = DrivstoffKostBensinbil + BomKostBensinbil + TrafikkforskringPrAar + ForsikringBensinbil
print(f"Totalkostnad Bensinbil pr år: {TotalkostBensinbil:.2f} kr \n") #Skriver Totalkostnad Bensinbil



#Oppsummering alle kostnader Elbil
print("Elbil:")
print(f"Trafikkforskring: {TrafikkforskringPrAar:.2f} kr") #Skriver trafikkforsikring resultatet
print(f"Forsikring: {ForsikringElbil:.2f} kr") #Skriver variabel for Elbil forsikring
print(f"Drivstoffkostnad: {DrivstoffKostElbil:.2f} kr") #Skriver variabel for Elbil drivstoffkostnad
print(f"Bomkostnader: {BomKostElbil:.2f} kr") #Skriver variabel for Elbil Bomkostnad
print(f"Totalkostnad Elbil pr år: {TotalkostElbil:.2f} kr \n") #Skriver Totalkostnad Elbil

#Oppsummering alle kostnader Bensinbil
print("Bensinbil:")
print(f"Trafikkforskring: {TrafikkforskringPrAar:.2f} kr") #Skriver trafikkforsikring resultatet
print(f"Forsikring: {ForsikringBensinbil:.2f} kr") #Skriver variabel for Bensinbil forsikring
print(f"Drivstoffkostnad: {DrivstoffKostBensinbil:.2f} kr") #Skriver variabel for Bensinbil drivstoffkostnad
print(f"Bomkostnader: {BomKostBensinbil:.2f} kr") #Skriver variabel for Bensinbil Bomkostnad
print(f"Totalkostnad Bensinbil pr år: {TotalkostBensinbil:.2f} kr \n") #Skriver Totalkostnad Bensinbil






# Differanse bensin vs elektrisk
#Differanse = TotalkostBensinbil - TotalkostElbil
#print(f"Differanse mellom Elbilkostnad og Bensinbilkostnad pr år: {Differanse:.2f} kr") #Skriver variabel for Differanse

if TotalkostBensinbil > TotalkostElbil: #Finner ut om Bensin er dyrere enn Elbil
    Differanse = TotalkostBensinbil - TotalkostElbil # Regner ut differanse Bensin - El
    print(f"Det er  {Differanse:.2f} kr dyrere med Bensinbil pr år") #Skriv resultat Bensinbil
else: 
    Differanse = TotalkostElbil - TotalkostBensinbil # Regner ut differanse El - Bensin
    print(f"Det er  {Differanse:.2f} kr dyrere med Elbil pr år") #Skriv resultat Elbil







