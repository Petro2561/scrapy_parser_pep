from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

# Константы
RESULTS_DIR = "results"
DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S"
STATUS_SUMMARY_NAME = "status_summary"

BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"

ROBOTSTXT_OBEY = True

FEEDS = {
    "results/pep_%(time)s.csv": {
        "format": "csv",
        "overwrite": True,
        "fields": ["number", "name", "status"],
    },
}

ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 1,
}
