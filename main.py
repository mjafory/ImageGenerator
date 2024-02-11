from flask import Flask, render_template
import threading
import webview

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def run_flask():
    app.run()

if __name__ == '__main__':
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Create and run the webview app
    webview.create_window("AI Image tools", "http://127.0.0.1:5000/")
    webview.start()
