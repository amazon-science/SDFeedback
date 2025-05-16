"""Import dataset from huggingface."""

import os

import datasets

from self_debug.proto import dataset_pb2
from migration_bench.common.hf_utils import load_hf_dataset

# https://huggingface.co/datasets/AmazonScience/migration-bench-java-full
JAVA_FULL = "AmazonScience/migration-bench-java-full"
JAVA_SELECTED = "AmazonScience/migration-bench-java-selected"
JAVA_UTG = "AmazonScience/migration-bench-java-utg"

COLUMN_REPO = "repo"
COLUMN_COMMIT = "base_commit"
COLUMNS = (COLUMN_REPO, COLUMN_COMMIT)

DATASET_NAME_OPTIONS = {
    dataset_pb2.Dataset.HuggingfaceOption.MIGRATION_BENCH_JAVA_FULL: JAVA_FULL,
    dataset_pb2.Dataset.HuggingfaceOption.MIGRATION_BENCH_JAVA_SELECTED: JAVA_SELECTED,
    dataset_pb2.Dataset.HuggingfaceOption.MIGRATION_BENCH_JAVA_UTG: JAVA_UTG,
}


def resolve_hf_dataset(ds_config, **kwargs):
    """Resolve HF dataset by name."""
    if (
        (not ds_config.HasField("hf_option"))
        or len(ds_config.dataset_repos)
        or ds_config.hf_option not in DATASET_NAME_OPTIONS
    ):
        return ds_config

    kwargs.update(
        {
            "name": DATASET_NAME_OPTIONS[ds_config.hf_option],
        }
    )

    rows = load_hf_dataset(**kwargs)
    for row in zip(rows[COLUMN_REPO], rows[COLUMN_COMMIT]):
        repo, commit = row
        cfg = ds_config.dataset_repos.add()
        cfg.github_repo.github_url = os.path.join("https://github.com", repo)
        cfg.github_repo.commit_id = commit

    return ds_config
