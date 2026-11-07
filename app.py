import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Basic HTML template
HTML_LAYOUT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Render Demo App</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #fff;
        }
        .card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            text-align: center;
            max-width: 400px;
        }
        button {
            background-color: #00d2ff;
            border: none;
            color: white;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s;
            margin-top: 15px;
        }
        button:hover { background-color: #0081ab; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Live on Render!</h1>
        <p>Your Python web app is officially deployed and running.</p>
        <button onclick="fetchMessage()">Test API Endpoint</button>
        <p id="api-response" style="margin-top: 20px; font-weight: bold;"></p>
    </div>

    <script>
        async function fetchMessage() {
            const res = await fetch('/api/hello');
            const data = await res.json();
            document.getElementById('api-response').innerText = data.message;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_LAYOUT)

@app.route('/api/hello')
def api_hello():
    return jsonify({"status": "success", "message": "Hello from Python Flask backend!"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)