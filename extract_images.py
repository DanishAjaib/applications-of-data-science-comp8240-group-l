from google_images_search import GoogleImagesSearch

api_key = 'AIzaSyCVBWvyO7ZsDowvVP_Z4NwObN8Yw21xM9A'
gse_key = 'c5be5a71be2f14070'
gis = GoogleImagesSearch(api_key, gse_key)
paths = ['contrast_enhancement/images/', 'lowlight_enhancement/images', 'real_denoising/images', 'super_resolution/images']
queries = ['low contrast', 'low light street', 'noisy images', 'low resolution']
for query, path in zip(queries, paths):
    _search_params = {
        'q': query,
        'num': 10,
    }
    results = gis.search(search_params=_search_params)
    for image in gis.results():
        image.download(path)