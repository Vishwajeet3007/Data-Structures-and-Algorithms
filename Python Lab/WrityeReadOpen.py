import shutil

def copy_file(source_file, dest_file):
    try:
        # Open the source file for reading
        with open(source_file, 'rb') as src:
            # Open (or create if not exist) the destination file for writing
            with open(dest_file, 'wb') as dest:
                # Copy the content from source to destination
                shutil.copyfileobj(src, dest)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Error: Source file not found.")
    except Exception as e:
        print("Error:", e)

# Usage
copy_file("source.txt", "destination.txt")
