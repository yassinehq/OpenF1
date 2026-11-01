import requests
import pandas as pd

#region Etape 1
#récupérer les infos de Monza 2024
params = {
    "year" : 2024,
    "country_name" : 'Italy',
    "location" : 'Monza',
    "session_name" : 'Qualifying'
}
reponse = requests.get("https://api.openf1.org/v1/sessions", params=params)
print(reponse.status_code)
#endregion

#region Etape 2
#création d'un tableau
donnees = reponse.json()
df_session = pd.DataFrame(donnees)
print(df_session)
#endregion

#region Etape 3
#récupérer tous les tours
session_key = df_session["session_key"].iloc[0]
params_sk = {
    'session_key' : session_key
}

reponse_tours = requests.get("https://api.openf1.org/v1/laps", params=params_sk)
donnees_tours = reponse_tours.json()
tours = pd.DataFrame(donnees_tours)
print(len(tours))
print(tours.columns)

#endregion


