import os
import zipfile
import re

# import time
# start_time = time.time()

# Set the path to the directory to search
# search_dir = '/path/to/search/directory'
search_dir = r'C:\Users\will.elliott\OneDrive - PeopleTec, Inc\ITE IV&V\ITE CDRLs\A060 (Product Drawings and Associated Lists)\A060 Draft (Developmental Drawings)\_zip_archives'

# Search pattern for files in the zip file
# Prompt the user for a regex pattern to match the contents of the zip files
content_pattern_str = input('Search pattern: ')

# Set the regex pattern to match zip files
zip_pattern = r'^.*\.zip$'
# content_pattern = r'^.*5189.*\.pdf$'
content_pattern = r'^.*' + re.escape(content_pattern_str) + r'.*\.pdf$'

# Compile the patterns into a regex object
zip_regex = re.compile(zip_pattern)
content_regex = re.compile(content_pattern)

# Set the path to the output file
output_file = 'file_list.txt'

empty_files_list = []

# Open the output file in write mode
with open(output_file, 'w') as f:
    f.write(f"Files matching pattern {content_pattern}:\n")
    # Loop through all files in the search directory
    for root, dirs, files in os.walk(search_dir):
        # print(search_dir)
        # print(os.path.exists(search_dir))
        for file in files:
            # Check if the file matches the regex pattern
            if zip_regex.match(file):
                # Open the zip file
                with zipfile.ZipFile(os.path.join(root, file)) as zip_file:

                    # Get the list of files in the zip file
                    file_list = zip_file.namelist()

                    #Filter the list of files based on the content regex pattern                    
                    matched_files = [name for name in file_list if content_regex.match(name)]
                    
                    #Write the list of matched files to the results file
                    if len(matched_files) > 0:
                        # print(len(matched_files))
                        f.write(f"- {file}:\n")
                        for file_name in matched_files:
                            f.write(f" -- {file_name}\n")
                    else:
                        empty_files_list.append(file)

    #Write files with no match to end of output file
    f.write(f"Files with no matching pattern {content_pattern}:\n")
    for empty_file in empty_files_list:
        f.write(f"- {empty_file}\n")

# end_time = time.time()
# total_time = end_time - start_time
# print(f"Script took {total_time:.4f} seconds to run.")
# print('start time: ', start_time)
# print('endtime: ', end_time)