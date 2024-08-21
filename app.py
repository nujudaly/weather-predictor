from flask import Flask, render_template, request
from tensorflow import keras
import pickle
import datetime

app = Flask(__name__)

# Load the model with corrected file path
with open(r'C:\Users\nujud\Desktop\Flask_APP\weather_model.pkl', 'rb') as file:
    model = pickle.load(file)

def preprocess_input(date_str):
    # Replace with the same preprocessing you did in your notebook
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    # Example: Convert the date to the format your model expects
    processed_date = [date_obj.year, date_obj.month, date_obj.day]  # This is just an example
    return processed_date

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        date_input = request.form['date']
        processed_date = preprocess_input(date_input)
        prediction = model.predict([processed_date])  # Adjust this according to your model's input

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
