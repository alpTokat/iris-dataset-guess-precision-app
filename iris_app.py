def read():
    dogru = 0
    yanlis = 0
    with open('iris.txt','r',encoding='utf-8')as file:
        line = file.readline()
        while line:
            dogru_yanlis = read_continue(line)
            dogru += dogru_yanlis[0]
            yanlis += dogru_yanlis[1]
            line =  file.readline()
    return dogru,yanlis
def read_continue(line):
    line = line[:-1]
    list = line.split(',')
    sepal_length = list[0]
    sepal_width = list[1]
    petal_length = list[2]
    petal_width = list[3]
    class_ = list[4]
    deger = tahmin_et(float(sepal_length),float(sepal_width),float(petal_length),float(petal_width),class_)
    return deger
    # print(f"{sepal_length},{sepal_width},{petal_length},{petal_width},{class_}") 
def tahmin_et(fsl,fsw,fpl,fpw,class_):
    tahmin = ''
    dogru = 0
    yanlis = 0
    if (fsl >= 4.3 and fsl <= 5.8) and (fsw >= 2.9 and fsw <= 4.4) and (fpl >= 1.0 and fpl <= 2.0) and (fpw >= 0.1 and fpw <= 0.6):
        tahmin = 'Iris-setosa'
    elif (fsl >= 4.9 and fsl <= 7) and (fsw >= 2.0 and fsw <= 3.4) and (fpl >= 3.0 and fpl <= 5.1) and (fpw >= 1.0 and fpw <= 1.7):
        tahmin = 'Iris-versicolor'
    elif (fsl >= 5.7 and fsl <= 7.9) and (fsw >= 2.2 and fsw<= 3.8) and (fpl >= 4.6 and fpl <= 6.9) and (fpw >= 1.4 and fpw <= 3.0):
        tahmin =  'Iris-virginica'

    print(tahmin)
    if tahmin == class_:
        dogru += 1
    else :
        yanlis += 1
    return dogru,yanlis


dogru_yanlis_sayisi=read()
print(f"dogru sayisi: {dogru_yanlis_sayisi[0]}, yanlis sayisi: {dogru_yanlis_sayisi[1]},Basari oraniniz: {(dogru_yanlis_sayisi[0]/ (dogru_yanlis_sayisi[0]+dogru_yanlis_sayisi[1])*100)}")