from api import app, db
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import Schema, fields
from datetime import datetime

class ApplicationAdNetworkModel(db.Model):
    __tablename__ = 'application_adnetwork'
    application_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey('application.id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    ad_network_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey('ad_network.id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    score = db.Column(db.Float(), primary_key=True, default=0.0)
    ad_network = db.relationship('AdNetworkModel')
    last_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    @classmethod
    def find_by_ids(cls, application_network_id, ad_network_id):
        app_adn = cls.query.filter_by(application_id=application_network_id, ad_network_id=ad_network_id).first()
        return app_adn

    def update_score(self, score):
        self.score = score
        self.last_update = datetime.utcnow()
        try:
            db.session.commit()
        except Exception as e:
            app.logger.error('Could not update score : {e}'.format(e=e))
            db.session.rollback()

class ApplicationAdNetworkUpdateScoreSchema(Schema):
    id = fields.UUID(required=True)
    score = fields.Float(required=True)

class ApplicationAdNetworkUpdateScorePostSchema(Schema):
    ad_networks = fields.Nested(ApplicationAdNetworkUpdateScoreSchema, many=True, required=True)

class AdNetworkSchemaAddOrRemove(Schema):
    ad_networks = fields.List(fields.UUID, required=True)