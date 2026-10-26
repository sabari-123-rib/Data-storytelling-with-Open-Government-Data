# AI Verification and Responsible Use Report

## Evidence base
The national figures used in the four charts and story are transcribed from the Ministry of Education's UDISE+ 2023–24 national highlights / report:
- Existing-structure report: https://www.education.gov.in/sites/upload_files/mhrd/files/statistics-new/udise_report_existing_23_24.pdf
- NEP-structure report: https://www.education.gov.in/sites/upload_files/mhrd/files/statistics-new/udise_report_nep_23_24.pdf
The Open Government Data Platform India lists relevant UDISE+ catalogues:
- Enrolment by location, management, school category and social category: https://www.data.gov.in/catalog/enrolment-location-school-management-school-category-and-social-category-udise-plus
- UDISE+ dataset group, including school infrastructure and teacher datasets: https://www.data.gov.in/dataset-group-name/Unified%20district%20information%20system%20for%20education
Census literacy tables are a possible supplementary source, but Census 2011 figures are older and must be labelled with their reference year:
- Census of India 2011 provisional population totals: https://censusindia.gov.in/nada/index.php/catalog/42611/download/46274/Census%20of%20India%202011-Provisional%20Population%20Totals.pdf

## Figures verified against the official national highlights
- Total schools: 1,471,891
- Total teachers: 9,807,600
- Enrolment, pre-primary to higher secondary: 248,045,828
- Enrolment, primary to higher secondary: 234,963,031
- Girls' enrolment, primary to higher secondary: 113,248,084
- Boys' enrolment, primary to higher secondary: 121,714,947
- GER: primary 93.0%; upper primary 89.7%; elementary 91.7%; secondary 77.4%; higher secondary 56.2%.

## Important caveats
1. The official report states pre-primary enrolment excludes Anganwadi ECCE centres and private kindergartens that are outside UDISE+.
2. GER is not an attendance, retention, learning-outcome, or completion rate.
3. Stage-wise counts do not track the same cohort of students, so differences alone cannot be labelled dropout counts.
4. Enrolment counts by sex are not population-adjusted equity measures.
5. Four charts are based on the national highlights transcribed into the included CSV. State/district-level data and infrastructure values were not independently downloaded and validated in this run; do not claim those analyses are complete.
6. The fourth chart places schools, teachers and students in millions despite different units; the note explicitly warns that bar heights are not directly comparable. A more conservative submission could replace it with a chart using one unit only.

## Hallucination and claim testing
Test performed: compare the headline values used in charts with the Ministry of Education's UDISE+ national highlights. Values listed above match the retrieved official table.
Potential hallucination traps and controls:
- Do not claim a reason for lower GER at higher-secondary level without additional evidence.
- Do not call the difference between stage enrolment counts a dropout rate.
- Do not describe GER as attendance.
- Do not fabricate state rankings, infrastructure percentages, quotations, or download dates.
- Do not imply that an AI model is a primary source.

## Human review required before submission
- Open the source PDFs and check the table in the version actually submitted.
- Record access date and exact table/page numbers.
- Download the actual data.gov.in CSVs for the final state/local comparisons.
- Recalculate chart values from raw files and compare with the report.
- Check whether any source has updated definitions or revised figures.
- Ensure citations remain visible in the PDF and slides.

## Responsible AI statement
AI was used to assist with drafting, chart code, and plain-language explanation. The government publication remains the evidence source. Human verification is required before final submission. No personal student-level data is included in this project.
