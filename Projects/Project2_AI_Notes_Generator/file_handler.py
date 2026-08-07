def load_text(filename):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            content = file.read()
        return content
        
    except FileNotFoundError:
        print()
        print("File not found..")
        return None
    except PermissionError:
        print()
        print("File permission denied..")
        return None
    except Exception as e:
        print()
        print(f"Something went wrong while reading the file: {e}..")
        return None