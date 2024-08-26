# Abnormal Report Template

Provided below are the abnormal findings and corresponding impression that you need to fill in the template for each abnormal conditions (structured by markdown headings):


## Liver Findings

### Parenchymatous Liver Disease

```markdown
**Liver:** Normal size and (mildly) `[increased | coarse]` parenchymal echogenicity. No focal lesion.
**IMPRESSION:**
- (Mild) parenchymatous disease of the liver without focal lesion.
```

### Fatty Liver

#### Mild Fatty Liver

```markdown
**Liver:** Normal size with mildly increased parenchymal echogenicity of the liver. No focal lesion.
**IMPRESSION:**
- Mild fatty liver without focal lesion.
```

#### Moderate Fatty Liver

```markdown
**Liver:** Normal size with diffusely increased parenchymal echogenicity of the liver, causing imparied visualization of intrahepatic vasculature. No focal lesion.
**IMPRESSION:**
- Moderate fatty liver without focal lesion.
```

#### Severe Fatty Liver

```markdown
**Liver:** Normal size with diffusely increased parenchymal echogenicity of the liver, causing imparied visualization of intrahepatic vasculature and right hemidiaphragm. No focal lesion.
**IMPRESSION:**
- Severe fatty liver without focal lesion.
```

#### Focal Fat Sparing 

If focal fat sparing area is present, add the following line in the `liver` field after the fatty liver sentence.

```markdown
**Liver:** <fatty_liver_findings>. Geographic hypoechoic areas `[at | adjacent to]` `[periportal region | gallbladder fossa]`, likely a focal fat sparing.
**IMPRESSION:**
- <fatty_liver_impression> with focal fat sparing at <focal_fat_sparing_location>
```

Example:

```markdown
**Liver:** Normal size with mildly increased parenchymal echogenicity of the liver. Geographic hypoechoic areas at periportal region, likely a focal fat sparing. No gross mass.
**IMPRESSION:**
- Severe fatty liver with focal fat sparing at periportal region.
```

### Cirrhosis

```markdown
**Liver:** `[Normal size | Enlarged caudate lobe]` with diffusely coarsen parenchymal echogenicity and surface nodularity. Portal vein enlarged, measuring ___ cm. No focal lesion.
**Spleen:** `[Normal in size | Spleenomegaly]`.
**IMPRESSION:**
- Liver cirrhosis without focal lesion.
```


## Gallbladder Findings

Order findings as:
1. Gallbladder distension
2. Gallbladder adenomyomatosis
3. Gallstone or bile sludge

```markdown
**Gallbladder:** <gallbladder_distend>. <gallbladder_adeno>. <gallbladder_stone_or_sludge>.
```

### Gallbladder Adenomyomatosis

```markdown
**Gallbladder:** Focal adenomyomatosis of the gallbladder.
**IMPRESSION:** 
- Focal adenomyomatosis of the gallbladder. 
```

### Gallstone(s)

```markdown
**Gallbladder:** Distended gallbladder containing `[a ?-cm | a few | many ]` gallstone(s), (measuring up to ___ cm). No gallbladder wall thickening or pericholecystic fluid. No mass
**IMPRESSION:** 
- `[a ?-cm | a few | many ]` gallstone(s) without evidence of cholecystitis 
```

### Bile sludge

```markdown
**Gallbladder:** Distended gallbladder containing bile sludge. No gallbladder wall thickening or pericholecystic fluid. No stone or mass.
**IMPRESSION:**
- Bile sludge in gallbladder without evidence of cholecystitis
```

### Post-cholecystectomy

```markdown
**Gallbladder:** Surgically absent gallbladder.
```

### Cholecystostomy

```markdown
**Gallbladder:** Collapsed gallbladder with retained cholecystostomy tube. No stone.
**IMPRESSION:** 
- Proper position of cholecystosmy tube within collapsed gallbladder.
```

## Biliary Findings

### Dilated CBD without cause

```markdown
**Biliary system:** Dilated CBD, measures about ___ mm without demonstrable cause of obstruction. No intrahepatic ductal dilatation. 
**IMPRESSION:** 
- Dilated CBD without demonstrable cause of obstruction.
```

## Kidney Findings


Order findings as:
1. Kidney size and echogenicity
2. (If any) Renal cyst(s)
3. (If any) Renal stone, hydronephrosis, or solid mass.

```markdown
**Kidneys:** <kidney_size_echo>. <renal_cyst>. <renal_stone_hydro_solid_mass>.
```


### (Chronic) Parenchymatous Kidney Disease

Definition: 

"Parenchymatous kidney disease" := normal kidney size but increased echogenicity. 
"Chronic parenchymatous kidney disease" := small kidney size and increased echogenicity. 

If one kidney is abnormal and the other is normal, report findings for each kidneys. 

Here is the format:

```markdown
**Kidneys:** `[Normal | Small]` size with (mildly) increased parenchymal echogenicity of the `[right | left | both]` kidney(s). No stone, hydronephrosis or solid mass.
**IMPRESSION:**
- (Chronic) parenchymatous disease of `[right | left | both]` kidney(s).
```

Examples:

- Parenchymatous right kidney and normal left kidney:

```markdown
**Kidneys:** Normal size with mildly increased parenchymal echogenicity of the right kidney. Normal size and parenchymal echogenicity of left kidney. No stone, hydronephrosis or solid mass.
**IMPRESSION:**
- Parenchymatous disease of right kidney.
```

- Chronic parenchymatous of both kidneys:

```markdown
**Kidneys:** Small size with increased parenchymal echogenicity of both kidneys. No stone, hydronephrosis or solid mass.
**IMPRESSION:**
- Chronic parenchymatous disease of both kidneys.
```

### Renal Cyst(s)

Here is how to report renal cyst according to Bosniak classification system.

#### Bosniak 1 (Simple Cyst)

Use this phase: "simple cortical cyst(s)" with <quantifier> as described in the english style guide.

```markdown
**Kidneys:** Normal size and parenchymal echogenicity of both kidneys. <quantifier> simple cortical cyst(s) at `[right | left | both]` kidney(s). No stone, hydronephrosis or solid mass.
**IMPRESSION:**
- <quantifier> simple `[right | left | bilateral]` cyst(s)
```

Examples:

```markdown
**Kidneys:** Normal size and parenchymal echogenicity of both kidneys. A 0.5-cm simple cortical cyst at right kidney. No stone, hydronephrosis or solid mass.
**IMPRESSION:**
- A 0.5-cm simple right renal cyst.
```

```markdown
**Kidneys:** Normal size and parenchymal echogenicity of both kidneys. A few simple cortical cysts at both kidneys, measuring up to 2.0 cm. No stone, hydronephrosis or solid mass.
**IMPRESSION:**
- A few simple bilateral renal cysts, measuring up to 2.0 cm.
```

### Renal Stone

```markdown
**Kidneys:** Normal size and parenchymal echogenicity of both kidneys. <quantifier> non-obstructing caliceal stone(s) at `[right | left | both]` kidney(s).  No hydronephrosis or solid mass.
**IMPRESSION:**
- <quantifier> non-obstructing caliceal stone(s) at `[right | left | both]` kidney(s)
```

Examples:

```markdown
**Kidneys:** Normal size and parenchymal echogenicity of both kidneys. A few non-obstructing caliceal stones at right kidney.  No hydronephrosis or solid mass.
**IMPRESSION:**
- A few non-obstructing caliceal stones at right kidney.
```

