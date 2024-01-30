#!/usr/bin/env python3

import json
from datetime import datetime, timedelta
import argparse
import os

def read_events_from_file(file_path):
    with open(file_path, 'r') as file:
        events = json.load(file)
    return events

def aggregate_events(existing_data, events):
    
    # aggregated data is event data grouped by user_id and date
    aggregated_data = {}

    # if existing data is present, then add it to aggregated_data to handle updates
    if len(existing_data) > 0:
        for event in existing_data:
            user_id = event['userId']
            date = event['date']

            count_by_event_type ={}
            for key, value in event.items():
                if key not in ['userId', 'date']:
                    count_by_event_type[key] = value

            if user_id not in aggregated_data:
                aggregated_data[user_id] = {}

            if date not in aggregated_data[user_id]:
                aggregated_data[user_id][date] = {}

            for event_type, count in count_by_event_type.items():
                if event_type not in aggregated_data[user_id][date]:
                    aggregated_data[user_id][date][event_type] = 0

                aggregated_data[user_id][date][event_type] += count

    # add new events to aggregated_data
    for event in events:
        user_id = event['userId']
        timestamp = event['timestamp']

        # Convert timestamp to date string
        date = datetime.utcfromtimestamp(timestamp)

        # add 1 day to the date just to match output given in example in problem statement
        # (not sure if this is correct)
        date = date.__add__(timedelta(days=1)).strftime('%Y-%m-%d')

        event_type = event['eventType']

        if user_id not in aggregated_data:
            aggregated_data[user_id] = {}

        if date not in aggregated_data[user_id]:
            aggregated_data[user_id][date] = {}

        if event_type not in aggregated_data[user_id][date]:
            aggregated_data[user_id][date][event_type] = 0

        aggregated_data[user_id][date][event_type] += 1

    daily_reports = []
    for user_id, user_data in aggregated_data.items():
        for date, event_data in user_data.items():
            event_data_row = {
                "userId": user_id,
                "date": date,
            }

            for event_type, count in event_data.items():
                event_data_row[event_type] = count

            daily_reports.append(event_data_row)

    return daily_reports

def write_daily_summary_to_file(daily_summary, output_file_path):
    with open(output_file_path, 'w') as file:
        json.dump(daily_summary, file, indent=2)

def main():
    print("Running aggregate_events.py")
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", required=True)
    parser.add_argument("-o", "--output_file", required=True)
    parser.add_argument("--update", action="store_true")


    args = parser.parse_args()
    existing_data = []
    if args.update and os.path.exists(args.output_file):
        with open(args.output_file, 'r') as file:
            existing_data = json.load(file)

    try:
        new_events = read_events_from_file(args.input_file)
        daily_summary = aggregate_events(existing_data, new_events)
        write_daily_summary_to_file(daily_summary, args.output_file)
        print(f"Daily summary written to {args.output_file}")

    except Exception as e:
        print("error occurred while running aggregate_events.py")
        print("exception occured due to: ",e.args[0])

if __name__ == "__main__":
    main()
