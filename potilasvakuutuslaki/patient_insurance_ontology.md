# Finnish Patient Insurance Ontology

**Based on:** Potilasvakuutuslaki (Patient Insurance Act) 948/2019  
**Version:** 1.0  
**Effective:** 2021-01-01  
**Source:** https://www.finlex.fi/fi/laki/alkup/2019/20190948

---

## Overview

This ontology represents the Finnish Patient Insurance system, which provides compensation for patient injuries that occur during healthcare treatment.

---

## 1. Person

### Patient
- **Description:** Person receiving healthcare services
- **Legal Basis:** Section 2
- **Attributes:**
  - patientId
  - treatmentDate
  - healthcareProvider

### HealthcareProfessional
- **Description:** Doctor, nurse, or other healthcare provider
- **Legal Basis:** Section 2
- **Attributes:**
  - licenseNumber
  - specialty
  - employer

### InjuredParty
- **Description:** Patient who suffered injury due to healthcare
- **Attributes:**
  - injuryDate
  - injuryType
  - severity
  - causation

---

## 2. HealthcareProvider

### PublicHealthcare
- **Description:** Public hospital or health center
- **Legal Basis:** Section 5
- **Subclasses:**
  - Hospital
  - HealthCenter
  - MunicipalHealthService

### PrivateHealthcare
- **Description:** Private clinic or practice
- **Legal Basis:** Section 5
- **Subclasses:**
  - PrivateClinic
  - PrivateHospital
  - DentalClinic

### SocialServices
- **Description:** Social and welfare services
- **Legal Basis:** Section 4

---

## 3. Insurance

### MandatoryPatientInsurance
- **Description:** Compulsory patient insurance for healthcare providers
- **Legal Basis:** Section 5
- **Attributes:**
  - coverageType
  - minimumCoverage

---

## 4. PatientInjury (Section 2-3)

### TreatmentInjury
- **Description:** Injury caused by examination, treatment, or care
- **Legal Basis:** Section 3

### InfectionInjury
- **Description:** Healthcare-associated infection
- **Legal Basis:** Section 3(1)

### DeviceInjury
- **Description:** Injury caused by medical device
- **Legal Basis:** Section 3(1)

### MedicationInjury
- **Description:** Injury from medication error
- **Legal Basis:** Section 3(1)

### DiagnosticInjury
- **Description:** Injury from delayed or missed diagnosis
- **Legal Basis:** Section 3(2)

---

## 5. Compensation (Sections 7-9)

### MedicalExpenseCompensation
- **Description:** Costs of medical care for injury
- **Legal Basis:** Section 7(1)
- **Subclasses:**
  - TreatmentCost
  - MedicineCost
  - TravelCost
  - RehabilitationCost
  - EquipmentCost

### LostEarningsCompensation
- **Description:** Loss of income due to injury
- **Legal Basis:** Section 7(2)

### PermanentInjuryCompensation
- **Description:** Compensation for permanent injury
- **Legal Basis:** Section 8

### PainAndSuffering
- **Description:** Compensation for pain and suffering
- **Legal Basis:** Section 9

### DeathCompensation
- **Description:** Compensation in case of patient death
- **Legal Basis:** Section 9a

---

## 6. Claim (Sections 16-23)

### InitialClaim
- **Description:** First claim submission
- **Legal Basis:** Section 16

### Appeal
- **Description:** Appeal of claim decision
- **Legal Basis:** Section 24

---

## 7. Investigation (Sections 11-15)

### MedicalInvestigation
- **Description:** Medical expert assessment
- **Legal Basis:** Section 12

### CausationAssessment
- **Description:** Assessment of causation between care and injury
- **Legal Basis:** Section 13

---

## Relationships

| From | To | Type |
|------|-----|------|
| Patient | HealthcareProvider | receives_care_from |
| HealthcareProvider | MandatoryPatientInsurance | must_have |
| PatientInjury | Patient | suffers |
| PatientInjury | HealthcareProvider | occurs_at |
| Compensation | PatientInjury | compensates |
| Claim | PatientInjury | filed_for |
| Investigation | PatientInjury | investigates |

---

## Business Rules

### Rule 1: Healthcare Provider Insurance Obligation
- **Condition:** healthcareProvider.type IN [PublicHealthcare, PrivateHealthcare, SocialServices]
- **Conclusion:** healthcareProvider.mustHave = MandatoryPatientInsurance
- **Legal Basis:** Section 5(1)

### Rule 2: Compensable Injury
- **Condition:** patientInjury.type IN [TreatmentInjury, InfectionInjury, DeviceInjury, MedicationInjury, DiagnosticInjury] AND patientInjury.causation = probable
- **Conclusion:** patientInjury.compensable = true
- **Legal Basis:** Section 3

### Rule 3: Claim Time Limit
- **Condition:** patientInjury.eventDate > 3 years ago
- **Conclusion:** claim.timeLimit = expired
- **Legal Basis:** Section 16(2)

---

## Law Structure Summary

| Part | Sections | Topic |
|------|----------|-------|
| 1 | 1-3 | Purpose, Definitions, Scope |
| 2 | 4-10 | Insurance, Compensation |
| 3 | 11-15 | Investigation |
| 4 | 16-24 | Claims, Appeals |

---

## JSON Format

See `patient_insurance_ontology.json` for machine-readable format.
