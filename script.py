from flask import Flask, request
from flask_cors import CORS, cross_origin

import http.server
import socketserver
import webbrowser
import os
import threading
import webbrowser


def openBrowser():
    url = 'http://127.0.0.1:5500/index.html'
    webbrowser.open(url)

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", 5500), Handler) as httpd:
        
        webbrowser.open_new_tab(f"http://127.0.0.1:{5500}/index.html") 

        httpd.serve_forever()
        
thread = threading.Thread(target=openBrowser)
thread.start()




app = Flask(__name__)
CORS(app)

@app.route('/location', methods=['POST'])
@cross_origin()
def location():
    data = request.get_json()
    print('Latitude:', data['latitude'])
    print('Longitude:', data['longitude'])
    print(data)
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)