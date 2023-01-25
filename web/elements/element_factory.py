from .element import Element


class ElementFactory:
    def __init__(self, locator, selector,context):
        self.locator = locator
        self.selector = selector
        self.context = context

    def element(self):
        return Element(self.locator, self.selector, self.context)

    def element_with_parameters(self, *args):
        return Element(self.locator, self.selector.format(*args), self.context)