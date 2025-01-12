from textSummarizer.logging import logger
from textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from textSummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline


STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f"Satge {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} Completed")
    logger.info(f"-----------------------------------------------------------------------------------")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f"Satge {STAGE_NAME} initiated")
    data_transformation_pipeline=DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e
