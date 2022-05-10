from flask import Blueprint, render_template, redirect, url_for, request, flash, Response
from . import db
from .models import Video

main = Blueprint('main', __name__)

@main.route('/')
def movie():
    allMovies = Video.query.all()
    return render_template("movies.html", movies = allMovies)


@main.route('/insert', methods = ['POST'])
def insert():
    data = request.get_json()

    if not data:
        link = request.form['url']
        title = request.form['title']

        newVideo = Video(url = link, title = title)
        db.session.add(newVideo)
        db.session.commit()

        flash("Movie Inserted Successfully")

        return redirect(url_for('main.movie'))
    elif data:
        link = data['url']
        title = data['title']

        newVideo = Video(url = link, title = title)
        db.session.add(newVideo)
        db.session.commit()
        return Response("Movie added", 201, mimetype = 'application/json')


@main.route('/update', methods = ['POST', 'PUT'])
def update():
    if request.method == 'POST':
        updatedVideo = Video.query.get(request.form.get('id'))

        updatedVideo.url = request.form['url']
        updatedVideo.title = request.form['title']

        db.session.commit()
        flash("Movie Updated Successfully")

        return redirect(url_for('main.movie'))

    elif request.method == 'PUT':
        data = request.get_json()

        updatedVideo = Video.query.get(data['id'])

        updatedVideo.url = data['url']
        updatedVideo.title = data['title']
        db.session.commit()

        return Response("Movie Updated", status = 200)


@main.route('/delete/<int:id>/', methods = ['GET', 'DELETE'])
def delete(id):
    videoId = Video.query.get(id)
    db.session.delete(videoId)
    db.session.commit()

    if request.method == 'GET':
        flash("Movie Deleted Successfully")
        return redirect(url_for('main.movie'))
    else:
        response = Response("Movie Deleted", status = 200)
        return response