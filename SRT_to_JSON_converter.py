import csv
import re

# Function to parse an SRT file
def parse_srt(srt_file_path):
    with open(srt_file_path, 'r', encoding='utf-8-sig') as file:
        content = file.read()
        # Split content at blank lines
        subtitles = re.split(r'\n\s*\n', content.strip(), flags=re.UNICODE)
        parsed_subtitles = []
        for subtitle in subtitles:
            parts = subtitle.split('\n')
            if len(parts) >= 3:
                seq_num = parts[0].strip()
                timecode = parts[1].strip()
                text = ' '.join(parts[2:]).replace('\n', ' ')
                parsed_subtitles.append((seq_num, timecode, text))
        return parsed_subtitles

# Function to write subtitles to a CSV file
def write_to_csv(subtitles, csv_file_path):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Sequence Number', 'Timecode', 'Subtitle Text'])
        for subtitle in subtitles:
            writer.writerow(subtitle)

# Path to your SRT file
srt_file_path = './One of the Greatest Speeches Ever   Steve Jobs.en.srt'

# Path where you want to save the CSV file
csv_file_path = './example.csv'

# Parse the SRT file
subtitles = parse_srt(srt_file_path)

# Write to CSV
write_to_csv(subtitles, csv_file_path)

print(f"Conversion complete. The CSV file is saved at {csv_file_path}")
