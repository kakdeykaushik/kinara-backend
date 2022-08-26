from django.conf import settings

logger = settings.LOGGER

def exception_handler(func):

    def inner_function(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.exception(e)
            raise e

    return inner_function
