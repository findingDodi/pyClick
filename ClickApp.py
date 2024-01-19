import flask
from datetime import datetime
import os


class ClickApp:

    CLICKS_DATA = "data/clicks.txt"

    def __init__(self):
        self.app = flask.Flask('ClickApp')
        self.setup_routes()

    def run(self, port=5001, debug=True):
        self.app.run(port=port, debug=debug)

    def setup_routes(self):
        @self.app.route('/')
        def index():
            return flask.render_template('clicker.j2', clicks=self.get_clicks())

        @self.app.route('/date')
        def show_date():
            return datetime.now().strftime('%d.%m.%Y')

        @self.app.route('/api/increment-clicks')
        def increment_clicks():
            self.increment_clicks()

        @self.app.route('/api/get-clicks')
        def get_clicks():
            return self.get_clicks()

        @self.app.route('/public/<string:public_file>')
        def public(public_file):
            path = os.path.join('public', public_file)

            if not os.path.isfile(path):
                flask.abort(404, "File not found")

            file_handle = open(path, "r")
            file_content = file_handle.read()
            file_handle.close()
            return file_content


    def get_clicks(self):
        if not os.path.isfile(ClickApp.CLICKS_DATA):
            self.set_clicks(0)

        file_handle = open(ClickApp.CLICKS_DATA, "r")
        file_content = file_handle.read()
        file_handle.close()

        return file_content

    def set_clicks(self, clicks):
        file_handle = open(ClickApp.CLICKS_DATA, "w")
        file_handle.write(str(clicks))
        file_handle.close()

    def increment_clicks(self):
        current_clicks = self.get_clicks()
        new_clicks = int(current_clicks) + 1
        self.set_clicks(new_clicks)
