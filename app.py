from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    os.system('python main.py')  # This runs your main.py file
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
