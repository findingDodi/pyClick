import flask
from datetime import datetime


class ClickApp:
    def __init__(self):
        self.app = flask.Flask('ClickApp')
        self.setup_routes()

    def run(self, port=5000, debug=True):
        self.app.run(port=port, debug=debug)

    def setup_routes(self):
        @self.app.route('/')
        def index():
            return 'Hello World!'

        @self.app.route('/date')
        def show_date():
            return datetime.now().strftime('%d.%m.%Y')

