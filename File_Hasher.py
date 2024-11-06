import hashlib
import argparse
import os

# Function to generate a hash for a file
def generate_file_hash(file_path, algorithm='sha256'):
    try:
        # Check if the algorithm is supported
        if algorithm not in hashlib.algorithms_available:
            raise ValueError(f"Unsupported hashing algorithm: {algorithm}")

        # Open the file in binary mode and create a hash object
        hash_obj = hashlib.new(algorithm)
        # With will close the file once we're done with it, opening in binary mode for our hash
        with open(file_path, 'rb') as f:
            # While their is still binary data being read, perform the function
            while chunk := f.read(8192):
                # Continue writing the data to our hash object while it exists
                hash_obj.update(chunk)

        return hash_obj.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except OSError as e:
        print(f"Error opening file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

# Function to save hash to a file
def save_hash_to_file(hash_value, file_path):
    try:
        #Open the file in append mode
        with open(file_path, 'a') as f:
            f.write(f"{hash_value}\n")
        print(f"Hash value saved to {file_path}")
    except OSError as e:
        print(f"Error writing to file: {e}")
    except FileNotFoundError:
        print(f"Error: Hash file '{file_path}' was not found.")

# Function to compare hash with the saved hashes in a file
def compare_hash(hash_value, file_path):
    try:
        with open(file_path, 'r') as f:
            saved_hashes = f.readlines()
            # Save the hashes in a list to compare
        saved_hashes = [line.strip() for line in saved_hashes]

        if hash_value in saved_hashes:
            print("Hash matches one that is in the file.")
        else:
            print("Hash does not match any saved value.")
    except FileNotFoundError:
        print(f"Error: Hash file '{file_path}' was not found.")
    except OSError as e:
        print(f"Error reading file: {e}")

# Main function to handle command-line arguments and runs by default
def main():
    parser = argparse.ArgumentParser(description="File Hashing Utility")

    # Command-line arguments
    parser.add_argument('file', help="Path of the file to hash")
    parser.add_argument('-a', '--algorithm', help="Hashing algorithm (default: sha256)", default='sha256')
    parser.add_argument('-s', '--save', help="Save the hash to a file")
    parser.add_argument('-c', '--compare', help="Compare the file's hash to a saved hash")
    parser.add_argument('-p', '--print', help="Print the hash to the console", action='store_true')

    args = parser.parse_args()

    # Generate file hash
    file_hash = generate_file_hash(args.file, args.algorithm)

    if file_hash:
        if args.print:
            print(f"Hash ({args.algorithm}): {file_hash}")

        if args.save:
            save_hash_to_file(file_hash, args.save)

        if args.compare:
            compare_hash(file_hash, args.compare)

if __name__ == "__main__":
    main()
