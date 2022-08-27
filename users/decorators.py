from django.conf import settings
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from users.exceptions import NotFound, BadRequest


logger = settings.LOGGER

def exception_handler(func):

    def inner_function(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        
        except ObjectDoesNotExist as e:
            logger.exception(e)
            raise NotFound

        except IntegrityError as e:
            logger.exception(e)
            raise BadRequest
        
        except Exception as e:
            logger.exception(e)
            raise e

    return inner_function
