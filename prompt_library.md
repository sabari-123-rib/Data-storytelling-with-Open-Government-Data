# CAPSTONE 46 — Prompt Library

## Prompt 1: Source discovery
Find official Indian government datasets on school enrolment, school infrastructure, and education indicators. Prioritise data.gov.in and Ministry of Education / UDISE+ sources. Return exact title, publisher, reference year, geographic coverage, variables, download link, definitions, and caveats. Do not invent sources or claim a file was inspected unless it was.

## Prompt 2: Dataset documentation
Read the attached CSV and produce a data dictionary. Identify units, row granularity, missing values, duplicate keys, inconsistent labels, outliers, and any values that need source confirmation. Do not silently change or impute values.

## Prompt 3: Chart selection
Given the dataset schema and the audience (general public and local-community readers), recommend a chart type for the stated question. Explain why it fits, what it cannot prove, axis choices, units, and a risk of misleading interpretation.

## Prompt 4: Chart caption
Write a plain-language caption of 40–60 words using only the supplied chart and verified source facts. Separate observation from explanation. Do not infer causation or describe GER as attendance or completion.

## Prompt 5: Data-story draft
Write a data story for general readers using only the supplied verified figures. Cite the source and year near every major claim. Include at least two limitations and one unanswered question. Do not invent a policy cause, quote, or local statistic.

## Prompt 6: Adversarial fact-check
Act as a skeptical reviewer. For every factual claim, label it Supported / Partially supported / Unsupported / Outdated. Identify the exact source evidence needed to verify it. Flag causal claims, denominator problems, mismatched years, and unsupported generalisations.

## Prompt 7: Social posts
Create five short posts from the verified story. Every post must preserve units, year, source, and caveats where needed. Avoid sensationalism, stigma, or claims stronger than the data.

## Prompt 8: Python automation
Write a Python script that reads a local CSV, validates required columns and missing values, regenerates charts, and reports validation errors. Never replace missing values with zero. Include setup instructions and a test case.

## Prompt 9: Before/after review
Compare a raw table or technical explanation with an AI-assisted plain-language version. Check whether the simplified version preserves numbers, units, reference period, caveats, and uncertainty. List any edits made by a human reviewer.

## Prompt 10: Ethical review
Check for privacy risks, sensitive small groups, possible stereotyping, copyright, source attribution, accessibility, and risks of misleading visual design. Recommend mitigations without claiming that the data proves more than it does.
