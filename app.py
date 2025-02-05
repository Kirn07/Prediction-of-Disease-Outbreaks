import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title= "Prediction of Disease Outbreaks", layout='wide', page_icon="😵‍💫")

working_dir = os.path.dirname(os.path.abspath(__file__))


diabetes_model = pickle.load(open(r"C:\\Users\\Admin\\Downloads\\AICTE\\datasets\\training_models\\diabetes_model.sav", 'rb'))

heart_model = pickle.load(open(r"C:\\Users\\Admin\\Downloads\\AICTE\\datasets\\training_models\\heart_model.sav", 'rb'))

parkinsons_model = pickle.load(open(r"C:\\Users\\Admin\\Downloads\\AICTE\\datasets\\training_models\\parkinsons_model.sav", 'rb'))


with st.sidebar:
    selection = option_menu("Prediction of Disease OutBreaks System", ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'], 
                            menu_icon = "hospital-fill",
                            icons = ['activity', 'heart', 'person'],
                            default_index = 0)
    

if selection == 'Diabetes Prediction':
    st.title("Diabetes Prediction")
    col, coll, col3 = st.columns(3)
    with col:
        Pregnancies = st.text_input('Number of Pregnancies')
    with coll:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
    with col:
        SkinThickness = st.text_input("Skin Thickness Value")
    with coll:
        Insulin = st.text_input("Insulin Level value")
    with col3:
        BMI = st.text_input("BMI Value")
    with col:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    with coll:
        Age = st.text_input("Age Value")


    didb =" "

    if st.button('Predict'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            didb = " This Person is Diabetes"
        else:
            didb = "This person has not diabetic"
        
    st.success(didb)

if selection == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction")
    colm, collm, colm3 = st.columns(3)
    with colm:
        age = st.text_input('Age')
    with collm:
        sex = st.text_input("Sex")
    with colm3:
        cp = st.text_input("Chest Pain types")
    with colm:
        trestbps = st.text_input("Resting Blood Pressure")
    with collm:
        chol = st.text_input("Serum Cholestrol level")
    with colm3:
        fbs = st.text_input("Fasting blood sugar")
    with colm:
        restecg = st.text_input("Resting Electrocardiographic results")
    with collm:
        thalach = st.text_input("Max Heart Acheived")
    with colm3:
        exang = st.text_input("Exercise Induced Angina")
    with colm3:
        oldpeak = st.text_input("ST depression induced by exercise")
    with collm:
        ca = st.text_input("Number of major vessels colored by fluoroscopy")
    with colm3:
        thal = st.text_input("thalassemia")
    

    heart_dia =" "

    if st.button('Predict'):
        user_input3 = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, ca, thal]

        user_input3 = [float(x) for x in user_input3]

        heart_prediction = heart_model.predict([user_input3])

        if heart_prediction[0] == 1:
            heart_dia = " This Person has heart disease"
        else:
            heart_dia = "This person has not heart disease"
        
    st.success(heart_dia)



if selection == 'Parkinsons Prediction':
    st.title("Parkinsons Prediction")
    coln, colln, coln3, coln4, coln5 = st.columns(5)
    with coln:
        fo = st.text_input("MDVP:Fo(Hz)")
    with colln:
        fhi = st.text_input("MDVP:Fhi(Hz)")
    with coln3:
        flo = st.text_input("MDVP:Flo(Hz)")
    with coln:
        ppe = st.text_input("MDVP:Jitter(%)")
    with colln:
        rppq = st.text_input("MDVP:Jitter(Abs)")
    with coln3:
        dfa = st.text_input("MDVP:RAP")
    with coln4:
        jdp = st.text_input("MDVP:PPQ")
    with coln5:
        rdp = st.text_input("Jitter:DDP")

    with coln:
        ddp = st.text_input("MDVP:Shimmer")
    with colln:
        RPDE = st.text_input("MDVP:Shimmer(dB)")
    with coln3:
        DFA = st.text_input("Shimmer:APQ3")
    with coln4:
        spread1 = st.text_input("Shimmer:APQ5")
    with coln5:
        spread2 = st.text_input("Shimmer:DDA")
    with coln:
        D2= st.text_input("NHR")
    with colln:
        PPE = st.text_input("HNR")
    with coln3:
        r = st.text_input("RPDE")
    with coln4:
        ppq = st.text_input("DFA")
    with coln5:
        apq = st.text_input("spread1")
    with coln:
        apq3 = st.text_input("spread2")
    with colln:
        apq4 = st.text_input("AD2")
    with coln3:
        apq5 = st.text_input("PPE")
    


    parki_dia =" "

    if st.button('Predict'):
        user_input4 = [fo, fhi, flo,ppe,rppq,dfa,jdp,rdp,ddp,RPDE,DFA,spread1,spread2,D2,PPE,r,ppq, apq, apq3, apq4, apq5]

        user_input4 = [float(x) for x in user_input4]

        park_prediction = parkinsons_model.predict([user_input4])

        if park_prediction[0] == 1:
            parki_dia = " This Person has Parkinsons"
        else:
            parki_dia = "This person has not Parkinsons"
        
    st.success(parki_dia)




