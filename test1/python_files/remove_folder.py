import os
import shutil
import logging


class RemoveFolder:
    @staticmethod
    def remove_folder(folder_path):
        logging.info("Finding the numeric name folders")
        for root, dirs, files in os.walk(folder_path):
            for d in dirs:
                if d.isnumeric(): # Find the numeric folders
                    logging.info("Moving files from folder " + str(d) + " to parent folder")
                    for dir in os.listdir(folder_path):
                        new_path = os.path.join(folder_path, dir, d)
                        if os.path.exists(new_path):
                            for root, dirs, files in os.walk(new_path):
                                for dir1 in dirs:
                                    try: # Move all the files from numeric folders
                                        shutil.move(os.path.join(root, dir1), os.path.join(folder_path, dir))
                                    except OSError:
                                        print("The folder", dir1 ," already present in on path", os.path.join(folder_path, dir))

                        if os.path.exists(os.path.join(folder_path, dir, d)):
                            logging.info("Removing folder " + str(d) + " from path " + os.path.join(folder_path, dir))
                            shutil.rmtree(os.path.join(folder_path, dir, d)) # Finally removing numeric folder


removeFolder = RemoveFolder()