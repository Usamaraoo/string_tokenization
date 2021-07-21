import requests
import psycopg2
import csv
import json

lahore_address =[]
with open('address_with_city.csv') as c:
    reader = csv.reader(c,delimiter=',',)
    for i in reader:
        lahore_address.append(i[0].replace("&","").replace("(","").replace(")","").replace("'",""))

try:
    file = open('bulk_searched_address.txt','a')

    for i in range(500):

        data ={
            "pick_city":"Lahore",
            "pick_address":f"""{lahore_address[i]}""",
            "drop_city": "Lahore",
            "drop_address": f"""{lahore_address[i]}""",

        }
        print('Searched Address: ',lahore_address[i])
        file.write('Searched Address: '+lahore_address[i]+"\n")
        r = requests.post("http://127.0.0.1:8000/label/", json=data, headers={
            "Authorization": "api-key pbkdf2_sha256$216000$PxstaVQEkCXN$e5Lm84WmJjtmipKSg0QUilyVO7m2PcmpTv/Fk7QXzec="})
        # print(r.json())
        print('Address returned')
        file.write('Address Returned'+"\n")
        for i in r.json():
            print(i)
            file.write(i+'\n')

        print("Response Time: ",r.elapsed.total_seconds()* 1000,"ms")
        file.write('\n')
        file.write("Response Time: "+str(r.elapsed.total_seconds()* 1000)+"ms"+"\n")
        print('=================END======================')
        file.write('=================END======================'+"\n")
    file.close()
except requests.HTTPError:
    print(requests.HTTPError)
