import requests

def download():
	mysession=requests.Session()
	url = 'https://www.natice.noaa.gov/pub/icebergs/Iceberg_Tabular.csv'

	# get the requested data, note that the auth. Login credentials have to be in .netrc file
	res = mysession.get(url)

	# save the results
	with open('icebergs.csv',"wb") as fd:
		fd.write(res.content)
		
		
def makejsonfile():
	import csv
	import json
	
	with open("icebergs.csv",'r') as csvfile_ind:
		reader_ind = csv.DictReader(csvfile_ind)
		rows = []
		for row in reader_ind:
			try: 
#				print(row["Iceberg"])
				length = round(float(row["Length (NM)"])*1.852,1)
				width = round(float(row["Width (NM)"])*1.852,1)
				
				row["Iceberg"] = row["Iceberg"]+';  L:'+str(length)+ 'km W:'+str(width)+'km'
				row["Latitude"] = float(row["Latitude"])
				row["Longitude"] = float(row["Longitude"])
				del row['Length (NM)']
				del row['Width (NM)']
				del row['Remarks']
				del row['Last Update']
				rows.append(row)
			except:
				pass


	with open("icebergs.json", 'w') as json_file_ind:
		json.dump(rows, json_file_ind, sort_keys=False, indent=4, separators=(',', ': '))


#download()
makejsonfile()