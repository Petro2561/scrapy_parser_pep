from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = "results"

DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S"
STATUS_SUMMARY_NAME = "status_summary"

BOT_NAME = "pep_parse"

NEWSPIDER_MODULE = "pep_parse.spiders"
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

FEEDS = {
    f"{RESULTS_DIR}/pep_%(time)s.csv": {
        "format": "csv",
        "overwrite": True,
        "fields": ["number", "name", "status"],
    },
}

ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 1,
}
