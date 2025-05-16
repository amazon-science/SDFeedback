# SDFeedback

<table>
  <tr>
    <td style="padding: 0;">
      <a href="https://huggingface.co/collections/AmazonScience/migrationbench-68125452fc21a4564b92b6c3">
        <img src="https://img.shields.io/badge/-🤗 MigrationBench-4d5eff?style=flatten&labelColor" alt="MigrationBench (Hugging Face)">
      </a>
    </td>
    <td style="padding: 0;">
      <a href="https://github.com/amazon-science/MigrationBench">
        <img src="https://img.shields.io/badge/MigrationBench-000000?style=flatten&logo=github" alt="MigrationBench (GitHub)">
      </a>
    </td>
    <td style="padding: 0;">
      <a href="https://github.com/amazon-science/SDFeedback">
        <img src="https://img.shields.io/badge/SDFeedback-000000?style=flatten&logo=github&logoColor=white" alt="SDFeedback (GitHub)">
      </a>
    </td>
    <td style="padding: 0;">
      <a href="https://arxiv.org/abs/2505.09569">
        <img src="https://img.shields.io/badge/arXiv-2505.09569-b31b1b.svg?style=flatten" alt="MigrationBench (arXiv)">
      </a>
    </td>
    <td style="padding: 0; padding-left: 10px; vertical-align: middle;">
      <a href="https://huggingface.co/datasets/AmazonScience/migration-bench-java-full">
        <img src="https://img.shields.io/badge/-🤗 java--full-8a98ff?style=flat&labelColor" alt="java-full">
      </a>
    </td>
    <td style="padding: 0; vertical-align: middle;">
      <a href="https://huggingface.co/datasets/AmazonScience/migration-bench-java-selected">
        <img src="https://img.shields.io/badge/-🤗 java--selected-8a98ff?style=flat&labelColor" alt="java-selected">
      </a>
    </td>
    <td style="padding: 0; vertical-align: middle;">
      <a href="https://huggingface.co/datasets/AmazonScience/migration-bench-java-utg">
        <img src="https://img.shields.io/badge/-🤗 java--utg-8a98ff?style=flat&labelColor" alt="java-utg">
      </a>
    </td>
  </tr>
</table>

<!--
npm install -g markdown-toc
markdown-toc -i README.md
-->

<!-- toc -->

- [1. 📖 Overview](#1--overview)
  * [1.1 MigrationBench: Datasets and Evaluation Framework](#11-migrationbench-datasets-and-evaluation-framework)
  * [1.2 SDFeedback: Migration with LLMs](#12-sdfeedback-migration-with-llms)
- [2. 🤗 MigrationBench Datasets](#2--migrationbench-datasets)
- [3. Code Migration with LLMs](#3-code-migration-with-llms)
  * [3.1 Single Job](#31-single-job)
    + [3.1.1 Basic Setup](#311-basic-setup)
    + [3.1.2 Install MigrationBench and SDFeedback](#312-install-migrationbench-and-sdfeedback)
    + [3.1.3 Local Run](#313-local-run)
  * [3.2 Batch Job](#32-batch-job)
    + [3.2.1 ~~Local Run~~](#321-local-run)
    + [3.2.2 EMRS Run](#322-emrs-run)
- [4. 📚 Citation](#4--citation)

<!-- tocstop -->

## 1. 📖 Overview

[SDFeedback](https://github.com/amazon-science/SDFeedback)
is a library to conduct code migration with LLMs,
and improves efficacy by providing feedback to LLMs as specific as possible,
motivated by [Teaching Large Language Models to Self-Debug](https://arxiv.org/abs/2304.05128).

- Reference paper: [MigrationBench: Repository-Level Code Migration Benchmark from Java 8](https://arxiv.org/abs/2505.09569)


### 1.1 [MigrationBench](https://github.com/amazon-science/MigrationBench): Datasets and Evaluation Framework

1. [🤗 MigrationBench](https://huggingface.co/collections/AmazonScience/migrationbench-68125452fc21a4564b92b6c3)
is a large-scale code migration **benchmark dataset** at the **repository** level,
across multiple programming languages.
    * Current and initial release includes `java 8` repositories with the `maven` build system, as of May 2025.
    * See more details in [2. 🤗 MigrationBench Datasets](#2--migrationbench-datasets)
1. [MigrationBench](https://github.com/amazon-science/MigrationBench)
is the **evaluation framework** to assess code migration success,
from `java 8` to `17` or any other long-term support versions.

### 1.2 [SDFeedback](https://github.com/amazon-science/SDFeedback): Migration with LLMs

[SDFeedback](https://github.com/amazon-science/SDFeedback)
(current package)
is to conduct code migration with LLMs as a baseline solution,
and it relies on the
[MigrationBench](https://github.com/amazon-science/MigrationBench)
package for the final evaluation.
- It builds an ECR image and then
- It runs both code migration and final evaluation with AWS Elastic Map Reduce Serverless (EMRS) in a scalable way.


## 2. [🤗 MigrationBench](https://huggingface.co/collections/AmazonScience/migrationbench-68125452fc21a4564b92b6c3) Datasets

There are three datasets in [🤗 MigrationBench](https://huggingface.co/collections/AmazonScience/migrationbench-68125452fc21a4564b92b6c3):
- All repositories included in the datasets are available on GitHub, under the `MIT` or `Apache-2.0` license.

| Index | Dataset                                       | Size  | Notes                                                                                               |
|-------|-----------------------------------------------|-------|-----------------------------------------------------------------------------------------------------|
| 1     | [🤗 `AmazonScience/migration-bench-java-full`](https://huggingface.co/datasets/AmazonScience/migration-bench-java-full)         | 5,102 | Each repo has a test directory or at least one test case                              |
| 2     | [🤗 `AmazonScience/migration-bench-java-selected`](https://huggingface.co/datasets/AmazonScience/migration-bench-java-selected) |   300 | A **subset** of [🤗 `migration-bench-java-full`](https://huggingface.co/datasets/AmazonScience/migration-bench-java-full)                                          |
| 3     | [🤗 `AmazonScience/migration-bench-java-utg`](https://huggingface.co/datasets/AmazonScience/migration-bench-java-utg)           | 4,814 | The unit test generation (utg) dataset, **disjoint** with [🤗 `migration-bench-java-full`](https://huggingface.co/datasets/AmazonScience/migration-bench-java-full)|


## 3. Code Migration with LLMs

We support running code migration for MigrationBench in two modes:
1. Single job mode: For a single repository and
2. Batch job mode: For multiple repositories with EMRS
    - **TL;DR**: To run batch mode, one can skip to [3.2.2 EMRS Run](#322-emrs-run) directly.

### 3.1 Single Job

To get started with code migration with LLMs from `java 8` to `17`,
under either minimal migration or maximal migration
(See the [arXiv paper](https://arxiv.org/abs/2505.09569) for the definition):

#### 3.1.1 Basic Setup

Verify you have `java 17`, `maven 3.9.6` and `conda` (optional) locally:

```
# java
~ $ java --version
openjdk 17.0.15 2025-04-15 LTS
OpenJDK Runtime Environment Corretto-17.0.15.6.1 (build 17.0.15+6-LTS)
OpenJDK 64-Bit Server VM Corretto-17.0.15.6.1 (build 17.0.15+6-LTS, mixed mode, sharing)
```

```
# maven
~ $ mvn --version
Apache Maven 3.9.6 (bc0240f3c744dd6b6ec2920b3cd08dcc295161ae)
Maven home: /usr/local/bin/apache-maven-3.9.6
Java version: 17.0.15, vendor: Amazon.com Inc., runtime: /usr/lib/jvm/java-17-amazon-corretto.x86_64
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "5.10.236-208.928.amzn2int.x86_64", arch: "amd64", family: "unix"
```

```
# conda (Optional)
$ conda --version
conda 25.1.1
```

#### 3.1.2 Install [MigrationBench](https://github.com/amazon-science/MigrationBench) and [SDFeedback](https://github.com/amazon-science/SDFeedback)

```
cd ~
git clone https://github.com/amazon-science/MigrationBench.git
git clone https://github.com/amazon-science/SDFeedback.git

# They're optional if one doesn't need a conda env
# export CONDA_ENV=sd-feedback
# conda create -n $CONDA_ENV python=3.9
# conda activate $CONDA_ENV

cd ~/MigrationBench
pip install -r requirements.txt -e .

cd ~/SDFeedback
pip install -r requirements.txt -e .
```

#### 3.1.3 Local Run

To run code migration for a single repository:

```
cd ~/SDFeedback/src/self_debug

python run_self_debugging.py ...
```

### 3.2 Batch Job

To run code migration in batch mode for multiple repositories,
one can run it ~~either locally or~~ through EMRs.

#### 3.2.1 ~~Local Run~~

**TL;DR**:
Local run for batch job is typically for debugging and integration test purposes,
and it's **NOT** recommended.

See relevant `spark` scripts for reference:
- `src/self_debug/batch/spark_build.py`
- `src/self_debug/batch/spark_debug.py`

#### 3.2.2 EMRS Run

Before submitting a job to EMRS, make sure you have the following ready:
- Set up IAM roles, network, security groups, etc correctly
- Set up ECR repository
- Set up SES (optional)

1. Build an ECR image

```
cd ~/SDFeedback/src/self_debug/container

./image.sh ...
```

2. Submit a spark job to EMRS

Note that security keys might be subject to `12h` timeout.

```
cd ~/SDFeedback/src/self_debug/batch

# Update config file as needed for `emrs.py`, e.g. use the right ECR image in step `#1`
python emrs.py ...
```


## 4. 📚 Citation

```bibtex
@misc{liu2025migrationbenchrepositorylevelcodemigration,
      title={MIGRATION-BENCH: Repository-Level Code Migration Benchmark from Java 8},
      author={Linbo Liu and Xinle Liu and Qiang Zhou and Lin Chen and Yihan Liu and Hoan Nguyen and Behrooz Omidvar-Tehrani and Xi Shen and Jun Huan and Omer Tripp and Anoop Deoras},
      year={2025},
      eprint={2505.09569},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      url={https://arxiv.org/abs/2505.09569},
}
```
