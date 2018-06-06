import falcon
from sqlalchemy.orm import Session

class CORSComponent(object):
    def process_response(self, req, resp, resource, req_succeeded):
        resp.set_header('Access-Control-Allow-Origin', '*')

        if (req_succeeded
            and req.method == 'OPTIONS'
            and req.get_header('Access-Control-Request-Method')
        ):
            # NOTE(kgriffs): This is a CORS preflight request. Patch the
            #   response accordingly.

            allow = resp.get_header('Allow')
            resp.delete_header('Allow')

            allow_headers = req.get_header(
                'Access-Control-Request-Headers',
                default='*'
            )

            resp.set_headers((
                ('Access-Control-Allow-Methods', allow),
                ('Access-Control-Allow-Headers', allow_headers),
                ('Access-Control-Max-Age', '86400'),  # 24 hours
            ))

class AuthMiddleware(object):
    def process_request(self, req, resp):
        req.ourAuth = None

        from pprint import pprint
        token = req.get_header('Authorization')
        account_id = req.get_header('Account-ID')
        pprint(req.headers)

        if token and account_id and self._token_is_valid(token, account_id):
            req.ourAuth = True

    def _token_is_valid(self, token, account_id):
        return True  # Suuuuuure it's valid...

class TransactionStart(object):
    def process_request(self, req, resp):
        # Start the transaction
        req.db = Session()

        from pprint import pprint
        token = req.get_header('Authorization')
        account_id = req.get_header('Account-ID')
        pprint(req.headers)

        if token and account_id and self._token_is_valid(token, account_id):
            req.ourAuth = True

    def _token_is_valid(self, token, account_id):
        return True  # Suuuuuure it's valid...

