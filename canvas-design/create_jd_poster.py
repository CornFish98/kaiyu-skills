#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kinetic Commerce - JD E-commerce Poster
Based on the Kinetic Commerce design philosophy
"""

import sys
import io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from PIL import Image, ImageDraw, ImageFont
import math

# Canvas dimensions (3:4 ratio, high quality)
WIDTH = 2250
HEIGHT = 3000

# Color palette
JD_RED = (225, 37, 27)  # JD brand red
DEEP_RED = (180, 20, 20)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CREAM = (250, 248, 245)
GRAY = (100, 100, 100)

# Create canvas
canvas = Image.new('RGB', (WIDTH, HEIGHT), CREAM)
draw = ImageDraw.Draw(canvas)

# Font paths
font_dir = "C:/Users/cornf/.claude/skills/canvas-design/canvas-fonts"
font_bold_path = f"{font_dir}/BigShoulders-Bold.ttf"
font_regular_path = f"{font_dir}/InstrumentSans-Regular.ttf"
font_mono_path = f"{font_dir}/GeistMono-Regular.ttf"

# Load fonts
try:
    font_huge = ImageFont.truetype(font_bold_path, 280)
    font_large = ImageFont.truetype(font_bold_path, 160)
    font_medium = ImageFont.truetype(font_regular_path, 72)
    font_small = ImageFont.truetype(font_mono_path, 36)
except:
    print("Using default font")
    font_huge = ImageFont.load_default()
    font_large = ImageFont.load_default()
    font_medium = ImageFont.load_default()
    font_small = ImageFont.load_default()

# === BACKGROUND GEOMETRIC ELEMENTS ===

# Large red circle (top right, partially off-canvas)
circle_center = (WIDTH - 300, 400)
circle_radius = 650
draw.ellipse(
    [circle_center[0] - circle_radius, circle_center[1] - circle_radius,
     circle_center[0] + circle_radius, circle_center[1] + circle_radius],
    fill=JD_RED
)

# Deep red accent circle (left side)
circle_center_2 = (200, HEIGHT - 600)
circle_radius_2 = 400
draw.ellipse(
    [circle_center_2[0] - circle_radius_2, circle_center_2[1] - circle_radius_2,
     circle_center_2[0] + circle_radius_2, circle_center_2[1] + circle_radius_2],
    fill=DEEP_RED
)

# Geometric triangular shapes for dynamic tension
triangle_points = [
    (WIDTH - 500, HEIGHT - 800),
    (WIDTH - 200, HEIGHT - 400),
    (WIDTH - 700, HEIGHT - 500)
]
draw.polygon(triangle_points, fill=BLACK)

# Sharp angle element (top left)
angle_points = [
    (0, 600),
    (450, 800),
    (0, 900)
]
draw.polygon(angle_points, fill=JD_RED)

# === HORIZONTAL BANDS FOR STRUCTURE ===

# Thin red band across middle
draw.rectangle([0, HEIGHT//2 - 8, WIDTH, HEIGHT//2 + 8], fill=JD_RED)

# Thin black band
draw.rectangle([0, HEIGHT//2 + 400, WIDTH, HEIGHT//2 + 404], fill=BLACK)

# === TYPOGRAPHY AS ARCHITECTURAL ELEMENTS ===

# Main number (centered, monumental)
main_text = "618"
# Calculate text bbox for centering
bbox = draw.textbbox((0, 0), main_text, font=font_huge)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
text_x = (WIDTH - text_width) // 2
text_y = HEIGHT // 2 - 300

# Draw text with slight offset shadow for depth
draw.text((text_x + 8, text_y + 8), main_text, fill=DEEP_RED, font=font_huge)
draw.text((text_x, text_y), main_text, fill=WHITE, font=font_huge)

# Secondary text (top - brand essence)
header_text = "KINETIC"
bbox = draw.textbbox((0, 0), header_text, font=font_large)
header_width = bbox[2] - bbox[0]
draw.text((WIDTH - header_width - 120, 180), header_text, fill=WHITE, font=font_large)

# Subheader (smaller, refined)
sub_text = "COMMERCE"
bbox = draw.textbbox((0, 0), sub_text, font=font_medium)
sub_width = bbox[2] - bbox[0]
draw.text((WIDTH - sub_width - 130, 380), sub_text, fill=CREAM, font=font_medium)

# Bottom text (minimal, grounding)
footer_text = "ENERGY IN MOTION"
bbox = draw.textbbox((0, 0), footer_text, font=font_small)
footer_width = bbox[2] - bbox[0]
draw.text((120, HEIGHT - 200), footer_text, fill=BLACK, font=font_small)

# Date marker (small, precise)
date_text = "2025.01.23"
draw.text((120, HEIGHT - 140), date_text, fill=GRAY, font=font_small)

# === REFINED GEOMETRIC ACCENTS ===

# Small circles as visual rhythm
accent_circles = [
    (700, 1100, 40),
    (1800, 1600, 60),
    (400, 2200, 35),
]

for x, y, r in accent_circles:
    draw.ellipse([x - r, y - r, x + r, y + r], fill=JD_RED)

# Thin lines for structure (minimal, precise)
draw.line([(WIDTH - 150, HEIGHT - 400), (WIDTH - 150, HEIGHT - 100)], fill=BLACK, width=3)
draw.line([(150, 1000), (150, 1300)], fill=JD_RED, width=4)

# === FINAL REFINEMENT ===

# Add subtle texture by overlaying semi-transparent rectangles
# (simulating paper grain effect - very subtle)
for i in range(0, WIDTH, 600):
    for j in range(0, HEIGHT, 600):
        if (i + j) % 1200 == 0:
            overlay = Image.new('RGBA', (200, 200), (255, 255, 255, 5))
            canvas.paste(overlay, (i, j), overlay)

# Save to desktop
output_path = "C:/Users/cornf/Desktop/JD_Kinetic_Commerce_Poster.png"
canvas.save(output_path, 'PNG', quality=95, optimize=True)
print(f"✅ Poster created successfully: {output_path}")
print(f"   Dimensions: {WIDTH}x{HEIGHT} (3:4 ratio)")
print(f"   Design Philosophy: Kinetic Commerce")
