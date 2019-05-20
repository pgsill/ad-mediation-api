from flask import jsonify
from flask_restful import Resource, request
from marshmallow import ValidationError

from api.models import AdNetworkModel, AdNetworkAddOrUpdateSchema
from api import app


class AdNetwork(Resource):

    def get(self, id):
        ad_network = AdNetworkModel.find_by_id(id)
        if ad_network:
            app.logger.info('Returning ad_network {adn}'.format(adn=ad_network.json()))
            return ad_network.json(), 200
        return {'message': 'ad_network not found'}, 404

    def delete(self, id):
        ad_network = AdNetworkModel.find_by_id(id)
        if ad_network:
            ad_network.delete()
            app.logger.info('Deleted ad_network {ad_network}'.format(ad_network=ad_network.json()))
            return {'message': 'ad_network deleted'}, 200
        return {'message': 'ad_network not found'}, 404

    def put(self, id):
        schema = AdNetworkAddOrUpdateSchema(strict=True)
        try:
            ad_network_data, _ = schema.load(request.get_json())
        except ValidationError as e:
            return e.messages, 400

        ad_network = AdNetworkModel.find_by_id(id)
        if ad_network:
            ad_network.name = ad_network_data['name']
            ad_network.code = ad_network_data['code']
            ad_network.endpoint = ad_network_data['endpoint']
            ad_network.save()
            app.logger.info('Updated ad_network {ad_network}'.format(ad_network=ad_network.json()))
            return ad_network.json()

        return {'message': 'ad_network not found'}, 404


class AdNetworkList(Resource):

    def get(self):
        ad_networks = [ad_network.json() for ad_network in AdNetworkModel.find_all()]
        return ad_networks, 200

    def post(self):
        schema = AdNetworkAddOrUpdateSchema(strict=True)
        try:
            ad_network_data, _ = schema.load(request.get_json())
        except ValidationError as e:
            return e.messages, 400
        if AdNetworkModel.find_by_name(ad_network_data['name']):
            return {'message': 'An ad_network with name {name} already exists.'.format(name=ad_network_data["name"])}, 400

        ad_network = AdNetworkModel(**ad_network_data)

        ad_network.save()

        return ad_network.json(), 201
