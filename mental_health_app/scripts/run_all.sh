# run_all.py
import subprocess

steps = [
    "pipeline/collect.py",
    "pipeline/preprocess.py",
    "pipeline/train_model.py",
    "pipeline/analyze.py"
]

print("🚀 Starting full mental health analytics pipeline...\n")

for step in steps:
    print(f"▶️ Running {step}...")
    result = subprocess.run(["python", step])
    if result.returncode != 0:
        print(f"❌ Error running {step}. Stopping pipeline.")
        break
    print(f"✅ Completed {step}\n")

print("🏁 Pipeline finished.")
