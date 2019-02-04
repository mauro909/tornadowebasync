#!/usr/bin/python
# -*- coding: utf-8 -*-

#Tornado imports
import tornado.web
import tornado.wsgi
import wsgiref.simple_server as ws
import os
#import asyncio
#from tornado.platform.asyncio import AnyThreadEventLoopPolicy

import logging
from logging.config import dictConfig

#Utils imports
from gaivota_email import GaivotaEmail

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("GaivotaPythonDash!")

#Creates routes
application = tornado.web.Application([
	(r"/email", GaivotaEmail),
	(r"/", MainHandler)
])

#Main server port
port = int(os.getenv('TORNADO_PORT'))#80
 
#When running direct from script, start webserver
if __name__ == "__main__":
	print("Starting Python Tornado Webserver at port {}".format(port))
	#asyncio.set_event_loop_policy(AnyThreadEventLoopPolicy())
	logging_config = dict(
		version = 1,
		formatters = {
			'f': {'format':
				'%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
			},
		handlers = {
			'h': {'class': 'logging.StreamHandler',
				'formatter': 'f',
				'level': logging.DEBUG}
			},
		loggers = {
			'tornado.general': {'handlers': ['h'],
					'level': logging.DEBUG}
			}
	)
	dictConfig(logging_config)
	wsgi_app = tornado.wsgi.WSGIAdapter(application)
	server = ws.make_server('', port, wsgi_app)
	server.serve_forever()