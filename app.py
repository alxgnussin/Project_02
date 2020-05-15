# -*- coding: utf-8 -*-
# Python 3.7.7 required
from flask import Flask, render_template, request

from operations import goals, teachers, week_time, teachers_generator
from operations import select_profile, select_goals, schedule, week_days, append_json_data

app = Flask(__name__)
app.secret_key = 'Y&blNBvsINyA5irX^OwZ*RkbWQSnT~pM'


@app.route('/')
def render_index():
    random_teachers = []
    for i in teachers_generator():
        random_teachers.append(select_profile('id', i))
    return render_template(
        'index.html',
        goal=goals(),
        random_teachers=random_teachers
    )


@app.route('/goals/<goal>/')
def render_goals(goal):
    goal_teachers = []
    for dic in teachers():
        if goal in dic['goals']:
            goal_teachers.append(dic)
    return render_template(
        'goal.html',
        goal=goals()[goal].lower(),
        goal_teachers=goal_teachers
    )


@app.route('/profiles/<trainer_id>/')
def render_profiles(trainer_id):
    profile = select_profile('id', int(trainer_id))
    teachers_goals = select_goals(profile['goals'])
    free = schedule(profile['free'])
    return render_template(
        'profile.html',
        dic=profile,
        goals=teachers_goals,
        sked=free
    )


@app.route('/request/')
def render_request():
    return render_template('request.html', goal=goals(), time=week_time())


@app.route('/request_done/', methods=['POST'])
def render_request_done():
    radio_goal = request.form.get('goal')
    radio_time = request.form.get('time')
    client_name = request.form.get('clientName')
    phone = request.form.get('clientPhone')
    if client_name and phone:
        new_record = {
            'clientName': client_name,
            'clientPhone': phone,
            'clientGoal': radio_goal,
            'clientTime': radio_time
        }
        append_json_data('request.json', new_record)
        return render_template('request_done.html', goal=goals()[radio_goal], time=radio_time, name=client_name,
                               phone=phone)
    else:
        return render_request()


@app.route('/booking/<trainer_id>/<day>/<lesson_time>/')
def render_booking(trainer_id, day, lesson_time):
    teacher = select_profile('id', int(trainer_id))
    return render_template(
        'booking.html',
        teacher_name=teacher['name'],
        picture=teacher['picture'],
        id=trainer_id,
        day=day,
        day_ru=week_days()[day],
        lesson_time=lesson_time
    )


@app.route('/booking_done/', methods=['POST'])
def render_booking_done():
    trainer_id = request.form.get('clientTeacher')
    day = request.form.get('clientWeekday')
    lesson_time = request.form.get('clientTime')
    client_name = request.form.get('clientName')
    phone = request.form.get('clientPhone')
    if client_name and phone:
        new_record = {
            'clientName': client_name,
            'clientPhone': phone,
            'clientTeacher': trainer_id,
            'clientWeekday': day,
            'clientTime': lesson_time
        }
        append_json_data('booking.json', new_record)
        return render_template('booking_done.html', day=day, time=lesson_time, name=client_name, phone=phone)
    else:
        return render_booking(trainer_id, day, lesson_time)


if __name__ == '__main__':
    app.run(debug=True)
