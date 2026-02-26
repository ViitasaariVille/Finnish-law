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

---

## 4. Compensation Types

### MedicalCareCompensation
- **Legal Basis**: Sections 36-49
- **Subclasses**: PublicHealthcare, PrivateHealthcare, ForeignHealthcare, Medicine

### DailyAllowance
- **Legal Basis**: Sections 56-62
- **Maximum Duration**: 1 year from accident date

### DisabilityPension
- **Legal Basis**: Sections 63-68
- **Requirement**: Minimum 10% work capacity reduction

### RehabilitationAllowance
- **Legal Basis**: Sections 69, 88-98

### PermanentDamageCompensation
- **Legal Basis**: Sections 83-87
- **Classes**: 1-20 based on severity

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
| InjuredParty | must_file_claim_within | 5 years | From accident/disease date |
| Survivor | has_right_to | DeathCompensation | When injured party dies |

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
