from flask import Flask,render_template,request
import pandas as pd
import pickle

app=Flask(__name__)

model=pickle.load(open('/Users/vaishnaviuttarkar/Life Expectany/Life_Expectancy_Model/LifeExpectancy_Deploy/RandomRegressionModel.pkl','rb'))
life=pd.read_csv('/Users/vaishnaviuttarkar/Life Expectany/Life_Expectancy_Model/LifeExpectancy_Deploy/CleanedLifeExpectancy.csv')

@app.route('/')
def index():
    Countries = sorted(life['Country'].unique())
    # year = sorted(life['Country'].unique())
    Status = sorted(life['Status'].unique())
    # adultMortality
    # infantdeaths
    # alcohol
    # precentageExpenditure
    # hepatitisB
    # Measles
    # bmi
    # underFiveDeaths
    # polio
    # totalExpenditure
    # diphtheria
    # hivAids
    # gdp
    # population
    # thinness1_19yrs
    # thinness5_9yrs
    # incomeCompositionOfResources
    # schooling

    return render_template('index.html', Countries= Countries, Status=Status)

@app.route('/predict',methods=['POST'])
def predict():
    country=(request.form.get('country'))
    year=int(request.form.get('year'))
    status=request.form.get('status')
    adultMortality=int(request.form.get('adultMortality'))
    infantdeaths=int(request.form.get('infantdeaths'))
    alcohol=(float((request.form.get('alcohol'))))
    percentageExpenditure=float((request.form.get('percentageExpenditure')))
    hepatitisB=int(request.form.get('hepatitisB'))
    Measles=int(request.form.get('measles'))
    bmi=float((request.form.get('bmi')))
    underFiveDeaths=int(request.form.get('underFiveDeaths'))
    polio=int(request.form.get('polio'))
    totalExpenditure=float((request.form.get('totalExpenditure')))
    diphtheria=int(request.form.get('diphtheria'))
    hivAids=float((request.form.get('hivAids')))
    gdp=int(request.form.get('gdp'))
    population=int(request.form.get('population'))
    thinness1_19yrs=float((request.form.get('thinness1_19yrs')))
    thinness5_9yrs=float((request.form.get('thinness5_9yrs')))
    incomeCompositionOfResources=float((request.form.get('incomeCompositionOfResources')))
    schooling=float((request.form.get('schooling')))

    prediction=model.predict([[country,year,status,adultMortality,infantdeaths,alcohol,percentageExpenditure,hepatitisB,Measles,bmi,underFiveDeaths,polio,totalExpenditure,diphtheria,hivAids,gdp,population,thinness1_19yrs,thinness5_9yrs,incomeCompositionOfResources,schooling]])

    print(prediction)
    return ''


if __name__=='__main__':
    app.run(debug=True)