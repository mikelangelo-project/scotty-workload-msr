import logging

from scotty import utils

import pymongo

logger = logging.getLogger(__name__)


def run(context):
    workload = context.v1.workload
    utils.ExperimentHelper(context)
    mongo_user = workload.params['mongo_user']
    mongo_password = workload.params['mongo_password']
    mongo_host = workload.params['mongo_host']
    mongo_port = workload.params['mongo_port']
    mongo_port = int(float(mongo_port))
    database_name = 'smartshark_test'
    mongo_client = pymongo.MongoClient(mongo_host,
                                       mongo_port,
                                       username=mongo_user,
                                       password=mongo_password,
                                       authSource=database_name
    )
    database = mongo_client[database_name]
    collection = database.code_entity_state
    logger.info(collection)
    collection_count = collection.count()
    logger.info('I\'ve found {} documents'.format(collection_count))
    return None


def clean(context):
    pass
