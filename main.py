import argparse
import logging
import sys

from datetime import datetime
from generate_report import generateReportObj
from remove_folder import removeFolder
from countFiles import countFile
from make_dict import dictObj
from process import renameFile
from send_email import mailObj

path = sys.argv[12]
logfile = datetime.now().strftime(path + 'Logfile_%Y%m%d_%H%M%S.log')
logging.basicConfig(filename=logfile, format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')


def main():
    logging.info("Reading command line arguments")
    parser = argparse.ArgumentParser()
    parser.add_argument('--root_path', type=str, required=True)
    parser.add_argument('--file_name_file', type=str, required=True)
    parser.add_argument('--dir_name_file', type=str, required=True)
    parser.add_argument('--root_name_file', type=str, required=True)
    parser.add_argument('--report_path', type=str, required=True)
    parser.add_argument('--log_file_path', type=str, required=True)
    args = parser.parse_args()

    # Creating dictionary from .csv files
    my_dict_file = dictObj.makedict(args.file_name_file)
    my_dict_dir = dictObj.makedict(args.dir_name_file)
    my_dict_root = dictObj.makedict(args.root_name_file)

    # Counting number of files to be renamed.
    countFile.countfile(args.root_path, my_dict_file)

    # Removing if there are numeric folder name in path.
    removeFolder.remove_folder(args.root_path)

    # Renaming root, folders and files.
    logging.info("Renaming files under process...\n")
    r_files = renameFile.renamefile(args.root_path, my_dict_file)
    logging.info("Renaming sub-folders under process...\n")
    renameFile.renamedirectory(args.root_path, my_dict_dir)
    logging.info("Renaming root-folders under process...\n")
    renameFile.renameroot(args.root_path, my_dict_root)

    # Generating an excel report if files get renamed.
    logging.info("Generating reports...\n")
    report = generateReportObj.generate_report(args.root_name_file, args.report_path, r_files, my_dict_dir)

    # Sending an notifying email if files get renamed.
    logging.info("Generating an email...\n")
    mailObj.generate_mail(report)


if __name__ == '__main__':
    main()
