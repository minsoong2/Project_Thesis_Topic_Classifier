# Project Thesis Topic Classifier

## Overview

The Project_Thesis_Topic_Classifier is designed to classify and analyze academic thesis topics. It utilizes various Python scripts for data collection, processing, and visualization to aid in the classification of thesis topics into relevant categories.

## Key Features

- **Data Collection**: Automated scripts to collect thesis data.
- **Topic Classification**: Algorithm to classify theses into predefined categories.
- **Data Visualization**: Histograms and other tools for visualizing data distributions and classifications.

## Project Structure

- `mongodbinsert.py`: Script to insert collected data into a MongoDB database.
- `request_data.py`: Retrieves data based on specific parameters.
- `request_data_all.py`: Fetches all available thesis data.
- `request_data_selected.py`: Gathers selected data from the database.
- `histogram_ex.py`: Generates histograms for data analysis.
- `histogram_paper_collection.py`: Collects and processes data for histogram generation.
- `new_x_labels_with_y.txt`: Contains labels and data points used in the classification.

## Data Preprocessing

This project places a significant emphasis on data preprocessing to ensure the reliability of its classification results. The preprocessing steps include:

- **Data Cleaning**: Removal of irrelevant or incorrect data, correcting errors and inconsistencies.
- **Normalization**: Standardizing the data formats for uniform analysis.
- **Feature Extraction**: Identifying and extracting relevant features from the raw data that significantly impact the classification process.
- **Label Encoding**: Converting text labels into a numerical format for easier processing by classification algorithms.

The processed data is then stored in a MongoDB database, ensuring that the classification algorithms work with the most refined data set possible.

### Prerequisites

- Python 3.x
- MongoDB
- Relevant Python libraries: `pymongo`, `matplotlib`, etc.