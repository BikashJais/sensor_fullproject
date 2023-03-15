import os
import logging
from datetime import datetime


#creating log file name
LOG_FILE_NAME= f"{datetime.now().strftime('%m%d%Y__%H%M%Y')}.log"

#creating logs directory/Folder

LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")


#create folder/directory if not exist
os.makedirs(LOG_FILE_DIR,exist_ok=True)


#creating whole  log file path

LOG_FILE_PATH= os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
