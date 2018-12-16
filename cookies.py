from flask import Flask , make_response, request

app = Flask(__name__)

@app.route('/set')
def set():
    resp = make_response('setting cookie!')
    resp.set_cookie('framework','flask')
    resp.set_cookie('eyo','i sit back')
    return resp

@app.route('/get')
def get():
    framework= request.cookies.get('framework')
    return 'the framework is '+ framework

if __name__=='__main__':
    app.run(debug=True)