import streamlit as st
import pandas as pd
import bz2



data = pd.read_csv('app/train-data.csv')

data['Date'] = pd.to_datetime(data['Date'])

data.set_index('Date', inplace=True)


class Form:
    def __init__(self):
        self.gender = st.number_input(" Enter the number of weeks to predict ", min_value=0,max_value=100,value=0,step=1)

        self.submit = st.button('Forecast')


def main():
    st.title('🥑 Avocado price forecasting 🧾')
    st.line_chart(data)
    form = Form()

    if form.submit:
      pass


if __name__ == '__main__':
    main()