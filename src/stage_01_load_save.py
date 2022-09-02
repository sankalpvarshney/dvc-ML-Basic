from ast import arg
from curses import raw
from src.utils.all_utils import read_yaml,create_directory
import argparse
import pandas as pd
import os


def get_data(config_path):
    config = read_yaml(config_path)
    remote_data_path = config["data_source"]
    df = pd.read_csv(remote_data_path,sep=";")

    # Save the dataset in the local directory
    # Create path to directory: artifact/raw_local_dir/data.csv
    artifact_dir = config["artifacts"]["artifacts_dir"]
    raw_local_dir = config["artifacts"]["raw_local_dir"]
    raw_local_file = config["artifacts"]["raw_local_file"]

    raw_local_dir_path = os.path.join(artifact_dir,raw_local_dir)
    raw_local_file_path = os.path.join(raw_local_dir_path,raw_local_file)
    create_directory(dirs=[raw_local_dir_path])
    
    df.to_csv(raw_local_file_path,sep=",",index=False)
    # print(raw_local_file_path)

    # print(df.head())

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)
    # print(parsed_args.config)