import matplotlib.pyplot as plt
import wordcloud
file1 = "/home/rishu/Programming/Programmings/zz_images_files/file.txt"
file2 = "/home/rishu/Programming/Programmings/zz_images_files/temp.txt"
punctuations = ['!', '"', '#', "\n" , '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=','>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
uninteresting_words = ["the", "mr", "mrs", "for", "us", "a", "so", "to", "if", "is", "not", "on", "it", "of", "and", "or", "an", "as", "in", "i", "me", "my",
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
                       "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
                        "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
                       "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", "than"]

new_content = ""
with open(file1, "r+") as fin, open(file2,"w+") as fout:  

    for line in fin:
        for chr in punctuations:
            line = line.replace(chr, "")
        fout.write(line)

file_contents = open(file2, "r", encoding="utf-8")

new_content = ""
for chr in file_contents:
    new_content += chr
temp_file = new_content.split(" ")
frequencies = {}
for word in temp_file:
    if word.lower() not in uninteresting_words:
        if word.lower() in frequencies:
            frequencies[word.lower()] +=1
        if word.lower() not in frequencies:
            frequencies[word.lower()] = 1

#with open(file3, "w") as file3:
#    file3.write(str(frequencies))

cloud = wordcloud.WordCloud(background_color="white",width=1200,height=720)
cloud.generate_from_frequencies(frequencies)

# Display your wordcloud image
cloud.to_file("/home/rishu/Programming/Programmings/zz_images_files/word.png")
plt.imshow(cloud, interpolation='bilinear')
plt.axis("off")
plt.show()