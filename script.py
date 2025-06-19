from flask import Flask, request

app = Flask(__name__)

@app.route('/location', methods=['POST'])
def location():
    data = request.get_json()
    print('Latitude:', data['latitude'])
    print('Longitude:', data['longitude'])
    print(data)
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)
