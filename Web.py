import streamlit as st
import pandas as pd
import joblib



model = joblib.load('model.pkl')
pipelines = joblib.load('preprocessing.pkl')


st.header("Context:")
st.write("""
The study discusses the impact of factors such as immunization and the HDI on life expectancy, as these factors were not considered in previous research that relied on multiple regression models. 
         The study aims to develop a regression model based on mixed effects and multiple regression using data from 2000 to 2015 for all countries, 
         focusing on important vaccinations such as hepatitis B, polio and diphtheria. The findings will help countries identify factors influencing the decline in life expectancy, 
         enabling them to identify areas that need to be improved to increase population life expectancy.

""")

st.header("Content:")
st.write("""
The project relies on data accuracy, using World Health Organization (WHO) data to track health conditions and other related factors across all countries. Data on life expectancy and health factors for 193 countries was gathered from the WHO website, 
         along with economic data from the United Nations website. The most representative health factors were selected, and the analyses showed a significant improvement in mortality rates over the past fifteen years, especially in developing countries. 
         The data covered the period from 2000 to 2015, and individual files were merged into a single dataset, with missing values addressed using R software. The results indicated that most missing values were related to population, hepatitis B, and GDP, leading to the exclusion of some lesser-known countries. 
         The final dataset contains 22 columns and 2,938 rows, 
         with variables categorized into broad groups including vaccination factors, mortality factors, economic factors, and social factors.
""")


st.header("Columns Description:")
st.markdown("""
* ***Status***: Developed or Developing status
* ***Adult Mortality***: Adult Mortality Rates of both sexes (probability of dying between 15 and 60 years per 1000 population)
* ***infant deaths***: Number of Infant Deaths per 1000 population
* ***Alcohol***: Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)
* ***percentage expenditure***: Expenditure on health as a percentage of Gross Domestic Product per capita(%)
* ***Hepatitis B***: Hepatitis B (HepB) immunization coverage among 1-year-olds (%)
* ***Measles***: Measles - number of reported cases per 1000 population
* ***BMI***: Average Body Mass Index of entire population
* ***under-five deaths***: Number of under-five deaths per 1000 population
* ***Polio***: Polio (Pol3) immunization coverage among 1-year-olds (%)
* ***Total expenditure***: General government expenditure on health as a percentage of total government expenditure (%)
* ***Diphtheria***: Diphtheria tetanus toxoid and pertussis (DTP3) immunization coverage among 1-year-olds (%)
* ***HIV/AIDS***: Deaths per 1 000 live births HIV/AIDS (0-4 years)
* ***GDP***: Gross Domestic Product per capita (in USD)
* ***Population***: Population of the country
* ***thinness 1-19 years***: Prevalence of thinness among children and adolescents for Age 10 to 19 (% )
* ***thinness 5-9 years***: Prevalence of thinness among children for Age 5 to 9(%)
* ***Income composition of resources***: Human Development Index in terms of income composition of resources (index ranging from 0 to 1)
* ***Schooling***: Number of years of Schooling(years)
""")

st.header("The model:")

col1,col2 = st.columns(2)
status = col1.radio('**Status**', ['Developed','Developing'])
infant_death = col1.slider("**Under-five Deaths**",min_value=0,max_value=3000)
alcohol = col1.slider("**Alcohol**",min_value=0,max_value=20)
Hepatitis = col1.slider("**Hepatitis B**",min_value=0,max_value=100)
expenditure = col1.slider("**Total expenditure**",min_value=0,max_value=20)
GDP = col1.slider("**GDP**",min_value=0,max_value=120000)
thinness = col1.slider("**thinness  1-19 years**",min_value=0,max_value=30)
Income =col2.slider("**Income composition of resources rate**",min_value=0.0,max_value=1.0)
schooling = col1.slider("**Schooling**",min_value=0,max_value=25)
Population = col2.slider("**Population**",min_value=1,max_value=1300000000)
AIDS = col2.slider("**HIV/AIDS**",min_value=0,max_value=50)
Diphtheria = col2.slider("**Diphtheria**",min_value=0,max_value=100)
Polio = col2.slider("**Polio**",min_value=0,max_value=100)
BMI = col2.slider("**BMI**",min_value=0,max_value=90)
Measles = col2.slider("**Measles**",min_value=0,max_value=200000)
adult_mor = col2.slider("**Adult Mortality**",min_value=0,max_value=1000)


button =st.button('Predict')

if button:
    index = [0]
    data = pd.DataFrame({'Status':status,'under-five deaths':infant_death,'Alcohol':alcohol,'Hepatitis B':Hepatitis,
                         'Total expenditure':expenditure,'GDP':GDP,'thinness  1-19 years':thinness,'Income composition of resources':Income,
                         'Schooling':schooling,'Population':Population,'HIV/AIDS':AIDS,'Diphtheria':Diphtheria,'Polio':Polio,'BMI':BMI,
                         'Measles':Measles,'Adult Mortality':adult_mor
                         }, index = index)
    

    ready_data = pipelines.transform(data)
    prediction = model.predict(ready_data)

    st.write(f"The predicted values of the life expectancy is {prediction[0]:0.1f} years old")




    


