from zipfile import ZipFile
import os
from os.path import basename

def zip_files(dir, zip, extensions):
    with ZipFile(zip, 'w') as zip_obj:
        # iterate over all the files in directory
        for folder, subfolders, files in os.walk(dir):
            for file in files:
                name, ext = os.path.splitext(file)
                if ext.lower() in extensions:
                    # create complete filepath of file in directory
                    file_path = os.path.join(folder, file)
                    # add file to zip
                    zip_obj.write(file_path, basename(file_path))

zip_files('./', 'zipped.zip', ['.txt'])

# Note: does not maintain folder structure