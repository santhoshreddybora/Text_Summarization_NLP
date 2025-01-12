from textSummarizer.entity import DataIngestionConfig
from textSummarizer.logging import logger
import os
from urllib import request
import zipfile
class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
    
    def download_data(self):
        logger.info(f"Downloading data from {self.config.source_url}")
        if not os.path.exists(self.config.local_data_file):
            filename,header=request.urlretrieve(self.config.source_url, self.config.local_data_file)
            logger.info(f"Data downloaded to {self.config.local_data_file}")
        else:
            logger.info(f"{self.config.local_data_file} already exists")
        
    def extract_unzip_file(self):
        logger.info(f"Extracting zip file {self.config.local_data_file}")
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        logger.info(f"Data extracted to {self.config.unzip_dir}")
        