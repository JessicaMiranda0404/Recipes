from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.hike import Hike
from flask_app.models.user import User


@app.route('/new/hike')
def new_hike():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_hike.html',user=User.get_by_id(data))


@app.route('/create/hike',methods=['POST'])
def create_hike():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Hike.validate_hike(request.form):
        return redirect('/new/hike')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under30": int(request.form["under30"]),
        "date_made": request.form["date_made"],
        "user_id": session["user_id"]
    }
    hike.save(data)
    return redirect('/dashboard')

@app.route('/edit/hike/<int:id>')
def edit_hike(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_hike.html",edit=Hike.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/hike',methods=['POST'])
def update_hike():
    if 'user_id' not in session:
        return redirect('/logout')
    if not hike.validate_hike(request.form):
        return redirect('/new/hike')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under30": int(request.form["under30"]),
        "date_made": request.form["date_made"],
        "id": request.form['id']
    }
    hike.update(data)
    return redirect('/dashboard')

@app.route('/hike/<int:id>')
def show_hike(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_hike.html",hike=hike.get_one(data),user=User.get_by_id(user_data))

@app.route('/destroy/hike/<int:id>')
def destroy_hike(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    hike.destroy(data)
    return redirect('/dashboard')