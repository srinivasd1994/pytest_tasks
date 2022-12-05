import json
import requests
import jsonpath
import socket

import urllib

try:
    from urllib3 import urlopen
except ImportError:
    urlopen = urllib.request.urlopen


#ApI users
Url = 'https://reqres.in/api/users'
def test_explicitly_enable_socket(enable_socket):
    # socket is enabled by pytest fixture from conftest. disabled in finalizer
    assert socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Read input json file
def test_resources():
   file = open('D:\\sample\\test_cases\\pytest_tasks\\samp.json','r')
   json_input = file.read()

   requests_json = json.loads(json_input)
   print(requests_json)

#make post using input body
   Response = requests.post(Url,requests_json)
   print(Response.content)

#validating response
   assert Response.status_code == 201

#fetch header from response

   print(Response.headers.get('content-length'))


#parse response grom json format

   Response_json = json.loads(Response.text)

#pick id using jsonpath

   id= jsonpath.jsonpath(Response_json,'id')
   print(id[0])