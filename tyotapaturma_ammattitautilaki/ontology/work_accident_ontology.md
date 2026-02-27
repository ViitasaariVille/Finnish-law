# Finnish Work Accident and Occupational Disease Insurance Ontology

## Overview

| Property | Value |
|----------|-------|
| **Name** | Finnish Work Accident and Occupational Disease Insurance Ontology |
| **Version** | 1.0 |
| **Based On** | Työtapaturma- ja ammattitautilaki (459/2015) |
| **Language** | English |
| **Effective Date** | 2016-01-01 |
| **Source** | https://www.finlex.fi/fi/laki/alkup/2015/20150459 |

---

## 1. Person Entities

### Employee
- **Description**: Person working in employment relationship under employment contract, public service, or similar
- **Legal Basis**: Section 8

### Entrepreneur  
- **Description**: Self-employed person with YEL insurance
- **Legal Basis**: Sections 188-190

### InjuredParty
- **Description**: Person who suffered a work accident or occupational disease
- **Attributes**: injuryDate, injuryType, severity, medicalFindings

### Survivor
- **Description**: Family member entitled to benefits after death
- **Subclasses**: Widow, Child, Dependent

### Employer
- **Description**: Entity with mandatory insurance obligation
- **Attributes**: businessId, companyName, annualPayroll

---

## 2. Insurance Types

### MandatoryInsurance
- **Description**: Compulsory insurance that employers must obtain
- **Legal Basis**: Section 3
- **Applies to**: Private employers with annual payroll > €1,200
- **Exemptions** (§3(2)-(3)):
  - Employers with annual payroll ≤ €1,200 (no insurance obligation)
  - State employers (compensation paid from state funds via Valtiokonttori)

### VoluntaryWorkTimeInsurance
- **Description**: Voluntary insurance for entrepreneurs covering work hours
- **Legal Basis**: Sections 188-198
- **Eligibility**: Entrepreneur with YEL insurance

### VoluntaryFreeTimeInsurance
- **Description**: Voluntary insurance for leisure time accidents
- **Legal Basis**: Sections 199-203

---

## 3. Insurable Events

### OccupationalAccident
- **Legal Basis**: Sections 17-25
- **Subclasses**:
  - WorkplaceAccident
  - CommuteAccident  
  - BusinessTripAccident
  - WorkRelatedActivityAccident

### OccupationalDisease
- **Legal Basis**: Sections 26-32
- **Attributes**: diseaseCode, exposureDuration, latencyPeriod

### RepetitiveStrainInjury
- **Legal Basis**: Section 33
- **Note**: Maximum 6 weeks compensation

### ViolenceDamage
- **Legal Basis**: Section 34
- **Condition**: Must be related to work duties

### PsychologicalShock
- **Legal Basis**: Section 35
- **Subclasses**: AcuteStressReaction, PTSD, PersonalityChange
- **Requirements for PTSD/PersonalityChange** (§35(2)): Diagnosis within 6 months of the event
- **Direct involvement** (§35(3)): Must be directly involved in the event
- **Activity exclusions** (§35(4)): Not compensated during commute breaks (§23(2)), recreation (§24(1)(2)), medical visits (§24(1)(4-5)), or fitness during work time (§24(1)(6)), unless §34 intentional harm

---

## 4. Compensation Types

### MedicalCareCompensation
- **Legal Basis**: Sections 36-49
- **Subclasses**: PublicHealthcare, PrivateHealthcare, ForeignHealthcare, Medicine

### DailyAllowance
- **Legal Basis**: Sections 56-62
- **First 28 days**: At sick pay level (employer pays) - §58
- **Day 29 to 1 year**: Based on annual earnings (vuosityöansio) - §§56, 59
- **Duration**: Maximum 1 year from accident date - §56(1)
- **After 1 year**: Converts to DisabilityPension (Tapaturmaeläke) - §63
- **Requirements**: Work capacity reduced by at least 10% (§56(2)), minimum 3 consecutive days inability (§56(3))

### DisabilityPension
- **Legal Basis**: Sections 63-68
- **Requirement**: Minimum 10% work capacity reduction

### RehabilitationAllowance
- **Legal Basis**: Sections 69, 88-98

### PermanentDamageCompensation
- **Legal Basis**: Sections 83-87
- **Base Amount**: €12,440 per year (§86)
- **Classes**: 1-20 based on severity
- **Combination Formula** (§84(4)): For multiple injuries: K = A + B - (A×B)/20, where K=total class, A=larger, B=smaller. Combine largest first, then repeat.
- **Formula Exceptions** (§84(5)): Does not apply to paired organs (eyes, kidneys) or combined vision+hearing loss
- **Payment Method** (§87(1)): Classes 1-5 lump sum (kertakaikkinen), Classes 6-20 continuous annual payments (jatkuva)
- **Rates** (§86): 1.15% to 60% of base depending on class

### DeathCompensation
- **Legal Basis**: Sections 99-109
- **Includes**: SurvivorsPension, FuneralExpenses

---

## 5. Key Relationships

| Subject | Predicate | Object | Condition |
|---------|-----------|--------|-----------|
| Employee | has_right_to | Compensation | When suffering occupational accident |
| Employer | must_obtain | MandatoryInsurance | For all employees |
| InsuranceCompany | must_pay | Compensation | When insured event occurs |
| InjuredParty | must_file_claim_within | 5 years | From accident date (§116) |
| InjuredParty | must_file_claim_within | From doctor assessment | Occupational disease only (§116) |
| InjuredParty | may_file_claim_after_deadline | If justified | When delay not claimant's fault (§116) |
| Survivor | has_right_to | DeathCompensation | When injured party dies |

---

## 5b. Procedural Rules (Sections 117-121)

### Parties to Proceedings (§117)
- **Parties**: Injured party (vahingoittunut) and survivors (edunsaajat)
- **Not parties**: Employer, healthcare provider, municipality

### Right to be Heard (§118)
- Close relative or caregiver can represent injured party if unable
- Until guardian (edunvalvoja) is appointed

### Investigation Procedures (§119)
- Must start investigation within 7 business days
- Must inform claimant of 1-year deadline

### Vocational Rehabilitation Assessment (§120)
- Must assess need within 3 months of disability start
- Review every 3 months thereafter

### Medical Expert Involvement (§121)
- Licensed physician must participate in medical assessments
- Must document findings in records

---

## 6. Institutions

### InsuranceCompany
- **Legal Basis**: Section 205
- Authorized to provide insurance

### StateTreasury (Valtiokonttori)
- **Legal Basis**: Section 207
- Pays compensation for state employees

### AccidentInsuranceCentre (Tapaturmavakuutuskeskus)
- **Legal Basis**: Sections 209-225
- Central coordinating organization

### ClaimAppealBoard (Tapaturma-asiain korvauslautakunta)
- **Legal Basis**: Sections 226-228
- Dispute resolution

---

## 7. Key Dates

- **Effective Date**: 2016-01-01
- **Replaced Laws**:
  - Tapaturmavakuutuslaki (608/1948)
  - Ammattitautilaki (1343/1988)
  - Tapaturmavakuutuslain mukainen kuntoutuslaki (625/1991)
  - Valtion virkamiesten tapaturmakorvaukset (449/1990)

---

## 8. Coverage

- **Geographical**: Finland primarily, extended to EU/agreement countries
- **Personal Scope**: Employees, entrepreneurs (voluntary), certain other groups
