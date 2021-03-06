from pyramid.compat import escape

from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config

import robot

@view_config(route_name='home', renderer='home.pt')
def home_view(request):
    return ''

@view_config(route_name='hello', renderer='hello_world.pt')
def hello_world (request):
    return dict(name=request.matchdict['name'])

@view_config(route_name='redirect')
def redirect_view(request):
    return HTTPFound(location="/problem")

@view_config(route_name='exception')
def exception_view(request):
    raise Exception()

@view_config(route_name='hello_json', renderer='home.pt')
def hello_json(request):
    input=request.POST["directions"].split()
    arr = []
    for i in input:
        if i == 'b':
            arr.append(robot.backward("1"))
        elif i == 'f':
            arr.append(robot.forward("1"))
        elif i == 'r':
            arr.append(robot.turn_right(request.POST["rightTime"]))
        else:
            arr.append(robot.turn_left(request.POST["leftTime"]))
    
    return ''
