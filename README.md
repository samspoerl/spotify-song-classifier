# Spotify Song Classifier
KMeans cluster model to group songs into genres. Evaluated against the most common Spotify playlists in each genre selected (Classical, Pop, and Rock).

Because the code calls the API directly each time, there is no input data file. Additionally, by using a single interactive python notebook and a utility script, no other files are needed to run the code.

## Getting Started

In order to call Spotify's Web API, you will need a Spotify account. You can login or sign up for a free account here. Once in your Developer Dashboard, create an app and copy and paste your Client ID and Client Secret into the first module under "Data Collection" in spotify.ipynb.

## Libraries

* spotipy
* pandas
* numpy
* matplotlib
* mpl_toolkits
* sklearn

## Notebook Structure

1. Module imports
2. Data collection
3. Feature selection
4. Cluster model
5. Conclusion
