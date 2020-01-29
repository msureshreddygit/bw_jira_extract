import logging
from datetime import datetime
import pandas as pd
from pandas import ExcelWriter


class GenerateReport:
    @staticmethod
    def generate_report(key_file, path, files_dict, folder_dict):
        if not files_dict:
            print("No report is generated, as no files were renamed")
            logging.warning("No report is generated, as no files were renamed")
        else:
            root_df = pd.read_csv(key_file)

            new_df = {}
            for k, v in files_dict.items():
                val = v.split('\\')
                new_df[k] = val

            # Creating dataframe by slicing the renamed file path
            file_df = pd.DataFrame.from_dict(new_df, orient='index', columns=['extra_path', 'exportProjectKey', 'Jira_name', 'Filename'])
            root_file_join_df = pd.merge(root_df, file_df, on='exportProjectKey')

            if root_file_join_df.empty:
                filename1 = datetime.now().strftime('Jira_Extract_Execution_Report_%d%m%Y_%H%M%S.xlsx')
                writer = ExcelWriter(path + filename1)
                file_df[['exportProjectKey', 'Jira_name', 'Filename']].to_excel(writer, sheet_name='Report', index=False,  engine='xlsxwriter')
                writer.save()
                print("Report generation successful")
                logging.info("Report generation successful")
            else:
                folder_df = pd.DataFrame(folder_dict.items(), columns=['Jira_name', 'New_Jira_Name'])
                final_df = pd.merge(root_file_join_df, folder_df, on='Jira_name')
                filename1 = datetime.now().strftime('Jira_Extract_Execution_Report_%d%m%Y_%H%M%S.xlsx')
                writer = ExcelWriter(path + filename1)
                final_df[['exportProjectKey', 'jiraProjectKey', 'jiraProjectName', 'New_Jira_Name', 'Filename']].to_excel(writer, sheet_name='Report', index=False, engine='xlsxwriter')
                writer.save()
                print("Report generation successful")
                logging.info("Report generation successful")


generateReportObj = GenerateReport()