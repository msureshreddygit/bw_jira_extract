import logging
import os


class RenameFiles:
    @staticmethod
    def renamefile(path, mydict):
        count = 0
        if os.path.exists(path):
            for root, directory, files in os.walk(path):
                for key, value in mydict.items():
                    for file in files:
                        if file == key:
                            count = count + 1
                            try:
                                os.rename(os.path.join(root, file), os.path.join(root, value))
                                print("The file", os.path.join(root, file), "is renamed with", os.path.join(root, value))
                                logging.info("The file" + os.path.join(root, file) + " is renamed with " + os.path.join(root, value))
                            except FileExistsError:
                                print("The file already renamed with key:", key, ", on path:", os.path.join(root, value))
                                logging.warning("File already renamed with key:" + str(key) + ", on path:" + os.path.join(root, value))
                                count = count - 1
            if count == 0:
                print("No file for renaming")
                logging.info("No files for renaming")
            else:
                print("Total ", count, " files renamed successfully")
                logging.info("Total " + str(count) + " files renamed successfully")
        else:
            print("Directory path does not exist")
            logging.error("Directory path does not exist")

    @staticmethod
    def renamedirectory(dir_path, mydict):
        count = 0
        if os.path.exists(dir_path):
            for d in os.listdir(dir_path):
                for root, directory, files in os.walk(os.path.join(dir_path , d)):
                    for key, value in mydict.items():
                        for dir in directory:
                            if dir == key:
                                count = count + 1
                                try:
                                    os.rename(os.path.join(root, dir), os.path.join(root, value))
                                    print("The folder", os.path.join(root, dir), "is renamed with",
                                          os.path.join(root, value))
                                    logging.info("The folder" + os.path.join(root, dir) + " is renamed with " +
                                                 os.path.join(root, value))
                                except FileExistsError:
                                    print("The folder already renamed with key:", key, ", on path:",
                                          os.path.join(root, value))
                                    logging.warning("Folder already renamed with key:" + str(key) + ", on path:" +
                                                    os.path.join(root, value))
                                    count = count - 1
            if count == 0:
                print("No folder for renaming")
                logging.info("No folder for renaming")
            else:
                print("Total ", count, " child folder renamed successfully")
                logging.info("Total " + str(count) + " folder renamed successfully")
        else:
            print("Directory path does not exist")
            logging.error("Directory path does not exist")

    @staticmethod
    def renameroot(root_path, mydict):
        count = 0
        if os.path.exists(root_path):
            for root, directory, files in os.walk(root_path):
                for key, value in mydict.items():
                    for dir in directory:
                        if dir == key:
                            count = count + 1
                            try:
                                os.rename(os.path.join(root, dir), os.path.join(root, value))
                                print("The root folder", os.path.join(root, dir), "is renamed with",
                                      os.path.join(root, value))
                                logging.info("The root folder" + os.path.join(root, dir) + " is renamed with " +
                                             os.path.join(root, value))
                            except Exception:
                                print("Root folder already renamed with key:" + str(key) + ", on path:"
                                                + os.path.join(root, value))
                                logging.warning("Root folder already renamed with key:" + str(key) + ", on path:"
                                                + os.path.join(root, value))
                                count = count - 1
            if count == 0:
                print("No root folder for renaming")
                logging.info("No root folder for renaming")
            else:
                print("Total ", count, " root folders renamed successfully")
                logging.info("Total " + str(count) + " root folder renamed successfully")
        else:
            print("Directory path does not exist")
            logging.error("Directory path does not exist")


renameFile = RenameFiles()
