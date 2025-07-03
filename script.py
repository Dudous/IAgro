import os
import webbrowser
import threading
from flask import Flask, request
from flask_cors import CORS, cross_origin
import http.server
import socketserver

def open_browser():
    url = 'http://127.0.0.1:5500/index.html'
    webbrowser.open(url)
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", 5500), Handler) as httpd:
        print(f"Serving static files on http://127.0.0.1:5500")
        httpd.serve_forever()

thread = threading.Thread(target=open_browser)
thread.daemon = True
thread.start()

app = Flask(__name__)
CORS(app)

@app.route('/location', methods=['POST'])
@cross_origin()
def location():
    data = request.get_json()
    print('Latitude:', data['latitude'])
    print('Longitude:', data['longitude'])
    print('Data received:', data)
    return 'OK', 200

if __name__ == '__main__':
    print("Starting Flask app on http://127.0.0.1:5000")
    app.run(debug=False, port=5000)
