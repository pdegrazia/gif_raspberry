import requests
import json
from flask import Flask
app = Flask(__name__)

public_key = 'dc6zaTOxFJmzC'
url = 'http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=funny+cat'


page = '''
<html>
    <body>
        <img src='%s' width='320px' height='240px'></img>
    </body>
</html>
'''



@app.route('/')
def main():
    gif = requests.get(url)
    gif_data = json.loads(gif.text)
    gif_src = gif_data['data']['fixed_width_downsampled_url']
    print gif_src
    final_page = page % gif_src
    return final_page

if __name__ == '__main__':
    app.run()