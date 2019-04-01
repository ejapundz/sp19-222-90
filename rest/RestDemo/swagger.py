from flask import jsonify, request

def echo_get():
    name = request.args.get('name', '').strip()
    msg = {"msg": "Hello " + name} if name else {"msg": "Hello"}
    return jsonify(msg)

def echo_post():
    if 'name' in request.form:
        name = request.form['name']
    else:
        name = ''
    msg = {"msg": "Hello " + name} if name else {"msg": "Hello"}
    return jsonify(msg)
