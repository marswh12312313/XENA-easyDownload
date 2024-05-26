import os
import json
import subprocess

# Load the JSON file
json_file_path = 'filtered_output_dict.json'  # replace with your path to the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Get the current script directory
script_directory = os.path.dirname(os.path.abspath(__file__))

total_files = 0
downloaded_files = 0
total_size = 0

# Count total files to download
for cohort_url, cohort_details in data.items():
    for dataset in cohort_details.get('Datasets', []):
        total_files += len(dataset.get('URLs', []))

print(f"Total files to download: {total_files}")


# Helper function to download file with progress checking
def download_with_progress_check(url, download_dir, timeout=300, check_interval=10):


    local_filename = os.path.join(download_dir, os.path.basename(url))

    result = subprocess.Popen(['aria2c', url, '-d', download_dir, '-o', os.path.basename(url)],
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

    for line in result.stdout:
        print(line, end='')

    result.wait()

    if result.returncode == 0:
        return local_filename, os.path.getsize(local_filename)
    else:
        print(f"Failed to download {url}.")
        return None, 0


# Iterate through the data and download files
for cohort_url, cohort_details in data.items():
    cohort_title = cohort_details["Cohort Title"].replace("cohort: ", "").replace(" ", "_").replace("(", "").replace(
        ")", "")
    cohort_dir = os.path.join(script_directory, cohort_title)

    os.makedirs(cohort_dir, exist_ok=True)

    for dataset in cohort_details.get('Datasets', []):
        dataset_title = dataset["Dataset Title"].replace("dataset: ", "").replace(" ", "_").replace("(", "").replace(
            ")", "")
        dataset_dir = os.path.join(cohort_dir, dataset_title)

        os.makedirs(dataset_dir, exist_ok=True)

        for url in dataset.get('URLs', []):
            try:
                local_filename = os.path.join(dataset_dir, os.path.basename(url))

                # Check if the file already exists and is not empty
                if os.path.exists(local_filename) and os.path.getsize(local_filename) > 0:
                    print(f"File already exists and is not empty: {local_filename}")
                    downloaded_files += 1
                    file_size = os.path.getsize(local_filename)
                    total_size += file_size
                    continue

                print(f"Downloading {url} to {local_filename}")

                # Use the helper function to download the file with progress check
                local_filename, file_size = download_with_progress_check(url, dataset_dir)
                if file_size > 0:
                    downloaded_files += 1
                    total_size += file_size
                    print(
                        f"Downloaded: {downloaded_files}/{total_files} - {url} (Size: {file_size / (1024 * 1024 * 1024):.2f} GB)")
                    print(f"Current total size of downloaded files: {total_size / (1024 * 1024 * 1024):.2f} GB")

            except Exception as e:
                print(f"Failed to download {url}. Error: {e}")

print("Download completed.")
print(f"Total files downloaded: {downloaded_files}")
print(f"Total size of downloaded files: {total_size / (1024 * 1024 * 1024):.2f} GB")
