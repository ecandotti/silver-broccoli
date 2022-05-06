from flask import Blueprint, render_template, redirect, url_for, request, flash
import json
from . import db
from .models import Video

main = Blueprint('main', __name__)

@main.route('/', methods = ['GET'])
def movie():
    allData = Video.query.all()
 
    return render_template("movies.html", movies = allData)


@main.route('/insert', methods = ['POST'])
def insert():
    myData = json.loads(request.data)
    db.session.add(myData)
    db.session.commit()

    flash("Movie Inserted Successfully")

    return redirect(url_for('main.movie'))
 
 
@main.route('/update/<id>/', methods = ['PUT'])
def update(id):
    myData = Video.query.get(id)

    db.session.commit()
    flash("Movie Updated Successfully")

    return redirect(url_for('main.movie'))
 
 

@main.route('/delete/<id>/', methods = ['DELETE'])
def delete(id):
    myData = Video.query.get(id)
    db.session.delete(myData)
    db.session.commit()
    flash("Movie Deleted Successfully")
 
    return redirect(url_for('main.movie'))