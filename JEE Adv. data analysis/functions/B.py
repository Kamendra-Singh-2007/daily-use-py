import pandas as pd
def merge(file1, file2, output_file):
    if file1 == "" or file2 == "" or output_file == "":
        print("merge(file1, file2, output_file)")
        return
    try:
        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)
        merged_df = pd.merge(df1, df2, on="Adv Roll No", how="inner")
        merged_df.to_csv(output_file, index=False)
        print(f"Merged CSV saved to {output_file}")
    except Exception as e:
        print(f"Error merging files: {e}")