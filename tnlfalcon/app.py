import falcon

from middleware import AuthMiddleware, CORSComponent, TransactionStart
from resources.sessions import Sessions
from resources.users import Users

class StaticResource(object):
    def on_get(self, req, resp, filename):
        # do some sanity check on the filename
        resp.status = falcon.HTTP_200
        with open('static/'+filename, 'r') as f:
            resp.body = f.read()

class IndexResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('static/index.html', 'r') as f:
            resp.body = f.read()

api = falcon.API(middleware=[
    # TransactionStarter(),
    AuthMiddleware(),
    CORSComponent(),
])

api.add_route('/', IndexResource())
api.add_route('/static/{filename}', StaticResource())
api.add_route('/sessions', Sessions())
api.add_route('/sessions/{id:int(None,1)}', Sessions())
api.add_route('/users', Users())
api.add_route('/users/{id:int(None,1)}', Users())

