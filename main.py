from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    return render_template('base.html', prof=prof, src_1=url_for('static', filename='img/img1.png'),
                           src_2=url_for('static', filename='img/img1-2.png'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
