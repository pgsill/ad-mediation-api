from api import db, app
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .ad_network import AdNetworkModel
from .application_adnetwork import ApplicationAdNetworkModel
from operator import itemgetter
from marshmallow import Schema, fields


class ApplicationModel(db.Model):
    __tablename__ = 'application'
    id = db.Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid4)
    name = db.Column(db.String(120), unique=True, nullable=False)
    code = db.Column(db.String(5), unique=True, nullable=False)
    application_adnetwork = db.relationship('ApplicationAdNetworkModel', cascade='all')

    def json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "code": self.code,
            "adNetworks": self.convert_ad_networks_to_json()
        }

    def convert_ad_networks_to_json(self):
        ad_networks_list = list()
        for app_adn in self.application_adnetwork:
            ad_networks_list.append(self.application_ad_network_to_json(app_adn))
        return ad_networks_list

    def application_ad_network_to_json(self, application_ad_network):
        return {
                'id': str(application_ad_network.ad_network.id),
                'name': application_ad_network.ad_network.name,
                'code': application_ad_network.ad_network.code,
                'endpoint': application_ad_network.ad_network.endpoint,
                'score': application_ad_network.score
            }

    def get_ad_networks_ordered_by_score(self):
        ad_networks = self.convert_ad_networks_to_json()
        ordered_list_by_score = sorted(ad_networks, key=itemgetter('score'), reverse=True)
        return ordered_list_by_score

    def add_ad_networks(self, ad_network_id_list):
        ad_networks_to_add = [AdNetworkModel.find_by_id(ad_network_id) for ad_network_id in ad_network_id_list]
        try:
            for ad_network_to_add in ad_networks_to_add:
                if not ad_network_to_add or ApplicationAdNetworkModel.find_by_ids(self.id, ad_network_to_add.id):
                    continue
                app_adn = ApplicationAdNetworkModel()
                app_adn.ad_network = ad_network_to_add
                self.application_adnetwork.append(app_adn)
            db.session.commit()
        except Exception as e:
            app.logger.error(
                'Something went wrong when trying to add ad_networks {ad_networks} to application {application} : {e}'.format(
                    ad_networks=ad_network_id_list,
                    application=self,
                    e=e))
            db.session.rollback()

    def remove_ad_networks(self, ad_network_id_list):
        try:
            app_adn_to_remove = [ApplicationAdNetworkModel.find_by_ids(self.id, ad_network_id) for ad_network_id in ad_network_id_list]
            for app_adn in app_adn_to_remove:
                if not app_adn:
                    continue
                db.session.delete(app_adn)
            db.session.commit()
        except Exception as e:
            app.logger.error(
                'Something went wrong when trying to remove ad_networks {ad_networks} from application {application} : {e}'.format(
                    ad_networks=ad_network_id_list,
                    application=self, e=e))
            db.session.rollback()

    def __repr__(self):
        return '<Application {name}>'.format(name=self.name)

    @classmethod
    def find_by_id(cls, id):
        application = cls.query.filter_by(id=id).first()
        return application

    @classmethod
    def find_by_name(cls, name):
        application = cls.query.filter_by(name=name).first()
        return application

    @classmethod
    def find_all(cls):
        applications = cls.query.all()
        return applications

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class ApplicationAddOrUpdateSchema(Schema):
    name = fields.Str(required=True)
    code = fields.Str(required=True)
