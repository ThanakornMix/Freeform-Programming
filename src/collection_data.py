import pandas as pd

def save_data_to_csv(data, output_file):
    """
    Saves the fetched data to a CSV file.

    :param data: Data to save (list of dictionaries or pandas DataFrame)
    :param output_file: Output CSV file path
    :return: None
    """
    # Convert the data to DataFrame if it's a list of dictionaries
    if isinstance(data, list):
        data = pd.DataFrame(data)
    
    # Save the DataFrame to a CSV file
    data.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")
