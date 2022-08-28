from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from shortner.exceptions import NotFound

logger = settings.LOGGER

def exception_handler(func):

    def inner_function(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except ObjectDoesNotExist as e:
            logger.exception(e)
            raise NotFound("Not found")

        except Exception as e:
            logger.exception(e)
            raise e

    return inner_function
