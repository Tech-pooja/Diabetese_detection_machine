from django.shortcuts import render
from django.http import HttpResponse

import pickle



model_file_path = 'static/svm_model.pkl'

with open(model_file_path, 'rb') as f:
    model = pickle.load(f)

# Create your views here.

def home(request):
    #return HttpResponse("Hello I am WOrking") 
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def Prediction(request):

    if request.method == "POST":
        Pregnancies= request.POST.get("Pregnancies")
        Glucose= request.POST.get("Glucose")
        BloodPressure= request.POST.get("BloodPressure")
        SkinThickness= request.POST.get("SkinThickness")
        Insulin= request.POST.get("Insulin")
        BMI= request.POST.get("BMI")
        DiabetesPedigreeFunction= request.POST.get("DiabetesPedigreeFunction")
        Age= request.POST.get("Age")

        print(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)

        # input_data = (Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)

        # #changing the input data to a numpyarray
        # input_data_as_numpy_array=np.asarray(input_data)


        # #reshape the array as we are predicting for one instance
        # input_data_reshape=input_data_as_numpy_array.reshape(1,-1)

        # # standardized the input_data

        # std_data=scaler.transform(input_data_reshape)

        # print(std_data)

        # prediction=model.predict(std_data)

        # print(prediction)
        # res=""

        # if(prediction[0]==0):
        #     res="The peron is not Diabetic"
        # else:
        #     res="The person is diabetic"

        # pred=model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        # res=""
        # if(pred[0]==1):
        #     res="The patient is diabetic"
        # else:
        #     res="The patient is not diabetic"

        pred = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        res = ""
        if pred[0] == 1:  # Access the first element of the prediction array
            res = "The patient is diabetic"
        else:
            res = "The patient is not diabetic"


        
        print(pred)

        output={
            "output":res
        }

        return render(request,"Prediction.html",output)
    else:
        return render(request,"Prediction.html")
