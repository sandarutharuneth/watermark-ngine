# WATERMARK NGINE
> Add a watermark to bulk of images automatically and easily. Fully customizable and and easy to understand.

<a href="https://imgur.com/qgpwlbQ"><img src="https://i.imgur.com/qgpwlbQ.png" title="source: imgur.com" /></a>

----

## How to Setup

> You need to have Python installed in your PC to run this program. Haven't installed it yet? Head over to [www.python.org](https://www.python.org/downloads/) to download Python or download it from Microsoft Store.

1. Clone the repository
```sh
git clone https://github.com/sandarutharuneth/watermark-ngine.git
```

2. Install Pillow
```sh
pip install Pillow
```

3. Add your watermark (.png or jpg) to the `static` folder
4. Add your images to `data` folder
5. Run the program
```sh
python app.py
```
### That all! You have successfully ran the program!

---


## Customizations
Increase or Decrease the size of your watermark
```py
new_width = int(watermark.width * 0.8) # 0.8% Increased
new_height = int(watermark.height * 0.8) # 0.8% Increased
```

Watermark Opacity
```py
watermark_with_opacity.putpixel((x, y), (r, g, b, int(a * 0.7)))
# 0.7 = 70% Watermark opacity
```
---

<h3 align="left">Support Me:</h3>
<p><a href="https://paypal.me/officialrazer"> <img src="https://github.com/andreostrovsky/donate-with-paypal/blob/master/dark.svg" height="50" width="210" alt="sandarudev" /></a>
</p><br><br>

---
