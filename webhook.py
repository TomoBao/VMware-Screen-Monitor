
import aiohttp

from config import WEBHOOK_URL
from logger import logger


async def send_webhook_message(message: str) -> bool:
    if not WEBHOOK_URL:
        logger.info("Webhook not configured")
        return False

    try:
        timeout = aiohttp.ClientTimeout(total=10)

        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(
                WEBHOOK_URL,
                json={"content": message[:2000]},
                allow_redirects=False,
            ) as response:
                if response.status not in (200, 204):
                    logger.warning(
                        "Webhook HTTP status: %s",
                        response.status,
                    )
                    return False

        logger.info("Webhook notification sent")
        return True

    except Exception:
        logger.exception("Webhook notification failed")
        return False
