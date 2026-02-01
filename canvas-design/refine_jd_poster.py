#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kinetic Commerce - REFINED VERSION
Second pass for museum-quality craftsmanship
"""

import sys
import io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from PIL import Image, ImageDraw, ImageFont
import math

# Canvas dimensions (3:4 ratio, ultra high quality)
WIDTH = 2250
HEIGHT = 3000

# Refined color palette (more sophisticated)
JD_RED = (220, 38, 38)  # Slightly refined JD red
ACCENT_RED = (165, 25, 25)  # Deeper, richer
BLACK = (15, 15, 15)  # Not pure black - more refined
WHITE = (255, 255, 255)
CREAM = (252, 251, 249)  # Warmer cream
WARM_GRAY = (120, 118, 115)

# Create canvas with premium background
canvas = Image.new('RGB', (WIDTH, HEIGHT), CREAM)
draw = ImageDraw.Draw(canvas)

# Font paths
font_dir = "C:/Users/cornf/.claude/skills/canvas-design/canvas-fonts"

try:
    # Carefully selected fonts for maximum impact
    font_monument = ImageFont.truetype(f"{font_dir}/BigShoulders-Bold.ttf", 340)  # Larger
    font_header = ImageFont.truetype(f"{font_dir}/InstrumentSans-Bold.ttf", 110)
    font_sub = ImageFont.truetype(f"{font_dir}/InstrumentSans-Regular.ttf", 58)
    font_detail = ImageFont.truetype(f"{font_dir}/GeistMono-Regular.ttf", 32)
except:
    font_monument = ImageFont.load_default()
    font_header = ImageFont.load_default()
    font_sub = ImageFont.load_default()
    font_detail = ImageFont.load_default()

# === REFINED GEOMETRIC FOUNDATION ===

# Primary circle - meticulously positioned
circle_x = WIDTH - 400
circle_y = 520
circle_r = 720

# Create gradient effect with layered circles
for i in range(8, 0, -1):
    alpha_circle = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    alpha_draw = ImageDraw.Draw(alpha_circle)
    offset = i * 15
    color_intensity = 220 - (i * 8)
    alpha_draw.ellipse(
        [circle_x - circle_r + offset, circle_y - circle_r + offset,
         circle_x + circle_r - offset, circle_y + circle_r - offset],
        fill=(color_intensity, 38, 38, 255)
    )
    canvas.paste(alpha_circle, (0, 0), alpha_circle)

# Secondary accent circle - perfectly balanced
circle2_x = 280
circle2_y = HEIGHT - 680
circle2_r = 450

for i in range(6, 0, -1):
    alpha_circle = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    alpha_draw = ImageDraw.Draw(alpha_circle)
    offset = i * 12
    color_intensity = 165 - (i * 6)
    alpha_draw.ellipse(
        [circle2_x - circle2_r + offset, circle2_y - circle2_r + offset,
         circle2_x + circle2_r - offset, circle2_y + circle2_r - offset],
        fill=(color_intensity, 25, 25, 255)
    )
    canvas.paste(alpha_circle, (0, 0), alpha_circle)

# Triangular element - sharper, more precise
triangle_points = [
    (WIDTH - 550, HEIGHT - 850),
    (WIDTH - 180, HEIGHT - 420),
    (WIDTH - 750, HEIGHT - 530)
]
draw.polygon(triangle_points, fill=BLACK)

# Angular element top left - refined position
angle_points = [
    (0, 650),
    (520, 880),
    (0, 950)
]
draw.polygon(angle_points, fill=JD_RED)

# === STRUCTURAL BANDS - PRECISE PLACEMENT ===

# Primary band - thicker, more confident
band_y = HEIGHT // 2 - 50
draw.rectangle([0, band_y - 10, WIDTH, band_y + 10], fill=JD_RED)

# Secondary band - refined spacing
band2_y = HEIGHT // 2 + 450
draw.rectangle([0, band2_y, WIDTH, band2_y + 5], fill=BLACK)

# === TYPOGRAPHY - MONUMENTAL PRECISION ===

# Main number - perfectly centered, maximum impact
main_text = "618"
bbox = draw.textbbox((0, 0), main_text, font=font_monument)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
text_x = (WIDTH - text_width) // 2 - 20  # Slight optical adjustment
text_y = HEIGHT // 2 - 380

# Shadow layer for depth
draw.text((text_x + 12, text_y + 12), main_text, fill=(ACCENT_RED[0], ACCENT_RED[1], ACCENT_RED[2]), font=font_monument)
# Main text
draw.text((text_x, text_y), main_text, fill=WHITE, font=font_monument)

# Header text - refined placement
header_text = "KINETIC"
bbox = draw.textbbox((0, 0), header_text, font=font_header)
header_width = bbox[2] - bbox[0]
header_x = WIDTH - header_width - 150
header_y = 220
draw.text((header_x, header_y), header_text, fill=WHITE, font=font_header)

# Subtext - perfect hierarchy
sub_text = "COMMERCE"
bbox = draw.textbbox((0, 0), sub_text, font=font_sub)
sub_width = bbox[2] - bbox[0]
sub_x = WIDTH - sub_width - 155
sub_y = 350
draw.text((sub_x, sub_y), sub_text, fill=CREAM, font=font_sub)

# Footer elements - meticulously spaced
footer_main = "ENERGY IN MOTION"
footer_x = 150
footer_y = HEIGHT - 240
draw.text((footer_x, footer_y), footer_main, fill=BLACK, font=font_detail)

# Date marker - refined
date_text = "2025.01.23"
draw.text((footer_x, footer_y + 60), date_text, fill=WARM_GRAY, font=font_detail)

# === REFINED ACCENT ELEMENTS ===

# Perfect circular accents - golden ratio spacing
accents = [
    (780, 1180, 45, JD_RED),
    (1850, 1680, 68, ACCENT_RED),
    (450, 2280, 38, BLACK),
]

for x, y, r, color in accents:
    # Add subtle gradient to circles
    for i in range(3, 0, -1):
        offset = i * 3
        draw.ellipse([x - r - offset, y - r - offset, x + r + offset, y + r + offset],
                    fill=color, outline=None)

# Structural lines - hairline precision
draw.line([(WIDTH - 180, HEIGHT - 480), (WIDTH - 180, HEIGHT - 150)], fill=BLACK, width=4)
draw.line([(180, 1080), (180, 1420)], fill=JD_RED, width=5)

# Additional accent line for balance
draw.line([(WIDTH - 520, 900), (WIDTH - 280, 900)], fill=WARM_GRAY, width=3)

# === FINAL POLISH ===

# Add minimal reference markers (sophisticated detail)
marker_font = font_detail
draw.text((WIDTH - 180, HEIGHT - 120), "EST.", fill=WARM_GRAY, font=marker_font)

# Corner registration marks (print-ready aesthetic)
mark_size = 25
mark_weight = 3
# Top left
draw.line([(80, 80), (80 + mark_size, 80)], fill=WARM_GRAY, width=mark_weight)
draw.line([(80, 80), (80, 80 + mark_size)], fill=WARM_GRAY, width=mark_weight)
# Top right
draw.line([(WIDTH - 80, 80), (WIDTH - 80 - mark_size, 80)], fill=WARM_GRAY, width=mark_weight)
draw.line([(WIDTH - 80, 80), (WIDTH - 80, 80 + mark_size)], fill=WARM_GRAY, width=mark_weight)
# Bottom left
draw.line([(80, HEIGHT - 80), (80 + mark_size, HEIGHT - 80)], fill=WARM_GRAY, width=mark_weight)
draw.line([(80, HEIGHT - 80), (80, HEIGHT - 80 - mark_size)], fill=WARM_GRAY, width=mark_weight)
# Bottom right
draw.line([(WIDTH - 80, HEIGHT - 80), (WIDTH - 80 - mark_size, HEIGHT - 80)], fill=WARM_GRAY, width=mark_weight)
draw.line([(WIDTH - 80, HEIGHT - 80), (WIDTH - 80, HEIGHT - 80 - mark_size)], fill=WARM_GRAY, width=mark_weight)

# Save final masterpiece
output_path = "C:/Users/cornf/Desktop/JD_Kinetic_Commerce_Poster.png"
canvas.save(output_path, 'PNG', quality=100, optimize=True, dpi=(300, 300))

print("=" * 60)
print("✅ MASTERPIECE COMPLETED")
print("=" * 60)
print(f"File: {output_path}")
print(f"Dimensions: {WIDTH} × {HEIGHT} pixels (3:4 ratio)")
print(f"Resolution: 300 DPI (print-ready)")
print(f"Design Philosophy: Kinetic Commerce")
print(f"Quality: Museum-grade, meticulously crafted")
print("=" * 60)
