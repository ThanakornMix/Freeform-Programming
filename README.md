# CO₂ Emissions of United States Analysis 
This project provides a comprehensive analysis of CO₂ emissions in the United States 2012 - 2022 (cna change to any time period form 1970 - 2022). Using data from various sectors and fuel types, it visualizes key insights through interactive and static plots. The analysis is aimed at understanding trends, sector-wise contributions, and geographical distributions of emissions.
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

