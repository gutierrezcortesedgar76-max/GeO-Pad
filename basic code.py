import time
from machine import I2C, Pin

# -------------------------------------------------------------------------
# 1. OLED Display Setup (SSD1306 over I2C)
# -------------------------------------------------------------------------
# Ensure ssd1306.py library is saved to your Raspberry Pi Pico / RP2040 board.
try:
    import ssd1306

    i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=400000)
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)

    oled.fill(0)
    oled.text("Keyboard Ready", 0, 0)
    oled.show()
    has_oled = True
except Exception as e:
    print(f"OLED Initialisation error: {e}")
    has_oled = False

# -------------------------------------------------------------------------
# 2. Key Matrix Pin Setup
# -------------------------------------------------------------------------
# Row output pins (Drive LOW sequentially)
rows = [
    Pin(4, Pin.OUT, value=1),
    Pin(6, Pin.OUT, value=1),
    Pin(7, Pin.OUT, value=1),
]

# Column input pins (Pull HIGH, active LOW)
cols = [
    Pin(0, Pin.IN, Pin.PULL_UP),
    Pin(1, Pin.IN, Pin.PULL_UP),
    Pin(2, Pin.IN, Pin.PULL_UP),
]

# Mapping matrix positions to key labels
key_map = {(0, 0): "Key 1", (1, 1): "Key 2", (2, 2): "Key 3"}

# State tracking for debouncing
prev_state = {k: False for k in key_map}

# -------------------------------------------------------------------------
# 3. Main Scanning Loop
# -------------------------------------------------------------------------
print("Scanning matrix...")

while True:
    for r_idx, row in enumerate(rows):
        row.value(0)  # Activate current row (Drive LOW)

        for c_idx, col in enumerate(cols):
            key = (r_idx, c_idx)
            if key in key_map:
                # Active LOW when pressed
                is_pressed = col.value() == 0

                # Detect state change
                if is_pressed and not prev_state[key]:
                    key_name = key_map[key]
                    print(f"Pressed: {key_name}")

                    if has_oled:
                        oled.fill(0)
                        oled.text("Key Pressed:", 0, 10)
                        oled.text(f"> {key_name}", 0, 30)
                        oled.show()

                prev_state[key] = is_pressed

        row.value(1)  # Deactivate row (Set back HIGH)

    time.sleep(0.01)  # Debounce polling delay