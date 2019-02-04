#!/usr/bin/python
# -*- coding: utf-8 -*-

#Tornado imports
import tornado.ioloop

#Utils imports
from datetime import date
import json
import time

#Project imports
from gaivota_handler import GaivotaHandler
import tornado.web
import sys,os

#Main REST item class
class GaivotaEmail(GaivotaHandler):
	#GET handler
	
	#
	#@tornado.gen.coroutine
	@tornado.web.asynchronous	
	def get(self):
		print('seding email...')		
		time.sleep(10)
		self.write(json.dumps('email sent.'))
		print('email sent!')
		self.finish()

	#
	#@tornado.gen.coroutine
	@tornado.web.asynchronous
	def post(self):
		print('seding email...')
		time.sleep(5)
		self.write(json.dumps('email sent.'))
		print('email sent!')
		self.finish()