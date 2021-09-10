import logging

from parse.api import send_document
from parse.link import DecisionLink, get_one_decision

logger = logging.getLogger(__name__)

if __name__ == '__main__':

    for link in DecisionLink(10):
        try:
            doc = get_one_decision(link)
        except:
            logger.warning(f"Ошибка разбора адреса {link}")
            continue
        res = send_document(doc)
        # Результат отправки на проверку:
        # logger.info(res.json())
