#!/usr/bin/python
# -*- coding: utf-8 -*-

#Tornado import
from tornado import web

#Simple HTTPError handling class (just instantiation)
class GaivotaException(web.HTTPError):
	pass