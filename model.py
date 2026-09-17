import math

def rgb_to_xyz(r, g, b):
    r = r / 255.0
    g = g / 255.0
    b = b / 255.0
    
    r = ((r + 0.055) / 1.055) ** 2.4 if r > 0.04045 else r / 12.92
    g = ((g + 0.055) / 1.055) ** 2.4 if g > 0.04045 else g / 12.92
    b = ((b + 0.055) / 1.055) ** 2.4 if b > 0.04045 else b / 12.92
    
    x = r * 0.412453 + g * 0.357580 + b * 0.180423
    y = r * 0.212671 + g * 0.715160 + b * 0.072169
    z = r * 0.019334 + g * 0.119193 + b * 0.950227
    
    return (x * 100, y * 100, z * 100)

def xyz_to_rgb(x, y, z):

    x = x / 100.0
    y = y / 100.0
    z = z / 100.0

    r = x * 3.2406 - y * 1.5372 - z * 0.4986
    g = -x * 0.9689 + y * 1.8758 + z * 0.0415
    b = x * 0.0557 - y * 0.2040 + z * 1.0570

    r = 1.055 * (r ** (1/2.4)) - 0.055 if r > 0.0031308 else 12.92 * r
    g = 1.055 * (g ** (1/2.4)) - 0.055 if g > 0.0031308 else 12.92 * g
    b = 1.055 * (b ** (1/2.4)) - 0.055 if b > 0.0031308 else 12.92 * b
    
    r = max(0, min(255, round(r * 255)))
    g = max(0, min(255, round(g * 255)))
    b = max(0, min(255, round(b * 255)))
    
    return (r, g, b)

def rgb_to_hsv(r, g, b):

    r = r / 255.0
    g = g / 255.0
    b = b / 255.0
    
    c_max = max(r, g, b)
    c_min = min(r, g, b)
    delta = c_max - c_min
    
    if delta == 0:
        h = 0
    elif c_max == r:
        h = 60 * (((g - b) / delta) % 6)
    elif c_max == g:
        h = 60 * (((b - r) / delta) + 2)
    else:
        h = 60 * (((r - g) / delta) + 4)
    
    s = 0 if c_max == 0 else delta / c_max
    
    v = c_max
    
    return (h, s * 100, v * 100)

def hsv_to_rgb(h, s, v):

    s = s / 100.0
    v = v / 100.0
    
    c = v * s
    x = c * (1 - abs((h / 60.0) % 2 - 1))
    m = v - c
    
    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
    
    r = round((r + m) * 255)
    g = round((g + m) * 255)
    b = round((b + m) * 255)
    
    return (r, g, b)

def xyz_to_hsv(x, y, z):

    r, g, b = xyz_to_rgb(x, y, z)
    return rgb_to_hsv(r, g, b)

def hsv_to_xyz(h, s, v):

    r, g, b = hsv_to_rgb(h, s, v)
    return rgb_to_xyz(r, g, b)