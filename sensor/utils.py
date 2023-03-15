import pandas as pd
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.config import mongo_client
import os,sys
import yaml
import numpy as np
import dill

def get_collection_as_dataframe(database_name:str,collection_name:str) ->pd.DataFrame:
    """
    Description: This function returns collection as pandas dataframe

    ====================================
    params:
    database_name= Database name
    collection_name= Collection name

    ====================================
    """
    try:
        logging.info(f"reading data from database:{database_name} and collection: {collection_name}")
        df=pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info("found columns {df.columns}")
        if "_id" in df.columns:
            logging.info("dropping column _id")
            df=df.drop("_id",axis=1)
        logging.info(f"rows and columns in df is {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e,sys)
    
