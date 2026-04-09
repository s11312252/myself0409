from flask import Flask, render_template

# 1. 先建立 app 物件
app = Flask(__name__)

# 2. 進行 Vercel 必要的設定
app.debug = True
main = app  # 有些 Vercel 設定會要求指向一個變數，維持 app = app 也可以

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

# 3. 本地端執行
if __name__ == '__main__':
    app.run(debug=True)