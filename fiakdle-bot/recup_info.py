import json

def requete_data():
    with open('data.json', 'r') as cfg:
        data = json.load(cfg)
    if data == {}:
        return -1
    return data

if __name__ == "__main__":
    data = requete_data()
    print(data)