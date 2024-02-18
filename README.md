# Laptop Price Predictor

This Streamlit app predicts the price of laptops based on various features. The data for this project was collected from Flipkart using web scraping techniques in September 2023. The collected data underwent necessary preprocessing, exploratory data analysis (EDA), and filtering to prepare it for model training and application development.

## Data Collection
The data collection process involved scraping laptop listings from Flipkart's website. Using the `requests` library in Python along with `BeautifulSoup`, we retrieved information such as product names, features, and prices. The collected data was stored in a structured format for further analysis and modeling.

## Exploratory Data Analysis (EDA)
Before building the prediction model, exploratory data analysis was conducted to gain insights into the dataset. This involved examining the distributions of features, identifying correlations between variables, handling missing values, and performing any necessary data transformations.

## Data Filtering
To ensure data quality and relevance for the prediction model, filtering was applied to the dataset. This included removing duplicates, handling outliers, and selecting features that were deemed important for predicting laptop prices.

## Streamlit App
Once the data was preprocessed and filtered, a Streamlit web application was developed to provide users with a user-friendly interface for predicting laptop prices. The app allows users to input various features such as brand, operating system, RAM size, etc., and provides a predicted price based on a pre-trained machine learning model.

## Usage
1. Clone this repository.
2. Install the required dependencies by running:
    ```
    pip install -r requirements.txt
    ```
3. Run the Streamlit app by executing:
    ```
    streamlit run app.py
    ```

After running the app, navigate to the provided local host URL in your web browser to interact with the application.

## Credits
- This app was created by Rahul Agrawal.
- The machine learning model was trained using the collected data from Flipkart.

