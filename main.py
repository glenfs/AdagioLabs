from flask import Flask, render_template

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


@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
