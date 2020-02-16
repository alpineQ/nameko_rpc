from nameko.rpc import rpc


class GreetService(object):
    name = 'greet_service'

    @rpc
    def greet(self, name):
        return f'Hello {name}!'
