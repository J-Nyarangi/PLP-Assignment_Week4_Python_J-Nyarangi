# PLP-Assignment_Week4_Python_J-Nyarangi
# File Processing Program

A simple Python utility that reads text files and creates modified versions with uppercase content. This program demonstrates file operations and error handling in Python.

## Features

- Interactive command-line interface
- Converts file contents to uppercase
- Error handling for common file operations
- Preview of processed content
- Continuous operation until user chooses to quit

## Requirements

- Python 3.x

## Installation

1. Download the `file_processor.py` script
2. No additional packages are required

## Usage

1. Run the program:
```bash
python file_processor.py
```

2. When prompted:
   - Enter the name of the file you want to process
   - Enter the name for the output file
   - Type 'quit' at any time to exit

Example session:
```
=== File Processing Program ===
This program will read a file and create an uppercase version.

Enter input filename (or 'quit'): input.txt
Enter output filename: output.txt

Success! First 100 characters of output.txt:
HELLO WORLD! THIS IS A TEST FILE...
```

## Error Handling

The program handles several common errors:
- File not found
- Permission denied
- Other file operation errors

Error messages are user-friendly and clearly indicate what went wrong.

## Example Files

Input file (`input.txt`):
```
Hello World!
This is a test file.
```

Output file (`output.txt`):
```
HELLO WORLD!
THIS IS A TEST FILE.
```

## Tips

- Make sure you have read permissions for input files
- Make sure you have write permissions in the output directory
- Backup important files before processing them
- The program will not overwrite files without warning

## Contributing

Feel free to fork this project and submit improvements via pull requests.

## License

This project is open source and available for educational purposes.
