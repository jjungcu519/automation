#0>1로 가는, 뭔가 코드 빼먹은듯

import os
from hdfs import InsecureClient

hdfs_client = InsecureClient('http://localhost:9870', user='ubuntu')

local_logs_path = '/home/ubuntu/dmf/automation/logs/' 
hdfs_logs_path = '/user/ubuntu/input/logs/'

local_files = os.listdir(local_logs_path)

for file_name in local_files:
    local_file_path = local_logs_path + file_name
    hdfs_file_path = hdfs_logs_path + file_name

    if hdfs_client.content(hdfs_file_path, strict=False):
        print(f'이미 존재하는 파일입니다. {file_name}')
    else:
        hdfs_client.upload(hdfs_file_path, local_file_path)
        print(f'{file_name}')