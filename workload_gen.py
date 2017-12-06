import logging

from scotty import utils

import pymongo

logger = logging.getLogger(__name__)


def run(context):
    workload = context.v1.workload
    utils.ExperimentHelper(context)
    logger.info('{}'.format(workload.params['greeting']))
    mongo_user = workload.params['mongo_user']
    mongo_password = workload.params['mongo_password']
    mongo_host = workload.params['mongo_host']
    mongo_port = workload.params['mongo_port']
    mongo_port = int(float(mongo_port))
    mongo_client = pymongo.MongoClient(mongo_host,
                                       mongo_port,
                                       username=mongo_user,
                                       password=mongo_password)
    logger.info(mongo_client)
    database = mongo_client.smartshark_test
    logger.info(database)
    collection = database.code_entity_state
    logger.info(collection)
    logger.info('I\'m workload generator {}'.format(workload.name))
    return None


def clean(context):
    pass
