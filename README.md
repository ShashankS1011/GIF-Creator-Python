# 🎨 GIF Creator Using Python  

![Demo GIF](cat.gif)  

## 📜 About  
🚀 A simple Python script to create animated GIFs from images using **PIL (Pillow)** and **ImageIO**. Perfect for quick animations, memes, or fun projects! 🎉  

## 🛠️ Features  
✅ Convert multiple images into a GIF  
✅ Resize images to a uniform size  
✅ Set custom duration & loop settings  
✅ Works with PNG, JPG, and other formats  

## 📦 Installation  
Make sure you have Python installed, then install dependencies:  

```bash
pip install pillow imageio
```

## 🚀 Usage  
Place your images (e.g., `image1.png`, `image2.png`, `image3.png`) in the same directory and run:  

```python
import imageio.v3 as iio
from PIL import Image

filenames = ['image1.png', 'image2.png', 'image3.png']
images = []

first_image = Image.open(filenames[0])
target_size = first_image.size  

for filename in filenames:
    img = Image.open(filename).convert("RGBA") 
    img = img.resize(target_size)  
    images.append(img)  

# Save as GIF using PIL
images[0].save("output.gif", save_all=True, append_images=images[1:], duration=500, loop=0)
```

## 📝 License  
This project is open-source under the **MIT License**. Feel free to use and modify it!  

---
