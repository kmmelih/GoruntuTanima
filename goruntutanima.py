from python_imagesearch import imagesearch

while True:
    nesne = imagesearch.imagesearch("nesne.PNG")
    if nesne[0] != -1:
        print(f"nesne bulundu (x:{nesne[0]} y:{nesne[1]})")
    else:
        print("nesne bulunamadı")