import os
A = input("Playlist Name: ")
os.system(f'dir /s /b /o:gn > {A}.txt')
file_path = f"{A}.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
lines = [f"file '{line.strip()}'\n" for line in lines]
with open(file_path, 'w', encoding='utf-8') as file:
    file.writelines(lines)
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
lines = [line for line in lines if not ('.txt' in line.lower() or '.py' in line.lower())]
with open(file_path, 'w', encoding='utf-8') as file:
    file.writelines(lines)
print(f"ffplay -f concat -safe 0 -i {A}.txt ")