import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

webpage = requests.get(f'https://www.scrapethissite.com/pages/forms/').text
soup = BeautifulSoup(webpage, 'lxml')
players = soup.find_all('tr')[1:]
#print(players)
name= []
year = []
wins = []
losses = []
ot_losses = []
win_perc = []
goals_for = []
goals_against = []
plus_minus = []

for i in players:
    name.append(i.find_all('td')[0].text.strip())
    year.append(i.find_all('td')[1].text.strip())
    wins.append(i.find_all('td')[2].text.strip())
    losses.append(i.find_all('td')[3].text.strip())
    ot_losses.append(i.find_all('td')[4].text.strip())
    win_perc.append(i.find_all('td')[5].text.strip())
    goals_for.append(i.find_all('td')[6].text.strip())
    goals_against.append(i.find_all('td')[7].text.strip())
    plus_minus.append(i.find_all('td')[8].text.strip())
    
data = pd.DataFrame({"Team Name":name,
                     "Year":year,
                     "Wins":wins,
                     "Losses":losses,
                     "OT Losses":ot_losses,
                     "Win %":win_perc,
                     "Goals For":goals_for,
                     "Goals Against":goals_against,
                     "+/-":plus_minus
                     })

st.table(data)