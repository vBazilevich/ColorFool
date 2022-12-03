from flask import Flask, make_response, request, send_from_directory, send_file
import ColorFool

app = Flask(__name__)
app.debug = True


def colorize_stub(data):
    return data


@app.route("/")
def hello_world():
    return send_from_directory('front-build', 'index.html')

@app.route('/colorize', methods=['PUT'])
def colorize():
    data = request.files['image']
    # resuling_data = ColorFool.colorize(data.read())
    resuling_data = colorize_stub(data.read())
    with open('/tmp/colorize-img', 'wb') as f:
        f.write(resuling_data)
    # data.save('/tmp/colorize-img')
    response = make_response(send_file('/tmp/colorize-img'))
    response.headers['Content-Type'] = 'image/png'
    return response

@app.route('/<path:path>')
def send_report(path):
    return send_from_directory('front-build', path)
