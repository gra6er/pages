import sys
from .block_calc import PlainText
from .block_view import PlainTextView


class BlockProcessor:
    def __init__(self, block):
        self.block = block
        self.calculation = self.get_calculation()
        self.view = self.get_view(self.calculation.data)

    def get_calculation(self):
        try:
            calc_class_name = self.block.calc_type
            calc_class = getattr(sys.modules["report.services.block_calc"], calc_class_name)
            calc_params = str(self.block.params).replace("'", "\"")
            calc = calc_class(calc_params)
            return calc
        except Exception as ex:
            # TODO refactor this for creating PlainTextView
            print(ex)
            param = '{"text": "Error creating calculation"}'
            return PlainText(param)

    # TODO refactor this: merge this def with previous into class generator tool
    def get_view(self, data):
        try:
            view_class_name = self.block.view_type
            view_class = getattr(sys.modules["report.services.block_view"], view_class_name)
            view_params = str(self.block.params).replace("'", "\"")
            view = view_class(data, view_params)
            return view
        except Exception as ex:
            # TODO refactor this for creating PlainTextView
            print(ex)
            return PlainTextView(pt_data=f"Error creating View: {ex}")
