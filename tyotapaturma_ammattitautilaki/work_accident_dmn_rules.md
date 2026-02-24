# Finnish Work Accident Insurance - DMN Business Rules

**Based on:** Työtapaturma- ja ammattitautilaki (459/2015)  
**Version:** 1.0  
**DMN Version:** 1.3  
**Compatible Engines:** Camunda, Drools, IBM ODM, Flowable

---

## 1. Insurance Obligation

**Decision:** Determines if employer has mandatory insurance obligation

| Person Type | Employment Status | Insurance Required | Legal Basis |
|-------------|-------------------|-------------------|-------------|
| Employee | employed | MandatoryInsurance | Section 3 |
| Employee | probation | MandatoryInsurance | Section 3 |
| Entrepreneur | YEL_insured | VoluntaryWorkTimeInsurance | Sections 188-190 |
| Farmer | any | Excluded | Section 11 |
| ForeignWorker | EU | MandatoryInsurance | Section 8 |
| ForeignWorker | non_EU | Check bilateral | Section 8 |

---

## 2. Compensable Event

**Decision:** Determine if event is compensable under the law

| Event Type | Location | Timing | Compensable | Legal Basis |
|------------|----------|--------|-------------|-------------|
| WorkplaceAccident | workplace | during_work | Compensable | Section 17 |
| WorkplaceAccident | workplace | before_after | Compensable if work-related | Section 18 |
| CommuteAccident | home_work_route | direct_route | Compensable | Section 21 |
| CommuteAccident | home_work_route | detour | Limited compensation | Section 21 |
| BusinessTripAccident | work_travel | during_travel | Compensable | Section 22 |
| BusinessTripAccident | free_time | during_trip | Limited | Section 24 |
| OccupationalDisease | any | diagnosed | Compensable | Section 26 |
| RepetitiveStrainInjury | any | any | Compensable | Section 33 |
| ViolenceIncident | work_related | during_work | Compensable | Section 34 |
| PsychologicalInjury | work_related | serious | Compensable | Section 35 |

---

## 3. Compensation Type

**Decision:** Determine type of compensation based on injury

| Injury Type | Severity | Duration | Compensation Type | Legal Basis |
|-------------|----------|----------|-------------------|-------------|
| PhysicalInjury | minor | < 1 year | MedicalExpenses | Section 36 |
| PhysicalInjury | moderate | 1-3 years | MedicalExpenses + LostWages | Sections 36, 55 |
| PhysicalInjury | severe | > 3 years | MedicalExpenses + LostWages + Disability | Sections 36, 55, 83 |
| PhysicalInjury | permanent | any | PermanentDisabilityCompensation | Section 83 |
| OccupationalDisease | any | any | MedicalExpenses + LostWages | Sections 26-32 |
| MentalInjury | moderate | any | Rehabilitation | Section 88 |
| Death | any | any | DeathCompensation | Sections 99-109 |

---

## 4. Compensation Amount

**Decision:** Calculate compensation amount

| Compensation Type | Income | Severity | Work Ability Lost | Formula | Legal Basis |
|-------------------|--------|----------|-------------------|---------|-------------|
| LostWages | any | any | 100% | income.annual / 365 × days | Section 56 |
| LostWages | any | any | 50% | income.annual / 365 × days × 0.5 | Section 56 |
| LostWages | any | any | 0% | 0 | Section 56 |
| PermanentDisability | any | 10-19% | any | income.annual × 0.1 | Section 84 |
| PermanentDisability | any | 20-50% | any | income.annual × 0.2 | Section 84 |
| PermanentDisability | any | 100% | any | income.annual | Section 84 |
| Death | any | any | any | Section 99-109 rates | Sections 99-109 |

---

## 5. Medical Care Coverage

**Decision:** Determine medical care coverage

| Treatment Type | Necessity | Provider | Coverage | Legal Basis |
|---------------|-----------|----------|----------|-------------|
| EmergencyCare | required | public | 100% | Section 37 |
| EmergencyCare | required | private | 100% (reimbursement) | Section 37 |
| Surgery | required | any | 100% | Section 38 |
| Medicines | prescribed | pharmacy | 100% (drug list) | Section 45 |
| Rehabilitation | medical_necessity | any | 100% | Section 88 |
| DentalTreatment | accident_related | any | 100% | Section 48 |
| TravelToTreatment | required | any | Kilometre allowance | Section 50 |

---

## 6. Claim Time Limit

**Decision:** Determine claim submission time limit

| Claim Type | Injury Timing | Time Limit | Legal Basis |
|------------|---------------|------------|-------------|
| WorkAccident | within_3_years | 3 years from accident | Section 110 |
| WorkAccident | after_3_years | Claim barred | Section 110 |
| OccupationalDisease | any | 3 years from diagnosis | Section 110 |
| DeathBenefit | within_3_years | 3 years from death | Section 110 |
| SurvivorBenefit | any | 3 years from death | Section 110 |

---

## 7. Rehabilitation Eligibility

**Decision:** Determine rehabilitation eligibility

| Injury Severity | Work Ability Reduced | Medical Recommendation | Eligible | Legal Basis |
|-----------------|---------------------|----------------------|----------|-------------|
| severe | yes | yes | Full rehabilitation | Section 88 |
| moderate | yes | yes | Vocational rehabilitation | Section 89 |
| minor | no | no | Medical rehabilitation only | Section 88 |
| any | any | no | Not eligible | Section 88 |

---

## 8. Insurance Premium

**Decision:** Calculate insurance premium

| Industry Risk | Payroll | Claims History | Premium Formula | Legal Basis |
|---------------|---------|---------------|----------------|-------------|
| low_risk | any | no_claims | payroll × 0.005 | Section 166 |
| medium_risk | any | no_claims | payroll × 0.01 | Section 166 |
| high_risk | any | no_claims | payroll × 0.02 | Section 166 |
| any | any | with_claims | base_premium + risk loading | Sections 171-176 |

---

## 9. Appeals Process

**Decision:** Determine appeals process

| Decision Type | Disagreement | Appeal Path | Legal Basis |
|---------------|--------------|-------------|-------------|
| Rejection | yes | Appeal to Insurance Company → Accident Board | Section 237 |
| AmountDispute | yes | Appeal to Accident Compensation Board | Section 237 |
| LateDecision | yes | Complaint + Late interest | Sections 146-155 |
| AnyDecision | no | No appeal | N/A |

---

## 10. Survivor Benefits

**Decision:** Determine survivor benefit eligibility

| Survivor Relationship | Age | Deceased Contributory | Benefit | Legal Basis |
|-----------------------|-----|----------------------|---------|-------------|
| Spouse | any | yes | Spouse pension | Section 100 |
| Spouse | any | no | Lump sum | Section 107 |
| Child | under_18 | yes | Child pension + orphan allowance | Sections 101-103 |
| Child | 18-24_student | yes | Student orphan pension | Section 103 |
| Dependent | any | yes | Dependent allowance | Section 105 |

---

## JSON Format (Machine-Readable)

See `work_accident_dmn_rules.json` for DMN-compatible JSON format that can be imported into:
- Camunda DMN
- Drools DMN
- IBM Operational Decision Manager
- Flowable DMN
