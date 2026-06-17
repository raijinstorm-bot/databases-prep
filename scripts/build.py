#!/usr/bin/env python3
"""
Compile questions/*.md into site/data.js (a plain <script> that sets
window.QUIZ_DATA). Using a .js file instead of fetch()ing JSON means the
page works both when opened directly (file://) and on GitHub Pages.

Run:  python3 scripts/build.py
"""
import os, re, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QDIR = os.path.join(ROOT, "questions")
OUT = os.path.join(ROOT, "site", "data.js")

# exam id -> human label  (order here = order shown in the UI)
EXAMS = [
    ("2023-1", "2023 — Variant 1"),
    ("2024-A", "2024 — Variant A"),
    ("2024-B", "2024 — Variant B"),
    ("2025",   "2025"),
]

# presentation slug -> (display name, pdf filename without extension)
PRESENTATIONS = {
    "relational-databases":   ("Relational Databases", "db_2_relational_databases"),
    "er-modelling":           ("Entity-Relationship Modelling", "db_3_4_entity_relationship_modelling"),
    "sql-select":             ("SQL SELECT", "db_5_sql_select"),
    "sql-select-2":           ("SQL SELECT II", "db_6_sql_select_part_II"),
    "physical-data-models":   ("Modifications & Physical Data Models", "db_7a_modifications_physical_data_models"),
    "indexes":                ("Indexes", "db_8_indexes"),
    "jdbc":                   ("JDBC", "db_9_jdbc"),
    "concurrency":            ("Concurrency Issues", "db_11_concurrency_issues"),
    "stored-procedures":      ("Stored Procedures", "db_12_stored_procedures"),
    "architecture-patterns":  ("System Architecture Patterns", "db_13_system_architecture_patterns"),
    "data-warehouses":        ("Data Warehouses", "db_14_data_warehouses"),
    "big-data":               ("Big Data", "db_15_Big_Data"),
    "nosql":                  ("NoSQL", "db_16_NoSQL_ISI_IAD"),
    "hbase":                  ("Apache HBase", "db_17_ApacheHBase"),
    "oracle-net":             ("Oracle Net", "db_18_Oracle_Net"),
    "gis":                    ("GIS", "db_19_GIS"),
    "oracle-storage-backup":  ("Oracle Storage & Backup", "db_20_Oracle_Storage_Backup"),
    "oracle-security":        ("Oracle Security", "db_21_Oracle_Security"),
    "vector-databases":       ("Vector Databases", "db_22_vector_databases"),
}

FM_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)
OPT_RE = re.compile(r"^-\s+([a-z])\)\s+(.*)$")


def parse_frontmatter(block):
    fm = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if val.startswith("[") or val.startswith('"') or val.lstrip("-").isdigit():
            try:
                fm[key] = json.loads(val)
                continue
            except json.JSONDecodeError:
                pass
        fm[key] = val.strip('"')
    return fm


def parse_question(path):
    raw = open(path, encoding="utf-8").read()
    m = FM_RE.match(raw)
    if not m:
        raise ValueError(f"No frontmatter in {path}")
    fm = parse_frontmatter(m.group(1))
    body = m.group(2).strip()

    # split off explanation / answer
    explanation = ""
    for heading in ("### Explanation", "### Answer"):
        if heading in body:
            head, _, expl = body.partition(heading)
            explanation = expl.strip()
            body = head.strip()
            break

    # remaining body = stem + (option lines)
    options = []
    stem_lines = []
    for line in body.splitlines():
        om = OPT_RE.match(line.strip())
        if om:
            options.append({"letter": om.group(1), "text": om.group(2).strip()})
        else:
            stem_lines.append(line)
    stem = "\n".join(stem_lines).strip()

    gen = fm.get("generated", False)
    if isinstance(gen, str):
        gen = gen.strip().lower() == "true"

    return {
        "id": fm["id"],
        "exam": fm.get("exam", ""),
        "number": int(fm.get("number", 0)) if str(fm.get("number", "0")).isdigit() else 0,
        "type": fm.get("type", "single"),
        "generated": bool(gen),
        "tags": fm.get("tags", []),
        "correct": fm.get("correct", []),
        "pdfs": fm.get("pdfs", []),
        "stem": stem,
        "options": options,
        "explanation": explanation,
    }


def main():
    files = sorted(glob.glob(os.path.join(QDIR, "*.md")))
    questions = [parse_question(p) for p in files]

    # build exam list with counts (only exams that exist or are declared)
    present = {q["exam"] for q in questions}
    exams = []
    for eid, label in EXAMS:
        closed = sum(1 for q in questions if q["exam"] == eid and q["type"] != "open")
        opened = sum(1 for q in questions if q["exam"] == eid and q["type"] == "open")
        if eid in present or (closed + opened) > 0:
            exams.append({"id": eid, "label": label, "closed": closed, "open": opened})

    presentations = {slug: {"name": name, "pdf": pdf}
                     for slug, (name, pdf) in PRESENTATIONS.items()}

    # topic list (presentations) with closed-question counts, in vocab order
    topics = []
    for slug, (name, pdf) in PRESENTATIONS.items():
        closed = sum(1 for q in questions
                     if q["type"] != "open" and slug in q.get("pdfs", []))
        opened = sum(1 for q in questions
                     if q["type"] == "open" and slug in q.get("pdfs", []))
        if closed + opened > 0:
            topics.append({"slug": slug, "name": name, "pdf": pdf,
                           "closed": closed, "open": opened})

    data = {"exams": exams, "topics": topics,
            "presentations": presentations, "questions": questions}

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("// AUTO-GENERATED by scripts/build.py — do not edit by hand.\n")
        f.write("window.QUIZ_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write(";\n")

    print(f"Wrote {OUT}")
    print(f"  exams: {len(exams)}  questions: {len(questions)} "
          f"({sum(1 for q in questions if q['type']!='open')} closed, "
          f"{sum(1 for q in questions if q['type']=='open')} open)")


if __name__ == "__main__":
    main()
