from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Breakout Pullback App</title>
        </head>
        <body>
            <h1>Welcome to the Breakout Pullback App!</h1>
            <p>This will eventually become your IBKR-powered trading dashboard.</p>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run()
