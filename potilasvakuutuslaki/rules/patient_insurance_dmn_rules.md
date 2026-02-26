# Finnish Patient Insurance - DMN Business Rules

**Based on:** Potilasvakuutuslaki (Patient Insurance Act) 948/2019  
**Version:** 1.0  
**Source:** https://www.finlex.fi/fi/laki/alkup/2019/20190948

---

## 1. Insurance Obligation

| **OUTPUT: Insurance Required** | Organization Type | Legal Basis | Source Text |
|-------------------------------|------------------|-------------|-------------|
| PatientInsurance | PublicHealthcareEntity | Section 6(1) | Terveyden- ja sairaanhoidon yhteisö |
| PatientInsurance | PrivateHealthcareEntity | Section 6(1) | Yksityinen terveydenhuolto |
| PatientInsurance | Employer | Section 6(1) | Työnantaja |
| PatientInsurance | SelfEmployedProfessional | Section 6(1) | Itsenäinen ammatinharjoittaja |
| Excluded | HealthcareProfessional (free, no org) | Section 6(2) | Vastikkeetta annettu hoito |

---

## 2. Compensable Patient Injury

| **OUTPUT: Compensable** | Injury Type | Condition | Legal Basis | Source Text |
|------------------------|-------------|-----------|-------------|-------------|
| Compensable | TreatmentInjury | Deviation from proper care | Section 23(1)(1) | Tutkimus tai hoito |
| Compensable | DeviceInjury | Device defect | Section 23(1)(2) | Laitteen vika |
| Compensable | ImplantInjury | Not as safe as expected | Section 23(1)(3) | Kehoon asennettu laite |
| Compensable | InfectionInjury | Patient shouldn't tolerate | Section 23(1)(4) | Infektio hoidon yhteydessä |
| Compensable | AccidentInjury | During treatment/transport | Section 23(1)(5) | Tapaturma |
| Compensable | FacilityInjury | Fire or damage | Section 23(1)(6) | Hoitohuoneiston palo |
| Compensable | MedicationInjury | Contrary to regulations | Section 23(1)(7) | Lääkkeen toimittaminen |
| Compensable | SevereConsequence | Unreasonable consequence | Section 23(1)(8) | Pysyvä vaikea sairaus |

---

## 3. Claim Time Limit

| **OUTPUT: Time Limit** | Knowledge Date | Event Date | Legal Basis | Source Text |
|-----------------------|----------------|------------|-------------|-------------|
| 3 years from knowledge | within 3 years | any | Section 31(1) | Tietää tai olisi pitänyt tietää |
| 10 years from event | any | within 10 years | Section 31(1) | 10 vuoden määräaika |
| Claim barred | after 3 years knowledge | over 10 years ago | Section 31(1) | Määräaika umpeutunut |

---

## 4. Compensation Type

| **OUTPUT: Compensation Type** | Injury Result | Legal Basis | Source Text |
|------------------------------|--------------|-------------|-------------|
| MedicalExpenseCompensation | Necessary care costs | Section 24 | Sairaanhoidon kustannukset |
| LostEarningsCompensation | Income loss | Section 24 | Ansiomenetys |
| PermanentInjuryCompensation | Permanent damage | Section 24 | Pysyvä haitta |
| PainAndSuffering | Pain and suffering | Section 24 | Kipu ja kärsimys |
| DeathCompensation | Death | Section 24 | Kuolema |
| VocationalRehabilitation | Work ability affected | Section 25 | Ammatillinen kuntoutus |
| RehabilitationAllowance | During rehabilitation | Section 27 | Kuntoutusajan korvaus |

---

## 5. Compensation Calculation

| **OUTPUT: Calculation** | Compensation Type | Method | Legal Basis | Source Text |
|------------------------|-------------------|--------|-------------|-------------|
| Per Tort Liability Act | Medical expenses | Chapter 5 | Section 24 | Vahingonkorvauslaki |
| Per Tort Liability Act | Lost earnings | Chapter 5 | Section 24 | Ansiomenetys |
| Per Tort Liability Act | Permanent injury | Chapter 5:2d | Section 24 | Pysyvä haitta |
| Lump sum option | Any | Special reason only | Section 24(3) | Erityisen painavasta syystä |
| Capital value | Continuous | Life expectancy + index | Section 24(4) | Pääoma-arvo |

---

## 6. Claim Processing Time

| **OUTPUT: Deadline** | Stage | Legal Basis | Source Text |
|----------------------|-------|-------------|-------------|
| Start investigation | 7 days from filing | Section 33(1) | 7 arkipäivän kuluessa |
| Decision | 3 months from complete claim | Section 33(2) | Kolmen kuukauden kuluessa |
| Undisputed portion | Immediate | Section 33(3) | Riidaton osa heti |

---

## 7. Late Payment Interest

| **OUTPUT: Interest Rate** | Situation | Legal Basis | Source Text |
|--------------------------|-----------|-------------|-------------|
| Interest Act 4a§ | Late compensation | Section 42 | Viivästyskorotus |
| Minimum 8€ | Below minimum not paid | Section 42(3) | Alle 8€ ei makseta |

---

## 8. Rehabilitation Eligibility

| **OUTPUT: Eligible** | Work Ability | Need | Legal Basis | Source Text |
|---------------------|--------------|------|-------------|-------------|
| Full rehabilitation | Affected | Yes | Section 25 | Työkyky heikentynyt |
| Vocational rehabilitation | May affect later | Probable | Section 25 | Voi myöhemmin heikentyä |
| Costs covered | Any level | Required | Section 26 | Kohtuulliset kustannukset |

---

## 9. Subrogation Rights

| **OUTPUT: Subrogation** | Party | Condition | Legal Basis | Source Text |
|------------------------|-------|-----------|-------------|-------------|
| Centre recovers from wrongdoer | Any | Compensation paid | Section 45 | Takautumisoikeus |
| Centre recovers from other insurer | Other system | Coordination | Section 46 | Yhteensovitus |
| Insurer recovers from Centre | Work/Traffic insurance | Duplicate payment | Section 47 | Vakuutuslaitoksen oikeus |

---

## 10. Appeal Process

| **OUTPUT: Appeal Path** | Decision Type | Legal Basis | Source Text |
|------------------------|---------------|-------------|-------------|
| Request Board recommendation | Within 1 year | Section 38 | Ratkaisusuositus |
| Court if no Board | After Board | Section 41 | Tuomioistuin |
| Mandatory Board consultation | Permanent disability/death | Section 40 | Pakollinen kuuleminen |

---

## Legal Reference Summary

| Section | Topic |
|---------|-------|
| Sections 1-5 | General Provisions |
| Sections 6-21 | Insurance Obligation |
| Sections 22-30 | Compensation |
| Sections 31-47 | Procedure |
| Sections 48-51 | Distribution System |
| Sections 52-66 | Miscellaneous |
| Sections 67-70 | Entry into Force |

---

## JSON Format

See `patient_insurance_dmn_rules.json` for machine-readable DMN format.
