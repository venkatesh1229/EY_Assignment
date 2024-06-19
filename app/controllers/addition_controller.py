from app.utils.addition_worker import add_numbers as add

def add_numbers(payload):
    """ calls the utility function to perform the addition """
    return add(payload)
