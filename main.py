from flask import Flask
from google.cloud import automl_v1beta1 as automl
app = Flask(__name__)

project_id = 'production-268923'
compute_region = 'Global'
model_display_name = 'model_prep_20200229090512'
inputs = {'trip_seconds': 600,'trip_miles': 4,'payment_type': 'Cash','company': 'Flash Cab', 'pickup_location': 'POINT (-87.7215590627 41.968069)','dropoff_location': 'POINT (-87.7215590627 41.968069)'}

client = automl.TablesClient(project=project_id, region=compute_region)

@app.route('/')
def results():
    response = client.predict(
        model_display_name=model_display_name, inputs=inputs
    )
    print("Prediction results:")
    for result in response.payload:
        print(
            "Prediction: {}".format(result.tables.value.string_value)
        )

    

if __name__ == '__main__': 
    app.run(host='127.0.0.1', port=8080, debug=True)








