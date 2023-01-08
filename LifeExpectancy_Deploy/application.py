from flask import Flask,render_template
import pandas as pd

app=Flask(__name__)
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

if __name__=='__main__':
    app.run(debug=True)