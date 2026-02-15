from flask import Flask, make_response, request
import time
app = Flask(__name__)
def nowtime():
    current_time = time.time()
    formatted_time = time.ctime(current_time)
    return formatted_time

@app.route('/', methods=['GET'])
def baseRequest():
    response = make_response("")
    response.headers['X-Custom-Header'] = 'Custom-Header'
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Content-Length'] = '0'
    response.headers['Content-Language'] = 'ru'
    response.headers['Date'] = nowtime()
    return response

@app.route('/success', methods=['GET'])
def successRequest():
    response = make_response("Успешный запрос")
    response.headers['X-Custom-Header'] = 'MyValue'
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Content-Language'] = 'ru'
    response.headers['Date'] = nowtime()
    return response

@app.route('/unsuccess', methods=['GET'])
def unSuccessRequest():
    response = make_response("Неуспешный запрос с ошибкой клиента")
    response.headers['X-Custom-Header'] = 'MyValue'
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Content-Language'] = 'ru'
    response.headers['Date'] = nowtime()
    response.status_code = 500
    return response

@app.route('/check', methods=['GET'])
def checkRequest():
    response = make_response()
    if(request.headers.get('MyHeader')=="check"):
        response.response = 'успешный запрос'
        response.status_code = 200
    else:
        response.response = 'Не указан заголовок MyHeader со значением check'
        response.status_code = 400
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Content-Language'] = 'ru'
    response.headers['Date'] = nowtime()
    return response

@app.route('/post/check', methods=['POST'])
def postRequest():
    response = make_response()
    print(str(request.data))
    if(str(request.data) == "b'check'"):
        response.response = 'успешный запрос'
        response.status_code = 200
    else:
        response.response = 'Не указано тело со значением check'
        response.status_code = 406
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Content-Language'] = 'ru'
    response.headers['Date'] = nowtime()
    return response

@app.route('/tea', methods=['PUT'])
def teapot():
    response = make_response("Я чайник")
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Content-Language'] = 'ru'
    response.headers['Date'] = nowtime()
    response.status_code = 418
    return response

@app.route('/getparam', methods=['GET'])
def param():
    all_params = request.args.to_dict()
    response = make_response(all_params)
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Content-Language'] = 'ru'
    response.headers['Date'] = nowtime()
    return response

if __name__ == '__main__':
    app.run()