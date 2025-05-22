import logging
import sys
from fastapi import Request
import time

logger = logging.getLogger()
formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler(stream=sys.stdout)
file_handler = logging.FileHandler('app.log')

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.handlers = [stream_handler, file_handler]

logger.setLevel(logging.INFO)


async def log_request(request: Request, call_next):
    body = await request.body()
    log_dict = {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "body": body.decode('utf-8')
    }
    logger.info(f"Request: {log_dict}")

    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"Response status: {response.status_code} in {duration:.2f} s")
    return response






