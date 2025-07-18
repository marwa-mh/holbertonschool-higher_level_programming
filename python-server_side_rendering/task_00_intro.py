#!/usr/bin/python3
import os

def generate_invitations(template, attendess):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendess, list) or not all(isinstance(item, dict) for item in attendess):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if not attendess:
        print("No data provided, no output files generated.")
        return

    # process each attendee
    for index, attendee in enumerate(attendess, start=1):
        filled_template = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            if value is None:
                value = 'N/A'
            filled_template = filled_template.replace(f"{{{key}}}", str(value))

        result_filename = f"output_{index}.txt"
        try:
            with open(result_filename, 'w') as output_file:
                output_file.write(filled_template)
                print(f"Generated: {result_filename}")
        except Exception as e:
            print(f"Failed to write {result_filename}: {e}")
