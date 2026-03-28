from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory

import mlflow


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the MLflow logging example."""
    parser = argparse.ArgumentParser(
        description="Log a small example experiment to a local MLflow server.",
    )
    parser.add_argument(
        "--tracking-uri",
        default=os.getenv("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000"),
        help="MLflow tracking URI.",
    )
    parser.add_argument(
        "--experiment-name",
        default="assignment-local-experiment",
        help="Name of the MLflow experiment to create or reuse.",
    )
    parser.add_argument(
        "--run-name",
        default="log-example-run",
        help="Name for the MLflow run.",
    )
    return parser.parse_args()


def main() -> None:
    """Create an experiment, log parameters, and upload a small artifact."""
    args = parse_args()

    mlflow.set_tracking_uri(args.tracking_uri)
    experiment = mlflow.set_experiment(args.experiment_name)

    with TemporaryDirectory() as temp_dir:
        artifact_path = Path(temp_dir) / "run_summary.json"
        artifact_path.write_text(
            json.dumps(
                {
                    "note": "Example artifact for the MLflow assignment.",
                    "tracking_uri": args.tracking_uri,
                    "experiment_name": args.experiment_name,
                    "run_name": args.run_name,
                },
                indent=2,
            ),
            encoding="utf-8",
        )

        with mlflow.start_run(
            experiment_id=experiment.experiment_id,
            run_name=args.run_name,
        ) as run:
            mlflow.log_param("dataset", "penguins")
            mlflow.log_param("model_type", "baseline-example")
            mlflow.log_metric("example_score", 0.99)
            mlflow.log_artifact(artifact_path.as_posix())

            print(f"Tracking URI: {args.tracking_uri}")
            print(f"Experiment: {args.experiment_name}")
            print(f"Run ID: {run.info.run_id}")
            print(f"Artifact logged: {artifact_path.name}")


if __name__ == "__main__":
    main()
