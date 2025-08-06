"""
Data collection pipeline for multi-agent GenAI collaboration study.

This script demonstrates how one might instrument a GitHub-hosted open-source
project to collect rich metadata about human–AI collaboration during software
development tasks. In the actual experiment, this script would be executed
as part of server-side Git hooks or client-side event handlers. It logs
commit metadata, static‑analysis reports, unit‑test coverage, AI prompts,
and LLM responses. The pseudocode below outlines key steps.

The research environment uses Python 3, Git hooks, and HTTP logging. You
should adapt paths and tools (e.g., SonarQube CLI) to your specific project
structure.

Usage:
    python data_collection.py --repo-path /path/to/clone --output-dir ./logs

This script is provided for transparency and reproducibility; it does not
execute external commands in this repository. Instead, it describes the
instrumentation tasks researchers can implement.
"""

import argparse
import json
import os
from datetime import datetime

# Placeholder for SonarQube analysis call
def run_sonarqube_analysis(repo_path: str, project_key: str, token: str) -> dict:
    """Run static analysis and return a dictionary of metrics.

    This function would call the SonarQube scanner CLI. Here we return
    dummy metrics for demonstration.
    """
    # TODO: Replace with actual SonarQube scanner invocation.
    return {
        "code_smells": 10,
        "bugs": 0,
        "vulnerabilities": 0,
        "coverage": 85.0,  # percent
        "duplicated_lines_density": 1.2,
    }


# Placeholder for capturing AI interaction logs
def capture_ai_interactions(prompt: str, response: str) -> dict:
    """Capture AI prompt/response pairs with timestamps.

    In the real experiment, the IDE plugin would log each call to the
    language model. This function simulates such a record.
    """
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": response,
    }


def write_json_log(data: dict, output_dir: str, filename: str) -> None:
    """Write a JSON dictionary to the specified output directory."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[info] Wrote log to {path}")


def main(repo_path: str, output_dir: str) -> None:
    """Main entry point for data collection."""
    print(f"[info] Starting data collection for repository: {repo_path}")
    # 1. Capture commit metadata
    # In practice, you could parse `git log` output or use GitPython.
    commit_metadata = {
        "commit_hash": "abc123",
        "author": "developer@example.com",
        "timestamp": datetime.utcnow().isoformat(),
        "message": "Implement feature X",
        "files_changed": ["src/module.py"],
    }
    write_json_log(commit_metadata, output_dir, "commit_metadata.json")

    # 2. Run static analysis (SonarQube) and record metrics
    # Note: Replace project_key and token with real values when running.
    sonar_metrics = run_sonarqube_analysis(repo_path, project_key="PROJECT_KEY", token="TOKEN")
    write_json_log(sonar_metrics, output_dir, "sonar_metrics.json")

    # 3. Log AI interactions (example)
    ai_log = capture_ai_interactions(
        prompt="How to implement a binary search?",
        response="Here is a Python implementation of binary search..."
    )
    write_json_log(ai_log, output_dir, "ai_interactions.json")

    # Additional instrumentation (e.g., unit‑test coverage via pytest-cov)
    coverage = {
        "total_lines": 1000,
        "covered_lines": 850,
        "coverage_percent": 85.0,
    }
    write_json_log(coverage, output_dir, "coverage.json")

    print("[info] Data collection completed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collect experiment data for multi-agent GenAI study.")
    parser.add_argument("--repo-path", type=str, default=".", help="Path to the cloned repository")
    parser.add_argument("--output-dir", type=str, default="./logs", help="Directory to store logs")
    args = parser.parse_args()

    main(args.repo_path, args.output_dir)