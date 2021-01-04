import os
from os import path
import glob
import requests

key = "WEETTERSYEETTERS"
load_url = "http://137.74.119.216/apis/soundboard_api.php"
resp = requests.get(load_url+"?key="+key)
data = resp.json()


def checkAPI():
    if resp.status_code == 200:
        print("API-version: "+data['version'])
        print("Checking for commands")
        if data['forcereload'] == True:
            print("    Reloading all sound files!")

        os.makedirs('data/categories/',exist_ok=True)
    
        print("Checking for missing files...")
        for i in data['categories']:
            if not path.exists('data/categories/'+i):
                print("    Creating missing category: "+str(i))
                os.mkdir('data/categories/'+i)
                
            print("    Checking sound files for "+str(i))

            filenames = os.listdir('data/categories/'+i+'.')
            
            for s in data['categories'][i]:
                if not s in filenames or data['forcereload'] == True:
                    print("        Downloading file: "+s)
                    r = requests.get(data['soundstorage']+i+"/"+s)
                    open("data/categories/"+i+"/"+s, 'wb').write(r.content)
        print("Done!")
        return True
   
    elif resp.status_code == 404:
        return False


