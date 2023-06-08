
from flask import Flask, request, render_template
from sklearn.ensemble import RandomForestClassifier
import os
import pickle
import numpy as np
# prediction function
def ValuePredictor(to_predict_list):
    
    to_predict = np.array(to_predict_list).reshape(1, 15)
    loaded_model = pickle.load(open("saved_model_RF.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

app=Flask(__name__,template_folder='templates')

@app.route('/')
def home():
	return render_template("index.html")	

@app.route('/result', methods = ['POST'])
def result():
	if request.method == 'POST':
		to_predict_list = request.form.to_dict()
		
		to_predict_list = list(to_predict_list.values())
		to_predict_list = list(map(int, to_predict_list))
		print(to_predict_list)
	   
		if result== 1:
			prediction ='Person is Eligible for loan Using RF'
		else:
			prediction ='Person is Not Eligible for loan Using RF'		
		return render_template("result.html", prediction = prediction)

if __name__ == "__main__":
    
    app.run(host="0.0.0.0",port=8080,debug=True)
	