import falcon, ujson


class Sessions(object):
    def on_get(self, req, resp):
        resp.body = ujson.encode({'d': ['session objects here']})
        resp.status = falcon.HTTP_200

