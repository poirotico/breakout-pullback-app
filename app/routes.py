from flask import Blueprint

bp = Blueprint("main", __name__)

@bp.route("/")
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