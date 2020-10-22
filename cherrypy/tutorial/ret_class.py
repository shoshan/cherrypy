import cherrypy
# class Band(object):
#     def __init__(self):
#         self.albums = Fault()
#     def _cp_dispatch(self, vpath):
#         if len(vpath) == 1:
#             cherrypy.request.params['name'] = vpath.pop()
#         return self
#         if len(vpath) == 3:
#             cherrypy.request.params['artist'] = vpath.pop(0) # /band name/
#         vpath.pop(0) # /albums/
#         cherrypy.request.params['title'] = vpath.pop(0) # /album title/
#         return self.albums
#         return vpath
#
#     @cherrypy.expose
#     def index(self, name):
#         return 'About %s...' % name

class Root(object):
    faults_dict = {'1':{'name':'first'},'2':{'name':'second'},'80':{'name':'eighty'}}
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def faults(self, fault_id=None):
        method = cherrypy.request.method
        params = cherrypy.request.params
        if fault_id is None:
            if method == 'GET':
                ids = {'faults ids': list(self.faults_dict.keys())}
            return ids
        else:
            if method == 'POST' or method == 'CREATE':
                # TODO self.faults[fault_id] =
                pass
            return self.faults_dict[fault_id]
if __name__ == '__main__':
    cherrypy.quickstart(Root())
