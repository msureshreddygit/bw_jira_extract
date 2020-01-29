import csv
import logging
import os


class MakeDict:
    @staticmethod
    def makedict(file):
        if os.path.isfile(file):
            with open(file, mode='r') as infile:
                reader = csv.reader(infile)
                try:
                    mydict = {rows[0]: rows[1] for rows in reader}
                    logging.info("Dictionary creation form file:" + file)
                    return mydict
                except IndexError:
                    print("File delimiter should be comma")
                    logging.ERROR("Error while creating dictionary from csv file")

        else:
            print("Please provide the valid file")
            logging.error("Error while reading csv file or not a csv file delimited by comma")
            exit()


dictObj = MakeDict()
