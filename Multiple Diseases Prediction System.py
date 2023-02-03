# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 23:05:39 2023

@author: Pearry
"""

import pickle
import streamlit as st
from  streamlit_option_menu import option_menu

diabetes_model=pickle.load(open('C:/Users/Pearry/Desktop/Multiple Diseases Prediction/saved models/Trained_model.sav','rb'))
heart_model=pickle.load(open('C:/Users/Pearry/Desktop/Multiple Diseases Prediction/saved models/Heart_Disease.sav','rb'))
breast_cancer_model=pickle.load(open('C:/Users/Pearry/Desktop/Multiple Diseases Prediction/saved models/Breast Cancer Classifier & Neural Network.sav','rb'))
#sidebar for navigation

with st.sidebar:
    selected= option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction','Breast Cancer Prediction'],default_index=0)
    
if selected=='Diabetes Prediction':
    
    #page title
    st.title('Diabetes Prediction Using ML ')
    
    #columns for input fields
    col1,col2,col3=st.columns(3)
    
     
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies:')
    
    with col2:
        Glucose=st.text_input('Glucose Levels:')
    
    with col3:
        BloodPressure=st.text_input('Blood Pressure value:')
   
    with col1:
        SkinThickness=st.text_input('SkinThickness value')
    
    with col2:
         Insulin=st.text_input('Insulin Levels')
    
    with col3:
        BMI=st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction=st.text_input('DiabetsPedigreeFunction')
    with col2:
        Age=st.text_input('Age')
    
    #code predciton
    diab_diagnosis=''
    
    if st.button('Diabetes Test Result'):
        diabetes_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age ]])
        
        if diabetes_prediction[0]==1:
            diab_diagnosis='This person is diabetic'
            
        else:
            diab_diagnosis='This person is not Diabetic'
            
    st.success(diab_diagnosis)
             
        
        
if selected=='Heart Disease Prediction':
    
    #page title
    st.title('Heart Disease Prediction Using ML ') 
    
    #columns
    col1,col2,col3=st.columns(3)
    with col1:
        Age=st.text_input('Age')
    
    with col2:
        Sex=st.text_input('Sex')
   
    with col3:
        cp=st.text_input('CP')
    
    with col1:
        trestbps=st.text_input('T Rest Bps')
    
    with col2:
        chol=st.text_input('Cholesterol')
   
    with col3:
        fbs=st.text_input('fbs')
        
    with col1:
         restecg=st.text_input('Rest ECG')
     
    with col2:
         thalach=st.text_input('thalac')
    
    with col3:
         exang=st.text_input('exang')
      
    with col1:
          oldpeak=st.text_input('oldpeak')
       
    with col2:
           slope=st.text_input('Slope')
      
    with col3:
           ca=st.text_input('CA')   
           
    with col1:
        thal=st.text_input('thal')
        
    if st.button('Show Heart Test Results'):
        heart_diagnosis=''
        
        heart_disease_pred=heart_model.predict([[Age,Sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if heart_disease_pred[0]==0:
            heart_diagnosis='No heart illness'
        else:
            heart_diagnosis='This is a Sickneesss'
            
        st.success(heart_diagnosis)

if selected=='Breast Cancer Prediction':
    
    #page title
    st.title('Breast Cancer Prediction Using ML ') 
    
    #columns
    col1,col2,col3=st.columns(3)
    with col1:
       radius_mean=st.text_input('radius_mean')
    
    with col2:
       texture_mean=st.text_input('texture_mean')
   
    with col3:
       perimeter_mean=st.text_input('perimeter_mean')
    
    with col1:
       area_mean=st.text_input('area_mean')
    
    with col2:
       smoothness_mean=st.text_input('smoothness_mean')
   
    with col3:
       compactness_mean=st.text_input('compactness_mean')
        
    with col1:
       concavity_mean=st.text_input('concavity_mean')
     
    with col2:
        concave_points_mean=st.text_input('concave points_mean')
    
    with col3:
       symmetry_mean=st.text_input('symmetry_mean')
      
    with col1:
        fractal_dimension_mean=st.text_input('fractal_dimension_mean')
       
    with col2:
           radius_se=st.text_input('radius_se')
      
    with col3:
         texture_se=st.text_input('texture_se')   
           
    with col1:
       perimeter_se=st.text_input('perimeter_se')
        
    
    with col1:
       area_se=st.text_input('area_se')
    
    with col2:
       smoothness_se=st.text_input('smoothness_se')
   
    with col3:
       compactness_se=st.text_input('compactness_se')
        
    with col1:
         concavity_se=st.text_input('concavity_se')
     
    with col2:
         concave_points_se=st.text_input('concave points_se')
    
    with col3:
        symmetry_se=st.text_input('symmetry_se')
      
    with col1:
        fractal_dimension_se=st.text_input('fractal_dimension_se')
       
    with col2:
          radius_worst=st.text_input('radius_worst')
      
    with col3:
         texture_worst=st.text_input('texture_worst')   
           
    with col1:
       perimeter_worst=st.text_input('perimeter_worst')
        
    with col1:
      area_worst=st.text_input('area_worst')
     
    with col2:
       smoothness_worst=st.text_input('smoothness_worst')
    
    with col3:
     compactness_worst=st.text_input('compactness_worst')
      
    with col1:
      concavity_worst=st.text_input('concavity_worst')
   
    with col2:
      concave_points_worst=st.text_input('concave points_worst')
  
    with col3:
      symmetry_worst=st.text_input('symmetry_worst')
    
    with col1:
       fractal_dimension_worst=st.text_input('fractal_dimension_worst')
     
       
    if st.button('Show Heart Test Results'):
        breast_cancer_diagnosis=''
        
        breast_cancer_pred=breast_cancer_model.predict([[radius_mean,
        texture_mean,
        perimeter_mean,
        area_mean,
        smoothness_mean,
        compactness_mean,
        concavity_mean,
        concave_points_mean,
        symmetry_mean,
        fractal_dimension_mean,
        radius_se,
        texture_se,
        perimeter_se,
        area_se,
        smoothness_se,
        compactness_se,
        concavity_se,
        concave_points_se,
        symmetry_se,
        fractal_dimension_se,
        radius_worst,
        texture_worst,
        perimeter_worst,
        area_worst,
        smoothness_worst,
        compactness_worst,
        concavity_worst,
        concave_points_worst,
        symmetry_worst,
        fractal_dimension_worst]])
        
        if breast_cancer_pred[0]==0:
            breast_cancer_diagnosis='No breast cancer'
        else:
            breast_cancer_diagnosis='This is a Sickneesss'
            
        st.success(breast_cancer_diagnosis)        
        

#radius_mean
#texture_mean
#perimeter_mean
#area_mean
#smoothness_mean
#compactness_mean
#concavity_mean
#concave_points_mean
#symmetry_mean
#fractal_dimension_mean
#radius_se
#texture_se
#perimeter_se
#area_se
#smoothness_se
#compactness_se
#concavity_se
#concave_points_se
#symmetry_se
#fractal_dimension_se
#radius_worst
#texture_worst
#perimeter_worst
#area_worst
#smoothness_worst
#compactness_worst
#concavity_worst
#concave_points_worst
#symmetry_worst
#fractal_dimension_worst