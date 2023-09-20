from faker import Faker

import json        
   
from random import randint    

fake = Faker()

def input_data(x):

    ip_data ={}

    for i in range(0, x):
        ip_data[i]={}
        ip_data[i]['IPv4']= fake.ipv4()
    print(ip_data)

    with open('ipv4List.json', 'w') as fp:
        json.dump(ip_data, fp)

     
def main():

    number_of_ips = 5000
    input_data(number_of_ips)
main()
