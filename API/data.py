import pandas as pd 

data = pd.read_csv('data-production/players_full1.csv')
data = data.set_index('player')

week1 = pd.read_csv('data/combined-predictions/predictions-week1.csv')
week1 = week1.set_index('player')
