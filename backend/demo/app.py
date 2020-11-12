import os
import json
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from demo.serializers import AlchemyEncoder

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# create the DB on demand
# @app.before_first_request
# def create_tables():
#     db.create_all()


class Index(Resource):
    def get(self):
        ret = []
        res = User.query.all()
        for user in res:
            ret.append(
                {
                    'username': user.username,
                    'email': user.email
                }
            )
        return ret, 200


def create_app() -> Flask:
    app = Flask(__name__)
    db.init_app(app)
    api = Api(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
        os.getenv('DB_USER', 'demo_user'),
        os.getenv('DB_PASSWORD', 'demo_password'),
        os.getenv('DB_HOST', 'database'),
        os.getenv('DB_NAME', 'demo'),
    )
    api.add_resource(Index, '/')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", debug=False)
