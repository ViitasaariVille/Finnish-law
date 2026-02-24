# Finnish Traffic Insurance - DMN Business Rules

**Based on:** Liikennevakuutuslaki (Traffic Insurance Act) 460/2016  
**Version:** 1.1  
**DMN Version:** 1.3  
**Source:** https://www.finlex.fi/fi/lainsaadanto/2016/460  
**Note:** Original `business_rules_verified.json` preserved

---

## 1. Mandatory Insurance Requirement

**Legal Source:** Section 5

| **OUTPUT: Insurance Required** | Vehicle Location | Requires Insurance | Vehicle Type | Legal Basis | Source Text |
|-------------------------------|------------------|-------------------|--------------|-------------|-------------|
| MandatoryTrafficInsurance | FI | true | MotorVehicle | Section 5(1) | Liikenteeseen käytettäväksi tarkoitettu ajoneuvo |
| MandatoryTrafficInsurance | FI | true | Trailer | Section 5(1) | Perävaunu |
| Check registration country | EEA | true | any | Section 6a | EEA-maasta tuotu ajoneuvo |
| MandatoryTrafficInsurance | Non-EEA | true | any | Section 5(1) | Kolmannesta maasta tuotu |

---

## 2. Insurance Obligation Liable Party

**Legal Source:** Section 6

| **OUTPUT: Liable Party** | Owner | Holder | Ownership Transferred | Legal Basis | Source Text |
|--------------------------|-------|--------|----------------------|-------------|-------------|
| Owner and Holder jointly liable | exists | exists | true | Section 6(1) | Omistaja ja haltija yhteisvastuussa |
| Owner liable | exists | null | true | Section 6(1) | Omistaja vastaa |
| Holder liable | null | exists | true | Section 6(1) | Haltija vastaa |
| Owner liable from ownership | exists | null | false | Section 6(2) | Omistus siirtyy |

---

## 3. Coverage Compensation

**Legal Source:** Sections 12-16

| **OUTPUT: Coverage** | Damage Type | Personal Injury | Property Damage | Legal Basis | Source Text |
|---------------------|-------------|----------------|-----------------|-------------|-------------|
| 100% covered | PersonalInjury | true | false | Section 12(1) | Henkilövahinko |
| 100% covered | PersonalInjury | true | true | Section 12(1) | Henkilö- ja esinevahinko |
| 100% covered | PropertyDamage | false | true | Section 12(1) | Esinevahinko |
| 100% covered | VehicleDamage | false | true | Section 12(1) | Ajoneuvovahinko |
| 100% covered | EnvironmentalDamage | false | true | Section 12(2) | Ympäristövahinko |

---

## 4. Exclusions

**Legal Source:** Sections 17-21

| **OUTPUT: Excluded** | Driver Intent | Drunkenness | Vehicle Purpose | Location | Legal Basis | Source Text |
|----------------------|---------------|-------------|-----------------|----------|-------------|-------------|
| Excluded - Intentional damage | Intentional | any | any | any | Section 17(1) | Tahallinen vahinko |
| Excluded - Drunken driving | any | intoxicated | any | any | Section 18(1) | Humalassa ajaminen |
| Excluded - Racing | any | any | Race | any | Section 19(1) | Kilpaileminen |
| Excluded - Stunt driving | any | any | Stunt | any | Section 19(2) | Temppujen ajaminen |
| May be excluded | any | any | any | PrivateArea | Section 20 | Yksityisalue |

---

## 5. Medical Expense Coverage

**Legal Source:** Section 5

| **OUTPUT: Coverage %** | Injury Type | Treatment Necessity | Provider | Legal Basis | Source Text |
|------------------------|-------------|---------------------|----------|-------------|-------------|
| 100% | Emergency | required | public | Section 5a | Ensiavun hoitokustannukset |
| 100% (reimbursement) | Emergency | required | private | Section 5a | Yksityisen ensiavun kustannukset |
| 100% | Surgery | required | any | Section 5a | Leikkaushoito |
| 100% | Medicines | prescribed | pharmacy | Section 5b | Lääkkeet |
| 100% | Rehabilitation | required | any | Section 5c | Kuntoutus |
| 100% | Dental | accident_related | any | Section 5e | Hammasvamman hoito |
| 100% | Prosthesis | required | any | Section 5f | Proteesi |

---

## 6. Lost Wages Compensation

**Legal Source:** Section 4

| **OUTPUT: Compensation** | Income Type | Income Amount | Work Ability Lost Days | Legal Basis | Source Text |
|--------------------------|-------------|---------------|----------------------|-------------|-------------|
| net_monthly / 30 * days | Employed | net_monthly | any | Section 4(1) | Työansion menetys |
| annual / 365 * days | SelfEmployed | annual | any | Section 4(2) | Yrittäjän ansionmenetys |
| Minimum 36.90/day | Unemployed | any | any | Section 4(3) | Työttömän ansionmenetys |
| Student grant adjustment | Student | any | any | Section 4(4) | Opiskelijan ansionmenetys |

---

## 7. Pain and Suffering Compensation

**Legal Source:** Section 5

| **OUTPUT: Compensation** | Permanent | Percentage | Pain Level | Legal Basis | Source Text |
|-------------------------|-----------|------------|------------|-------------|-------------|
| Section 5(2) scale | true | 1-10% | moderate | Section 5(2) | Pysyvä haitta 1-10% |
| Section 5(2) scale | true | 11-20% | moderate | Section 5(2) | Pysyvä haitta 11-20% |
| Section 5(2) scale | true | 21-50% | significant | Section 5(2) | Pysyvä haitta 21-50% |
| Section 5(2) scale | true | 51-100% | severe | Section 5(2) | Pysyvä haitta 51-100% |
| Temporary pain - scale | false | any | any | Section 5(1) | Tilapäinen kipu |

---

## 8. Death Compensation

**Legal Source:** Sections 7-8

| **OUTPUT: Compensation** | Deceased Income | Survivor Relationship | Dependent | Legal Basis | Source Text |
|-------------------------|-----------------|----------------------|-----------|-------------|-------------|
| Spouse pension + lump sum | exists | Spouse | true | Section 7(1) | Leskeneläke |
| Child pension | exists | Child | true | Section 7(2) | Lapseneläke |
| Lump sum | none | Dependent | true | Section 8 | Kertakorvaus |
| Funeral expenses + compensation | any | Parent | true | Section 8 | Vanhemmille korvaus |

---

## 9. Property Damage Compensation

**Legal Source:** Section 3

| **OUTPUT: Compensation** | Property Type | Property Value | Damage Severity | Legal Basis | Source Text |
|-------------------------|---------------|----------------|----------------|-------------|-------------|
| Market value | Vehicle | market_value | TotalLoss | Section 3(1) | Ajoneuvon täysarvo |
| Repair cost | Vehicle | market_value | Partial | Section 3(1) | Korjauskustannukset |
| Actual value | Property | any | any | Section 3(1) | Esinevahinko |
| Replacement value | Clothing | any | any | Section 3(2) | Vaatevahinko |

---

## 10. Claim Time Limit

**Legal Source:** Section 74

| **OUTPUT: Time Limit** | Claim Type | Accident Date | Legal Basis | Source Text |
|------------------------|------------|---------------|-------------|-------------|
| 3 years from injury | PersonalInjury | any | Section 74(1) | Henkilövahinko 3 vuotta |
| 1 year from accident | PropertyDamage | within_1_year | Section 74(2) | Esinevahinko 1 vuosi |
| Claim barred | PropertyDamage | after_1_year | Section 74(2) | Määräaika umpeutunut |

---

## 11. Premium Calculation

**Legal Source:** Sections 89-92

| **OUTPUT: Premium** | Vehicle Type | Driver Age | Claims History | Usage Purpose | Legal Basis | Source Text |
|--------------------|--------------|------------|---------------|--------------|-------------|-------------|
| Base premium | PrivateCar | over_25 | no_claims | Private | Section 89 | Perusvakuutusmaksu |
| Base premium * 1.5 | PrivateCar | under_25 | no_claims | Private | Section 90 | Nuori kuljettaja |
| Base premium + claim loading | PrivateCar | any | with_claims | any | Section 91 | Korotusmaksu |
| Commercial rate | Commercial | any | any | any | Section 92 | Kaupallinen ajoneuvo |

---

## 12. International Coverage

**Legal Source:** Sections 10-11

| **OUTPUT: Coverage** | Accident Country | Green Card Valid | Vehicle Registered | Legal Basis | Source Text |
|---------------------|-----------------|------------------|-------------------|-------------|-------------|
| Full coverage | Finland | any | FI | Section 10(1) | Suomessa |
| Full coverage - Green Card | EEA | true | any | Section 10(2) | Eta-maassa vihreällä kortilla |
| Limited - Bureau guarantee | EEA | false | any | Section 10(3) | Kansainvälinen sopimus |
| Check bilateral agreement | Non-EEA | any | any | Section 11 | Kolmannet maat |

---

## 13. Insolvency Protection

**Legal Source:** Section 77

| **OUTPUT: Protection** | Insurer Status | Policy Active | Claim Pending | Legal Basis | Source Text |
|----------------------|----------------|---------------|---------------|-------------|-------------|
| Finnish Guarantee Fund pays | Insolvent | true | true | Section 77(1) | Suomen vakuutusrahasto |
| Transfer to another insurer | Insolvent | true | false | Section 77(2) | Siirto toiselle vakuuttajalle |
| Normal claims process | Healthy | true | true | Section 76 | Normaali käsittely |

---

## Legal Reference Summary

| Section | Topic |
|---------|-------|
| Section 3 | Property damage compensation |
| Section 4 | Lost wages compensation |
| Section 5 | Medical expenses + pain & suffering |
| Section 5a-5f | Specific medical coverage types |
| Section 6 | Insurance obligation |
| Section 6a | EEA vehicle insurance choice |
| Sections 7-8 | Death compensation |
| Sections 10-11 | International coverage |
| Sections 12-16 | Coverage |
| Sections 17-21 | Exclusions |
| Section 74 | Claim time limits |
| Sections 76-77 | Claims handling + insolvency |
| Sections 89-92 | Premium calculation |

---

## JSON Format (Machine-Readable)

See `car_insurance_dmn_rules.json` for DMN-compatible JSON format.
