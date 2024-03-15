def clear_file_content(filename):
    try:
        file = open(filename, 'w')
        file.truncate(0)
        file.close()
        print(f"Contents of {filename} cleared.")
    except:
        print(f"Error clearing contents of {filename}.")
