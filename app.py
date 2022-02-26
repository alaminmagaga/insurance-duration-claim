import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model= pickle.load(open('insurance_duration.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/duration',methods=["POST"])
def duration():
    gender = request.form['Gender']
    if gender=="Male":
        gender=0
    elif gender=="Female":
        gender=1
        
    age=request.form['Age']
    age=int(age)
    
    np=request.form['No_Pol']
    np=int(np)
    
 
    carc = request.form['Car_Category']
    if carc=="Saloon":
        carc=0
    elif carc=="JEEP":
        carc=1
    elif carc=="Truck":
        carc=2
    elif carc=="Mini Bus":
        carc=3
    elif carc=="Pick Up":
        carc=4
    elif carc=="Wagon":
        carc=5
    elif carc=="Motorcycle":
        carc=6
    elif carc=="Shape Of Vehicle Chasis":
        carc=7
    elif carc=="Station 4 Wheel":
        carc=8
    elif carc=="Pick Up > 3 Tons":
        carc=9
    elif carc=="CAMRY CAR HIRE":
        carc=10
    elif carc=="Tipper Truck":
        carc=11
        
    
    
    
    scm = request.form['Subject_Car_Make']
    scm=int(scm)

    state=request.form['State']
    if state=="Abia":
        state=0
    elif state=="Adamawa":
        state=1
    elif state=="Akwa Ibom":
        state=2
    elif state=="Anambra":
        state=3
    elif state=="Bauchi":
        state=4
    elif state=="Bayelsa":
        state=5
    elif state=="Benue":
        state=6
    elif state=="Borno":
        state=7
    elif state=="Cross River":
        state=8
    elif state=="Delta":
        state=9
    elif state=="Ebonyi":
        state=10
    elif state=="Edo":
        state=11
    elif state=="Ekiti":
        state=12
    elif state=="Enugu":
        state=13
    elif state=="Gombe":
        state=14
    elif state=="Imo":
        state=15
    elif state=="Jigawa":
        state=16
    elif state=="Kaduna":
        state=17
    elif state=="Kano":
        state=18
    elif state=="Katsina":
        state=19
    elif state=="Kebbi":
        state=20
    elif state=="Kogi":
        state=21
    elif state=="Kwara":
        state=22
    elif state=="Lagos":
        state=23
    elif state=="Nasarawa":
        state=24
    elif state=="Niger":
        state=25
    elif state=="Ogun":
        state=26
    elif state=="Ondo":
        state=27
    elif state=="Osun":
        state=28
    elif state=="Oyo":
        state=29
    elif state=="Plateau":
        state=30
    elif state=="Rivers":
        state=31
    elif state=="Sokoto":
        state=32
    elif state=="Taraba":
        state=33
    elif state=="Yobe":
        state=34
    elif state=="Zamfara":
        state=35
    elif state=="Abuja":
        state=36

       
    pn=request.form['ProductName']
    if pn=="Car Classic":
        pn=0
    elif pn=="CarSafe":
        pn=1
    elif pn=="Customized Motor":
        pn=2
    elif pn=="Car Plus":
        pn=3
    elif pn=="CVTP":
        pn=3
    elif pn=="CarFlex":
        pn=4
    elif pn=="Muuve":
        pn=5
    elif pn=="Motor Cycle":
        pn=6
    
    
    
    ty=request.form['Transaction Year']
    ty=int(ty)
    
    psy=request.form['Policy Start Year']
    psy=int(psy)
    
    pey=request.form['Policy End Year']
    pey=int(pey)
    
    
    
    int_features = [gender,age,np,carc,scm,state,pn,ty,psy,pey]
    final_features = [(int_features)]
    prediction = model.predict(final_features).round(2)
		

	
    return render_template('result.html', prediction_text='The Passenger {}'.format(prediction[0]))



if __name__ == "__main__":
    app.run(debug=True)
    
    
