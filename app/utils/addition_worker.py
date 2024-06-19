import multiprocessing
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add_numbers_worker(numbers):
    """ adds the numbers in a single list  """
    try:
        return sum(numbers)
    except Exception as e:
        logger.error(f"Error in worker: {e}")
        raise

def add_numbers(payload):
    """  multiprocessing pool to process multiple lists concurrently   """
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(add_numbers_worker, payload)
        return results
