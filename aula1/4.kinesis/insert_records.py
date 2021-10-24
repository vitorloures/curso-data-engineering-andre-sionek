import boto3
import json
from fake_web_events import Simulation


client = boto3.client('firehose')


# OBS: Firehose é um serviço de ingestão de dados batch ou streaming,
# semelhante a uma versão simples do Kafka, gerenciado pela AWS.
# Ele permite de forma simples inserir dados em datalake, datawarehouse,
# ou plataforma de dados análogas.
def put_record(event):
    data = json.dumps(event) + "\n"
    response = client.put_record(
        DeliveryStreamName='kinesis-firehose-vitor-loures',
        Record={"Data": data}
    )
    print(event)
    return response


simulation = Simulation(user_pool_size=100, sessions_per_day=10000)
events = simulation.run(duration_seconds=300)

for event in events:
    put_record(event)
