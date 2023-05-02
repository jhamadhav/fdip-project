def gammaTransformation(img,gamma_val=2.2):
#     # Apply Gamma=2.2 on the normalised image and then multiply by scaling constant (For 8 bit, c=255)
#     gamma_two_point_two = np.array(255*(img/255)**gamma_val,dtype='uint8')
#     result gamma_two_point_two