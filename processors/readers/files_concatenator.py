import glob
import shutil


def concatenate_files_in_folder(input_folder_path: str, input_files_extension: str, output_file_path: str):
    with open(output_file_path, 'wb') as outfile:
        for filename in glob.glob(input_folder_path+'/*.'+input_files_extension):
            if filename == output_file_path:
                continue
            with open(filename, 'rb') as readfile:
                shutil.copyfileobj(readfile, outfile)