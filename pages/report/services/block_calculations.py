from .calculations import get_calculation_by_block_type


class BlockCalculation:
    def __init__(self, block):
        self.block = block
        self.calculation = get_calculation_by_block_type(self.block)
