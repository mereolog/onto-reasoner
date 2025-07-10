import glob
import os
import shutil

from processors.utils.root_finder import find_project_root


def concatenate_cl_files_in_folder(root_folder, output_file):
    project_root = find_project_root()
    output_file_path = os.path.join(project_root, output_file)
    root_folder_path = os.path.join(project_root, root_folder)
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        for dirpath, _, filenames in os.walk(root_folder_path):
            for filename in filenames:
                if filename.endswith('.cl'):
                    file_path = os.path.join(dirpath, filename)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(f"// Start of {file_path}\n")
                        outfile.write(infile.read())
                        outfile.write(f"\n// End of {file_path}\n\n")
