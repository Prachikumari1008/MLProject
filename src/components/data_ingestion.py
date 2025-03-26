import os
import sys

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()


    def initiate_data_ingestion(self):
        
        logging.info("Entered the data ingestion components")
        try:
            df = pd.read_csv("notebook\stud.csv")
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.data_ingestion_config.raw_data_path , index=False , header=True)

            logging.info("Train Test Split initiated")
            train_set , test_set = train_test_split(df, test_size= 0.2 , random_state=42)
           
            train_set.to_csv(self.data_ingestion_config.train_data_path, index= False, header= True)

            test_set.to_csv(self.data_ingestion_config.test_data_path, index=False,header=True)

            logging.info("Ingestion of the data is completed.")

            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()