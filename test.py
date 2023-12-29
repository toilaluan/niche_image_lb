import requests
from tqdm import tqdm

prompt_url = "http://127.0.0.1:15000"
rv_reward_url = "http://127.0.0.1:15001"
sdxl_turbo_reward_url = "http://127.0.0.1:15002"

urls = [prompt_url, rv_reward_url, sdxl_turbo_reward_url]
for url in tqdm(urls):
    for _ in tqdm(range(100), total=100):
        try:
            requests.get(url)
        except:
            pass