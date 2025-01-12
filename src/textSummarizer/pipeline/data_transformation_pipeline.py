from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.conponents.data_transformation import DataTransformation


class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.convert()
        
