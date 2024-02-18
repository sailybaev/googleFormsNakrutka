class URLMaker:

    def __init__(self, base_url):
        self.base_url = base_url

    def form_response_url(self):
        return self.base_url + '/formResponse'

    def view_form_url(self):
        return self.base_url + '/viewform'