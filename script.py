import os
import fnmatch

# Directory path where your MHTML files are located
directory_path = 'data'

# List all files in the directory
files = os.listdir(directory_path)

# Filter MHTML files using the "*.mhtml" pattern
mhtml_files = fnmatch.filter(files, '*.mhtml')

if len(mhtml_files) == 0:
    print('No MHTML files found in the directory.')
else:
    print('MHTML files found in the directory:')
    for file_name in mhtml_files:
        print(file_name)