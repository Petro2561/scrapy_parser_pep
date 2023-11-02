import csv
import datetime as dt
from collections import defaultdict

from scrapy.exceptions import DropItem

from pep_parse.settings import (BASE_DIR, DATETIME_FORMAT, RESULTS_DIR,
                                STATUS_SUMMARY_NAME)

ITEM_ERROR = "Объект не содержит статуса"


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses = defaultdict()

    def process_item(self, item, spider):
        if "status" not in item:
            raise DropItem(ITEM_ERROR)
        self.statuses[item["status"]] = (
            self.statuses.get(item["status"], 0) + 1
        )
        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f"{STATUS_SUMMARY_NAME}_{now_formatted}.csv"
        file_path = self.results_dir / file_name
        with open(file_path, mode="w", encoding="utf-8") as file:
            csv.writer(file, dialect=csv.unix_dialect).writerows(
                [
                    ("Статус", "Количество"),
                    *self.statuses.items(),
                    ("Total", sum(self.statuses.values())),
                ]
            )
