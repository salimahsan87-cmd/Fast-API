from fastapi import FastAPI , HTTPException
from pydantic import Field , BaseModel
from tensorflow.keras.models import load_model
import pandas as pa
import numpy as np
import joblib as jb

app = FastAPI(title='Diabetes')

model = load_model('diabetes_kaggle.h5',compile=False)
#model = jb.load('diabetes_random.pkl')

@app.get('/')
def message() :
    return {'message' : 'api is running'}

class User(BaseModel) :

    gender : str = Field(min_length=1)
    age : float = Field(gt=0)
    hypertension : int = Field(ge=0 , le=1)
    heart_disease : int = Field(ge=0 , le=1)
    smoking_history : str = Field(min_length=1)
    bmi : float = Field(gt=0)
    HbA1c_level : float = Field(gt=0)
    blood_glucose_level : int = Field(gt=0)

@app.post('/predict')
def predict_robot(user : User) :

    gender = [user.gender.lower().strip()]
    age = [user.age]
    smoking_history = [user.smoking_history.lower().strip()]
    bmi = [user.bmi]
    HbA1c_level = [user.HbA1c_level]
    blood_glucose_level = [user.blood_glucose_level]

    message_smoking = ['no info' , 'never' , 'former' , 'current' , 'ever' , 'not current']
    message_gender = ['female' , 'male' , 'other']

    if gender[0] not in message_gender :
        raise HTTPException(status_code=404,detail=f'please enter your gender : {message_gender}')

    if smoking_history[0] not in message_smoking :
        raise HTTPException(status_code=404,detail=f'please enter your smoking history : {message_smoking}')

    x_file_gender = [0 if i == 'female' else 1 if i == 'male' else 2 for i in gender]
    x_file_age = [0 if j < 18 else 1 if j >= 18 and j < 30 else 2 if j >= 30 and j < 40 else 3 if j >= 40 and j < 50 else 4 if j >= 50 and j < 60 else 5 if j >= 60 and j < 70 else 6 for j in age]
    x_file_bmi = [0 if t < 10 else 1 if t >= 10 and t < 20 else 2 if t >= 20 and t < 30 else 3 if t >= 30 and t < 40 else 4 if t >= 40 and t < 50 else 5 if t >= 50 and t < 60 else 6 for t in bmi]
    x_file_smoking_history = [0 if h == 'never' else 1 if h == 'no info' else 2 if h == 'not current' else 3 if h == 'former' else 4 if h == 'ever' else 5 for h in smoking_history]
    x_file_HbA1c_level = [0 if n < 3.5 else 1 if n >= 3.5 and n < 4.5 else 2 if n >= 4.5 and n < 5 else 3 if n >= 5 and n < 6.5 else 4 if n >= 6.5 and n < 7 else 5 if n >= 7 and n < 8.5 else 6 for n in HbA1c_level]
    x_file_blood_glucose_level = [0 if a < 80 else 1 if a >= 80 and a < 95 else 2 if a >= 95 and a < 100 else 3 if a >= 100 and a < 150 else 4 if a >= 150 and a < 200 else 5 if a >= 200 and a < 250 else 6 for a in blood_glucose_level]


    file = pa.DataFrame({
        'gender' : x_file_gender,
        'age' : x_file_age,
        'hypertension' : [user.hypertension],
        'heart_disease' : [user.heart_disease],
        'smoking_history' : x_file_smoking_history,
        'bmi' : x_file_bmi,
        'HbA1c_level' : x_file_HbA1c_level,
        'blood_glucose_level' : x_file_blood_glucose_level
    })
    #file = file[model.feature_names_in_]
    select_prediction = model.predict(file)
    result = select_prediction.tolist()
    array = []

    for i in result :
        array.append(i.index(max(i)))
    
    print(array)
    print(result)
    print(max(result[0]))

    context = '' 
    if array[0] == 1 :
        context = 'Yes'
    else : 
        context = 'No'    


    return {
        "predicted_diabetes": context
    }
    


