from rest_framework.exceptions import ValidationError


# custom validator, you need override __call__ function
class CustomEmailValidator(object):
    def __call__(self, value):
        black_list = ["gmail.com", "email.ru", ]
        for row in black_list:
            if row in value:
                raise ValidationError("This domain blocked")
        return value
