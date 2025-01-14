def process_file():
    try:
        # Get filenames from user
        infile = input("Enter input filename (or 'quit'): ")
        if infile.lower() == 'quit':
            return False
            
        outfile = input("Enter output filename: ")
        
        # Read and modify content
        with open(infile) as f:
            content = f.read().upper()
            
        # Write to new file
        with open(outfile, 'w') as f:
            f.write(content)
            
        # Show preview
        print(f"\nSuccess! First 100 characters of {outfile}:")
        print(content[:100] + "..." if len(content) > 100 else content)
        return True
            
    except FileNotFoundError:
        print(f"\nError: The file '{infile}' was not found.")
        return True
    except PermissionError:
        print(f"\nError: Permission denied when accessing the file.")
        return True
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        return True

def main():
    print("=== File Processing Program ===")
    print("This program will read a file and create an uppercase version.")
    
    while True:
        if not process_file():
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()