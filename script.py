import csv
from huggingface_hub import HfApi

def list_all_datasets():
    api = HfApi()
    print("Fetching list of all datasets from Hugging Face Hub...")
    all_datasets = list(api.list_datasets())  # Convert generator to list
    print(f"Total datasets fetched: {len(all_datasets)}")
    return [dataset.id for dataset in all_datasets]

def filter_datasets(datasets, keywords):
    print("Filtering datasets for specified keywords...")
    filtered = [dataset for dataset in datasets if any(keyword in dataset for keyword in keywords)]
    print(f"Total datasets after filtering: {len(filtered)}")
    return filtered

def save_datasets_to_csv(dataset_names, filename="text_to_image_datasets.csv"):
    print(f"Saving datasets to {filename}...")
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for dataset in dataset_names:
            writer.writerow([dataset])  # Each dataset name is written to a new row
    print("Datasets successfully saved to CSV.")

if __name__ == "__main__":
    keywords = ['text-to-image', 'image-captioning', 'vision-language']  # Modify as needed
    datasets = list_all_datasets()
    filtered_datasets = filter_datasets(datasets, keywords)
    save_datasets_to_csv(filtered_datasets)
    print("Operation completed successfully.")
