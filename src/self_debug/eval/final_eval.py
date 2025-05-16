"""Final eval."""

import logging
import sys

from self_debug.common import utils


# pylint: disable=unused-import
from migration_bench.eval.final_eval import (
    KEY_GITHUB_URL,
    KEY_GIT_DIFF_CONTENT,
    KEY_GIT_DIFF_FILE,
    DATASET_COMMIT_IDS,
    DATASET_NUM_TESTS,
    LHS_BRANCH,
    alias,
    run_eval,
    # run_batch_eval,
)
# pylint: enable=unused-import


def _run(github_url: str, git_diff_file: str = None):
    logging.info("Final eval: success = `%s`.", run_eval(github_url, git_diff_file))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format=utils.LOGGING_FORMAT)
    _run(*(sys.argv[1:]))
