import boto3
import logging
import os
import dotenv

from download import download_file
from upload import upload_file
from utils import (
    get_next_file,
    get_bookmark,
)

logging.basicConfig(level=logging.INFO)
dotenv.load_dotenv()


ENVIRON = os.environ.get('ENVIRON')

FILE_PREFIX=os.environ.get('FILE_PREFIX')
BUCKET_NAME=os.environ.get('BUCKET_NAME')

BASELINE_FILE = os.environ.get('BASELINE_FILE')
BOOKMARK_FILE=os.environ.get('BOOKMARK_FILE')


def fetch_data():
    current_file = get_bookmark(BUCKET_NAME,BOOKMARK_FILE,FILE_PREFIX,BASELINE_FILE)
    current_file = get_next_file(current_file)
    while True:
        logging.info(f"Getting file {current_file}")
        download_res = download_file(current_file)
        if download_res.status_code == 200:
            logging.info(f"Uploading file {current_file}")
            upload_file(bucket=BUCKET_NAME, file=f'{FILE_PREFIX}/{current_file}',data=download_res.content)
            upload_file(bucket=BUCKET_NAME, file=f'{FILE_PREFIX}/{BOOKMARK_FILE}',data=current_file.encode('utf-8'))
        else:
            break
        current_file = get_next_file(current_file)
        
    logging.info(f"Failed to get file {current_file} with status {download_res.status_code} ")
    return


if __name__ == '__main__':
    logging.info(f"Starting")
    fetch_data()
    logging.info(f"Wrapping up")