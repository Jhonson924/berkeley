from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load model and scaler
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

# Create Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Expect JSON input
        input_data = request.get_json()
        df = pd.DataFrame([input_data])

        # Scale the input
        scaled_input = scaler.transform(df)

        # Predict class and probability
        prediction = model.predict(scaled_input)[0]
        probability = model.predict_proba(scaled_input)[0][1]

        return jsonify({
            "prediction": int(prediction),
            "probability_fraud": float(probability)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
