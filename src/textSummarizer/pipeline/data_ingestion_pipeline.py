from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.conponents.data_ingestion import DataIngestion


class DataIngestionPipeline:
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_unzip_file()
