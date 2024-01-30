# SugarBoxAssignment

## Overview

This project provides a simple command-line utility (`aggregate_events.py`) to aggregate user events from a JSON file and generate daily summary reports.

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd SugarBoxAssignment
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Make the script executable:**
    ```bash
    chmod +x aggregate_events.py
    ```

## Usage

### Step 1: Create `input.json`

Create an `input.json` file and enter your JSON data inside the file.

### Step 2: Run the script

Run the `aggregate_events.py` script to generate aggregated daily reports.
```bash
./aggregate_events.py -i input.json -o output.json
```

If you want to update the existing summary report with new events without reprocessing all previous events, use the `--update` flag

### Step 3: Check for the output
Check the generated `output.json` file, which will contain the aggregated daily report of user events.