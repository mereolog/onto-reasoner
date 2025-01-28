import pandas as pd


def deduplicate_report(report_file_path: str, deduplicated_report_file_path: str):
    report = pd.read_excel(report_file_path)
    report.drop_duplicates(subset=['theory_id'],keep='last',inplace=True)
    report.to_excel(deduplicated_report_file_path, index=False)
