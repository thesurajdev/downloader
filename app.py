from flask import Flask, request, jsonify
from pytube import YouTube

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    url = request.json['url']
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download('/path/to/download')
    return jsonify({'message': 'Download started'})

if __name__ == '__main__':
    app.run(debug=True)
