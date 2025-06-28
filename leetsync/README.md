# LeetSync

LeetSync is a Python tool to automatically sync your LeetCode (DSA) solutions to your GitHub repository.

## Features
- Watches your local DSA folder for new or updated files
- Automatically commits and pushes changes to your GitHub repository

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the tool:
   ```bash
   python leetsync.py
   ```

## Configuration
- By default, the tool will be configured to watch a specified folder for your LeetCode solutions.
- You can customize the folder and GitHub repository in future versions. 