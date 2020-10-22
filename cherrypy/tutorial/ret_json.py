import cherrypy
from datetime import datetime as dt
from datetime import timedelta as td
import os


def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    cherrypy.response.headers['Content-Type'] = 'application/json'


class Root(object):
    faults = {}
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def index(self):
        return "Hello World {}".format(cherrypy.request)

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def bins(self):
        ids =  {'faults ids': list(self.faults.keys())}
        return ids

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def remove_fault(self, _id):
        message = 'Fault {_id} incorrect '
        if _id in self.faults.keys():
            self.faults.pop()
            message = f'fault id {_id} removed'
        return {'status': 'ok', 'message': message}


if __name__ == '__main__':
    #cherrypy_cors.install()
    cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8080,
    })

    cherrypy.quickstart(Root(), '', {'/': {
        'tools.CORS.on': True
    }})