
from flask import Flask, render_template, request
from module.bili2txt.totxet import *
from module.txt2txt.GLM import *

app = Flask(__name__)


# 首页，提供表单让用户输入Bilibili视频的URL
@app.route('/')
def index():
    return render_template('index.html')

# 接受用户输入并处理
@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        url = request.form['url']  # 获取用户提交的Bilibili URL
        try:
            # 调用你的 bili2txt 方法处理视频
            result = bili2txt(url)
            return f"处理成功，结果是: {result}"
        except Exception as e:
            return f"处理过程中出错: {str(e)}"



# 启动应用
if __name__ == '__main__':
    app.run(debug=True)
