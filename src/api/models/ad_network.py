from api import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from marshmallow import Schema, fields


class AdNetworkModel(db.Model):
    __tablename__ = 'ad_network'
    id = db.Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid4)
    name = db.Column(db.String(120), unique=True, nullable=False)
    code = db.Column(db.String(5), unique=True, nullable=False)
    endpoint = db.Column(db.String(120), nullable=True)
    application_adnetwork = db.relationship('ApplicationAdNetworkModel', cascade='all')

    def json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'code': self.code,
            'endpoint': self.endpoint
        }

    def __repr__(self):
        return '<AdNetwork {name}>'.format(name=self.name)

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


class AdNetworkAddOrUpdateSchema(Schema):
    name = fields.Str(required=True)
    code = fields.Str(required=True)
    endpoint = fields.Str(required=True)
