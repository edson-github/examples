import http.client as httplib
from asset.asset_model import AssetModel
from log_cfg import logger


def asset_list(event, context):
    logger.debug(f'event: {event}, context: {context}')

    results = AssetModel.scan()
    return {
        'statusCode': httplib.OK,
        'body': {
            'items': [dict(result) for result in results]
        }
    }
