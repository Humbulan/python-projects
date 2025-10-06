import os

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Python Projects Portfolio</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; background: #f5f5f5; }
        .header { background: #2c3e50; color: white; padding: 2rem; text-align: center; }
        .projects { max-width: 800px; margin: 2rem auto; padding: 0 1rem; }
        .project-card { background: white; padding: 1.5rem; margin: 1rem 0; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
    </style>
</head>
<body>
    <div class="header">
        <h1>🐍 Python Developer Portfolio</h1>
        <p>Data Analysis | Web Scraping | Automation</p>
    </div>
    
    <div class="projects">
        <div class="project-card">
            <h2>📈 Data Analysis Suite</h2>
            <p>Advanced data processing and visualization tools</p>
        </div>
        
        <div class="project-card">
            <h2>🌐 Web Scraping Toolkit</h2>
            <p>Extract and analyze web data efficiently</p>
        </div>
        
        <div class="project-card">
            <h2>🔬 Scientific Analysis</h2>
            <p>Chemical elements and periodic table research</p>
        </div>
    </div>
</body>
</html>
"""

with open('index.html', 'w') as f:
    f.write(html_content)

print("Website generated successfully!")
