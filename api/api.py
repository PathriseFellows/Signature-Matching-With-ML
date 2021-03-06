from flask import Flask
from flask_cors import CORS
from apis import api

app = Flask(__name__)
cors = CORS(app)
api.init_app(app)

app.run(debug=True)
