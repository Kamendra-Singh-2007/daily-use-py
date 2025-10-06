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


