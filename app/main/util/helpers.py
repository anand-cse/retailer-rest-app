import uuid


def create_id(prefix: str = None):
    """
    Generates a random ID with aa prefix
    :param prefix:
    :return:
    """
    an_id = str(uuid.uuid4())
    if prefix is not None:
        an_id = prefix + "-" + an_id
    return an_id
