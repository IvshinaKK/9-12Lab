import json
def z1(q):
    with open ("1.json", "r", encoding='utf-8') as read_file:
        slov=json.load(read_file)
    print(slov)
    print(slov["products"][0]['name'])
    n=len(slov["products"])
    np={"Продукты":[ {"Название":0,"Цена":0,"Вес":0,"В наличии":0},{"Название":0,"Цена":0,"Вес":0,"В наличии":0},{"Название":0,"Цена":0,"Вес":0,"В наличии":0}]}
    for i in range(n):
        for key in slov["products"][i]:
            if key == 'name':
                np["Продукты"][i]["Название"]=slov["products"][i][key]
            elif key=='price':
                np["Продукты"][i]["Цена"] = slov["products"][i][key]
            elif key =='weight':
                np["Продукты"][i]["Вес"] = slov["products"][i][key]
            elif slov["products"][i][key]==0:
                np["Продукты"][i]["В наличии"] = "нет"
            else:
                np["Продукты"][i]["В наличии"] = "присутствует"
    print(np)
    with open ("1.json", "w") as file:
        json.dump(np, file, ensure_ascii=False)
    return ""
def z2(q):
    with open ("1.json", "r", encoding='utf-8') as read_file:
        slov=json.load(read_file)
    print(slov)
    print(slov["products"][0]['name'])
    n=len(slov["products"])
    np={"Продукты":[ {"Название":0,"Цена":0,"Вес":0,"В наличии":0},{"Название":0,"Цена":0,"Вес":0,"В наличии":0},{"Название":0,"Цена":0,"Вес":0,"В наличии":0}]}
    for i in range(n):
        for key in slov["products"][i]:
            if key == 'name':
                np["Продукты"][i]["Название"]=slov["products"][i][key]
            elif key=='price':
                np["Продукты"][i]["Цена"] = slov["products"][i][key]
            elif key =='weight':
                np["Продукты"][i]["Вес"] = slov["products"][i][key]
            elif slov["products"][i][key]==0:
                np["Продукты"][i]["В наличии"] = "нет"
            else:
                np["Продукты"][i]["В наличии"] = "присутствует"
    print(np)
    a=input("Желаете добавить новый продукт? ")
    while a=='yes':
        np["Продукты"].append({"Название":0,"Цена":0,"Вес":0,"В наличии":0})
        n = len(np["Продукты"])
        m=input("Введите название продукта: ")
        np["Продукты"][n-1]["Название"]=m
        m = int(input("Введите стоимость продукта: "))
        np["Продукты"][n - 1]["Цена"] = m
        m = int(input("Введите вес продукта: "))
        np["Продукты"][n - 1]["Вес"] = m
        m = input("Продукт есть в наличии?: ")
        np["Продукты"][n - 1]["В наличии"] = m
        a = input("Желаете добавить новый продукт? ")
    print(np)
    with open ("1.json", "w") as file:
       json.dump(np, file, ensure_ascii=False)
    return ""
def z3(q):
    sl={}
    with open ("en-ru.txt", "r", encoding='utf-8') as file:
        while True:
            n=file.readline()
            n=n.rstrip()
            if not n:
                break
            n=n.split('-')
            c=n[len(n)-1].split(',')
            for i in range(len(c)):
                c[i]=c[i].lstrip()
                sl[c[i]]=n[0]
    sl=dict(sorted(sl.items()))
    print(sl)
    f = open('ru-en.txt', 'wt')
    f.write(str(sl))
    f.close()
    return ""
z1(' ')
z2(' ')
z3(' ')