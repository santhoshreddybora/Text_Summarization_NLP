from textSummarizer.logging import logger
from textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline


STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f"Satge {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e
