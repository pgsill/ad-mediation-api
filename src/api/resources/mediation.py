from flask_restful import Resource, reqparse
from api.models import ApplicationModel


class Mediation(Resource):

    def get(self, id):
        application = ApplicationModel.find_by_id(id)
        if application:
            mediated_list = application.get_ad_networks_ordered_by_score()
            return mediated_list, 200
        return {'message': 'application not found'}, 404
