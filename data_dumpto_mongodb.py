import pymongo
import pandas as pd
import json

# connect to mongodb by giving URL
client=pymongo.MongoClient("mongodb+srv://JAISWA_B:Bikoo1996@clusterbik.2grbd0c.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH="C://Users//Bikash//Desktop//IMPORTNT//APS fault detection//aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")
    #converting data onto json so that it can be dumped into mongo db
    df.reset_index(drop=True,inplace=True)
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    #inserting record
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
