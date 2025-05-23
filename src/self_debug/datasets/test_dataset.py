"""Unit tests for dataset.py."""

import logging
import os
import unittest

from parameterized import parameterized
from self_debug.proto import config_pb2

from self_debug.common import utils
import dataset as dataset_utils
from self_debug.datasets import hf_utils


class TestDatasets(unittest.TestCase):
    """Unit tests for dataset.py."""

    @parameterized.expand(
        (
            (
                "./configs/dataset_java_demo--xmpp-light.pbtxt",
                8,
                (0, 0, 0, 0, 0),
            ),
            # Java
            (
                "configs/java/java__hf_full_20250429.pbtxt",
                5102,
                (5102, 0, 0, 5102, 5102),
            ),
            (
                "configs/java/java__hf_selected_20250429.pbtxt",
                300,
                (300, 0, 0, 300, 300),
            ),
            (
                "configs/java/java__hf_utg_20250429.pbtxt",
                4814,
                (4814, 0, 0, 4814, 4814),
            ),
            (
                "configs/java/java__v05_raw_20250113.pbtxt",
                16154,
                (16154, 0, 0, 16154, 16154),
            ),
            (
                "configs/java/java__v05.1_valid-url_20250202.pbtxt",
                16010,
                (16010, 0, 0, 16010, 16010),
            ),
            (
                "configs/java/java__v05.2_valid-j-version_20250204.pbtxt",
                12107,
                (12107, 0, 0, 12107, 12107),
            ),
            (
                "configs/java/java__v05.2x_valid-eff-j-version_20250207.pbtxt",
                11378,
                (11378, 0, 0, 11378, 11378),
            ),
            (
                "configs/java/java__v05.3_base-commit-index-0_20250210.pbtxt",
                9366,
                (9366, 0, 0, 9366, 9366),
            ),
            (
                "configs/java/java__v05.3c_base-commit-index-0_20250210.pbtxt",
                2012,
                (2012, 0, 0, 2012, 2012),
            ),
            (
                "configs/java/java__v05.4_base-commit-index-any_20250212.pbtxt",
                610,
                (610, 0, 0, 610, 610),
            ),
            (
                "configs/java/java__v05.4c_base-commit-index-any_20250212.pbtxt",
                1402,
                (1402, 0, 0, 1402, 1402),
            ),
            (
                "configs/java/java__v05.6_20250321.pbtxt",
                9978,
                (9978, 0, 0, 9978, 9978),
            ),
            (
                "configs/java/java__v05.6.0-timeout-05min_20250320.pbtxt",
                9750,
                (9750, 0, 0, 9750, 9750),
            ),
            (
                "configs/java/java__v05.6.0c-timeout-05min_20250320.pbtxt",
                1628,
                (1628, 0, 0, 1628, 1628),
            ),
            (
                "configs/java/java__v05.6.1-timeout-15min_20250321.pbtxt",
                228,
                (228, 0, 0, 228, 228),
            ),
            (
                "configs/java/java__v05.6.1c-timeout-15min_20250321.pbtxt",
                1400,
                (1400, 0, 0, 1400, 1400),
            ),
        )
    )
    def test_load_dataset(self, filename, expected_len, expected_field_stats):
        """Unit tests load_dataset."""
        pwd = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(pwd, filename)
        if not filename.endswith(".json"):
            config = utils.load_proto(filename, config_pb2.Config)
            hf_utils.resolve_hf_dataset(config.dataset)
            if config.dataset.dataset_repo.HasField(
                "github_repo"
            ) and config.dataset.dataset_repo.github_repo.HasField("filename_json"):
                config.dataset.dataset_repo.github_repo.filename_json = (
                    config.dataset.dataset_repo.github_repo.filename_json.replace(
                        "/self-dbg/src/self_debug/datasets", pwd
                    )
                )
            logging.info("Config: <<<%s>>>", config)
            filename = config.dataset

            if config.dataset.HasField(
                "dataset_partition"
            ) and config.dataset.dataset_partition.HasField("partition_repos"):
                self.assertEqual(
                    config.dataset.dataset_partition.partition_repos, expected_len
                )

        dataset = dataset_utils.load_dataset(filename)

        self.assertIsInstance(dataset, tuple)
        self.assertEqual(len(dataset), expected_len)

        self.assertEqual(dataset_utils.show_stats(dataset), expected_field_stats)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format=utils.LOGGING_FORMAT)
    unittest.main()
