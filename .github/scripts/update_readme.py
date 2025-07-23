import os
import re
from datetime import datetime

def get_problem_list():
    problems = []

    for name in os.listdir('.'):
        if os.path.isdir(name) and re.match(r'^\d{4}-', name):
            match = re.match(r'^(\d+)-(.+)', name)
            if match:
                problem_id = int(match.group(1))
                title_raw = match.group(2)
                title = title_raw.replace("-", " ").title()
                path = name
                problems.append({
                    "id": problem_id,
                    "title": title,
                    "slug": title_raw,
                    "path": path
                })

    return sorted(problems, key=lambda x: x["id"])

def generate_readme(problems):
    now = datetime.now().strftime("%B %d, %Y")
    total = len(problems)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# 🧠 LeetCode Daily Sync\n\n")
        f.write(f"![Problems Solved](https://img.shields.io/badge/Total_Problems-{total}-success)\n")
        f.write(f"![Last Sync](https://img.shields.io/badge/Last_Update-{now.replace(' ', '_')}-blue)\n")
        f.write("\n---\n\n")
        f.write("## 📈 Problem Table\n\n")
        f.write("| #    | Title                           | Link |\n")
        f.write("|------|----------------------------------|------|\n")

        for prob in problems:
            f.write(f"| {prob['id']:04} | {prob['title']} | [Folder]({prob['path']}) |\n")

        f.write("\n---\n📌 Auto-updated daily using GitHub Actions.\n")

if __name__ == "__main__":
    problems = get_problem_list()
    generate_readme(problems)
