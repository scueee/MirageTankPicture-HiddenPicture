import cv2
import numpy as np

def make(file1, file2, savePath):
    up_pic = cv2.imread(file1)
    down_pic = cv2.imread(file2)
    pic_shape = up_pic.shape
    down_pic = cv2.resize(down_pic, (pic_shape[1],pic_shape[0]))

    # 转化为灰度图
    up_pic = cv2.cvtColor(up_pic, cv2.COLOR_BGR2GRAY)
    down_pic = cv2.cvtColor(down_pic, cv2.COLOR_BGR2GRAY)
    
    # 添加透明通道
    up_pic = cv2.cvtColor(up_pic, cv2.COLOR_GRAY2BGRA)
    down_pic = cv2.cvtColor(down_pic, cv2.COLOR_GRAY2BGRA)

    # 反相(1-imgA)
    cv2.bitwise_not(up_pic,up_pic);

    # 1-imgA+imgB
    out_pic = cv2.add(up_pic,down_pic)

    red_channel = out_pic[:,:,2]
    # imgB / (1-imgA+imgB)
    out_pic = out_pic.astype(np.float)
    out_pic[out_pic == 0] = 1e-10
    out_pic = np.uint8(np.clip((down_pic / out_pic)*255, 0, 255))
    out_pic[:,:,3] = red_channel

    cv2.imwrite(savePath, out_pic)

if __name__ == '__main__':
	savePath = r"output.png"
	f1 = input("表层图像：")
	f2 = input("里层图像：")
	if f1 and f2:
		try:
			make(f1, f2, savePath)
		except err:
			print("生成失败 :(",err)
		else:
			print("生成成功 :)")
		
