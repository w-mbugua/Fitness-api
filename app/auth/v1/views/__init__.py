from flask import Blueprint
from flask_restful import Api

from app.auth.v1.views.user_views import Users

version1 = Blueprint('auth_v1', __name__ , url_prefix='/api/v1')

app = Api(version1 , catch_all_404s=True)

app.add_resource(Users, '/auth/users' , strict_slashes= False)