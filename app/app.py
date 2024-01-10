import pickle
import streamlit as st
import pandas as pd
import bz2

model_pkl = bz2.BZ2File("pkl/sarima.pkl", 'rb')
model = pickle.load(model_pkl)

prices_data = pd.read_csv('app/csv/data.csv')
prices_data['Date'] = pd.to_datetime(prices_data['Date'])
prices_data.set_index('Date', inplace=True)

start_date = prices_data.index.max()

class Form:
    def __init__(self):
        self.end_date = st.date_input("Select the end date to forecast 📅", min_value=start_date)
        self.submit = st.button('Forecast')

def main():
    st.title('🥑 Avocado price forecasting 🧾')
    form = Form()

    if form.submit:
        predicted = model.predict(start=start_date, end=form.end_date)
        date_range = pd.date_range(start=start_date, end=form.end_date, periods=len(predicted))
        predicted_data = pd.DataFrame({"Date": date_range, "Predicted avocado price": predicted})
        predicted_data.set_index('Date', inplace=True)

        prices_data.rename(columns={'AveragePrice': 'Avocado price'}, inplace=True)
        combined_data = pd.concat([prices_data, predicted_data])

        st.header("Predicted avocado prices")
        st.line_chart(combined_data, use_container_width=True, color=['#75FA8D', '#FF4548'])

        st.divider()

        st.dataframe(predicted_data,width=800)


if __name__ == '__main__':
    main()
