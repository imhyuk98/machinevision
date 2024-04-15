import numpy as np, cv2, time
def scaling(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    y = np.arange(0, img.shape[0], 1)
    x = np.arange(0, img.shape[1], 1)
    y, x = np.meshgrid(y, x)
    i, j = np.int32(y * ratioY), np.int32(x * ratioX)
    dst[i, j] = img[y, x]
    return dst

def scaling2(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            i, j = int(y * ratioY), int(x * ratioX)
            dst[i, j] = img[y, x]
    return dst

def time_check(func, image, size, title):
    start_time = time.perf_counter()
    ret_img = func(image, size)
    clapsed = (time.perf_counter() - start_time) * 1000
    print(title, "t숳ㅇ시간 = %0.2f ms" % clapsed)
    return ret_img

image = cv2.imread('../image/scaling.jpg', cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상 파일을 읽기 에러")

dst1 = scaling(image, (150, 200))
dst2 = scaling2(image, (150, 200))
dst3 = time_check(scaling, image, (300, 40), "[방법1] 좌표행렬 방식")
dst4 = time_check(scaling2, image, (300, 40), "[방법2] 좌표행렬 방식")

cv2.imshow("image", image)
cv2.imshow("dst1- zoom out", dst1)
cv2.imshow("dst3- zoom out", dst3)
cv2.resizeWindow("dst1- zoom out", 260, 200)
cv2.waitKey(0)