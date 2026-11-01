import requests
import pandas as pd

# MARK: - Étape 1
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

# MARK: - Étape 2
#region Etape 2
#création d'un tableau
donnees = reponse.json()
df_session = pd.DataFrame(donnees)
print(df_session)
#endregion

# MARK: - Étape 3
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

# MARK: - Étape 4
#region Etape 4
print(tours["lap_duration"].min())
index_pole = tours["lap_duration"].idxmin()
print(index_pole)
tour_pole = tours.loc[index_pole]
print(tour_pole)

#endregion

# MARK: - Étape 5
#region Etape 5
numero_pilote = tour_pole["driver_number"]
params_pilote = {
    'session_key' : session_key,
    'driver_number' : numero_pilote
}

reponse_pilote = requests.get("https://api.openf1.org/v1/drivers", params=params_pilote)
donnees_pilote = reponse_pilote.json()
df_pilote = pd.DataFrame(donnees_pilote)

print(df_pilote["full_name"].iloc[0])
print(df_pilote["team_name"].iloc[0])




#endregion


