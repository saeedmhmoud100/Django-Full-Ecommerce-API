from django.utils.text import slugify
from django.utils.timezone import now


def generate_image_filename(instance, filename):
    slug = slugify(instance.name)
    folder = instance.__class__.__name__
    return f"{folder}/{(str(now().time()).replace('.',''))}--{slug}--{filename}"
