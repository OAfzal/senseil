from flask import Flask
from flask import request
from senseil import runModel

app = Flask(__name__)


@app.route('/predicted')
def predict():
    ca = request.args.get("ca")
    p = request.args.get("p")
    ph = request.args.get("ph")
    sol = request.args.get("sol")
    sand = request.args.get("sand")
    print(ca,p,ph,sol,sand)
    val = runModel(ca,p,ph,sol,sand)
    return val

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
    # app.run(host = '0.0.0.0',port="8080")
    # app.run(debug=True,host="0.0.0.0")

