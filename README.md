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
watermark_width_factor = 0.8  # Adjust the watermark width (0.8 means 80%)
watermark_height_factor = 0.8  # Adjust the watermark height (0.8 means 80%)
```

Watermark Opacity
```py
watermark_opacity = 0.7  # Adjust the watermark opacity (0.7 means 70%)
```
Watermark Position
```py
watermark_position = "TOP_LEFT"
# Available position values:
# TOP_RIGHT
# TOP_LEFT
# BOTTOM_RIGHT
# BOTTOM_LEFT
# CENTER
```

---

<h3 align="left">Support Me:</h3>
<p><a href="https://paypal.me/officialrazer"> <img src="https://github.com/andreostrovsky/donate-with-paypal/blob/master/dark.svg" height="50" width="210" alt="sandarudev" /></a>
</p><br><br>

---
