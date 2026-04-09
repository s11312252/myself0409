from flask import Flask, render_template

app = Flask(__name__)

# 這些路由都要放在 app = Flask 之後
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/goals')
def goals():
    return render_template('goals.html')

@app.route('/test_results')
def test_results():
    return render_template('test_results.html')

@app.route('/job')
def job():
    return render_template('job.html')

# Vercel 部署時這段可以不用跑，但本地端還是需要它
if __name__ == '__main__':
    app.run(debug=True)