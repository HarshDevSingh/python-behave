from .base_element import BaseElement


class Element(BaseElement):
    def __int__(self, locator, selector, context):
        super().__init__(locator, selector, context)