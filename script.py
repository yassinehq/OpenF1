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

