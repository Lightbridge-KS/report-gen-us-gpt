# User Guide for "ReportGen-US-GPT"


"ReportGen-US-GPT" is an AI-powered assistant designed to assist radiologists in generating ultrasound radiology reports. It utilizes a structured approach to create detailed, accurate reports based on provided findings and predefined templates. The application ensures consistency in reporting and adherence to institutional style guidelines.


## How to Use

1. **Input Findings:**

   - You will provide specific findings from the ultrasound study. 
   - If findings for any specific organ are not provided, "ReportGen-US-GPT" will assume normal findings for that organ and generate the report accordingly.

2. **Report Generation:**

   - "ReportGen-US-GPT" constructs the report using the following resources:
     - **English Style Guide:** Ensures the language used in the report follows the preferred style for phrasing and quantifying findings.
     - **Reporting Structure:** Provides the blueprint for the layout of the report, ensuring that all necessary sections are included and properly organized.
     - **Normal Report Template:** Supplies templates for normal findings, which will be used if no abnormal findings are provided.
     - **Abnormal Report Template:** Supplies templates for various abnormal findings and impressions, tailored to specific conditions and organs.

> Note: These resources can be found in the `prompt/` folder in the [GitHub](https://github.com/Lightbridge-KS/report-gen-us-gpt) repository

1. **Output Format:**

   - The generated report will be returned in **markdown format**. This format excludes any code blocks and contains only the finalized report text.
   - The report will include an automatic disclaimer stating: "*This is a generative report produced by AI and has not been reviewed by the attending radiologist.*"

---

## Example Workflow

1. **Input:** 
   - You provide the following findings: "Increased echogenicity in the liver, measuring 15 cm in size, with no focal lesions."

2. **Process:**
   - "ReportGen-US-GPT" uses the "Abnormal Report Template" to structure the liver findings and impression according to the provided input.
   - It defaults to normal findings for other organs not mentioned.

3. **Output:**
   - The application returns the report as:
  
     ```markdown
     **US OF THE UPPER ABDOMEN**

     **FINDINGS:**

     **Liver:** Normal size with diffusely increased parenchymal echogenicity of the liver. No focal lesion.
     **Biliary system:** CBD size ___ mm. No intrahepatic ductal dilatation.
     **Gallbladder:** Well-distended gallbladder. No stone or mass.
     **Spleen:** Normal in size.
     **Pancreas:** Visualized portions are unremarkable.
     **Kidneys:** Normal size and parenchymal echogenicity of both kidneys. No stone, hydronephrosis, or solid mass.
     **Aorta:** Normal caliber.

     **IMPRESSION:**
     *This is a generative report produced by AI and has not been reviewed by the attending radiologist.*
     - Moderate fatty liver without focal lesion.
     ```

---

**Important Notes**

- **Normal Assumption:** If no specific findings are provided for an organ, the application assumes normal findings based on the "Normal Report Template."
- **Review Requirement:** The final output should always be reviewed by the attending radiologist before being finalized in the patient's record.