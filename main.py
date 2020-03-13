from flask import Flask
from google.cloud import automl_v1beta1 as automl
app = Flask(__name__)

# AutoML requirements
project_id = 'production-268923'
compute_region = 'us-central1'
model_display_name = 'model_prep_20200310053214'
inputs = {"trip_seconds": 614, "trip_miles": 3.2}

# homepage
@app.route('/')
def placeholder():
    return "Taxi Fare Predictions"

# return predictions
@app.route('/predict', methods=['GET', 'POST'])
def get_result():
    client = automl.TablesClient(project=project_id, region=compute_region)
    response = client.predict(model_display_name=model_display_name, inputs=inputs)
    return str(response.payload)

if __name__ == '__main__': 
    app.run()








