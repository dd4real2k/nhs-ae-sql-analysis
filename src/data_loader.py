import pandas as pd
import os

def load_all_files(folder_path):
    all_dfs = []

    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path)

            df["source_file"] = file  # track origin
            all_dfs.append(df)

    combined_df = pd.concat(all_dfs, ignore_index=True)
    return combined_df
