# import os 
# import sys 
# from src.exception import CustomException
# from src.logger import logging
# import pandas as pd

# from sklearn.model_selection import train_test_split
# from dataclasses import dataclass

# @dataclass
# class DataIngestionConfig:
#     train_test_split: str=os.path.join('artificts','train.csc' )
#     test_test_split: str=os.path.join('artificts','test.csc' )
#     raw_test_split: str=os.path.join('artificts','data.csc' )

# class DataIngestion:    
#     def __init__(self):
#         self.ingestion_config = DataIngestionConfig()

#     def initiate_data_ingestion(self):
#         logging.info("Entered the data ingestion or component  ")

#         try:
            
#             df = pd.read_csv("notebook/data/stud.csv")  # Raw string
#             logging.info('Read the dataset as dataframe')

#             os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

#             df.to_csv(self.ingestion_config.raw_data_path,index=False)

#             logging.info("Train test split initiated")
#             train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

#             train_set.to_csv(self.ingestion_config.train_data_path,index=False)

#             test_set.to_csv(self.ingestion_config.test_data_path,index=False)

#             logging.info("Ingestion of the data is completed")

#             return( 
#                 self.ingestion_config.train_data_path,
#                 self.ingestion_config.test_data_path,
#             )

#         except Exception as e:
#             raise CustomException(e,sys)


# if __name__ == "__main__":
#     obj = DataIngestion()
#     obj.initiate_data_ingestion() 

import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', 'data.csv')
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion component.")

        try:
            df = pd.read_csv(r'notebook/data/stud.csv')  # Fixed path issue
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Saved raw data.")

            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)  # Fixed test data saving

            logging.info("Data ingestion completed successfully.")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
