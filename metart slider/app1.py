from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# List of default image URLs and texts
# These will be replaced with the results from the API call
# after the user enters a search term.
image_urls = [
    "https://www.singulart.com/blog/wp-content/uploads/2023/09/Mona-Lisa-by-Leonardo-da-Vinci-1031x1536.jpg",
    "https://www.singulart.com/blog/wp-content/uploads/2023/10/Girl-with-a-Pearl.jpg",
    "https://www.singulart.com/blog/wp-content/uploads/2023/10/American-Gothic-1140x1376.jpg",
    "https://www.singulart.com/blog/wp-content/uploads/2023/10/Portrait-of-Dr.-Gachet.jpg"
]
text_list = [
    "Mona Lisa by Leonardo da Vinci",
    "Girl with a Pearl Earring by Johannes Vermeer",
    "American Gothic by Grant Wood",
    "Portrait of Dr. Gachet by Vincent van Gogh"
]


def fetch_images_and_text(search_term):
    image_urls = []
    text_list = []

    search_url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
    search_params = {
        "q": search_term,
        "hasImages": "true"
    }

    search_response = requests.get(search_url, params=search_params)
    object_ids = search_response.json().get("objectIDs", [])[:10]  # Limit to 10 results

    object_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"
    for obj_id in object_ids:
        obj_response = requests.get(f"{object_url}{obj_id}")
        if obj_response.status_code == 200:
            obj_data = obj_response.json()
            image = obj_data.get("primaryImage")
            title = obj_data.get("title")
            artist = obj_data.get("artistDisplayName")

            if image:  # Only add if image exists
                image_urls.append(image)
                text_list.append(f"{title} by {artist}" if artist else title)

    return image_urls, text_list




# Search for object IDs with a query term
search_url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
search_params = {
    "q": "Battle of Borodino", # replace with search term from user!
    "hasImages": "true"
}


search_response = requests.get(search_url, params=search_params)
object_ids = search_response.json().get("objectIDs", [])[:20]  # Limit to first 20 results


# Fetch object details and filter by date
object_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"
for obj_id in object_ids:
    obj_response = requests.get(f"{object_url}{obj_id}")
    if obj_response.status_code == 200:
        obj_data = obj_response.json()
        year = obj_data.get("objectBeginDate", "")
        try:
            title = obj_data.get("title")
            image = obj_data.get("primaryImage")
            print(f"Title: {title}\nYear: {year}\nImage URL: {image}\n")
        except KeyError as e:
            continue  # Skip if some data is missing

    return image_urls, text_list


@app.route('/', methods=['GET'])
def index():
    # get access to global image_urls and text_list
    # (this is a bit of hack but works for this simple app)
    global image_urls, text_list

    search_term = request.args.get('search')
    if search_term:
        print(f"Search term entered: {search_term}")
        image_urls, text_list = fetch_images_and_text(search_term)
    else: https://collectionapi.metmuseum.org/public/collection/v1/artistAlphaSort

    # zip IMAGE_URLS and TEXT_LIST to create pairs for display
    slides = zip(image_urls, text_list)

    return render_template('index.html', slides=slides)


if __name__ == '__main__':
    app.run(debug=True)
