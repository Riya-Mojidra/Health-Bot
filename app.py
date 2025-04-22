from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health_tips')
def health_tips():
    return render_template('health_tips.html')

@app.route('/track_health')
def track_health():
    return render_template('track_health.html')

@app.route('/assistant')
def assistant():
    return render_template('assistant.html')

if __name__ == '__main__':
    app.run(debug=True)