from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class SymbolCheckValidator(BaseValidator):
    message = f'Нельзя использовать символы в названии задачи'
    code = 'invalid_summary'

    def compare(self, a, b):
        for i in a:
            bool_val = i in b
            if bool_val:
                return bool_val


@deconstructible
class ForbiddenWordsValidator(BaseValidator):
    message = f'описание содержит запрещенное слово.'
    code = 'forbidden_word'

    def compare(self, a, b):
        all_words = a.split(' ')
        for i in all_words:
            bool_val = i.lower() in b
            if bool_val:
                return bool_val