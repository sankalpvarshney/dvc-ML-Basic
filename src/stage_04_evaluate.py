from src.utils.all_utils import read_yaml,create_directory,save_local_df,save_reports
import argparse
import pandas as pd
import os
import joblib
from sklearn.metrics import mean_squared_error,mean_absolute_error, r2_score
import numpy as np


def evaluate_metrics(actual_values, predicted_values):
    rmse = np.sqrt(mean_squared_error(actual_values,predicted_values))
    mae = mean_absolute_error(actual_values,predicted_values)
    r2 = r2_score(actual_values,predicted_values)
    return rmse,mae,r2

def evaluate(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifact_dir = config["artifacts"]["artifacts_dir"]
    split_data_dir = config["artifacts"]["split_data_dir"]

    test_data_filename = config["artifacts"]["test"]
    test_data_path = os.path.join(artifact_dir,split_data_dir,test_data_filename)

    test_data = pd.read_csv(test_data_path)

    test_y = test_data["quality"]
    test_x = test_data.drop("quality",axis=1)

    model_dir = config["artifacts"]["model_dir"]
    model_file_name = config["artifacts"]["model_file"]
    model_path = os.path.join(artifact_dir,model_dir,model_file_name)

    lr = joblib.load(model_path)

    predicted_values = lr.predict(test_x)
    rmse,mae,r2 = evaluate_metrics(test_y,predicted_values)
    scores = {
        "rmse":rmse,
        "mae":mae,
        "r2":r2
    }
    # print(rmse,mae,r2)

    scores_dir = config["artifacts"]["report_dir"]
    score_dir_path = os.path.join(artifact_dir,scores_dir)
    create_directory([score_dir_path])

    score_file = config["artifacts"]["scores"]
    score_file_path = os.path.join(score_dir_path,score_file)
    save_reports(scores,score_file_path)




    

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")
    
    parsed_args = args.parse_args()
    evaluate(config_path=parsed_args.config,params_path=parsed_args.params)
    # print(parsed_args.config)