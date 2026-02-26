# Patient Insurance Dmn Rules DMN Rules

**Version:** 1.0
**Total Decisions:** 10

---

## Unknown

### InsuranceObligation

- **Description:** Determine if organization has patient insurance obligation
- **Legal Source:** Section 6
- **Hit Policy:** FIRST
- **Output:** insurance_required
- **Inputs:** organization.type, organization.is_free, organization.has_employer

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| PublicHealthcareEntity | any | any | PatientInsurance | Section 6(1) |
| PrivateHealthcareEntity | any | any | PatientInsurance | Section 6(1) |
| SelfEmployedProfessional | any | any | PatientInsurance | Section 6(1) |
| HealthcareProfessional | True | False | PatientInsurance (personal) | Section 6(2) |
| HealthcareProfessional | True | True | Employer liable | Section 6(2) |

### CompensableInjury

- **Description:** Determine if patient injury is compensable
- **Legal Source:** Section 23
- **Hit Policy:** FIRST
- **Output:** compensable
- **Inputs:** injury.type, injury.condition_met

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| TreatmentInjury | True | Compensable | Section 23(1)(1) |
| DeviceInjury | True | Compensable | Section 23(1)(2) |
| ImplantInjury | True | Compensable | Section 23(1)(3) |
| InfectionInjury | True | Compensable | Section 23(1)(4) |
| AccidentInjury | True | Compensable | Section 23(1)(5) |
| FacilityInjury | True | Compensable | Section 23(1)(6) |
| MedicationInjury | True | Compensable | Section 23(1)(7) |
| SevereConsequenceInjury | True | Compensable | Section 23(1)(8) |
| any | False | Not compensable | Section 23 |

### ClaimTimeLimit

- **Description:** Determine claim time limit
- **Legal Source:** Section 31
- **Hit Policy:** UNIQUE
- **Output:** time_limit
- **Inputs:** claim.knowledge_date, claim.event_date

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| within_3_years | any | 3 years from knowledge | Section 31(1) |
| any | within_10_years | 10 years from event | Section 31(1) |
| after_3_years | over_10_years | Claim barred | Section 31(1) |

### CompensationType

- **Description:** Determine type of compensation
- **Legal Source:** Section 24
- **Hit Policy:** FIRST
- **Output:** compensation_type
- **Inputs:** injury.result, patient.status

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| medical_costs | alive | MedicalExpenseCompensation | Section 24 |
| income_loss | alive | LostEarningsCompensation | Section 24 |
| permanent_damage | alive | PermanentInjuryCompensation | Section 24 |
| pain | alive | PainAndSuffering | Section 24 |
| death | deceased | DeathCompensation | Section 24 |
| work_ability_affected | alive | VocationalRehabilitation | Section 25 |

### ProcessingDeadline

- **Description:** Determine processing deadline
- **Legal Source:** Section 33
- **Hit Policy:** UNIQUE
- **Output:** deadline
- **Inputs:** claim.stage

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| filing | 7 days to start | Section 33(1) |
| complete | 3 months to decision | Section 33(2) |
| undisputed | Immediate payment | Section 33(3) |

### LatePaymentInterest

- **Description:** Determine late payment interest
- **Legal Source:** Section 42
- **Hit Policy:** UNIQUE
- **Output:** interest
- **Inputs:** payment.status, payment.amount

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| late | over_8_euros | Interest Act 4a§ rate | Section 42(1) |
| late | under_8_euros | Not paid | Section 42(3) |
| on_time | any | No interest | Section 42 |

### RehabilitationEligibility

- **Description:** Determine rehabilitation eligibility
- **Legal Source:** Section 25
- **Hit Policy:** FIRST
- **Output:** eligible
- **Inputs:** work_ability.affected, future.affect_probable

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | any | Vocational rehabilitation | Section 25(1) |
| False | True | May become eligible | Section 25(1) |
| False | False | Not eligible | Section 25 |

### SubrogationRight

- **Description:** Determine subrogation rights
- **Legal Source:** Sections 45-47
- **Hit Policy:** FIRST
- **Output:** subrogation
- **Inputs:** claimant.type, injury.causation

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| PatientInsuranceCentre | any | Can recover from wrongdoer | Section 45 |
| OtherInsurer | coordinate | Coordination required | Section 46 |
| WorkAccidentInsurer | duplicate | Can recover from Centre | Section 47 |

### AppealProcess

- **Description:** Determine appeal path
- **Legal Source:** Sections 38-40
- **Hit Policy:** FIRST
- **Output:** appeal_path
- **Inputs:** decision.type, timeline

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| rejection | within_1_year | Request Board recommendation | Section 38 |
| amount_dispute | any | Request Board recommendation | Section 38 |
| permanent_disability | any | Mandatory Board consultation | Section 40 |
| death_benefit | any | Mandatory Board consultation | Section 40 |

### IndexAdjustment

- **Description:** Determine if compensation is index-adjusted
- **Legal Source:** Section 28
- **Hit Policy:** UNIQUE
- **Output:** index_adjusted
- **Inputs:** compensation.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| continuous | Annual adjustment (TyEL index) | Section 28 |
| lump_sum | No adjustment | Section 28 |
| medical_expenses | As incurred | Section 24 |

