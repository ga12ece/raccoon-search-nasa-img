from wtforms import Form, TextField

class ImageSearch(Form):
    q = TextField()
    center = TextField()
    keywords = TextField()
    location = TextField()
    year_start = TextField()
    year_end = TextField()
    media_type = TextField()
    description = TextField()
