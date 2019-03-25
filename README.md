# Raccoon Search NASA Image

<h3 align="center">Live Demo: https://raccoon-search-nasa-img.herokuapp.com/</h3>

<p align="center">
  <a href="https://raccoon-search-nasa-img.herokuapp.com/" target="\_blank">
    <img src="https://github.com/ga12ece/raccoon-search-nasa-img/blob/master/static/image/Front-page.png" width="700px">
  </a>
</p>


## Features:
Raccoon knows how to search NASA Image Database so he creates an search that:
- A search function that displays results in an intuitive, easy to navigate interface.
<img src="https://github.com/ga12ece/raccoon-search-nasa-img/blob/master/static/image/result.png" width="700px">

When users select an image, Raccoon makes the light turn off, allowing users to see the image better.

<img src="https://github.com/ga12ece/raccoon-search-nasa-img/blob/master/static/image/turn%20off%20the%20light.png" width="700px">

- Image metadata for the individual search results, displayed intuitively.

Raccoon gives users about the image's description, time created as well as hyperlink keywords so that users can explore more about NASA Image Database

<img src="https://github.com/ga12ece/raccoon-search-nasa-img/blob/master/static/image/metadata.png" width="500px">

- Give users the ability to refine search results by a date range, location, NASA center, Media type (image and audio).

Users can refine search criteria by clicking on More Details button from Front Page:

<img src="https://github.com/ga12ece/raccoon-search-nasa-img/blob/master/static/image/refine%20search.png" width="700px">

From this image, users can refine search based on its description, NASA data center related to it, Location, Date range of the NASA project as well as media type

<img src="https://github.com/ga12ece/raccoon-search-nasa-img/blob/master/static/image/error_noitem.png" width="700px">
         
Unless users don't enter anything to search, Raccoon feels sad :'(

## Requirements

* Flask 1.0.2
* gunicorn 19.9.0
* requests 2.21.0
* Flask-Bootstrap 3.3.7.1
* WTForms 2.2.1
