import cv2

gray_image=cv2.imread('image/fruits.jpg', cv2.IMREAD_GRAYSCALE)


if gray_image is None:
    print("erro")
else:
    
    cv2.imshow('Gray Image', gray_image)
    
  
    cv2.waitKey(0)
   
    cv2.destroyAllWindows()



dst_fruits = gray_image.copy() 

cv2.namedWindow('dst') 

cv2.imshow('dst', dst_fruits)



for i in range(240,250): 

    for j in range(500, 510):
        dst_fruits[i][j] = 0


if dst_fruits is None:
    print("erro")
else:
    
    cv2.imshow('imge/dst_fruits', dst_fruits)
    
  
    cv2.waitKey(0)
   
    cv2.destroyAllWindows()



file_dst = 'image/dst_fruits.png'

cv2.imwrite(file_dst,dst_fruits)

