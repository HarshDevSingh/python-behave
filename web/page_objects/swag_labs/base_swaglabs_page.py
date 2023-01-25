class BaseSwagLabsPage:
    def __int__(self, context):
        self.context = context

    def open(self):
        self.context.browser.get(self.context.WEB_URL)
