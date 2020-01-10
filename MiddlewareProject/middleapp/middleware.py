class TestMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("pre proccessing request...")
        response=self.get_response(request)
        print(response)
        print("post proccessing request.....")
        return response
