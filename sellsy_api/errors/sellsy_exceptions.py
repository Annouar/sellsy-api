class SellsyAuthenticateError(Exception):
    pass


class SellsyError(Exception):
    def __init__(self, sellsy_code_error, message):
        super(SellsyError, self).__init__(message)

        self.sellsy_code_error = sellsy_code_error
        self.message = message

    def __str__(self):
        return '{} - {}'.format(self.sellsy_code_error, self.message)
