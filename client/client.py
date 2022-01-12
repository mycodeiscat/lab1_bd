import requests
import sys
import functools


IP = sys.argv[1]
PORT = sys.argv[2]

r = requests.get('http://'+IP+':'+PORT+'/text.txt')

text_path = '/clientdata/text.txt'

open(text_path, 'wb').write(r.content)

checksum = r.headers['checksum']

def checksum256(st):
    return functools.reduce(lambda x,y:x+y, map(ord, st)) % 256

with open(text_path, 'r') as file:
    data = file.read()
    if checksum256(data) == int(checksum):
        print('Succesfully verified')
    else:
        print('Error occured')
        exit()
        
while True:
    pass
