import os
import random
from faker import Faker
from datetime import datetime, timedelta #기간 지정할때 사용 ex. D-100

fake = Faker()

local_file_path ='/home/ubuntu/dmf/automation/logs/'

def generate_log_line(timestamp):
    ip = fake.ipv4()

    method = random.choice(['GET', 'POST'])

    if random.random() < 0.5:
        path = f'/product/{random.randint(1000,9000)}'

    else:
        path = random.choice(['/index','/login', '/contact', '/signup'])

    protocol = 'HTTP/1.1'
    status_code = random.choice([200, 301, 400, 404, 500])
    respone_size = random.randint(200, 5000)
    log_line = f'{ip} [{timestamp}] "{method} {path} {protocol}" {status_code} {respone_size}'

    return log_line

def generate_logs (start_date, end_date):
    while start_date <= end_date:
        log_date_str = start_date.strftime('%Y-%m-%d') #출력 형식 포맷팅
        file_name = f'access_{log_date_str}.log'

        num_logs = random.randint(1000,2000)

        logs = []

        for _ in range(num_logs): #i(인덱스)값을 활용할 일이 없을때 _사용
            log_timestamp = start_date + timedelta(seconds=random.randint(0, 86400))
            log_timestamp = log_timestamp.strftime('%Y-%m-%d %H:%M:%S')
            log_line = generate_log_line(log_timestamp)
            logs.append(log_line)
        
        #정렬 기준점을 변경하는 코드
        logs.sort(key=lambda x: x.split('[')[1].split(']')[0])

        #파일 생성 자동화(?)
        if not os.path.exists(local_file_path):
            os.makedirs(local_file_path)

        with open(local_file_path + file_name, 'w', encoding='utf-8') as local_file:
            for log_line in logs:
                local_file.write(log_line + '\n')

        start_date += timedelta(days=1)


# 실행 구조
start_date = datetime(2024, 8, 13)
end_date = datetime(2024, 8, 31)

generate_logs(start_date,end_date)

