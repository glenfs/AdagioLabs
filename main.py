from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def home():
    products = [
        {
            'title': 'Sight Reader Expert',
            'description': 'Meet Sight Reader, your go-to app for mastering piano sight-reading effortlessly. Whether you\'re a pro or just starting out, this app helps you improve your reading skills easily. With its easy-to-use interface, you can dive into a fun learning experience. Adjust difficulty levels, choose clefs, and octaves to match your skills. Challenge yourself gradually and boost your speed and accuracy. Sight Reader makes piano practice simple and effective.',
            'image': '/static/music.png'
        }
    ]
    return render_template('index.html', products=products)

@app.route('/downloadFileWin')
def download_file_Win():
    return send_from_directory('data', "sightreader.zip", as_attachment=True)

@app.route('/downloadFileMac')
def download_file_Mac():
    return send_from_directory('data', "SightReader.dmg", as_attachment=True)

if __name__ == '__main__':
    app.run()
