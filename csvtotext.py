import csv
from cleantext import clean
inputfile = csv.reader(open('womensucks.csv','r',encoding='utf-8'))

i=1006



for row in inputfile:
    if (i > 0 and i < i+1):
        place = row[3].replace(' ,',',')
        place = clean(place, no_emoji=True)
        print(place)
        open('placelist'+str(i)+'.txt','w').write(place+'\n')
    i+=1