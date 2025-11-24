from pdfminer.high_level import extract_text
import pandas as pd
import os
def process_pdf(pdf_path):
    """Process the PDF to extract Adv Roll No and rank column data."""
    if not pdf_path.endswith('.pdf'):
        pdf_path += '.pdf'
    try:
        print("Extracting text from the PDF...")
        text = extract_text(pdf_path)
        with open('extracted_text.txt', 'w', encoding='utf-8') as f:
            f.write(text)
    except Exception as e:
        print(f"Error processing the PDF: {e}")

def extract_adv_roll_no(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        save_roll_numbers = False  
        skip_until_next_adv_roll_no = False  
        for line in infile:
            line = line.strip()  
            if line == "Adv Roll No": 
                save_roll_numbers = True
                skip_until_next_adv_roll_no = False  
                continue
            if line == "" or line == "a":  
                save_roll_numbers = False
                skip_until_next_adv_roll_no = True
                continue
            if save_roll_numbers and not skip_until_next_adv_roll_no:
                if line.isdigit():
                    outfile.write(line + '\n') 

def extract_rank_values(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        save_rank_values = False
        skip_until_next_rank = False 
        for line in infile:
            line = line.strip() 
            if line == a:  
                save_rank_values = True
                skip_until_next_rank = False  
                continue
            if line == "" or line == "Adv Roll No":  
                save_rank_values = False
                skip_until_next_rank = True
                continue
            if save_rank_values and not skip_until_next_rank:
                if line.isdigit():
                    outfile.write(line + '\n')

def SaveToCSV(adv_roll_no_file, rank_values_file, output_csv_file):
    with open(adv_roll_no_file, 'r') as file:
        adv_roll_no_list = [line.strip() for line in file if line.strip().isdigit()]
    with open(rank_values_file, 'r') as file:
        rank_values_list = [line.strip() for line in file if line.strip().isdigit()]
    data = {
        "Adv Roll No": adv_roll_no_list,
        a: rank_values_list
    }
    df = pd.DataFrame(data)
    df[a] = df[a].astype(int)
    df = df.sort_values(by=a)
    df.to_csv(output_csv_file, index=False)
    print(f"Combined CSV file created: {output_csv_file}")

def delete_txt_files(*file_paths):
    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        else:
            print(f"File not found: {file_path}")

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
            print(f"Missing Ranks in the '{column_name}' column:", sorted(missing_ranks))
        else:
            print(f"No Missing Ranks in the '{column_name}' column.")

a = input("Name Of Rank Column As It Is: ")
pdf_path = input("Enter the PDF file path: ")
process_pdf(pdf_path)
input_file = r'extracted_text.txt'
output_file = r'adv_roll_numbers.txt'
extract_adv_roll_no(input_file, output_file)
print("Adv Roll No extraction completed. Check the output file:", output_file)
rank_output_file = f'{a}_values.txt'
extract_rank_values(input_file, rank_output_file)
print(f"{a} values extraction completed. Check the output file:", rank_output_file)
adv_roll_no_file = r'adv_roll_numbers.txt'
rank_values_file = f'{a}_values.txt'
output_csv_file = f'{a} Ranklist.csv'
SaveToCSV(adv_roll_no_file, rank_values_file, output_csv_file)
delete_txt_files('adv_roll_numbers.txt', f'{a}_values.txt', 'extracted_text.txt')
if input("Do you want to check for Missing Ranks (y/n): ") == "y":
    w = input("Enter ranklist.csv: ")
    e = w.removesuffix(" Ranklist.csv")
    samerank(w, e)
if input("Do you want to (merge ranklists/comparison) (y/n): ") == "y":
    q = input("Enter first ranklist.csv: ")
    w = input("Enter secound ranklist.csv: ")
    e = w.removesuffix(" Ranklist.csv")
    merge(q, w, f"{e} Comparison.csv")


   
