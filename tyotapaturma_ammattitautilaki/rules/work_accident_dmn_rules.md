# Work Accident Dmn Rules DMN Rules

**Version:** 1.1
**Total Decisions:** 10

---

## Unknown

### InsuranceObligation

- **Description:** Determine if employer has mandatory insurance obligation
- **Legal Source:** Part I, Sections 1-14
- **Hit Policy:** UNIQUE
- **Output:** insurance_required
- **Inputs:** person.type, person.employment_status

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Employee | employed | MandatoryInsurance | Section 3(1) |
| Employee | probation | MandatoryInsurance | Section 3(1) |
| Employee | contract | MandatoryInsurance | Section 3(2) |
| Entrepreneur | YEL_insured | VoluntaryWorkTimeInsurance | Sections 188-190 |
| Farmer | any | Excluded | Section 11 |
| ForeignWorker | EU | MandatoryInsurance | Section 8(1) |
| ForeignWorker | non_EU | Check bilateral | Section 8(2) |

### CompensableEvent

- **Description:** Determine if event is compensable under the law
- **Legal Source:** Part II, Sections 15-35
- **Hit Policy:** FIRST
- **Output:** compensable
- **Inputs:** event.type, event.location, event.timing

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| WorkplaceAccident | workplace | during_work | Compensable | Section 17(1) |
| WorkplaceAccident | workplace | before_after | Compensable | Section 18 |
| WorkplaceAccident | workplace | breaks | Compensable | Section 17(3) |
| CommuteAccident | home_work_route | direct_route | Compensable | Section 21(1) |
| CommuteAccident | home_work_route | detour_necessary | Compensable | Section 21(2) |
| CommuteAccident | home_work_route | detour_personal | Not compensable | Section 21(3) |
| BusinessTripAccident | work_travel | during_travel | Compensable | Section 22 |
| BusinessTripAccident | accommodation | any | Compensable | Section 23 |
| BusinessTripAccident | free_time | during_trip | Limited | Section 24 |
| OccupationalDisease | any | diagnosed | Compensable | Section 26(1) |
| RepetitiveStrainInjury | any | any | Compensable | Section 33 |
| ViolenceIncident | work_related | during_work | Compensable | Section 34 |
| PsychologicalInjury | work_related | serious | Compensable | Section 35 |

### CompensationType

- **Description:** Determine type of compensation based on injury
- **Legal Source:** Part III, Sections 36-109
- **Hit Policy:** FIRST
- **Output:** compensation_type
- **Inputs:** injury.type, injury.severity, injury.duration

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| PhysicalInjury | minor | < 1 year | MedicalExpenses | Section 36 |
| PhysicalInjury | moderate | 1-3 years | MedicalExpenses + LostWages | Sections 36, 55 |
| PhysicalInjury | severe | > 3 years | MedicalExpenses + LostWages + Disability | Sections 36, 55, 83 |
| PhysicalInjury | permanent | any | PermanentDisabilityCompensation | Section 83(1) |
| OccupationalDisease | any | any | MedicalExpenses + LostWages | Sections 26-32 |
| MentalInjury | moderate | any | Rehabilitation | Section 88(1) |
| Death | any | any | DeathCompensation | Section 99(1) |

### CompensationAmount

- **Description:** Calculate compensation amount
- **Legal Source:** Part III, Sections 36-109
- **Hit Policy:** UNIQUE
- **Output:** compensation_amount
- **Inputs:** compensation_type, income.annual, injury.severity, work_ability.lost_percentage

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| LostWages | any | any | 100% | income.annual / 365 * days | Section 56(1) |
| LostWages | any | any | 50% | income.annual / 365 * days * 0.5 | Section 56(2) |
| LostWages | any | any | 0% | 0 | Section 56 |
| PermanentDisability | any | 10-19% | any | income.annual * 0.1 | Section 84(1) |
| PermanentDisability | any | 20-50% | any | income.annual * 0.2 | Section 84(1) |
| PermanentDisability | any | 51-100% | any | income.annual | Section 84(2) |
| Death | any | any | any | Section 99-109 rates | Sections 99-109 |

### MedicalCareCoverage

- **Description:** Determine medical care coverage
- **Legal Source:** Part III, Sections 36-54
- **Hit Policy:** FIRST
- **Output:** coverage
- **Inputs:** treatment.type, treatment.necessity, treatment.provider

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| EmergencyCare | required | public | 100% | Section 37(1) |
| EmergencyCare | required | private | 100% (reimbursement) | Section 37(2) |
| Surgery | required | any | 100% | Section 38(1) |
| Medicines | prescribed | pharmacy | 100% (drug list) | Section 45 |
| Rehabilitation | medical_necessity | any | 100% | Section 88(1) |
| DentalTreatment | accident_related | any | 100% | Section 48 |
| TravelToTreatment | required | any | Kilometre allowance | Section 50 |
| Prosthesis | required | any | 100% | Section 47 |

### ClaimTimeLimit

- **Description:** Determine claim submission time limit
- **Legal Source:** Part IV, Section 110
- **Hit Policy:** UNIQUE
- **Output:** time_limit
- **Inputs:** claim.type, injury.timing

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| WorkAccident | within_3_years | 3 years from accident | Section 110(1) |
| WorkAccident | after_3_years | Claim barred | Section 110(3) |
| OccupationalDisease | any | 3 years from diagnosis | Section 110(2) |
| DeathBenefit | within_3_years | 3 years from death | Section 110(1) |
| SurvivorBenefit | any | 3 years from death | Section 110(1) |

### RehabilitationEligibility

- **Description:** Determine rehabilitation eligibility
- **Legal Source:** Part III, Sections 88-98
- **Hit Policy:** FIRST
- **Output:** eligible
- **Inputs:** injury.severity, work_ability.reduced, rehabilitation.medical_recommendation

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| severe | yes | yes | Full rehabilitation | Section 88(1) |
| moderate | yes | yes | Vocational rehabilitation | Section 89(1) |
| minor | no | no | Medical rehabilitation only | Section 88(1) |
| any | any | no | Not eligible | Section 88(1) |

### InsurancePremium

- **Description:** Calculate insurance premium
- **Legal Source:** Part V, Sections 156-186
- **Hit Policy:** UNIQUE
- **Output:** premium
- **Inputs:** employer.industry_risk, employer.payroll, employer.claims_history

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| low_risk | any | no_claims | payroll * 0.005 | Section 166(1) |
| medium_risk | any | no_claims | payroll * 0.01 | Section 166(1) |
| high_risk | any | no_claims | payroll * 0.02 | Section 166(1) |
| any | any | with_claims | base_premium + risk loading | Sections 171-176 |

### AppealsProcess

- **Description:** Determine appeals process
- **Legal Source:** Part VIII, Sections 237-247
- **Hit Policy:** UNIQUE
- **Output:** appeal_path
- **Inputs:** decision.type, claimaint.disagreement

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Rejection | yes | Appeal to Insurance Company -> Accident Board | Section 237(1) |
| AmountDispute | yes | Appeal to Accident Compensation Board | Section 238 |
| LateDecision | yes | Complaint + Late interest | Section 146 |
| AnyDecision | no | No appeal | N/A |

### SurvivorBenefits

- **Description:** Determine survivor benefit eligibility
- **Legal Source:** Part III, Sections 99-109
- **Hit Policy:** FIRST
- **Output:** benefit
- **Inputs:** survivor.relationship, survivor.age, deceased.contributory

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Spouse | any | yes | Spouse pension | Section 100(1) |
| Spouse | any | no | Lump sum | Section 107(1) |
| Child | under_18 | yes | Child pension + orphan allowance | Sections 101-102 |
| Child | 18-24_student | yes | Student orphan pension | Section 103 |
| Dependent | any | yes | Dependent allowance | Section 105 |

