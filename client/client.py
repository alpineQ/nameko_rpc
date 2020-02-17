from nameko.standalone.rpc import ClusterRpcProxy
import pika
from time import sleep

config = {
    'AMQP_URI': 'amqp://guest:guest@rabbitmq'
}


def check_connection():
    """try to establish connection and check its status"""
    # set amqp credentials
    parameters = pika.URLParameters(config['AMQP_URI'])
    try:
        connection = pika.BlockingConnection(parameters)
        if connection.is_open:
            print('OK')
            connection.close()
            return True
    except Exception as error:
        print('Error:', error.__class__.__name__)
        return False


while not check_connection():
    print("Waiting...")
    sleep(2)

with ClusterRpcProxy(config) as rpc:
    print(rpc.greet_service.greet('Max K'))

