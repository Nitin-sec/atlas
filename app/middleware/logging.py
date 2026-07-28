import logging
import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("atlas")


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request: Request,
        call_next,
    ):
        start = time.perf_counter()

        logger.info(
            "Started %s %s",
            request.method,
            request.url.path,
        )

        try:
            response = await call_next(request)

            return response

        except Exception:
            logger.exception(
                "Unhandled exception during %s %s",
                request.method,
                request.url.path,
            )
            raise

        finally:
            duration = (
                time.perf_counter() - start
            ) * 1000

            logger.info(
                "Completed %s %s | %.2f ms",
                request.method,
                request.url.path,
                duration,
            )