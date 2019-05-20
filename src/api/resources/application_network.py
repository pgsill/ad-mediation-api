from flask_restful import Resource, request
from api.models import (
    ApplicationModel, AdNetworkSchemaAddOrRemove, ApplicationAdNetworkUpdateScorePostSchema, ApplicationAdNetworkModel)
import api
from marshmallow import ValidationError


class ApplicationNetwork(Resource):

    def get(self, id):
        application = ApplicationModel.find_by_id(id)
        if application:
            api.app.logger.info('Getting networks from {app_name}'.format(app_name=application.name))
            networks = application.convert_ad_networks_to_json()
            return networks, 200
        return {'message': 'application not found'}, 404

    def post(self, id):
        schema = AdNetworkSchemaAddOrRemove(strict=True)
        try:
            app_adn_data, _ = schema.load(request.get_json())
        except ValidationError as e:
            return e.messages, 400

        ad_networks_ids = app_adn_data['ad_networks']

        application = ApplicationModel.find_by_id(id)
        if application:
            application.add_ad_networks(ad_networks_ids)
            return application.json(), 200

        return {'message': 'application not found'}, 404

    def delete(self, id):
        schema = AdNetworkSchemaAddOrRemove(strict=True)
        try:
            app_adn_data, errors = schema.load(request.get_json())
        except ValidationError as e:
            return e.messages, 400

        application = ApplicationModel.find_by_id(id)
        if application:
            application.remove_ad_networks(app_adn_data['ad_networks'])
            return application.json(), 200
        return {'message': 'application not found'}, 404

    def put(self, id):
        schema = ApplicationAdNetworkUpdateScorePostSchema(strict=True)
        try:
            app_adn_data, _ = schema.load(request.get_json())
        except ValidationError as e:
            return e.messages, 400

        networks_not_found = list()
        application = ApplicationModel.find_by_id(id)
        if application:
            for app_adn in app_adn_data['ad_networks']:
                app_adn_to_update = ApplicationAdNetworkModel.find_by_ids(application.id, app_adn['id'])
                if app_adn_to_update:
                    app_adn_to_update.update_score(app_adn['score'])
                else:
                    networks_not_found.append(app_adn['id'])

            return {
                'updated': application.convert_ad_networks_to_json(),
                'errors': 'Networks {networks_not_found} not found'.format(networks_not_found=networks_not_found) if len(networks_not_found) > 0 else list()
            }, 200

        return {'message': 'application not found'}, 404