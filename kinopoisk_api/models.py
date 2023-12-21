
import requests
from .models.season import SeasonModel

# Example usage:
data = requests.get("https://api.kinopoisk.dev/v1.4/movie/awards?page=1&limit=10", headers={"X-API-KEY": "KX96F4Y-TA5M2DK-GG0D2GW-VHXD7G7"})
movie_instance = SeasonModel(**data.json())
print(movie_instance.docs)
