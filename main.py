from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

#logger.info("welcome to my cutome log")

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f" >>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> dtage {STAGE_NAME} completed <<<<<< \n\n x===================x \n\n")
except Exception as e:
    logger.exception(e)
    raise e