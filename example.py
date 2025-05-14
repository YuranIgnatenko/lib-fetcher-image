from lib_fetcher_image.fetcher import FetcherImage

# create fetcher-object
fetcher_image = FetcherImage()

# get array
fetcher_image.get_images_urls("Цветы", 2)

# get iterator
i = 0
for url in fetcher_image.search_iterator("белые роз", 2):
	print(f"{i}-{url}")
	fetcher_image.download(url, f"image_search_{i}.jpg")
	i+=1

# get iterator 
i = 0
for url in fetcher_image.popular_iterator(2):
	print(f"{i}-{url}")
	fetcher_image.download(url, f"image_popular_{i}.jpg")
	i+=1