# CO₂ Emissions Analysis (2012-2022)
This project provides a comprehensive analysis of CO₂ emissions in the United States from 2012 to 2022. Using data from various sectors and fuel types, it visualizes key insights through interactive and static plots. The analysis is aimed at understanding trends, sector-wise contributions, and geographical distributions of emissions.
## Features
1. Data Fetching:
    - Retrieves CO₂ emissions data from an external API based on year, sector, and fuel type.

2. Data Processing:
    - Cleans and aggregates the raw data for analysis.

3. Exploratory Data Analysis (EDA):
    - Summarizes data structure, identifies trends, and detects anomalies.

4. Visualizations:
    - Line plots, pie charts, stacked bar charts, strip plots, and an animated choropleth map.
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
    ├── requirements.txt               # Python dependencies
    └── README.md                      # Project documentation

