# Production

[![CircleCI](https://circleci.com/gh/MWMartley001/Production.svg?style=svg)](https://circleci.com/gh/MWMartley001/Production)

This is a repo for a Chicago taxi fare prediction application. Further refinements can be implemented and a user can input trip distance and estimated time in seconds (or they can enter minutes and the code converts to seconds) to receive an estimated ride fare. 

The model for prediction was built in the GCP AutoML application. The data for building the model was retrieved from BigQuery and preprocessed using Dataflow and ingested into GCP Tables. 

Monitoring is in place using Stackdriver. Continuous integration (CI) and continuous deployment (CD) are in place using Cloud Repositories and were utilized throughout the development process. 
