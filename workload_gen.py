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
    logger.info(mongo_user)
    logger.info(mongo_password)
    pymongo.MongoClient()
    logger.info('I\'m workload generator {}'.format(workload.name))
    return None


def clean(context):
    pass
