def mise_en_forme(str):
    reponse = ''.join(str.split()).lower()
    return reponse

if __name__ == "__main__":
    str = "Kimetsu no Yaiba"
    rep = mise_en_forme(str)
    print(rep)