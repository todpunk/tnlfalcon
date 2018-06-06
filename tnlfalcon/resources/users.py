import falcon, ujson

class Users(object):

    def on_get(self, req, resp):
        if req.ourAuth is None:
            raise falcon.HTTPUnauthorized('Authentication required',
                                          'This resource is protected',
                                          ['This is a thing'],
                                          href='http://docs.example.com/auth')

        resp.body = ujson.encode({'d': ['clearly a user object']})
        resp.status = falcon.HTTP_200
