#!/usr/bin/env python3
"""Draw entry.png — a 1024x1024 newspaper front page summing up
Friday 20 November 2026's world news in six stories.

Facts come from research-20nov.md (six stories, each cross-checked
against at least two news sources). Nothing here is invented.

Run: python3 draw_news.py   -> writes entry.png next to this script.
"""

import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))

FONT_DIR = "/usr/share/fonts/truetype/liberation"
SERIF_BOLD = os.path.join(FONT_DIR, "LiberationSerif-Bold.ttf")
SANS = os.path.join(FONT_DIR, "LiberationSans-Regular.ttf")
SANS_BOLD = os.path.join(FONT_DIR, "LiberationSans-Bold.ttf")
SANS_ITALIC = os.path.join(FONT_DIR, "LiberationSans-Italic.ttf")

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (18, 18, 18)
RED = (178, 34, 34)
RULE = (120, 110, 95)
PANEL_BG = (255, 253, 246)
MUTED = (70, 66, 58)

MASTHEAD = "THE WORLD IN ONE DAY"
DATELINE = "FRIDAY 20 NOVEMBER 2026  •  SIX STORIES  •  ALL FACTS VERIFIED"

STORIES = [
    {
        "kicker": "KYIV UNDER FIRE",
        "headline": "Russia Hits Kyiv Bridges, 8 Killed",
        "sub": "Biggest barrage of the war; power cut across Ukraine",
        "summary": (
            "Russia launched one of the largest missile and drone attacks of "
            "the war on Friday, hitting three Dnipro bridges in Kyiv and "
            "power plants nationwide; 8 killed, 28 wounded. Retaliation for "
            "Ukraine's strikes on the Kerch Bridge."
        ),
    },
    {
        "kicker": "NATO ALERT",
        "headline": "Russian Missiles Crash in Poland",
        "sub": "NATO jets scrambled; Warsaw seeks reinforcements",
        "summary": (
            "Two Russian missiles and a jet-powered drone crashed in eastern "
            "Poland during the attack on Ukraine. Polish F-16s and Swedish "
            "Gripens scrambled; Patriots activated. Poland asks NATO for "
            "more support."
        ),
    },
    {
        "kicker": "BERLIN TALKS",
        "headline": "Allies Say Europe Ready to Talk to Russia",
        "sub": "Kushner floats NATO-style guarantee for Ukraine",
        "summary": (
            "The Coalition of the Willing met in Berlin and said Europe has "
            "a united position for talks with Russia. US envoy Jared Kushner "
            "discussed a NATO-style guarantee for Ukraine if it cedes "
            "territory. Trump phoned in: Putin \u201cwants to end the war\u201d."
        ),
    },
    {
        "kicker": "COP31 CLIMATE",
        "headline": "Fossil Fuels Erased From COP31 Draft",
        "sub": "Final day in Antalya; talks head to overtime",
        "summary": (
            "On COP31's final scheduled day in Antalya, a revised draft "
            "dropped every reference to fossil fuels and a $120 billion "
            "adaptation finance target. Talks look set to run into overtime."
        ),
    },
    {
        "kicker": "GTA 6 RECORD",
        "headline": "GTA 6 Makes $2.36 Billion in One Day",
        "sub": "24.6 million copies; biggest launch ever",
        "summary": (
            "Sensor Tower estimates GTA 6 sold 24.58 million copies and made "
            "$2.36 billion on its first day, the biggest entertainment "
            "launch in history. Take-Two has not released official figures."
        ),
    },
    {
        "kicker": "IRAQ CRACKDOWN",
        "headline": "Iraq Moves on Iran-Backed Militia Stronghold",
        "sub": "Forces deploy in Jurf al-Sakhar",
        "summary": (
            "Iraqi security forces deployed in Jurf al-Sakhar, a stronghold "
            "of the Iran-aligned Kataib Hezbollah armed group, under a deal "
            "to limit the group, accused of running an oil-smuggling network."
        ),
    },
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap; returns a list of lines that fit max_width."""
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        line = words[0]
        for word in words[1:]:
            trial = line + " " + word
            if draw.textlength(trial, font=fnt) <= max_width:
                line = trial
            else:
                lines.append(line)
                line = word
        lines.append(line)
    return lines


def draw_centered(draw, y, text, fnt, fill, width=W):
    x = (width - draw.textlength(text, font=fnt)) / 2
    draw.text((x, y), text, font=fnt, fill=fill)
    return y + fnt.size


def draw_panel(draw, box, story):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=PANEL_BG, outline=RULE, width=1)
    pad = 16
    cx0, cx1 = x0 + pad, x1 - pad
    text_w = cx1 - cx0
    y = y0 + 14

    # Kicker
    kicker_font = font(SANS_BOLD, 15)
    draw.text((cx0, y), story["kicker"], font=kicker_font, fill=RED)
    y += 22

    # Headline (serif bold, wrapped, up to 3 lines)
    head_font = font(SERIF_BOLD, 30)
    head_lines = wrap(draw, story["headline"], head_font, text_w)
    for line in head_lines:
        draw.text((cx0, y), line, font=head_font, fill=INK)
        y += 34
    y += 2

    # Sub-headline (sans italic, wrapped)
    sub_font = font(SANS_ITALIC, 17)
    sub_lines = wrap(draw, story["sub"], sub_font, text_w)
    for line in sub_lines:
        draw.text((cx0, y), line, font=sub_font, fill=MUTED)
        y += 22
    y += 6

    # Thin divider
    draw.line([(cx0, y), (cx1, y)], fill=RULE, width=1)
    y += 9

    # Summary — shrink font if it would overflow the panel
    inner_bottom = y1 - 12
    size = 16
    while size >= 13:
        sum_font = font(SANS, size)
        sum_lines = wrap(draw, story["summary"], sum_font, text_w)
        if y + len(sum_lines) * (size + 6) <= inner_bottom:
            break
        size -= 1
    sum_font = font(SANS, size)
    sum_lines = wrap(draw, story["summary"], sum_font, text_w)
    for line in sum_lines:
        draw.text((cx0, y), line, font=sum_font, fill=INK)
        y += size + 6


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # Masthead
    y = 26
    y = draw_centered(draw, y, MASTHEAD, font(SERIF_BOLD, 56), INK)
    y += 4
    draw.line([(24, y), (W - 24, y)], fill=INK, width=3)
    y += 8
    y = draw_centered(draw, y, DATELINE, font(SANS_BOLD, 16), RED)
    y += 10
    draw.line([(24, y), (W - 24, y)], fill=INK, width=1)

    # Grid: 2 columns x 3 rows
    margin = 24
    gap = 12
    grid_top = y + 12
    grid_bottom = H - 44
    grid_w = W - 2 * margin
    grid_h = grid_bottom - grid_top
    col_w = (grid_w - gap) // 2
    row_h = (grid_h - 2 * gap) // 3

    for i, story in enumerate(STORIES):
        col = i % 2
        row = i // 2
        x0 = margin + col * (col_w + gap)
        y0 = grid_top + row * (row_h + gap)
        draw_panel(draw, (x0, y0, x0 + col_w, y0 + row_h), story)

    # Footer
    footer = (
        "Sources: Reuters, The Times, CNN, AP, UN News, Sensor Tower — "
        "each story verified against at least two sources."
    )
    draw_centered(
        draw, grid_bottom + 12, footer, font(SANS_ITALIC, 13), MUTED
    )

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG")
    print("Wrote", out, img.size)


if __name__ == "__main__":
    main()
