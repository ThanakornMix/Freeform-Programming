# CO₂ Emissions of United States Analysis 
This project provides a comprehensive analysis of CO₂ emissions in the United States 2012 - 2022 (can change to any time period form 1970 - 2022). Using data from various sectors and fuel types, it visualizes key insights through interactive and static plots. The analysis is aimed at understanding trends, sector-wise contributions, and geographical distributions of emissions.
## File Descriptions
1. api_data_fetcher.py
    - Purpose: Fetches raw data from the EIA (Energy Information Administration) API.
    - Key Functionality:
        - fetch_data: Retrieves data for a specified route, year range, and other parameters.
        - fetch_all_data: Handles pagination to fetch all available data within a given range.
    - Input: API route, frequency, year range, and maximum records.
    - Output: Raw CO₂ emissions data as a Python list of dictionaries.
2. data_collection.py
    - Purpose: Saves raw data fetched from the API to a CSV file for further analysis.
    - Key Functionality:
        - save_data_to_csv: Converts the raw data into a DataFrame and saves it to a CSV file.
    - Input: Raw data from api_data_fetcher.py.
    - Output: co2_emissions_2012_2022.csv.
3. process_data.py
    - Purpose: Cleans and processes the raw data to ensure reliability and consistency.
    - Key Functionality:
        - inspect_data: Displays data types, missing values, and summary statistics.
        - clean_missing_values: Handles missing values by removing or filling them.
        - handle_duplicates: Removes duplicate rows.
        - validate_data_types: Ensures consistent data types for all columns.
        - standardize_categorical_data: Standardizes categorical data formatting.
        - filter_invalid_data: Removes rows with invalid or nonsensical values.
        - process_api_data: Executes the full cleaning process on the raw data.
    - Input: Raw data from data_collection.py.
    - Output: Cleaned DataFrame ready for analysis.
4. visualization.py
    - Purpose: Generates visualizations to explore and analyze CO₂ emissions trends.
    - Key Functionality:
        - plot_total_emissions_by_year: Plots total CO₂ emissions for each year (2012-2022).
        - plot_sector_emissions_by_year: Plots total CO₂ emissions by sector for each year.
    - Input: Cleaned data from process_data.py.
    - Output: Interactive graphs visualized using matplotlib.
5. save_plot.py
    - Purpose: Saves visualizations as image files for reporting and documentation purposes.
    - Key Functionality:
        - save_figure: Saves the currently active matplotlib figure to a specified file.
    - Input: File path for saving the plot.
    - Output: Saves plots as .png or .jpg files.
6. main.py
    - Purpose: Integrates all components of the project to execute the complete analysis pipeline.
    - Key Functionality:
      - Fetches raw data from the API.
      - Saves raw data to a CSV file.
      - Cleans and processes the data.
      - Generates visualizations for exploratory data analysis (EDA).
    - Execution: Run this file to perform the entire data fetching, cleaning, and visualization process.
## Features
1. Data Fetching:
    - Retrieves CO₂ emissions data from an external API based on year, sector, and fuel type.

2. Data Processing:
    - Cleans and aggregates the raw data for analysis.

3. Exploratory Data Analysis (EDA):
    - Summarizes data structure, identifies trends, and detects anomalies.

4. Visualizations:
    - Line plots, pie charts, stacked bar charts, strip plots, and an animated choropleth map.
## Data Source
This project utilizes the **U.S. Energy Information Administration (EIA) Open Data API** for CO₂ emissions data.  
For more details, visit the [EIA Open Data API](https://www.eia.gov/opendata/).

### API Key
To access the EIA API, you need a valid API key. Follow these steps:
1. Register for an API key at [EIA API Key Registration](https://www.eia.gov/opendata/register.php).
2. You will receive an API key, which looks like a long alphanumeric string.
3. Create a file named .env in the root directory of your project.
4. Add the following line to the file, replacing your_api_key_here with your actual API key:
   ```bash
   API_KEY = your_api_key_here
## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ThanakornMix/Freeform-Programming

2. **Navigate to the project directory:**:
    ```bash
    cd Freeform-Programming
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
## Usage
1. **Run the project**
   ```bash
   python src/main.py
## Dependencies
    - Python Version: 3.
    - Required Libraries:
        - pandas
        - matplotlib
        - seaborn
        - requests
        - numpy
        - scipy
## Visualizations
The following visualizations are generated:
1. Total Emissions by Year: Line plot.
2. Emissions by Sector and Year: Line plot with multiple sectors.
3. Fuel-Type Contributions: Pie chart.
4. Stacked Bar Chart of Sector and Fuel Type.
5. Strip Plot of Emissions Distribution by Year.
6. Geographical Distribution of Emissions: Animated choropleth map.
## Project Structure
    Freeform-Programming/
    ├── src/                           # Source code
    │   ├── api_data_fetcher.py        # Fetches data from the API
    │   ├── collection_data.py         # Saves raw data to CSV
    │   ├── process_data.py            # Cleans and processes data
    │   ├── eda.py                     # Functions for exploratory data analysis
    │   ├── visualization.py           # Visualization functions
    │   └── main.py                    # Main script
    │   
    │
    ├── data/                          # Optional: Store fetched/cleaned data
    │   ├── co2_emissions_2012_2022.csv
    │   └── cleaned_co2_emissions.csv
    │
    ├──graphs/                          # Optional: Save visualization 
    │    ├── total_emissions_by_year.png
    │    ├── sector_emissions_by_year.png
    │    └── .....
    │
    ├── requirements.txt               # Python dependencies
    └── README.md                      # Project documentation

