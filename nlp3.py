#creating a word cloud
from pathlib import Path
from wordcloud import WordCloud #can't install wordcloud on 3.9 ????
import imageio
import matplotlib.pyplot as plt
#need to install wordcloud package

text = Path("RomeoAndJuliet.txt").read_text()

mask_image = imageio.imread("mask_heart.png") #mask image = shape of word cloud
wordcloud = WordCloud(colormap = "prism", mask=mask_image, background_color = "white")

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("RomeoJulietHeart.png")

plt.imshow(wordcloud)
plt.show()
print("done")