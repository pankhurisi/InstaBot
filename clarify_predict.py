from clarifai import rest
from clarifai.rest import ClarifaiApp


def get_tags_from_image(image_url):
    app = ClarifaiApp(api_key='c90eb18d55344320921e26362b92742d')
    # get the general model
    model = app.models.get("general-v1.3")
    # predict with the model
    r = model.predict_by_url(url='image_url')
    return r
