
# Flight Fare Prediction

## Overview

The Flight Fare Prediction project is a machine learning-based system designed to predict the cost of flights based on various features such as airline, source, destination, departure time, arrival time, duration, and the number of stops. This system aims to provide users with accurate fare estimates for better travel planning and budgeting.

## Features

- Predict flight fares based on input features
- Supports multiple airlines and routes
- User-friendly interface for inputting flight details and viewing fare predictions

## Project Structure

├── .gitignore

├── .idea/

├── Crop_recommendation.csv

├── Images/

├── app.sav

├── crop.py

├── crop_recommendation.ipynb

├── requirements.txt

├── venv/

└── README.md


- **.gitignore**: Specifies files and directories to be ignored by Git.
- **.idea/**: Contains project-specific settings and configurations for your IDE.
- **`Data_Train.xlsx` and `Test_set.xlsx`**: The dataset used for training and testing the model.
- **app.sav**: The saved machine learning model.
- **air.py**: The main script for running the flight fare prediction system.
- **flight_price_prediction.ipynb**: Jupyter Notebook containing the project workflow and model training process.
- **requirements.txt**: Lists the dependencies required to run the project.
- **venv/**: The virtual environment directory.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Rohit-katkar2003/flight-fare-prediction.git
    cd flight-fare-prediction
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the flight fare prediction script:**
    ```bash
    python fare.py
    ```

2. **Interact with the system:**
   - Input the required features (airline, source, destination, departure time, arrival time, duration, number of stops).
   - Get the predicted flight fare based on the input features.

## Dataset

The dataset (`Data_Train.xlsx` and `Test_set.xlsx`) contains various features required for predicting the flight fare. Each row represents a data point with the following columns:

- **Airline**: The airline operating the flight
- **Source**: The source city
- **Destination**: The destination city
- **Departure Time**: The time of departure
- **Arrival Time**: The time of arrival
- **Duration**: The duration of the flight
- **Total Stops**: The number of stops
- **Fare**: The flight fare (target variable)

## Model

The machine learning model used in this project is saved in `flight_model.sav`. The model is trained using various algorithms to ensure high accuracy in fare prediction.


## Acknowledgements

- Thanks to the dataset providers and the open-source community for their valuable resources.

## Contact

For any questions or suggestions, please contact [katkarrohit203@gmail.com].
