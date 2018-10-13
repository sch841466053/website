class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class Core(MiddlewareMixin):
    def process_response(self,request,response):
        # print(123)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = ' GET, POST, OPTIONS, PUT, DELETE'
        response['Access-Control-Allow-Headers'] = 'Authorization, Content-Type, Depth, User-Agent, ' \
                                                   'X-File-Size, X-Requested-With, X-Requested-By,' \
                                                   ' If-Modified-Since, X-File-Name, X-File-Type, Cache-Control, Origin'

        return response