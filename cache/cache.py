from flask import Flask,request ,make_response,g#, url_for
import xml.etree.ElementTree as ET
import time
import logging
import csv
import json

import redis

from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import datetime

from flask import request
from flask import Response, stream_with_context

from xml.etree import ElementTree
from xml.dom import minidom
# from ElementTree_pretty import prettify

generated_on = str(datetime.datetime.now())

app = Flask(__name__)

#'tid-redis'
db = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
# db = redis.StrictRedis('192.168.10.102', 6379, charset="utf-8", decode_responses=True)
# db = redis.StrictRedis('tid-redis', 6379, charset="utf-8", decode_responses=True)

def prettify(elem):
	"""Return a pretty-printed XML string for the Element.
	"""
	rough_string = ElementTree.tostring(elem, 'utf-8')
	reparsed = minidom.parseString(rough_string)
	return reparsed.toprettyxml(indent="  ")

@app.before_request
def before_request():
   g.request_start_time = time.time()
   g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)

@app.route('/')
def api_root():
	return 'Welcome to WMP Cache API'


@app.route('/<parameter>', methods = ['GET'])
def get_parameter(parameter):
	if not db.exists(parameter): #does the hash exist?
		return "Error: %s doesn't exist" % parameter,500
	data = db.get(parameter)
	return data,200


@app.route('/<parameter>/<value>', methods = ['POST'])
def set_parameter(parameter,value):
	if parameter == '' or value =='':
		return "Error : system requires both Parameter and Value",500
	if db.exists(parameter): #does the hash exist?
		db.delete(parameter)
	ttl = 10368000 #4 months in seconds
	db.set(parameter,value)
	db.expire(parameter, ttl)
	return value,200

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
	# serve(app, host='0.0.0.0', port=8013)