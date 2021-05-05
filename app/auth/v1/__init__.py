from app import api
from flask import Blueprint
from flask_restful import Api

from app.auth.v1.views.routine_views import Routine



version1 = Blueprint('auth_v1', __name__,url_prefix='/api/v1')

app= api(version1,catch_all_404=True)

