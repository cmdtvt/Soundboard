import os
from os import path
import glob
import requests
import asyncio

from settings import *


totalDownloads = 0
allDone = False



resp = requests.get(load_url+"?key="+key)
data = resp.json()


print("EXECUXE WAT TA FUG",flush=True)
def checkAPI():
	global totalDownloads
	global allDone
	if resp.status_code == 200:
		print("API-version: "+data['version'],flush=True)
		print("Checking for commands",flush=True)
		if data['forcereload'] == True:
			print("    Reloading all sound files!",flush=True)

		os.makedirs('data/categories/',exist_ok=True)
		
		filesToDownload = []


		print("Checking for missing files...",flush=True)
		for i in data['categories']:
			if not path.exists('data/categories/'+i):
				print("    Creating missing category: "+str(i),flush=True)
				os.mkdir('data/categories/'+i)
				
			print("    Checking sound files for "+str(i),flush=True)

			filenames = os.listdir('data/categories/'+i+'.')
			
			for s in data['categories'][i]:
				if not s in filenames or data['forcereload']:
					filesToDownload.append(
						(
							data['soundstorage']+i+"/"+s,
							"data/categories/"+i+"/"+s
						)
					)
						



		print("    Found "+str(len(filesToDownload))+" files to download.",flush=True)
		for f in filesToDownload:
			print("        Downloading file: "+str(f),flush=True)
			r = requests.get(f[0])
			open(f[1], 'wb').write(r.content)

			totalDownloads += 1/len(filesToDownload)

		totalDownloads = int(totalDownloads)
		print("Done!",flush=True)

		allDone = True
		return allDone
   
	elif resp.status_code == 404:
		return allDone


