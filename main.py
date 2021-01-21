from flask import Flask, request, json

app = Flask(__name__)


@app.route('/api/echo', methods=['GET', 'POST', 'DELETE', 'PUT'])
def add():
    print("HEADERS: ")
    print(request.headers)
    print("BODY: ")
    print(request.get_data().decode("utf-8"))
    print("Method:")
    print(request.method)

    data = {"mensaje": "recibido"}
    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run()
