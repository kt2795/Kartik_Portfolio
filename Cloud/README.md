# CloudPlatformsAWSGroupB10
This repository contains all files relevant to AWS final project for Group 10 MIBA Section B.

# Navigating the Github repository
All files in folder 'All Final Project Files Group B10'
## AWS S3
Contains the folder 'aws-ml-groupb10' which is a bucket on S3, which also has three folders
### model-building
The folder contains all data for training the forecasting model - 
1. train.csv
2. features.csv
3. stores.csv
### to-predit
The folder contains files that require predictions, i.e., future dates -
1. test.csv
### output
The folder contains the output from the model post-predictions, which is
1. predictions_{current_date,current_time}.csv: Contains all our predictions
2. output_{current_date,current_time}.txt: Contains brief description such as model, MAE and cross validation average error
## AWS Sagemaker
Contains - 
1. The ipynb file, 'AWS-Final-Project-GroupB10-VerFinal-Updated.ipynb' - This is the file through which our data flows, gets train, cross validated, evaluated. Following which we run our predictions. Currently the file runs LightGBM (Light Gradient Boosting Machine) model but we have placeholder code to run KNN, ExtraTreeRegressor,RandomForestRegressor, SVM, neural networks, lasso and ridge regression.
2. IAM folder contains all the json files related to the notebook instance with respect to permissions
## AWS lambda
This folder contains all components relevant to running the lambda function on AWS
1. lambda_function.py: This is the script which runs with the event configuration as {}, since we don't require parameters to run this
2. lambda_function.txt: Same script but stored in txt file (Can be ignored for practical purposes)
3. Trigger.txt: Contains details of the trigger, API Gateway which enables getting outputs via a HTTP link
4. IAM roles folder containing necesary IAM policies with respect to lambda, trigger and S3 
## AWS API Gateway Folder
Contains two files - 
1. Details about the API such protocol, integrations, authorization, stage, etc.
2. A text file containing the link which triggers a zip folder to be downloaded on the local machine with the output files
a. Predictions
b. Brief description of the model

# Project Process
## Step 1 - Setting the S3 bucket/folders
Created a S3 bucket with three folders
1. mode-bilding/ :- For training data that would be useful for model building, training and evaluation. Note: The names of the files should be as is, 'train.csv', 'features.csv', 'stores.csv'. Any updated training process (re-training) would involve re-uploading the updated files, with the same name and the same schema
2. to-predict/ :- The necessary predictions required, the name of the file 'test.csv' will contain the same name and schema
3. output/ :- This is where the model completes the predictions, example: 'output_2023-03-14-19-58-24.txt','predictions_2023-03-14-19-58-24.csv'. This is empty at the beginning of the ML lifecycle and only gets updated once the model completes prediction

## Step 2 - Running the AWS Sagemaker, Processing & training
Leveraging the training data, post processing we train the model on the processed training set. While there are placeholders to run KNN, ExtraTreeRegressor, RandomForestRegressor, SVM, neural networks, lasso and ridge regression; we currently go forward with LightGBM (Light Gradient Boosting Machine) model. This part is focused until before 'Test' header in the sagemaker notebook file, that is run via a Sagemaker notebook instance

## Step 3 - AWS Sagemaker, Predictions
This is where we run the code post 'Test' header to pre-process the test.csv data to gather predictions of weekly sales on future dates

## Step 4 - AWS Sagemaker + S3
We gather information on the best model, metrics and cross validaition comparison and store the information in a text file. Then we also go ahead and save the predictions csv as predicitons_{current_date,current_time}.csv into the output folder we mentioned in step 1. Now the output folder has 2 files (in case of no earlier predictions)

## Step 5 - AWS Lambda + S3 + API Gateway
After we have gathered our preferred results in the desired format (predictions in csv, model information in txt file). We run a script in lambda function which is triggered by running the link - 'https://300i0o6rxg.execute-api.us-east-1.amazonaws.com/AssignmentGroupB10' which is able to pull the latest txt file, and the latest csv file, compress them into zip and download them on any local machine that runs the link. This is enabled by additionally setting an AWS API gateway integrated with the lambda function on a HTTP protocol. 

## Additonal note
Apart from the above mentioned services we also use *IAM* to set permissions to allow for integrations that makes the end to end ML possible and *CloudWatch* to monitor logs when encoutnered with errors

# About Data

## stores.csv
This file contains anonymized information about the 45 stores, indicating the type and size of store.

## train.csv

This is the historical training data, which covers to 2010-02-05 to 2012-11-01. Within this file you will find the following fields:

Store - the store number
Dept - the department number
Date - the week
Weekly_Sales -  sales for the given department in the given store
IsHoliday - whether the week is a special holiday week
test.csv

This file is identical to train.csv, except we have withheld the weekly sales. You must predict the sales for each triplet of store, department, and date in this file.

## features.csv

This file contains additional data related to the store, department, and regional activity for the given dates. It contains the following fields:

Store - the store number
Date - the week
Temperature - average temperature in the region
Fuel_Price - cost of fuel in the region
MarkDown1-5 - anonymized data related to promotional markdowns that Walmart is running. MarkDown data is only available after Nov 2011, and is not available for all stores all the time. Any missing value is marked with an NA.
CPI - the consumer price index
Unemployment - the unemployment rate
IsHoliday - whether the week is a special holiday week

# About Walmart
Walmart operates as a large-scale retail corporation that sources products from manufacturers and distributes them to its brick-and-mortar stores and e-commerce platform. 
