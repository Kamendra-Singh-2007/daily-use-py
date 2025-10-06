from functions import *
a = ainput()
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
