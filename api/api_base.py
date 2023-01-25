import requests


class ApiBaseActions:
    def __init__(self, base_url):
        if base_url.endswith("/"):
            self.base_url = base_url
        else:
            self.base_url = base_url + "/"
        self.session = requests.Session()

    def make_request(self, method: str, route_url: str = None, **kwargs):
        request_methods = {"GET": self.session.get,
                           "POST": self.session.post
                           }
        if route_url is not None:
            if route_url.startswith("/"):
                route_url = route_url[1:]
            reuest_url = self.base_url + route_url

        if request_methods.get(method) is not None:
            print(f" making {method} request to {reuest_url}")
            response = request_methods[method](reuest_url, **kwargs)
        else:
            raise NameError("Invalid API method provided")
        return response

