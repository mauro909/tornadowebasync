#!/usr/bin/python
# -*- coding: utf-8 -*-

#Tornado imports
import tornado.web
from concurrent.futures import ThreadPoolExecutor

#Utils imports
import json
import traceback
import os

#Project imports
from gaivota_exception import GaivotaException

MAX_WORKERS = int(os.getenv('MAX_WORKERS'))
#Main app request handler
class GaivotaHandler(tornado.web.RequestHandler):
	executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)	
	#executor = concurrent.futures.ThreadPoolExecutor(5)	
	#No matter what the HTTP request, Tornado calls the prepare method. If you call either finish or send_error, Tornado won't call 
	#any additional methods. You can override the prepare method to execute code that is necessary for any HTTP request, then write 
	#your specific code in the head(), get(), post(), delete(), patch(), put() or options() method.
	#@run_on_executor
	#@tornado.gen.coroutine
	#@tornado.web.asynchronous		
	@tornado.gen.coroutine
	def prepare(self):
		#First, check if token is not in headers (and raise an error if so)
		print('receiving request...')		
		if False and not 'Token' in self.request.headers: 
			reason_str='"token" wasn\'t set on header!'
			print('error=',reason_str)
			raise GaivotaException(reason=reason_str, status_code=403)
		#Stores the token
		#self.token = self.request.headers['Token']
		
		if False: #check if token is valid, ignore this part
			reason_str='"token" is invalid!'
			print('error=',reason_str)
			raise GaivotaException(reason=reason_str, status_code=403)

	#If a handler raises an exception, Tornado will call RequestHandler.write_error to generate an error page. tornado.web.HTTPError 
	#can be used to generate a specified status code; all other exceptions return a 500 status.
	@tornado.web.asynchronous	
	def write_error(self, status_code, **kwargs):

		self.set_header('Content-Type', 'application/json')
		self.finish(json.dumps({
			'error': {
				'code': status_code,
				'message': self._reason,
			}
		}))

	@tornado.web.asynchronous	
	def check_parameters(self,list_check,funcName):
		raise_str='{} header is mandatory at {} function!'
		missing=[]
		for parameter in list_check:
			if not parameter in self.request.headers:
				missing.append(parameter) 
		if len(missing)>0:
			reason_str=raise_str.format(missing,funcName)
			print('error=',reason_str)
			raise GaivotaException(reason=reason_str, status_code=400)
			
	"""
	These comments are here just for a rapid consulting on request events handling in Tornado

	def on_fetch(self, http_response):
		if http_response.error: raise tornado.web.HTTPError(500)
		response = http_response.body.decode().replace("Most Recent Premium Content", "Most Recent Content")
		self.write(response)
		self.set_header("Content-Type", "text/html")
		self.finish()

	Whenever the Web application receives a request and matches the URL pattern, Tornado performs the following actions:

		1 - It creates a new instance of the RequestHandler subclass that has been mapped to the URL pattern.
		2 - It calls the initialize method with the keyword arguments specified in the application configuration. You can override the initialize method to save the arguments into member variables.
		3 - No matter what the HTTP request, Tornado calls the prepare method. If you call either finish or send_error, Tornado won't call any additional methods. You can override the prepare method to execute code that is necessary for any HTTP request, then write your specific code in the head(), get(), post(), delete(), patch(), put() or options() method.
		4 - It calls the method according to the HTTP request with the arguments based on the URL regular expression that captured the different groups. As you already know, you must override the methods you want your RequestHandler subclass to be able to process. For example, if there is an HTTP GET request, Tornado will call the get method with the different arguments.
		5 - If the handler is synchronous, Tornado calls on_finish after the previous method called, according to the HTTP request returns. But if the handler is asynchronous, Tornado executes on_finish after the code calls finish. The previous asynchronous example showed the usage of finish. You can override the on_finish method to perform cleanup or logging. Notice that Tornado calls on_finish after it sends the response to the client.
		X - If the client closes the connection in asynchronous handlers, Tornado calls on_connection_close. You can override this method to clean up resources in this specific scenario. However, the cleanup after processing the request must be included in the on_finish method.
	"""
