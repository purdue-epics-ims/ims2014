from django.shortcuts import render
from django.http import HttpResponse
	
def index( request ):
	return HttpResponse ( "Hello World! You're at the poll index" )

def hello( request, number ):
	return HttpResponse( "Answer = %s" % (int(number)*5) )
	
'''
Basic views to be written:
	- index page which can list each kind of entity (Organizations, Users, Jobs, and Service Categories
	- details page for each entity - most important right now is Organization page
	- login page
	'''
