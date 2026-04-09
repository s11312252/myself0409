from flask import Flask, render_template

app = Flask(__name__)

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

# 這是點擊首頁右邊卡片按鈕後會跳轉的頁面
@app.route('/job')
def job():
    return render_template('job.html')

if __name__ == '__main__':
    app.run(debug=True)