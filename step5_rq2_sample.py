import pandas as pd
import random

def select_random_rows_from_excel(file_path, sheet_name, num_rows):
    # Read the specified sheet
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Check if the requested number of rows exceeds the number of rows in the sheet
    if num_rows > len(df):
        raise ValueError(f"Requested number of rows {num_rows} exceeds the number of rows in the sheet {len(df)}")
    
    # Select only the specified columns
    df = df[['id', 'title', 'topic_link']]
    
    # Randomly select the specified number of rows
    selected_rows = df.sample(n=num_rows, random_state=random.randint(1, 10000))
    
    return selected_rows

if __name__ == "__main__":
    # User-defined variables
    file_path = 'step5_rq2/concerns_topics.xlsx'
    output_file_path = 'step5_rq2/sample.xlsx'  # Path for the output file

    # Dictionary containing sheet names as keys and number of rows to select as values
    sheet_info = {
        'api_chatgpt': 366,
        'gpts': 286,
        'prompting': 234
    }
    
    # Dictionary to hold the DataFrames for each sheet
    selected_rows_dict = {}
    
    # Process each sheet
    for sheet_name, num_rows in sheet_info.items():
        selected_rows = select_random_rows_from_excel(file_path, sheet_name, num_rows)
        selected_rows_dict[sheet_name] = selected_rows
    
    # Write the selected rows to a new Excel file with each sheet as a separate sheet
    with pd.ExcelWriter(output_file_path) as writer:
        for sheet_name, selected_rows in selected_rows_dict.items():
            selected_rows.to_excel(writer, sheet_name=sheet_name, index=False)
    
    print(f"Selected rows have been written to {output_file_path}")
    
          