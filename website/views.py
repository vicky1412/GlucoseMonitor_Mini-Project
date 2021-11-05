from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import mysqldb
from . import virtualpro


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html',user=current_user)

@views.route("/about")
def about_us():
    return render_template('about-us.html',user=current_user)

@views.route('/members', methods=['GET', 'POST'])
@login_required
def members():
    badge = 0
    search_results = mysqldb.view()
    search_multiple = virtualpro.globject.total_patient
    if request.method == 'POST':
        super_name = request.form.get('bar')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        gender = request.form.get('gender')
        age = request.form.get('age')
        contact = request.form.get('contact')
        address = request.form.get('address')
        room_no = request.form.get('room_no')
        bed_no = request.form.get('bed_no')

        try:
            if request.form.get("bar") == "add":
                if first_name:
                    mysqldb.insert(first_name, last_name, gender, age, contact, address, room_no, bed_no)
                    flash("Added Successfully.!", category='success')
                else:
                    flash("Insuffient Data!",category='danger')
                search_results = mysqldb.search(first_name)
            elif request.form.get("bar") == "search":
                if first_name or last_name or gender or age or contact or address or room_no or bed_no:
                    search_results = mysqldb.search(first_name, last_name, gender,age, contact, address, room_no, bed_no)
                else:
                    search_results=mysqldb.view()
            elif request.form.get("bar") == "showall":
                search_results = mysqldb.view()
            elif request.form.get("bar") == "update":
                if first_name:
                    mysqldb.update(first_name,last_name, gender,age, contact,address,room_no,bed_no)
                    flash("Updated Successfully.!", category='success')
                    search_results = mysqldb.search(first_name)
                else:
                    flash("Insufficient Data!",category='danger')
            elif request.form.get("bar") == "delete":
                mysqldb.delete(first_name,last_name)
                flash("Deleted Successfully.!", category='success')
                search_results = mysqldb.view()
            elif request.form.get("bar") == "deletemultiple" and first_name != '':
                first_name = first_name.split(',')
                for name in first_name:
                    mysqldb.delete(name)
                flash("Deleted Successfully.!", category='success')
                search_results = mysqldb.view()
            elif request.form.get("bar") == "showdetails":
                search_results = mysqldb.search_multiple(search_multiple)
            elif request.form.get("bar") == "filter":
                if last_name or gender or age:
                    search_results = mysqldb.filter(age,gender,last_name)
                else:
                    search_results=mysqldb.view()
            else:
                flash("Insufficient Data!", category='danger')
        except Exception:
            flash("Unkown error!", category='danger')


    return render_template("members.html", user=current_user,search_results=search_results,badge=virtualpro.globject.number)


@views.route("/ajax",methods=['GET','POST'])
@login_required
def ajax():
    return virtualpro.globject.number

