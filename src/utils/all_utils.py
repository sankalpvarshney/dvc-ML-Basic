import yaml
import os
import json

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    
    return content

def create_directory(dirs: list):
    for dir_parh in dirs:
        os.makedirs(dir_parh, exist_ok=True)
        print(f"directory is created at {dir_parh}")

def save_local_df(data,data_path,index_status=False):
    data.to_csv(data_path, index=index_status)
    print(f"Data is saved at the path {data_path}")

def save_reports(report:dict, report_path:str):
    with open(report_path,"w") as f:
        json.dump(report,f,indent=4)
    print(f"Reports are saved at {report_path}")