import logging
import os


class CountFiles:
    @staticmethod
    def countfile(path, mydict):
        count = 0
        if os.path.exists(path):
            for root, directory, files in os.walk(path):
                for key, value in mydict.items():
                    for file in files:
                        if file == key:
                            count = count + 1
            print("Total", count, " files to be renamed")
            logging.info("Total " + str(count) + " files to be renamed")

        else:
            print("Directory path does not exist to count number of files to be renamed")
            logging.error("Directory path does not exist")
            exit()


countFile = CountFiles()
