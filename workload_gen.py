import logging
import time

import pymongo
from scotty import utils

logger = logging.getLogger(__name__)


def run(context):
    workload = context.v1.workload
    utils.ExperimentHelper(context)
    mongo_user = workload.params['mongo_user']
    mongo_password = workload.params['mongo_password']
    mongo_host = workload.params['mongo_host']
    mongo_port = workload.params['mongo_port']
    sample_size = workload.params['sample_size']
    mongo_port = int(float(mongo_port))
    database_name = 'smartshark_test'
    mongo_client = pymongo.MongoClient(
        mongo_host,
        mongo_port,
        username=mongo_user,
        password=mongo_password,
        authSource=database_name)
    database = mongo_client.smartshark_test
    collection = database.code_entity_state
    document_count = collection.count()
    collection_size_messge = 'Collection count:'.format(document_count)
    logger.info(collection_size_messge)
    pipeline = [{
        '$sample': {
            'size': sample_size
        }
    }, {
        '$group': {
            '_id': None,
            'avg': {
                '$avg': '$start_line'
            }
        }
    }]
    start_time = time.time()
    collection.aggregate(pipeline)
    end_time = time.time()
    duration = end_time - start_time
    logger.info('The MSR workload took {}s'.format(duration))
    return {'duration': duration}


def clean(context):
    pass
