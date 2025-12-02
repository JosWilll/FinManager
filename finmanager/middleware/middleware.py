class AuthMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
    

    def __call__(self, request):

        # Here check if device is logged in
        # redirect to the login page if not
        print("hello there!")  # Debug

        response = self.get_response(request)
        return response
   
