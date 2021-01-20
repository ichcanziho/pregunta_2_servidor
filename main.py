from flask import Flask, request, json
import pprint

app = Flask(__name__)


@app.route('/api/echo', methods=['GET', 'POST', 'DELETE', 'PUT'])
def add():
    data = request.get_json()
    print("HEADERS:")
    pp = pprint.PrettyPrinter(depth=4)
    pp.pprint(data.get("headers", {"not": "info"}))
    print()
    print("BODY:")
    pp.pprint(data.get("json", {"not": "info"}))
    print()
    print("METHOD:")
    print(request.method)

    data = {"mensaje": "recibido"}
    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run()
