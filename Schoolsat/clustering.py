import matplotlib.pyplot as plt
import numpy as np
import cv2

def clustering(image_input, k, attempts):
    original_image = cv2.imread(image_input)
    img = cv2.cvtColor(original_image,cv2.COLOR_BGR2RGB)
    vectorized = img.reshape((-1,3))
    vectorized = np.float32(vectorized)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
    ret,label,center = cv2.kmeans(vectorized,k,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    return res

def calaurate_area(image_input):
    each_area = []
    res = clustering(image_input, 3, 10)
    unique, counts = np.unique(res, return_counts=True)
    for i in counts:
        if i not in each_area:
            each_area.append(i)
    dict(zip(unique, counts))
    total_area = sum(each_area)
    percen_each_area = [ i*100/total_area for i in each_area]
    return percen_each_area

def plot_cluster(image_input,figure_size,total_realarea):
    res = clustering(image_input, 3, 10)
    original_image = cv2.imread(image_input)
    img = cv2.cvtColor(original_image,cv2.COLOR_BGR2RGB)
    result_image = res.reshape((img.shape))
    explode = (0,0.1, 0)
    sizes = calaurate_area(image_input)
    labels = f'occean {sizes[0]*total_realarea//100}', f'forest {sizes[1]*total_realarea//100}', f'area {sizes[2]*total_realarea//100}'
    
    plt.figure(figsize=(figure_size,figure_size))
    
    plt.subplot(1,3,1),plt.imshow(img)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,3,2),plt.imshow(result_image)
    plt.title('Segmented Image'), plt.xticks([]), plt.yticks([])
    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',colors= ['lightblue', 'olive', 'gray'],
       shadow={'ox': -0.04, 'edgecolor': 'none', 'shade': 0.9}, startangle=90)
    plt.show()

plot_cluster('shot1.png', 15,20000)