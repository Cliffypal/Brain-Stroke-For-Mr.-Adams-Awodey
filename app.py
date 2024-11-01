from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

# Load your trained model
model = joblib.load('model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    data = request.get_json()

    # Prepare the data for prediction
    input_data = pd.DataFrame({
        'gender': [data['gender']],
        'age': [data['age']],
        'hypertension': [data['hypertension']],
        'heart_disease': [data['heart_disease']],
        'ever_married': [data['ever_married']],
        'work_type': [data['work_type']],
        'Residence_type': [data['Residence_type']],
        'avg_glucose_level': [data['avg_glucose_level']],
        'bmi': [data['bmi']],
        'smoking_status': [data['smoking_status']]
    })

    # Perform one-hot encoding for categorical features
    input_data_encoded = pd.get_dummies(input_data, drop_first=True)

    # Ensure the columns match the model's expected input
    model_input = input_data_encoded.reindex(columns=model.feature_names_in_, fill_value=0)

    # Perform prediction
    prediction = model.predict(model_input)

    # Prepare response
    response = {
        'stroke_risk': 'High Risk' if prediction[0] == 1 else 'Low Risk'
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
