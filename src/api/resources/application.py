from flask_restful import Resource, request
from marshmallow import ValidationError
from api.models import ApplicationModel, ApplicationAddOrUpdateSchema
from api import app


class Application(Resource):

    def get(self, id):
        application = ApplicationModel.find_by_id(id)
        if application:
            app.logger.info('Returning application {application}'.format(application=application.json()))
            return application.json(), 200
        return {'message': 'application not found'}, 404

    def delete(self, id):
        application = ApplicationModel.find_by_id(id)
        if application:
            application.delete()
            app.logger.info('Deleted application {application}'.format(application=application.json()))
            return {'message': 'application deleted'}, 200
        return {'message': 'application not found'}, 404

    def put(self, id):
        schema = ApplicationAddOrUpdateSchema(strict=True)
        try:
            app_data, _ = schema.load(request.get_json())
        except ValidationError as e:
            return e.messages, 400

        application = ApplicationModel.find_by_id(id)
        if application:
            application.name = app_data['name']
            application.code = app_data['code']
            application.save()
            app.logger.info('Updated application {application}'.format(application=application.json()))
            return application.json()

        return {'message': 'application not found'}, 404


class ApplicationList(Resource):

    def get(self):
        applications = [application.json() for application in ApplicationModel.find_all()]
        return applications, 200

    def post(self):
        schema = ApplicationAddOrUpdateSchema(strict=True)
        try:
            app_data, _ = schema.load(request.get_json())
        except ValidationError as e:
            return e.messages, 400

        if ApplicationModel.find_by_name(app_data["name"]):
            return {'message': 'An item with name {name} already exists.'.format(name=app_data["name"])}, 400

        application = ApplicationModel(**app_data)

        application.save()

        return application.json(), 201
