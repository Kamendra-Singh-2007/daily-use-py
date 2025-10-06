import pandas as pd
def samerank(csv_file, column_name):
    if csv_file == "" or column_name == "":
        print("Sameranks(csv_file, column_name): csv_file and column_name cannot be empty!")
        return
    df = pd.read_csv(csv_file)
    if column_name not in df.columns:
        print(f"Error: The column '{column_name}' was not found in the CSV file!")
        return
    else:
        Samerank = df[column_name].dropna().astype(int).sort_values().reset_index(drop=True)
        full_rank_sequence = list(range(Samerank.min(), Samerank.max() + 1))
        missing_ranks = list(set(full_rank_sequence) - set(Samerank))
        if missing_ranks:
            print(f"Same Ranks in the '{column_name}' column:", sorted(missing_ranks))
        else:
            print(f"No Same Ranks in the '{column_name}' column.")
