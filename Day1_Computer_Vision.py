import cv2

path = input("Enter Image Path: ")
output = input("Enter Output Filename: ")
image = cv2.imread(path)

if image is None:
    print("Image Not Found")

else:
    cv2.imshow("Image Preview", image)
    cv2.imwrite(output, image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()