from nameko.standalone.rpc import ClusterRpcProxy

config = {
    'AMQP_URI': 'pyamqp://guest:guest@rabbitmq'
}

with ClusterRpcProxy(config) as rpc:
    print(rpc.greet_service.greet('Max K'))

