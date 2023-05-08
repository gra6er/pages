import json
from abc import ABC, abstractmethod


class BlockView(ABC):
    def __init__(self, data):
        self.context = self.gen_context(data)

    @abstractmethod
    def gen_context(self, data):
        pass

    def get_params(self):
        return json.loads(self.params)


class ValueLogoView(BlockView):
    def __init__(self, vl_data, vl_params):
        self.error_logo = ''
        self.params = vl_params
        self.logo = self.get_params()['logo']
        self.template = 'block/value_logo.html'
        super().__init__(data=vl_data)
        # TODO add error log image

    def gen_context(self, data):
        # TODO check is this a value
        if isinstance(data, float) or isinstance(data, int):
            return {"data": str(data), "logo": self.logo}
        else:
            msg = f"Incorrect data type for ValueLogo view: float or int expected, get {type(data)}. Data: {data}"
            return {"data": msg, "logo": self.error_logo}


class PlainTextView(BlockView):
    def __init__(self, pt_data, pt_params='{}'):
        self.template = 'block/plain_text.html'
        self.params = pt_params
        super().__init__(data=pt_data)

    def gen_context(self, data):
        if isinstance(data, str):
            return data
        else:
            return f"Incorrect data type for PlainText view: str expected, get {type(data)}"
