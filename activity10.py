from getpass import getpass

username = "gerald"
password = "gnmancia21"

u = input("USERNAME --> ")
p = getpass("PASSWORD --> ")
from getpass import getpass

if (u == username) and (p == password) :
        print("Access Granted") 
else:
        print("Access Denied")
