import pandas as pd

from recognition import utils
from recognition import classification

def buildHistogram(path, level):

    # Read in vocabulary & data
    voc = utils.loadDataFromFile("Data/voc.pkl")
    Data = utils.readImages(path)

    # Transform each feature into histogram
    featureHistogram = []
    labels = []

    index = 0
    for oneImage in Data:

        featureHistogram.append(voc.buildHistogramForEachImageAtDifferentLevels(oneImage, level))

    return featureHistogram

output= buildHistogram('/Users/annacrawford/Desktop/Images_Sort/',1)
Out=pd.DataFrame(data=output)
Out.to_csv('/Users/annacrawford/Colin/GA/Week1/DSI_LDN_1_LESSON_NOTES/projects/capstone/Texture_Features_All.csv',index=False)
