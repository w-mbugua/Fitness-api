
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

