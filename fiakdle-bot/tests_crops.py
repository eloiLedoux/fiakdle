from construire_info import construire_fiak
from cropper import crop_image
from construire_info import nb_images_bdd

nb_images_bdd = nb_images_bdd()

if __name__ == "__main__":

    for id in range(1,nb_images_bdd+1):
        img_save_url = "tests_images/f"+str(id)+"_z"
        print(img_save_url)
        fiaks_totest = construire_fiak(id)
        fiaks_totest.augmenterAide()

        img_save_url_0 = img_save_url+str(fiaks_totest.getAide())+".jpg"
        print(img_save_url_0)
        crop_image(fiaks_totest.getImgUrl(), img_save_url_0, fiaks_totest.getZoom())
        fiaks_totest.augmenterAide()
        
        img_save_url_1 = img_save_url+str(fiaks_totest.getAide())+".jpg"
        print(img_save_url_1)
        crop_image(fiaks_totest.getImgUrl(), img_save_url_1, fiaks_totest.getZoom())
        fiaks_totest.augmenterAide()
        
        img_save_url_2 = img_save_url+str(fiaks_totest.getAide())+".jpg"
        print(img_save_url_2)
        crop_image(fiaks_totest.getImgUrl(), img_save_url_2, fiaks_totest.getZoom())
        fiaks_totest.augmenterAide()

        img_save_url_3 = img_save_url+str(fiaks_totest.getAide())+".jpg"
        print(img_save_url_3)
        crop_image(fiaks_totest.getImgUrl(), img_save_url_3, fiaks_totest.getZoom())
        fiaks_totest.augmenterAide()