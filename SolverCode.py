import requests
import base64
import hashlib

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

URL = "http://192.168.0.222:8000" 


def opdracht1():

    opdracht =  {
            "nr1"   :   "Eerste regel",
            "nr2"   :   "Tweede regel",
            "nr3"   :   "Derde regel"
        }

    x = requests.post(URL + "/opdracht2", json=opdracht)

    print(x.text)



def opdracht2():

    my_string = "opdracht 3"
    my_bytes = bytearray(my_string, "utf-8")

    x = requests.post(URL + "/opdracht3/" + my_bytes.hex())

    result = x.text
    print(result)



def opdracht3():

    my_string = "opdracht 4 lijkt heel erg op opdracht 3"
    my_bytes = my_string.encode("utf-8")

    x = requests.post(URL + "/opdracht4/" + base64.b64encode(my_bytes).decode("utf-8"))

    result = x.text
    print(result)


def opdracht4():

    input = 'Dit is een testbestand voor opdracht 4!'
    hash = hashlib.sha512( str( input ).encode("utf-8") ).hexdigest()

    sha512 =   {
            "sha512"   :   hash
        }

    x = requests.post(URL + "/opdracht5", json=sha512)

    print(x.text)


def opdracht5():
    md5 =   {
        "relatieve_url" : "/static/opdracht5/applicatie_george.exe"
    }

    x = requests.post(URL + "/opdracht6", json=md5)

    print(x.text)



def opdracht6():
    data = b'Geheim bericht bestemd voor de docenten IoT aan de KdG'
    key = get_random_bytes(32)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    x = requests.post(URL + "/opdracht7", json={"bericht_versleuteld": ciphertext.hex(), "sleutel": key.hex(), "nonce": cipher.nonce.hex()})

    result = x.text
    print(result)




def main():
    opdracht1()
    opdracht2()
    opdracht3()
    opdracht4()
    opdracht5()
    opdracht6()

if __name__ == "__main__":
    main()