# run_pipeline.py
import subprocess
import argparse

def run_step(script):
    print(f"▶️ Running {script}...")
    result = subprocess.run(["python", script])
    if result.returncode != 0:
        print(f"❌ Error running {script}")
    else:
        print(f"✅ Completed {script}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run specific steps of the mental health analytics pipeline.")
    parser.add_argument(
        "--steps",
        nargs="+",
        choices=["collect", "preprocess", "train", "analyze"],
        help="Steps to run (e.g. --steps collect preprocess train)"
    )
    args = parser.parse_args()

    if not args.steps:
        print("⚠️ No steps specified. Use --steps to select stages.")
        print("Example: python run_pipeline.py --steps collect preprocess train analyze")
    else:
        for step in args.steps:
            run_step(f"pipeline/{step}.py")

    print("🏁 Selected pipeline steps finished.")
