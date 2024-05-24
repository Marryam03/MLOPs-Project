from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('SavedWeights.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json() 
    if 'text' not in data:
        return jsonify({'error': 'No data provided'}), 400
    
    try:
        # Convert JSON to DataFrame
        dataframe = pd.DataFrame(data['text'])
        
        # Make predictions
        numeric_output = model.predict(dataframe)
        
        # Mapping numeric outputs to labels
        label_mapping = {0: 'Adware', 1: 'Backdoor', 2: 'Banker', 3: 'Benign', 4: 'Dropper', 5: 'FileInfector', 6: 'NoCategory', 7: 'PUA', 8: 'Ransomware', 9: 'Riskware', 10: 'SMS', 11: 'Scareware', 12: 'Spy', 13: 'Trojan', 14: 'Zeroday'}
        labeled_output = [label_mapping[label] for label in numeric_output]
        
        return jsonify({'answer': labeled_output}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
