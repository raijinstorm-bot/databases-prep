# Databases — Exam Quiz

A static study app for past database-exam questions. Pick one or more past
exams, take a quiz (single/multi choice — the UI never reveals which), get
scored, and review what you missed. Deployable to GitHub Pages with zero
backend.

## Folder structure

```
questions/            One Markdown file per question (source of truth).
                      Frontmatter holds answer / type / tags / linked presentations.
presentations_md/     Full Markdown conversions of the lecture slides.
presentation_pdf/     Original slide PDFs (linked from each question).
site/                 The web app (index.html, app.js, style.css, data.js).
scripts/seed_questions.py   One-time generator that created questions/.
scripts/build.py      Compiles questions/*.md -> site/data.js.
.github/workflows/deploy.yml   Builds + deploys to GitHub Pages on push.
tests/                Original raw question sources (left untouched).
```

## Question file format

```markdown
---
id: "q-2024-b-13"
exam: "2024-B"        # which exam it appeared on
number: 13
type: "multi"         # single | multi | open
tags: ["2024-B"]      # exam tags (a question can carry several)
correct: ["b", "c"]   # correct option letters; [] for open
pdfs: ["er-modelling"] # linked presentation slug(s)
---

Question stem in Markdown.

- a) option text
- b) option text
...

### Explanation
Short explanation (a few sentences). Open questions use `### Answer`
with a longer multi-paragraph model answer instead.
```

## Editing / adding questions

1. Add or edit a `*.md` file in `questions/` (copy the format above).
2. Run `python3 scripts/build.py` to regenerate `site/data.js`.
3. Open `site/index.html` (double-click works) or commit and push.

The presentation slugs allowed in `pdfs:` are defined in `scripts/build.py`
(`PRESENTATIONS`). Use those exact strings so tags stay unified.

## Run locally

```bash
python3 -m http.server 8000
# then open http://localhost:8000/site/
```

(Opening `site/index.html` directly via `file://` also works, since the data
is loaded as a plain script, not via fetch.)

## Deploy to GitHub Pages

1. Create a GitHub repo and push this folder to the `main` branch.
2. In the repo: **Settings → Pages → Build and deployment → Source =
   "GitHub Actions"**.
3. Every push to `main` runs `.github/workflows/deploy.yml`, which rebuilds
   `site/data.js` and publishes the whole repo. The quiz lives at
   `https://<user>.github.io/<repo>/` (the root `index.html` redirects into
   `site/`), and the "Covered in" chips link to the slide PDFs.
