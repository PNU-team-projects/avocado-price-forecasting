# Avocado price forecasting

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://avocado-price-forecasting.onrender.com/)


The main aim of this project is to develop a model that accurately predicts future avocado prices. The insights gained from this project will enable better decision-making for stakeholders in the avocado industry, facilitating proactive strategies for pricing, supply chain management, and market trends.


## Dataset
https://www.kaggle.com/datasets/neuromusic/avocado-prices


## Libraries
| Part                 | Libs                     | 
| -------------------- | ------------------------ |  
| Data Manipulation    | `pandas` `numpy`        |
| Data Visualization   | `matplotlib` `seaborn` `missingno`  |   
| Machine Learning     | `sklearn` `statsmodels` |
| Application          | `streamlit` |  


## Setting up a project

#### 1) Clone the repository
```
git clone https://github.com/VladHolobyn/avocado-price-forecasting.git 
cd avocado-price-forecasting 
```

#### 2) Create an environment

Windows:
```
py -3 -m venv env
env\Scripts\activate
```
macOS/Linux:
```
python3 -m venv env
. env/bin/activate
```

#### 3) Install requirements
```
pip install -r requirements.txt
```

#### 4) Run application
```
streamlit run run.py
```


## Preview 
![image](https://github.com/VladHolobyn/avocado-price-forecasting/assets/125756054/e4a4ab50-fd33-44fc-aec7-2a348e390b24)
