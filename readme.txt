Commands to run code:
--root_path your_path/Bitwise_Jira_Extract_project/Jira
--file_name_file your_path/Bitwise_Jira_Extract_project/MappingFiles/out.csv
--dir_name_file your_path/Bitwise_Jira_Extract_project/MappingFiles/issue_id_summary_mapping.csv
--root_name_file your_path/Bitwise_Jira_Extract_project/MappingFiles/project_key_title_mapping.csv
--report_path your_path/Bitwise_Jira_Extract_project/Reports/
--log_file_path your_path/Bitwise_Jira_Extract_project/Logs/

Key points:
1. The log file path must be provided at the end. i.e. 6th position.
2. Path must be delimited by '/' delimiter not by '\\' delimiter.


Folder structure:
Bitwise_Jira_Extract_project
            |
            ---> Jira
            |
            ---> MappingFiles
                    |
                    ---> out.csv
                    ---> issue_id_summary_mapping.csv
                    ---> project_key_title_mapping.csv
            |
            ---> Reports
                    |
                    ---> Jira_Extract_Execution_Report_20200131_155809.xlsx
            |
            ---> Logs
                    |
                    ---> Logfile_20200131_155809.log