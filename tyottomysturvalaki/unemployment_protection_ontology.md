# Finnish Unemployment Protection Act - Ontology

**Based on:** Työttömyysturvalaki (Unemployment Protection Act) 1290/2002  
**Version:** 1.0  
**Source:** https://www.finlex.fi/fi/lainsaadanto/2002/1290

---

## 1. Core Entities

### UnemploymentBenefit (Työttömyysetuus)
- **Description:** Unemployment benefit or allowance
- **Legal Basis:** Sections 1-2
- **Subclasses:**
  - **UnemploymentDailyAllowance (Työttömyyspäiväraha):** Daily unemployment allowance
  - **EarningsRelatedAllowance (Ansiopäiväraha):** Earnings-related daily allowance (§5-6)
  - **BasicAllowance (Peruspäiväraha):** Basic daily allowance (§7)
  - **LabourMarketSupport (Työmarkkinatuki):** Labour market support (Part III, Chapter 7)

### UnemployedPerson (Työtön)
- **Description:** Unemployed person seeking work
- **Legal Basis:** Chapter 2.1

### JobSeeker (Työnhakija)
- **Description:** Job seeker registered with TE services
- **Legal Basis:** Section 2.1

### Employee (Palkansaaja)
- **Description:** Employee
- **Legal Basis:** Section 5.2

### Entrepreneur (Yrittäjä)
- **Description:** Self-employed person
- **Legal Basis:** Section 1.6

---

## 2. Benefit-Related Entities

### EmploymentCondition (Työssäoloehto)
- **Description:** Employment requirement for benefit
- **Legal Basis:** Section 5.3

### InsurancePeriod (Vakuutuskausi)
- **Description:** Insurance period
- **Legal Basis:** Section 5.5

### BenefitApplication (Etuushakemus)
- **Description:** Application for benefit
- **Legal Basis:** Section 11.1

### BenefitDecision (Etuuspäätös)
- **Description:** Benefit decision
- **Legal Basis:** Section 11.3

### BenefitAmount (Etuuden määrä)
- **Description:** Amount of benefit
- **Legal Basis:** Section 6

### BenefitDuration (Etuuden kesto)
- **Description:** Duration of benefit
- **Legal Basis:** Section 6.7

### DisregardPeriod (Omavastuuaika)
- **Description:** Waiting period before benefit
- **Legal Basis:** Section 5.13

### IncomeRelatedComponent (Ansiopäivärahan ansio-osa)
- **Description:** Earnings-related component
- **Legal Basis:** Section 6.2

### BasicComponent (Perusosa)
- **Description:** Basic component of benefit
- **Legal Basis:** Section 6.1

### AdditionalDays (Lisäpäiväoikeus)
- **Description:** Additional days for older workers
- **Legal Basis:** Section 6.9

---

## 3. Adjustment Entities

### AdjustedBenefit (Soviteltu etuus)
- **Description:** Adjusted/reduced benefit
- **Legal Basis:** Chapter 4

### LabourMarketPolicy (Työvoimapoliittinen)
- **Description:** Labour market policy conditions
- **Legal Basis:** Chapter 2

---

## 4. Support Entities

### MobilitySupport (Liikkuvuusavustus)
- **Description:** Mobility support
- **Legal Basis:** Part III, Chapter 8

### RedundancyPay (Muutosturvaraha)
- **Description:** Redundancy payment
- **Legal Basis:** Part III, Chapter 9

### EmploymentService (Työllistymistä edistävä palvelu)
- **Description:** Employment promoting service
- **Legal Basis:** Part IV, Chapter 10

---

## 5. Requirement Entities

### JobSearchRequirement (Työnhak_velvollisuus)
- **Description:** Job search requirement
- **Legal Basis:** Section 2a.1

### AcceptableReason (Pätevä syy)
- **Description:** Acceptable reason for refusing work
- **Legal Basis:** Section 2a.2

### BenefitRestriction (Etuuden rajoitus)
- **Description:** Restriction of benefit
- **Legal Basis:** Chapter 3

---

## 6. Administrative Entities

### Recovery (Takaisinperintä)
- **Description:** Recovery of overpaid benefit
- **Legal Basis:** Section 11.10

### Appeal (Muutoksenhaku)
- **Description:** Right to appeal
- **Legal Basis:** Chapter 12

---

## 7. Person Entities

### Employer (Työnantaja)
- **Description:** Employer
- **Legal Basis:** Section 1

### UnemploymentFund (Työttömyyskassa)
- **Description:** Unemployment fund
- **Legal Basis:** Section 1.4

### SelfEmployedWorker (Itsenäinen ammatinharjoittaja)
- **Description:** Self-employed worker
- **Legal Basis:** Section 1.6

### FamilyMember (Perheenjäsen)
- **Description:** Family member working in enterprise
- **Legal Basis:** Section 2.7

### WorkDisability (Työkyvyttömyys)
- **Description:** Work disability
- **Legal Basis:** Section 3.3

### Training (Koulutus)
- **Description:** Training
- **Legal Basis:** Section 2.10

---

## Relationships

| From | To | Type |
|------|----|------|
| UnemployedPerson | JobSeeker | registers_as |
| Employee | EmploymentCondition | must_meet |
| JobSeeker | UnemploymentBenefit | may_qualify_for |
| EarningsRelatedAllowance | UnemploymentFund | paid_by |
| BenefitApplication | BenefitDecision | results_in |
| AdjustedBenefit | IncomeRelatedComponent | reduces |
| JobSeeker | JobSearchRequirement | must_fulfill |
| JobSeeker | AcceptableReason | may_invoked |

---

## Legal Structure

| Part | Topic | Chapters |
|------|-------|----------|
| I | Common Provisions | 1-4 |
| II | Unemployment Daily Allowance | 5-6 |
| III | Mobility Support & Redundancy | 7-9 |
| IV | Employment Services | 10 |
| V | Implementation & Appeal | 11-12 |
| VI | Miscellaneous | 13-15 |

---

*Total: 30+ entities covering Työttömyysturvalaki (1290/2002)*
