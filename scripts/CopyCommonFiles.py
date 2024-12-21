import os
import shutil

def copy_common_files(source_dir, dest_dir, target_dir):
    # List files in both directories
    source_files = set(os.listdir(source_dir))
    dest_files = set(os.listdir(dest_dir))

    # Find common files
    common_files = source_files & dest_files

    # Create target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Copy common files to the target directory
    for file_name in common_files:
        source_file_path = os.path.join(source_dir, file_name)
        target_file_path = os.path.join(target_dir, file_name)
        shutil.copy2(source_file_path, target_file_path)
        print(f"Copied: {file_name}")

# Example usage:
source_directory = 'C:\\WorkingDir\\apache-tomcat-9.0.87\\webapps\\ART\\resources\\AWF\\images\\blue\\icons'
destination_directory = 'C:\\WorkingDir\\apache-tomcat-9.0.87\\webapps\\ART\\resources\\APP\\images\\blue\\icons'
target_directory = 'C:\\WorkingDir\\apache-tomcat-9.0.87\\webapps\\ART\\resources\\APP\\images\\blue\\icons'


copy_common_files(source_directory, destination_directory, target_directory)
