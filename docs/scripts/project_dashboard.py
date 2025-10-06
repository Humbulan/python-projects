#!/usr/bin/env python3
import os
import pandas as pd

def show_dashboard():
    print("🚀 PYTHON PROJECTS DASHBOARD")
    print("=" * 50)
    
    # Project info
    scripts_dir = "."
    data_dir = "../data"
    output_dir = "../output"
    
    # Count files
    python_files = [f for f in os.listdir(scripts_dir) if f.endswith('.py')]
    data_files = os.listdir(data_dir) if os.path.exists(data_dir) else []
    output_files = os.listdir(output_dir) if os.path.exists(output_dir) else []
    
    print(f"📊 Project Statistics:")
    print(f"   Python scripts: {len(python_files)}")
    print(f"   Data files: {len(data_files)}")
    print(f"   Output files: {len(output_files)}")
    
    print(f"\n🐍 Available Scripts:")
    for i, script in enumerate(python_files, 1):
        print(f"   {i}. {script}")
    
    print(f"\n📁 Data Files:")
    for file in data_files:
        print(f"   📄 {file}")
    
    print(f"\n🎨 Output Files:")
    for file in output_files:
        print(f"   🖼️  {file}")
    
    # Show periodic table info if available
    if 'periodic_table_found.csv' in data_files:
        try:
            df = pd.read_csv(f'{data_dir}/periodic_table_found.csv')
            print(f"\n🧪 Periodic Table Info:")
            print(f"   Total elements: {len(df)}")
            if 'Element' in df.columns:
                print(f"   First 5: {', '.join(df['Element'].head().astype(str).tolist())}")
        except:
            pass
    
    print(f"\n💡 Quick Commands:")
    print(f"   Run all tests: python run_all_projects.py")
    print(f"   Advanced analysis: python advanced_analysis.py")
    print(f"   Fixed web scraping: python scrape_and_analyze_fixed.py")

if __name__ == "__main__":
    show_dashboard()
