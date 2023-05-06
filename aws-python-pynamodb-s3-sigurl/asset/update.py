import http.client as httplib
from pynamodb.exceptions import DoesNotExist

from asset.asset_model import AssetModel
from log_cfg import logger


def update(event, context):
    logger.debug(f'event: {event}')
    try:
        asset_id = event['path']['asset_id']
        asset = AssetModel.get(hash_key=asset_id)
        asset.mark_uploaded()

    except AssertionError as e:
        return {
            'statusCode': httplib.PRECONDITION_FAILED,
            'body': {
                'error_message': f'ASSET {asset_id} state incorrect: {e}'
            },
        }

    except DoesNotExist:
        return {
            'statusCode': httplib.NOT_FOUND,
            'body': {'error_message': f'ASSET {asset_id} not found'},
        }

    return {
        "statusCode": httplib.ACCEPTED,
        "body": {
            'status': asset.state
        }
    }
