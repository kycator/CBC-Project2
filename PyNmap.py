

# LIBRARIES
from datetime import date
import os
import pickle
import json
import subprocess

# SET VARIABLES
my_dir = '/home/kali/Downloads/LogonID'
my_pickle = '/home/kali/Downloads/data.pickle'
my_json = '/home/kali/Downloads/data.json'
port_list = ['10.0.2.1:80', '10.0.2.1:23', '10.0.2.1:22']
nmap_path = '/usr/bin/nmap'
nmap_network = '10.0.2.0/24'

def create_directory():   
    if(os.path.isdir(my_dir)) == False:
        try:  
            os.mkdir(my_dir)
            print ("INFO: The directory was created:", my_dir) 
        except OSError:  
            print ("ERROR: Failed to create directory:", my_dir)
    else:
        print ("INFO: The directory already exists:", my_dir) 
        
def create_date_string():
    date_str = date.today().strftime("%m%d%y")
    return date_str

def write_files():
    # write the pickle file
    with open(my_pickle, 'wb') as fp:
        pickle.dump(port_list, fp)
    fp.close()
    
    # write the json file
    with open(my_json, 'w') as fp:  
        json.dump(port_list, fp)
    fp.close()

def read_files():
    port_list = []
    
    # read the pickle file
    with open (my_pickle, 'rb') as fp:
        port_list = pickle.load(fp)
    fp.close()
    
    print("pickle:", port_list)
    
    port_list = []
    
    # read the json file
    with open(my_json, 'r') as fp:  
        port_list = json.load(fp)
    fp.close()
    
    print("json:", port_list)

def run_nmap():
    nmap_out = subprocess.run([nmap_path, "-T4", nmap_network], capture_output=True)
    nmap_data = nmap_out.stdout.splitlines() 
    return nmap_data
   
    
create_directory()
create_date_string()
write_files()
read_files()
run_nmap()

print(create_date_string())












