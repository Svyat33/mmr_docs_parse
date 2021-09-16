import logging
import os
from dotenv import load_dotenv
from parse.api import send_document
from parse.link import DecisionLink, get_one_decision

load_dotenv()
logger = logging.getLogger(__name__)

if __name__ == '__main__':

    for link in DecisionLink(int(os.getenv('DOC_QTY', 10))):
        try:
            doc = get_one_decision(link)
        except:
            logger.warning(f"Ошибка разбора адреса {link}")
            continue
        res = send_document(doc)
        print(res.status_code, res.json())
        # Результат отправки на проверку:
        # logger.info(res.json())
