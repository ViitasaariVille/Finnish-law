## Gap Description

The DMN rules are missing §58 which specifically covers compensation for emergency medical care received in private healthcare WITHOUT prior maksusitoumus (payment commitment) from the insurer.

## Law Reference

**§58:**
> Vahinkoa kärsineelle korvataan yksityisessä terveydenhuollossa annetun sairaanhoidon kustannukset ilman 59 §:ssä tarkoitettua maksusitoumusta:
> 1) kiireellisestä sairaanhoidosta, jolla tarkoitetaan välittömän hoidon tarpeen arviointia ja hoitoa, jota ei voida siirtää ilman vamman tai sairauden olennaista pahentumista;
> 2) vastaanottokäynnistä ja sen yhteydessä tehdystä röntgentutkimuksesta, ultraäänitutkimuksesta tai muusta niihin rinnastettavasta vähäisestä tutkimus- ja hoitotoimenpiteestä.

**Key Points:**
1. Emergency care = immediate treatment that cannot be delayed without worsening condition
2. Outpatient visits with minor diagnostics (X-ray, ultrasound) are covered
3. **NO maksusitoumus required** for these specific services

## Current DMN Status

- E5 covers medical expense compensation
- §57 covers maksusitoumus-based care
- §59 covers non-emergency private care (requires maksusitoumus)
- **NO specific rule for §58 emergency exception**

## Missing DMN Rule

#### EMERGENCY-001: Emergency Care Without Maksusitoumus (§58)

| treatment.type | treatment.urgency | treatment.setting | maksusitoumus.required | Output |
|----------------|-------------------|-------------------|------------------------|--------|
| EmergencyAssessment | Immediate | private | **NO** | **100%_Covered** |
| EmergencyTreatment | CannotBeDelayed | private | **NO** | **100%_Covered** |
| OutpatientVisit | NonEmergency | private | YES | **CustomerFeeOnly** |
| OutpatientVisit + XRay | MinorProcedure | private | **NO** | **100%_Covered** |
| OutpatientVisit + Ultrasound | MinorProcedure | private | **NO** | **100%_Covered** |
| Surgery | NonEmergency | private | YES | **CustomerFeeOnly** |

**Definition: Emergency Care (§58(1))**
- Immediate treatment needs assessment
- Treatment that cannot be postponed without significant worsening of injury/illness

**Definition: Minor Procedures (§58(2))**
- Outpatient visits
- X-ray examination
- Ultrasound examination  
- Comparable minor diagnostic/treatment procedures

## Severity: HIGH

- **Critical for victim access to emergency care**
- Distinguishes between emergency (covered) vs non-emergency (requires approval)
- Currently gap in coverage rules

## Related Sections

- §56: Healthcare provider notification
- §57: Maksusitoumus-based care
- §59: Non-emergency private care
- E5: Medical expense compensation

## Tags

@VilleMoltBot for review

---
*Identified during law compliance check - February 26, 2026*
