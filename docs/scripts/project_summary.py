#!/usr/bin/env python3
import os
import subprocess
import pandas as pd

def run_analysis():
    print("🎯 RUNNING COMPLETE PROJECT ANALYSIS")
    print("=" * 60)
    
    # Test all scripts
    scripts_to_test = [
        ('hello.py', 'Basic Python Test'),
        ('analyze_data.py', 'Data Analysis Demo'),
        ('working_analysis.py', 'Periodic Table Analysis'),
        ('project_dashboard.py', 'Project Dashboard')
    ]
    
    for script, description in scripts_to_test:
        if os.path.exists(script):
            print(f"\n▶️  Running: {description} ({script})")
            print("-" * 40)
            try:
                result = subprocess.run(['python', script], capture_output=True, text=True, timeout=30)
                if result.returncode == 0:
                    print("✅ SUCCESS")
                    # Show first few lines of output
                    lines = result.stdout.strip().split('\n')
                    for line in lines[:5]:
                        if line.strip():
                            print(f"   {line}")
                    if len(lines) > 5:
                        print("   ... (output truncated)")
                else:
                    print("❌ FAILED")
                    if result.stderr:
                        print(f"   Error: {result.stderr[:100]}...")
            except Exception as e:
                print(f"❌ ERROR: {e}")
        else:
            print(f"⚠️  Script not found: {script}")
    
    print(f"\n{'='*60}")
    print("🎉 PROJECT ANALYSIS COMPLETE!")
    print("Next: Consider pushing to GitHub or adding new features!")

if __name__ == "__main__":
    run_analysis()
