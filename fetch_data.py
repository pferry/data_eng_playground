import boto3
import logging
import os

from download import download_file
from utils import get_next_file

logging.basicConfig(level=logging.INFO)

FILE = "2022-07-01-01.json.gz"
ENVIRON = os.environ.get('ENVIRON','DEFAULT')


def fetch_data():
    current_file = get_next_file(FILE)
    res = download_file(current_file)
    logging.info(f"starting with {current_file}")
    while res.status_code == 200:
        logging.info(f"Got file {current_file}")
        print(res.status_code)
        current_file = get_next_file(current_file)
        res = download_file(current_file)
    logging.info(f"Failed to get file {current_file} with status {res.status_code} ")
    return


if __name__ == '__main__':
    print(ENVIRON)
    logging.info(f"starting")
    fetch_data()