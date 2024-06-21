import json
from flask import Flask,render_template, request, redirect
from record import match_faces,mark_attendence,attendence
from model import trainer
import time


app=Flask(__name__)

@app.route("/attendence/login",methods=['GET'])
def login_get(): 
    return render_template('login.html')

@app.route("/attendence/login",methods=['POST'])
def login_post():
    if request.method == 'POST':
        with open('static/data/user_data.json','r') as user_data_file:
            user_data=user_data_file.read()
        user_data=json.loads(user_data)# json.loads convert json to dictionary
        data=user_data['login_details']
        print(request)
        print(request.form)
        userid = request.form['Userid']#request is a object which will store any data that is request we make
        password = request.form['Password']
        if userid in data and data[userid] == password:
            return redirect(f'/attendence/{userid}')#instead of rendering something , it send new request to url:redirect
        else:
            return render_template('login.html')

@app.route("/attendence/signup",methods=['GET'])
def signup_get():
        return render_template('sign_up.html')

@app.route("/attendence/signup",methods=['POST'])
def signup_post():
    with open('static/data/user_data.json','r') as user_data_file:
        user_data=user_data_file.read()
    user_data=json.loads(user_data)
    new_user={
        "firstname": request.form['Firstname'],
        "lastname":request.form['Lastname'],
        "userid" : request.form['Userid'],
        "password":request.form['Password']
    }
    user_data['users'].append(new_user)
    user_data['login_details'][request.form['Userid']]=request.form['Password']#
    with open('static/data/user_data.json','w') as user_data_file:
        user_data_file.write(json.dumps(user_data))# dict to json
    return redirect('/attendence/login')

@app.route("/attendence/<userid>",methods=['GET'])
def home(userid):
    current_user=dict()
    with open('static/data/user_data.json','r') as user_data_file:
        user_data=user_data_file.read()
    user_data=json.loads(user_data)# json to dict
    for user in user_data['users']:
        if user['userid'] == userid:
            current_user=user
            break
    return render_template('home.html',userid=userid,sections=current_user['sections'])

@app.route("/attendence/<userid>/take_attendence",methods=['GET'])
def get_section(userid):
    section=request.args['section']
    return redirect(f'/attendence/{userid}/take_attendence/{section}')

@app.route("/attendence/<userid>/take_attendence/<section>",methods=['GET'])
def take_attendence(userid,section):
    return render_template('attendence.html',userid=userid,section=section)

@app.route("/attendence/<userid>/take_attendence/<section>/start_attendence")
def start_attendence(userid,section):
    start=time.time()
    my_model,encoder,attendence_matrix=trainer(section)
    # folder_path=f'sections//{section}//{section}.csv'
    # dir=
    # for im_name in os.listdir(dir):
    present=match_faces("img_path",my_model,encoder)
    print(present)
    attendence_matrix=mark_attendence(attendence_matrix,present)
    print(attendence_matrix)
    attendence_list=attendence(section,attendence_matrix)
    print(attendence_list)
    end=time.time()
    print("time ",end-start)
    return render_template('table.html',student_list=attendence_list)

if __name__=="__main__":
    app.run(debug=True,port=5000)