from flask import jsonify, request
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("swagger.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "It's working!"}
    return jsonify(msg)

@app.route("/echo", methods=['GET', 'POST'])
def echo():
    if request.method == 'GET':
        name = request.args.get('name', '').strip()
    elif request.method == 'POST':
        if 'name' in request.form:
            name = request.form['name']
        else:
            name = ''
    msg = {"msg": "Hello " + name} if name else {"msg": "Hello"}
    return jsonify(msg)

if __name__ == "__main__":
    # app.run(host="localhost", port=8080, debug=False)
    app.run(host="0.0.0.0", port=8080, debug=False)
