from datetime import datetime, timedelta

EXTENSION='.json.gz'

def get_next_file(filename):
    date = datetime.strptime(filename[0:12],"%Y-%m-%d-%H") + timedelta(hours=1)
    return f'{datetime.strftime(date,"%Y-%m-%d-%-H")}{EXTENSION}' 