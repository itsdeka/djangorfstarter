from django.core.exceptions import ValidationError

import re

class NumberValidator(object):
    error = 'The password must contain at least one numeric character, 0-9.'

    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(self.error)

    def get_help_text(self):
        return self.error

class UppercaseValidator(object):
    error = 'The password must contain at least one capital letter, A-Z.'

    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(self.error)

    def get_help_text(self):
        return self.error

class LowercaseValidator(object):
    error = 'The password must contain at least one lowercase letter, a-z.'

    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(self.error)

    def get_help_text(self):
        return self.error
