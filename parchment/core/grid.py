from parchment.core.row import Row
from parchment.core.core import period_key
from parchment.core.validation import is_valid_date_or_datetime
from parchment.core.choices import PERIOD_ITERATION_CHOICES, OVER_PERIOD_ITERATION_CHOICES


class Grid:

    def __init__(self, row_index, period_iteration='month', over_period_iteration='year'):
        if period_iteration in PERIOD_ITERATION_CHOICES:
            self.period_iteration = period_iteration
        else:
            raise SyntaxError('Invalid period iteration choices %s' % PERIOD_ITERATION_CHOICES)

        if over_period_iteration in OVER_PERIOD_ITERATION_CHOICES:
            self.over_period_iteration = over_period_iteration
        else:
            raise SyntaxError('Invalid layer iteration choices %s' % OVER_PERIOD_ITERATION_CHOICES)

        self.row_index = row_index

        self.row_dict = dict()
        for row in self.row_index:
            self.row_dict[row[0]] = Row(row[0], row[1], row[2])

    def add_period(self, period, value_list):
        if is_valid_date_or_datetime(period):
            if type(value_list) is list:
                for loop_index, row in enumerate(self.row_index):
                    self.row_dict[row[0]].create_block(period_key(period, self.period_iteration), value_list[loop_index])
                    print(self.row_dict[row[0]])

    def to_dict(self):
        print(self.row_dict)
        grid_dict = dict()
        for row in self.row_index:
            grid_dict[row[0]] = self.row_dict[row[0]].to_dict()
        return grid_dict
