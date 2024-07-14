import requests
from bs4 import BeautifulSoup

def fetch_text_to_image_datasets(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())
    dataset_links = soup.find_all('h4', href=True, attrs={})
    dataset_names = [link.text.strip() for link in dataset_links if link.text.strip() != '']
    return dataset_names

if __name__ == "__main__":
    url = "https://huggingface.co/datasets?task_categories=task_categories:text-to-image&sort=trending"
    datasets = fetch_text_to_image_datasets(url)
    print("Text-to-Image Datasets found:")
    for dataset in datasets:
        print(dataset)
