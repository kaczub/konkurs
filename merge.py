import os

def merge_python_files(output_filename="projekt_calosc.txt"):
    with open(output_filename, "w", encoding="utf-8") as outfile:
        for root, dirs, files in os.walk("."):
            # Omiń foldery wirtualne i cache
            if any(x in root for x in [".venv", "venv", "__pycache__", ".git"]):
                continue
            
            for file in files:
                if file.endswith(".py") and file != output_filename:
                    full_path = os.path.join(root, file)
                    outfile.write(f"\n{'='*50}\n")
                    outfile.write(f"PLIK: {full_path}\n")
                    outfile.write(f"{'='*50}\n\n")
                    with open(full_path, "r", encoding="utf-8") as infile:
                        outfile.write(infile.read())
                        outfile.write("\n")
    print(f"Gotowe! Wszystko jest w pliku: {output_filename}")

merge_python_files()

# by chatgpt