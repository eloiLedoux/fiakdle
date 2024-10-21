import json
from pyairtable import Api
from pyairtable.formulas import *

with open('config.json', 'r') as cfg:
  configs = json.load(cfg)

API_KEY        = configs["API_KEY"]
FIAKS_BASE_ID  = configs["FIAKS_BASE_ID"]
FIAKS_TABLE_ID = configs["FIAKS_TABLE_ID"]

api      = Api(API_KEY)
table    = api.table(FIAKS_BASE_ID, FIAKS_TABLE_ID)
nb_fiaks = len(table.all())

with open('shared_info.json', 'r') as shinfo:
  shared_data = json.load(shinfo)

nb_data_bdd    = shared_data["nb_data_in_base"]
update_version = shared_data["update_version"]

RENDU = ""
for id in range(nb_data_bdd, nb_fiaks+1):
  field        = "id"
  value        = id 
  formula      = match({field: value})
  json_data    = table.all(formula = formula)[0]
  json_element = json_data["fields"]

  JOJO_BUG = 'Jojo\'s Bizarre Adventure;jojo;jojosbizarreadventure;jojobizarreadventure;jjba;jojonokimyounabouken;stoneocean'
  JOJO_SQL = 'Jojo\'\'s Bizarre Adventure;jojo;jojosbizarreadventure;jojobizarreadventure;jjba;jojonokimyounabouken;stoneocean'

  print(json_element['nom_manga'])

  ID        = json_element['id']
  IMAGE_ID  = json_element['image_id']
  IMAGE_URL = json_element['image_url']
  NOM_PERSO = json_element['nom_perso']
  NOM_MANGA = JOJO_SQL if json_element['nom_manga'] == JOJO_BUG else json_element['nom_manga']
  #NOM_MANGA = json_element['nom_manga']
  ZOOM      = json_element['zoom']

  TEMPLATE = (f"INSERT INTO FIAK(IMAGE_ID, IMAGE_URL, NOM_PERSO, NOM_MANGA, ZOOM)\n"
  +f"VALUES ('{IMAGE_ID}', '{IMAGE_URL}',\n"
  +f"	'{NOM_PERSO}', '{NOM_MANGA}',\n"
  +f"	'{ZOOM}');\n"
  +f"\n")

  RENDU += TEMPLATE
  #print(RENDU)

filename = f"update_{update_version}.sql"
with open(filename, 'w') as f:
    print(RENDU, file=f)

shared_data["nb_data_in_base"] = nb_fiaks+1
shared_data["update_version"]  = update_version+1
with open('shared_info.json', 'w') as f:
    f.write(json.dumps(shared_data))