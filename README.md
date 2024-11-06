Written by Sampson Prince, November 2024

	File_Hasher.py is a simple program that accepts the location of a file and after reading it, generates a hash value in one of the algorithms supported by the hashlib library. After generating the hash value it can be printed to standard out, written to a file, or both. New hash values can also be compared to those written to one of our desired files (see Usage at the bottom). The same value can be written to the same file more than once if desired, because the program will check all values in the comparison file and stop once a matching hash has been found.

Imported Modules:
 - hashlib for hashing.
 - argparse for handling command-line arguments.
 - os for additional file checks.

Function Explanations:
 - generate_file_hash(): Generates a hash for the file.
 - save_hash_to_file(): Saves the generated hash to a file. It can write to an existing file or create a new one.
 - compare_hash(): Compares the generated hash with saved hashes.
 - main(): Handles command-line argument parsing.

Error Detection:
 - Catches and handles file-related errors (like file not found or permission denied).
 - Ensures that only valid algorithms are used from hashlib.algorithms_available.

 Error Handling:
 - If the file doesn't exist, an appropriate error message will be shown.
 - Invalid hashing algorithms will result in a ValueError with a custom message.

Command Line Interface:
 - Can specify the file path, algorithm, save option, compare option, and whether to print the hash to the console using command-line arguments.

Usage Examples:
Show the command-line help(-h or --help):
python file_hasher.py -h

The generic format is the following:
python file_hasher.py <file to generate hash for> <argument> <target or option for argument where needed>

Generate and print a hash to standard out(-p or --print):
python file_hasher.py myfile.txt --print

Generate a hash with a different algorithm and save it(-a or --algorithm):
python file_hasher.py myfile.txt --algorithm sha1 --save hashes.txt

Compare a file's hash to previously saved hashes(-c or --compare):
python file_hasher.py myfile.txt --compare hashes.txt

Print the hash to standard out and compare it to a previously saved value:
python file_hasher.py myfile.txt -p -c hashes.txt