from flask import Flask, jsonify

demo_server = Flask(__name__)


@demo_server.route('/get_message', methods=['GET'])
def send_demo_message():
    # verify request recieved
    print('Received Request for Message')
    # send canned message
    return jsonify({'response': 'A message from CS361, Zachary Fowler'})


if __name__ == '__main__':
    print('Starting Demo Server')
    demo_server.run(host='127.0.0.1', port=8080, debug=True)    # local host, default port to http
