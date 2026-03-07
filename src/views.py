from flask import render_template, abort
from models import courses

def index():
    return render_template('index.html', courses=courses)

def course(course_id):
    idx = int(course_id) - 1
    if idx < 0 or idx >= len(courses):
        abort(404)
    return render_template('course.html', course=courses[idx])

def contact():
    return render_template('contact.html')