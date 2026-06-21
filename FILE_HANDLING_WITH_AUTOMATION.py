import os
import shutil
import csv

# Define paths for our demonstration
base_dir = './file_demo'
input_file = os.path.join(base_dir, 'sample.txt')
csv_file = os.path.join(base_dir, 'data.csv')
moved_file = os.path.join(base_dir, 'archived_sample.txt')

def setup_demo():
    """Creates a directory and sample files for automation demo."""
    try:
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
            print(f"Created directory: {base_dir}")

        # 1. Writing to a Text File
        with open(input_file, 'w') as f:
            f.write("Hello, this is a sample text file for automation demo.")

        # 2. Writing to a CSV File
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Name', 'Status'])
            writer.writerow([1, 'Task_A', 'Completed'])
            writer.writerow([2, 'Task_B', 'Pending'])

        print("Sample files created successfully.")
    except Exception as e:
        print(f"Error during setup: {e}")

def automate_files():
    """Demonstrates reading, renaming, and moving files with error handling."""
    try:
        # 3. Reading the text file
        print("\n--- Reading File ---")
        with open(input_file, 'r') as f:
            content = f.read()
            print(f"Content read: {content}")

        # 4. Renaming/Moving a file (Automation)
        print("\n--- Automating File Operations ---")
        if os.path.exists(input_file):
            shutil.move(input_file, moved_file)
            print(f"Moved and Renamed '{input_file}' to '{moved_file}'")

        # 5. Reading from the CSV file
        print("\n--- Reading CSV Data ---")
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(f"Processing: {row['Name']} - {row['Status']}")

    except FileNotFoundError:
        print("Error: The requested file was not found.")
    except PermissionError:
        print("Error: You do not have permission to access these files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nFile operation sequence completed.")

# Execute the demo
setup_demo()
automate_files()

# Verification: List files in the demo directory
if os.path.exists(base_dir):
    print(f"Current files in {base_dir}:")
    print(os.listdir(base_dir))