from flask import Flask, jsonify
from ytmusicapi import YTMusic
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

auth = {
 "scope": "https://www.googleapis.com/auth/youtube",
 "token_type": "Bearer",
 "access_token": "ya29.a0AXooCgtJOpDuznup_GlsT14sIQjOKRecsfll90I46LZi39KxCSmELRxJ1XLlhiaiH_80-Vw2dJA_XTbj3id4xze--1Xqal5jwHWM7mgUqq4IEf6t9-LfG5Qv92hzrQO8V3JKYg2lD9xke_Ecw0Xgljh4IiMvn5em-zpGMw8TeGZ7R-wzaCgYKAawSARMSFQHGX2MiCLzNcMiVkbpF7GlayeeKdg0183",
 "refresh_token": "1//0467UN7KB4VwfCgYIARAAGAQSNwF-L9IryZuzoFGoLG8s85GaDOcqGJnJ6CynTaONpUhmJsrpgTVBIVMcMHrZ6dFY1-Z3Mv3-1KE",
 "expires_at": 1718549450,
 "expires_in": 67661
}
yt = YTMusic(auth)

@app.route('/search/<query>')
def search_ytmusic(query):
    search_results = yt.search(query)
    title = search_results[0]['title']
    video_id = search_results[0]['videoId']
    video_url = f"https://www.youtube.com/watch?v={video_id}.com"
    return jsonify({'results': search_results, 'title': title, 'video_url': video_url})

if __name__ == '__main__':
    app.run(debug=True)

