#from flask import Flask, request, abort
#import xmlrpc.client
from website import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)






# app = Flask(__name__)
#
# @app.route('/webhook', methods=['POST'])
# def webhook():
#     if request.method == 'POST':
#         print(request.json)
#         url = "http://194.195.119.84:8069"
#         db = "demo"
#         username = 'info@appeul.com'
#         password = "jasoos74."
#
#         common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
#         # common.version()
#
#         uid = common.authenticate(db, username, password, {})
#         models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
#         if uid:
#             models.execute_kw(db, uid, password, 'res.partner', 'create', [request.json])
#         return 'success', 200
#     else:
#         abort(400)
#
#
# @app.route('/', methods=['GET'])
# def test():
#     return '<h1>Success!</h1>'
#
#
#
# @app.route('/get_parters', methods=['GET'])
# def get_partners():
#
#     url = "http://194.195.119.84:8069"
#     db = "demo"
#     username = 'info@appeul.com'
#     password = "jasoos74."
#
#     common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
#     # common.version()
#
#     uid = common.authenticate(db, username, password, {})
#     models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
#     if uid:
#
#
#         # product_id = models.execute_kw(db, uid, password, 'res.partner', 'search_read',
#         #                                [[]], {'fields': ['id', 'name']})
#         # print(product_id)
#         return '<h1></h1>'












#
#
#
# if __name__ == '__main__':
#     app.run()

