from flask import Flask, jsonify, redirect, url_for
from werkzeug.exceptions import HTTPException, default_exceptions

from flask_restful import Api
from logging.config import dictConfig
from flask_sqlalchemy import SQLAlchemy
from envparse import env


app = Flask(__name__, instance_relative_config=True)
print(' * Loading configuration : {config}'.format(config=env('CONFIG_ENVIRONMENT', default='config.default')))
app.config.from_object(env('CONFIG_ENVIRONMENT', default='config.default'))
app.config.from_envvar('CONFIG_FILE', silent=True)

db = SQLAlchemy(app)

# Importing after because we need db initialized to use these
from api.resources import (
    Application, ApplicationList, ApplicationNetwork, AdNetwork, AdNetworkList, Mediation, HealthCheck)
from api.utils import populate_sample

dictConfig(app.config['LOG_CONFIG'])

api = Api(app, prefix="/api")

@app.before_first_request
def init_app():
    db.create_all()
    if app.config['POPULATE_SAMPLE']:
        app.logger.info('Populating with sample data...')
        populate_sample()
    for ex in default_exceptions:
        app.register_error_handler(ex, handle_error)


api.add_resource(ApplicationList, '/app')
api.add_resource(Application, '/app/<string:id>')
api.add_resource(Mediation, '/app/<string:id>/mediate')
api.add_resource(AdNetworkList, '/network')
api.add_resource(AdNetwork, '/network/<string:id>')
api.add_resource(ApplicationNetwork, '/app/<string:id>/networks')
api.add_resource(HealthCheck, '/healthcheck')


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    app.logger.error(str(e))
    if isinstance(e, HTTPException):
        code = e.code
    if code != 500:
        return jsonify({'message': 'An error has ocurred : {e}'.format(e=str(e))}), code
    return jsonify({'message': 'Internal Server Error'}), code


@app.route('/')
def entrypoint():
    return redirect(api.url_for(ApplicationList))


if __name__ == "__main__":
    app.run()