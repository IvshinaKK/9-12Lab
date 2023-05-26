from PIL import Image
import os
from pathlib import Path
def z_1(n):
    f=os.listdir()
    Path('FF').mkdir(parents=True, exist_ok=True)
    print(f)
    for i in f:
        with Image.open(i) as im:
            im.load()
        imm = im.convert('L')
        imm.save(Path("FF", i))
    return ''
def z_2(n):
    f=os.listdir()
    Path('FF').mkdir(parents=True, exist_ok=True)
    print(f)
    for i in f:
        if i.find('.jpg')>0 or i.find('.png')>0:
            with Image.open(i) as im:
                im.load()
                imm = im.convert('L')
                imm.save(Path("FF", i))
    return ''
import csv
def z_3(n):
    with open('data.csv', 'r') as f:
        r = csv.reader(f, delimiter=',')
        print(r)
        s=0
        for row in r:
            print(row[0],"-", row[1], "шт. за", row[2], "руб")
            s=s+int(row[2])*int(row[1])
    print('Итоговая сумма:', s)
    return ''
z_1(" ")
z_2(" ")
z_3(" ")