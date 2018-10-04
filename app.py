from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from text_processor import TextProcessor
from polyglot.downloader import downloader

print(downloader.supported_tasks(lang="pl"))


app = Flask('Visual Search Engine')
CORS(app)


api = Api(app)
api.add_resource(TextProcessor, '/')

app.run('127.0.0.1', 5000)

