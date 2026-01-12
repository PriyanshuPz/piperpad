# PiperPad

PiperPad is a tiny 3×3 hackpad with per-key RGB and a personality.  
It’s not just a macro pad. it’s a *pattern device*.

Each of the 9 keys has its own RGB LED. Instead of just pressing buttons, you can enter **sequences** and **patterns** that unlock behaviors, layers, or macros. Think of it like a physical pattern lock that doubles as a productivity tool.

Built around an RP2040 and powered by KMK firmware, PiperPad is:

- Fully USB HID (plug & play)
- Individually-lit keys (SK6812)
- Direct GPIO wiring (no matrix)
- Perfect for macros, launchers, or secret rituals 😈

---

## Hackpad Overview

![Overall Hackpad](assets/pcb_front.png)

---

## Schematic

![Schematic](assets/sch.png)

- 9 push switches, each on its own GPIO  
- 9 SK6812 RGB LEDs, daisy-chained  
- RP2040 (XIAO) as the controller  
- Internal pull-ups for all keys  

---

## PCB

**Front:**

![PCB Front](assets/pcb_front.png)

**Back:**

![PCB Back](assets/pcb_back.png)

The board is a compact 3×3 layout with each LED placed close to its key for clean per-key lighting.

---

## Case Design

**Top:**

![Case Top](assets/case_top.png)

**Bottom:**

![Case Bottom](assets/case_bottom.png)

The case is a simple two-part shell:

- Top plate with 9 key cutouts  
- Bottom plate that holds the PCB  
- Designed to sandwich the board securely  

STEP files are available in `/cad` for modification or 3D printing.

---

## Bill of Materials (BOM)

The full BOM is available in:

```

pcb/bom.csv

```

Key components:

| Part                     | Quantity |
|--------------------------|----------|
| RP2040 (XIAO)            | 1        |
| Tactile switches         | 9        |
| SK6812 Mini RGB LEDs     | 9        |

---

## Firmware

Firmware lives in:

```

firmware/main.py

```
> Firmware is not complete only test code for now, will update code when I get physical materials to work on.

It uses **KMK** and runs in “direct pin” mode (no matrix).  
Each key maps 1:1 to a GPIO pin, making the hardware simple and reliable.

This makes PiperPad:

- Easy to reprogram  
- Friendly for experimentation  
- Perfect for pattern-based logic  

---

PiperPad is small, expressive, and weird in the best way.  
It’s not just something you press.

It’s something you *perform*. 🎭

Pz~