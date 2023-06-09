from pyrebase import pyrebase
import os
import sys
import json
Path ="./.backup_util/jsons/"

def fill_details():
  flag=False
  entries = os.listdir(Path)
  for entry in entries:
      if(entry=='Config.json'):
        flag=True
  if(flag==False):
    attribute=["apiKey","authDomain","projectId","storageBucket","messagingSenderId","appId","measurementId","databaseURL"]
    data=dict()
    print("Enter the following details:")
    try:
      for attr in attribute:
          print(attr)
          data[attr]=input()
      jsonString = json.dumps(data)
      jsonFile = open(Path+"/Config.json", "w")
      jsonFile.write(jsonString)
      jsonFile.close()
      print("Now Copy the AccountKey file into the Firebase folder")
    except Exception as e:
        print(str(e))
      
def initialize_and_getconfig():
  try:
      with open(Path+'/Config.json', 'r') as file:
      # Load the JSON data from the file into a Python object
          data = json.load(file)
      # config=open(Path+'/Config.json',"w")
      # print(config)
  except Exception as e:
      error="Config Not Present In Required Path"
      print(error)
      print(str(e))
      return error
  # data = config
  # print(data)
  try:
    Modulejsonfile=["Config.json"]
    json_file_names = [filename for filename in os.listdir(Path) if filename.endswith('.json')]
    for file in json_file_names:
        if file not in Modulejsonfile:
            data["serviceaccount"]=file
            break
  except Exception as e:
      print(str(e))
      return str(e)
  if "serviceaccount" not in data.keys():
     print("Accountkey file not present in Firebase file")
  datakeys = json.dumps(data)
  config = open(Path+"/Config.json", "w")
  config.write(datakeys)
  config.close()
  return data

def getconfig():
    try:
      config=open(Path+'/Config.json')
    except Exception as e:
      print("Config Not Present In Required Path")
      print(str(e))
      return
    data = json.load(config)
    return data

def initialize(Projname):
    try:
      firebase=pyrebase.initialize_app(initialize_and_getconfig())
      storage=firebase.storage() 
      print("Firebase Connection Successful")
    except Exception as e:
      error= "Connection Unsuccessful"
      print(error)
      print(str(e))
      return error
    try:
      storage.child(Projname).put(None)
      print("Project Initialized")
    except Exception as e: 
      error= "Project Not Initialized"
      print(error)
      print(str(e))
      return error
      
def connect():
    try:
      firebase=pyrebase.initialize_app(getconfig())
      storage=firebase.storage() 
      print("Firebase Connection Successful")
      return storage
    except Exception as e:
      error= "Connection Unsuccessful"
      print(error)
      print(str(e))
      return error
   
def upload_file(Projname,RFilename,Filepath,Filename):
    storage=connect()
    try:
      storage.child(Projname+"/"+RFilename).put(Filepath+Filename)
      print("Version", RFilename,"File Upload Successful")
    except Exception as e:
      error= "File Upload Unsuccessful"
      print(error)
      print(str(e))
      return error

def delete_file(Projname,RFilename,Filename=None):
    storage=connect()
    try:
      storage.child(Projname+"/"+RFilename).delete(Filename,None)
      print("File Delete Successful")
    except Exception as e:
      error= "File Delete Unsuccessful"
      print(error)
      print(str(e))
      return error    

def download_file(Projname,RFilename,Filepath,Filename):
    storage=connect()
    try:
      storage.child(Projname+"/"+RFilename).download(Filepath+Filename)
      print("Version", RFilename,"File Download Successful")
    except Exception as e:
      error= "File Download Unsuccessful"
      print(error)
      print(str(e))
      return error

def geturl(Projname,RFilename):
    storage=connect()
    try:
      url=storage.child(Projname+"/"+RFilename).get_url(None)
      print("File Download Successful")
      return url
    except Exception as e:
      error= "File Download Unsuccessful"
      print(error)
      print(str(e))
      return error

    
cmd=sys.argv[1]

if(cmd=="fill_details"):
  fill_details()
elif(cmd=="initialize"):
  # print(sys.argv[2])
  initialize(sys.argv[2])
elif(cmd=="upload_file"):
  upload_file(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
elif(cmd=="delete_file"):
  upload_file(sys.argv[2],sys.argv[3])
elif(cmd=="download_file"):
  download_file(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
elif(cmd=="geturl"):
  geturl(sys.argv[2],sys.argv[3])
