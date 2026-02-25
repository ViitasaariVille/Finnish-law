# Insurance Distribution Act - DMN Rules

## Decision Tables

---

### 1. RegistrationRequirement
**Legal Source:** Section 6  
**Description:** Determines if entity must register as insurance intermediary

| Entity Type | Activity | Output | Legal Basis |
|-------------|----------|--------|------------|
| InsuranceBroker | Primary activity | Registration required | § 6(1) |
| InsuranceAgent | Any | Registration required | § 6(1) |
| InsuranceCompany | Any | Not required (exempt) | § 6(3) |
| PartTimeAgent | Within limits | Limited registration | § 4 |

---

### 2. GoodReputation
**Legal Source:** Section 16  
**Description:** Determines if person meets good reputation requirement

| Conviction Status | Timeframe | Output | Legal Basis |
|------------------|-----------|--------|------------|
| No conviction | N/A | Good reputation | § 16 |
| Prison sentence | Within 5 years | No good reputation | § 16 |
| Fine sentence | Within 3 years | No good reputation | § 16 |
| Bankruptcy | Active | No good reputation | § 16 |
| Business ban | Active | No good reputation | § 16 ref |

---

### 3. ProfessionalQualification
**Legal Source:** Section 18  
**Description:** Determines if person has required professional qualification

| Qualification Type | Status | Output | Legal Basis |
|-------------------|--------|--------|------------|
| Broker exam | Passed | Qualified | § 18 |
| Equivalent qualification | Approved | Qualified | § 18 |
| No qualification | Any | Not qualified | § 18 |
| Exemption | Applicable | Exempt from exam | § 84 |

---

### 4. ContinuingEducation
**Legal Source:** Section 20  
**Description:** Minimum continuing education requirements

| Training Hours | Output | Legal Basis |
|----------------|--------|-------------|
| 15 or more | Compliant | § 20 |
| Under 15 | Non-compliant | § 20 |

---

### 5. DisclosureObligations
**Legal Source:** Sections 32-38  
**Description:** Information disclosure requirements before contract

| Entity | Information Type | Output | Legal Basis |
|--------|------------------|--------|-------------|
| Insurer | Any | Must disclose: name, contact, licensing | § 32 |
| Agent | Any | Must disclose: name, register, principal | § 33 |
| Broker | Any | Must disclose: commission, analysis, conflicts | § 33 |
| Broker | Recommendation | Must explain why recommended | § 37 |
| Any | Advice given | Must disclose commission/fees | § 38 |

---

### 6. ProductGovernance
**Legal Source:** Section 42  
**Description:** Product governance requirements for insurers

| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Offers products | Must have product governance | § 42(1) |
| Target market defined | Target market defined | § 42(2) |
| Risk assessment completed | Risk assessment done | § 42(3) |
| Distribution strategy documented | Distribution plan in place | § 42(4) |

---

### 7. InvestmentInsuranceRequirements
**Legal Source:** Sections 44-54  
**Description:** Additional requirements for investment insurance

| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Conflict of interest exists | Must disclose to customer | § 45 |
| Incentive offered | Must not impair service quality | § 46 |
| Investment insurance recommended | Suitability assessment required | § 49 |
| Professional customer | Exempt from suitability | § 54 |

---

### 8. ProfessionalLiabilityInsurance
**Legal Source:** Section 58  
**Description:** Mandatory liability insurance for brokers

| Condition | Coverage | Output | Legal Basis |
|-----------|----------|--------|-------------|
| Broker registered | Per claim | 1,564,610 EUR minimum | § 58(1) |
| Broker registered | Annual aggregate | 2,315,610 EUR minimum | § 58(1) |
| Any | EEA coverage | Must cover entire EEA | § 58(2) |

---

### 9. ClientAssetSegregation
**Legal Source:** Section 59  
**Description:** Requirements for segregating client assets

| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Holds client funds | Must segregate in bank account | § 59 |
| Consumer funds | Cannot hold consumer funds | § 59(2) |
| Record keeping | Must keep proper records | § 59 |

---

### 10. CrossBorderOperations
**Legal Source:** Sections 22-29  
**Description:** Requirements for operating in other EEA states

| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Services to EEA planned | Notify home state authority | § 22 |
| Establishment planned | Provide additional information | § 22(2) |
| Home state approval received | Can start operations | § 24 |
| Host state rules applicable | Must comply with host state rules | § 24(2) |

---

### 11. SupervisorySanctions
**Legal Source:** Sections 70-71  
**Description:** Available sanctions for violations

| Violation Type | Output | Legal Basis |
|----------------|--------|-------------|
| Unregistered activity | Prohibition to operate | § 70 |
| Violation significant | Administrative fine possible | § 71 |
| Repeated violation | Deregistration possible | § 73 |
| Customer damage proven | Compensation liability | § 74-75 |

---

### 12. CompensationLiability
**Legal Source:** Sections 74-75  
**Description:** Liability for damages to customers

| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Broker breach + damage proven | Broker liable to compensate | § 74(1) |
| Information omission | Compensate for losses | § 74(2) |
| Insurer breach (30/34/45/46) | Insurer liable | § 75 |
| Professional conduct proven | Exempt from liability | § 74 |

---

### 13. DataProtection
**Legal Source:** Sections 79-81  
**Description:** Confidentiality and data protection requirements

| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Customer data obtained | Must maintain confidentiality | § 79 |
| Supervisory request legitimate | Can disclose to FIN-FSA | § 80(1) |
| Legal proceedings required | Can disclose for investigations | § 80(5) |
| Breach proven | Criminal liability | § 81 |

---

### 14. DocumentRetention
**Legal Source:** Section 78  
**Description:** Requirements for document retention

| Document Type | Retention Period | Legal Basis |
|---------------|------------------|-------------|
| Qualification records | 5 years minimum | § 78 |
| Customer contracts | 5 years minimum | § 78(2) |
| Professional development | Record of training | § 78 |

---

## Key Thresholds Summary

| Requirement | Threshold |
|-------------|-----------|
| Part-time agent premium | €600/year or €200/person |
| Liability insurance (per claim) | €1,564,610 |
| Liability insurance (annual) | €2,315,610 |
| Continuing education | 15 hours/year |
| Good reputation | No relevant conviction: 5 years (prison), 3 years (fine) |
| Processing time | 3 months max |
| Document retention | 5 years minimum |
