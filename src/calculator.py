import logging

logger = logging.getLogger(__name__)

def add(a: int, b: int, c: int) -> int:
    result = a + b + c
    logger.info("Adding %s + %s = %s", a, b, result)
    return result