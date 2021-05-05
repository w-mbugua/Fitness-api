import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False'
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    DEBUG = False
    TESTING = False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://name:password@localhost/test_db_name'


class StagingConfig(Config):
    DEBUG = True


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://name:password@localhost/db_name'
    DEBUG = True

    @app.route('/api/v1/workout/<id>', methods=['PUT'])
def update_workout_by_id(id):
   data = request.get_json()
   get_workout = workout.query.get(id)
   if data.get('title'):
       get_workout.title = data['title']
   if data.get('workout_description'):
        get_workout.workout_description = data['workout_description']
    db.session.add(get_workout)
   db.session.commit()
   workout_schema = workoutSchema(only=['id', 'title', 'workout_description'])
   workout = workout_schema.dump(get_workout)

   return make_response(jsonify({"workout": workout}))




config_options = {
    'development': DevConfig,
    'staging': StagingConfig,
    'production': ProdConfig,
    'test': TestConfig
}