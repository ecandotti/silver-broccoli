from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import Video

main = Blueprint('main', __name__)

@main.route('/')
def movie():
    allData = Video.query.all()
 
    return render_template("movies.html", movies = allData)
 

@main.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        lien = request.form['url']
        title = request.form['title']
 
        myData = Video(url=lien, title = title)
        db.session.add(myData)
        db.session.commit()
 
        flash("Movie Inserted Successfully")
 
        return redirect(url_for('main.movie'))
 
 
@main.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        myData = Video.query.get(request.form.get('id'))
 
        myData.url = request.form['url']
        myData.title = request.form['title']

 
        db.session.commit()
        flash("Movie Updated Successfully")
 
        return redirect(url_for('main.movie'))
 
 

@main.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    myData = Video.query.get(id)
    db.session.delete(myData)
    db.session.commit()
    flash("Movie Deleted Successfully")
 
    return redirect(url_for('main.movie'))