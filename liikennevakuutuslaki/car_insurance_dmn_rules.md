# Finnish Traffic Insurance - DMN Business Rules

**Based on:** Liikennevakuutuslaki (Traffic Insurance Act) 460/2016  
**Version:** 1.0  
**DMN Version:** 1.3  
**Source:** https://www.finlex.fi/fi/lainsaadanto/2016/460  
**Note:** Original `business_rules_verified.json` preserved

---

## 1. Mandatory Insurance Requirement

**Legal Source:** Section 5

| Vehicle Location | Requires Insurance | Vehicle Type | **Insurance Required** | Legal Basis | Source Text |
|------------------|-------------------|--------------|-------------------|-------------|-------------|
| FI | true | MotorVehicle | MandatoryTrafficInsurance | Section 5(1) | Liikenteeseen käytettäväksi tarkoitettu ajoneuvo |
| FI | true | Trailer | MandatoryTrafficInsurance | Section 5(1) | Perävaunu |
| EEA | true | any | Check registration country | Section 6a | EEA-maasta tuotu ajoneuvo |
| Non-EEA | true | any | MandatoryTrafficInsurance | Section 5(1) | Kolmannesta maasta tuotu |

---

## 2. Insurance Obligation Liable Party

**Legal Source:** Section 6

| Owner | Holder | Ownership Transferred | **Liable Party** | Legal Basis | Source Text |
|-------|--------|----------------------|--------------|-------------|-------------|
| exists | exists | true | Owner and Holder jointly liable | Section 6(1) | Omistaja ja haltija yhteisvastuussa |
| exists | null | true | Owner liable | Section 6(1) | Omistaja vastaa |
| null | exists | true | Holder liable | Section 6(1) | Haltija vastaa |
| exists | null | false | Owner liable from ownership | Section 6(2) | Omistus siirtyy |

---

## 3. Coverage Compensation

**Legal Source:** Sections 12-16

| Damage Type | Personal Injury | Property Damage | **Coverage** | Legal Basis | Source Text |
|-------------|----------------|-----------------|----------|-------------|-------------|
| PersonalInjury | true | false | 100% covered | Section 12(1) | Henkilövahinko |
| PersonalInjury | true | true | 100% covered | Section 12(1) | Henkilö- ja esinevahinko |
| PropertyDamage | false | true | 100% covered | Section 12(1) | Esinevahinko |
| VehicleDamage | false | true | 100% covered | Section 12(1) | Ajoneuvovahinko |
| EnvironmentalDamage | false | true | 100% covered | Section 12(2) | Ympäristövahinko |

---

## 4. Exclusions

**Legal Source:** Sections 17-21

| Driver Intent | Drunkenness | Vehicle Purpose | Location | **Excluded** | Legal Basis | Source Text |
|---------------|-------------|-----------------|----------|----------|-------------|-------------|
| Intentional | any | any | any | Excluded - Intentional damage | Section 17(1) | Tahallinen vahinko |
| any | intoxicated | any | any | Excluded - Drunken driving | Section 18(1) | Humalassa ajaminen |
| any | any | Race | any | Excluded - Racing | Section 19(1) | Kilpaileminen |
| any | any | Stunt | any | Excluded - Stunt driving | Section 19(2) | Temppujen ajaminen |
| any | any | any | PrivateArea | May be excluded | Section 20 | Yksityisalue |

---

## 5. Medical Expense Coverage

**Legal Source:** Section 5

| Injury Type | Treatment Necessity | Provider | Coverage % | Legal Basis | Source Text |
|-------------|---------------------|----------|------------|-------------|-------------|
| Emergency | required | public | 100% | Section 5a | Ensiavun hoitokustannukset |
| Emergency | required | private | 100% (reimbursement) | Section 5a | Yksityisen ensiavun kustannukset |
| Surgery | required | any | 100% | Section 5a | Leikkaushoito |
| Medicines | prescribed | pharmacy | 100% | Section 5b | Lääkkeet |
| Rehabilitation | required | any | 100% | Section 5c | Kuntoutus |
| Dental | accident_related | any | 100% | Section 5e | Hammasvamman hoito |
| Prosthesis | required | any | 100% | Section 5f | Proteesi |

---

## 6. Lost Wages Compensation

**Legal Source:** Section 4

| Income Type | Income Amount | Work Ability Lost Days | Compensation | Legal Basis | Source Text |
|-------------|---------------|----------------------|--------------|-------------|-------------|
| Employed | net_monthly | any | net_monthly / 30 * days | Section 4(1) | Työansion menetys |
| SelfEmployed | annual | any | annual / 365 * days | Section 4(2) | Yrittäjän ansionmenetys |
| Unemployed | any | any | Minimum 36.90/day | Section 4(3) | Työttömän ansionmenetys |
| Student | any | any | Student grant adjustment | Section 4(4) | Opiskelijan ansionmenetys |

---

## 7. Pain and Suffering Compensation

**Legal Source:** Section 5

| Permanent | Percentage | Pain Level | Compensation | Legal Basis | Source Text |
|-----------|------------|------------|--------------|-------------|-------------|
| true | 1-10% | moderate | Section 5(2) scale | Section 5(2) | Pysyvä haitta 1-10% |
| true | 11-20% | moderate | Section 5(2) scale | Section 5(2) | Pysyvä haitta 11-20% |
| true | 21-50% | significant | Section 5(2) scale | Section 5(2) | Pysyvä haitta 21-50% |
| true | 51-100% | severe | Section 5(2) scale | Section 5(2) | Pysyvä haitta 51-100% |
| false | any | any | Temporary pain - scale | Section 5(1) | Tilapäinen kipu |

---

## 8. Death Compensation

**Legal Source:** Sections 7-8

| Deceased Income | Survivor Relationship | Dependent | Compensation | Legal Basis | Source Text |
|-----------------|----------------------|-----------|--------------|-------------|-------------|
| exists | Spouse | true | Spouse pension + lump sum | Section 7(1) | Leskeneläke |
| exists | Child | true | Child pension | Section 7(2) | Lapseneläke |
| none | Dependent | true | Lump sum | Section 8 | Kertakorvaus |
| any | Parent | true | Funeral expenses + compensation | Section 8 | Vanhemmille korvaus |

---

## 9. Property Damage Compensation

**Legal Source:** Section 3

| Property Type | Property Value | Damage Severity | Compensation | Legal Basis | Source Text |
|---------------|----------------|-----------------|--------------|-------------|-------------|
| Vehicle | market_value | TotalLoss | Market value | Section 3(1) | Ajoneuvon täysarvo |
| Vehicle | market_value | Partial | Repair cost | Section 3(1) | Korjauskustannukset |
| Property | any | any | Actual value | Section 3(1) | Esinevahinko |
| Clothing | any | any | Replacement value | Section 3(2) | Vaatevahinko |

---

## 10. Claim Time Limit

**Legal Source:** Section 74

| Claim Type | Accident Date | Time Limit | Legal Basis | Source Text |
|------------|---------------|------------|-------------|-------------|
| PersonalInjury | any | 3 years from injury | Section 74(1) | Henkilövahinko 3 vuotta |
| PropertyDamage | within_1_year | 1 year from accident | Section 74(2) | Esinevahinko 1 vuosi |
| PropertyDamage | after_1_year | Claim barred | Section 74(2) | Määraika umpeutunut |

---

## 11. Premium Calculation

**Legal Source:** Sections 89-92

| Vehicle Type | Driver Age | Claims History | Usage Purpose | Premium | Legal Basis | Source Text |
|--------------|------------|---------------|--------------|---------|-------------|-------------|
| PrivateCar | over_25 | no_claims | Private | Base premium | Section 89 | Perusvakuutusmaksu |
| PrivateCar | under_25 | no_claims | Private | Base premium * 1.5 | Section 90 | Nuori kuljettaja |
| PrivateCar | any | with_claims | any | Base premium + claim loading | Section 91 | Korotusmaksu |
| Commercial | any | any | any | Commercial rate | Section 92 | Kaupallinen ajoneuvo |

---

## 12. International Coverage

**Legal Source:** Sections 10-11

| Accident Country | Green Card Valid | Vehicle Registered | **Coverage** | Legal Basis | Source Text |
|-----------------|------------------|-------------------|----------|-------------|-------------|
| Finland | any | FI | Full coverage | Section 10(1) | Suomessa |
| EEA | true | any | Full coverage - Green Card | Section 10(2) | Eta-maassa vihreällä kortilla |
| EEA | false | any | Limited - Bureau guarantee | Section 10(3) | Kansainvälinen sopimus |
| Non-EEA | any | any | Check bilateral agreement | Section 11 | Kolmannet maat |

---

## 13. Insolvency Protection

**Legal Source:** Section 77

| Insurer Status | Policy Active | Claim Pending | Protection | Legal Basis | Source Text |
|----------------|---------------|--------------|------------|-------------|-------------|
| Insolvent | true | true | Finnish Guarantee Fund pays | Section 77(1) | Suomen vakuutusrahasto |
| Insolvent | true | false | Transfer to another insurer | Section 77(2) | Siirto toiselle vakuuttajalle |
| Healthy | true | true | Normal claims process | Section 76 | Normaali käsittely |

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
| Sections 12-16 | **Coverage** |
| Sections 17-21 | Exclusions |
| Section 74 | Claim time limits |
| Sections 76-77 | Claims handling + insolvency |
| Sections 89-92 | Premium calculation |

---

## JSON Format (Machine-Readable)

See `car_insurance_dmn_rules.json` for DMN-compatible JSON format.
