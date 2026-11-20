# The World in One Day — 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/intan151/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/intan151/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

An entry for the [make.fun](https://make.fun) competition
["Sum up 20 November's world news in one image"](https://make.fun/bounty/news-image-20261120)
($250, 50 paid places, entries close 22 November 2026).

## The image

A newspaper front page, **THE WORLD IN ONE DAY — Friday 20 November 2026**,
summing up the day in six stories, two columns by three rows:

1. **Kyiv Under Fire** — Russia launches one of the largest missile and
   drone attacks of the war, hitting three Dnipro bridges in Kyiv; 8 killed,
   28 wounded; power cut across Ukraine.
2. **NATO Alert** — two Russian missiles and a jet-powered drone crash in
   eastern Poland; Polish F-16s and Swedish Gripens scramble, Patriots
   activated.
3. **Berlin Talks** — the Coalition of the Willing meets in Berlin and says
   Europe has a united position for talks with Russia; Kushner floats a
   NATO-style guarantee for Ukraine.
4. **COP31 Climate** — on the final scheduled day in Antalya, a revised
   draft drops every reference to fossil fuels and a $120 billion adaptation
   finance target; talks head to overtime.
5. **GTA 6 Record** — Sensor Tower estimates GTA 6 sold 24.58 million copies
   and made $2.36 billion on its first day, the biggest entertainment launch
   in history.
6. **Iraq Crackdown** — Iraqi security forces deploy in Jurf al-Sakhar, a
   stronghold of the Iran-aligned Kataib Hezbollah group, accused of running
   an oil-smuggling network.

Every story happened, or was first reported, on 20 November 2026, and was
cross-checked against at least two news sources (Reuters, The Times, CNN, AP,
UN News and others). No fact is invented.

## How it is built

- `draw_news.py` — draws `entry.png` (1024×1024) with Pillow: masthead,
  date line, six panels, each with a kicker, headline, sub-headline and a
  one-to-two-line summary. Run it with `python3 draw_news.py`.
- `main.py` — the graded entry point (Python standard library only). It
  copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. Run it with
  `MAKEFUN_OUTPUT_DIR=out python3 main.py`; running it twice writes
  byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
