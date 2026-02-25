# Unemployment Protection (Työttömyysturvalaki 1290/2002) - Data Points for Business Rules

This file documents the **data points needed** to calculate each business rule in the DMN decision tables.

---

## 1. UnemploymentBenefitTypes

**Decision:** Determine type of unemployment benefit

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| person.type | Enum | Employment records | Section 1 |
| person.employee | Boolean | Employment contract | Section 1 |
| person.entrepreneur | Boolean | Business registration | Section 1 |
| person.unemployment_fund_member | Boolean | Fund membership | Section 5 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: UnemploymentBenefitTypes

---

## 2. EmploymentConditionEmployee

**Decision:** Determine if employee meets employment condition

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| employment.months_last_24 | Integer | Employer / Tax records | Section 5.3 |
| employment.hours_per_week | Decimal | Payslips | Section 5.3 |
| employment.ended_reason | Enum | Employer certificate | Section 5.3 |
| employment.date_ended | Date | Employer / UIM | Section 5.3 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: EmploymentConditionEmployee

---

## 3. EmploymentConditionEntrepreneur

**Decision:** Determine if entrepreneur meets employment condition

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| entrepreneur.months_last_48 | Integer | TYEL / Tax records | Section 5.7 |
| entrepreneur.annual_income | Decimal | Tax return | Section 5.7 |
| entrepreneur.tyel_insured | Boolean | Pension provider | Section 5.7 |
| entrepreneur.active_business | Boolean | Business registration | Section 5.7 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: EmploymentConditionEntrepreneur

---

## 4. BenefitAmountCalculation

**Decision:** Calculate benefit amount

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| wages.12_month_total | Decimal | Payslips / Tax | Section 6.1 |
| wages.daily_average | Decimal | Calculated | Section 6.1 |
| person.age | Integer | Population register | Section 6.9 |
| children.count | Integer | Population register | Section 6.3 |
| children.ages | Array | Population register | Section 6.3 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: BenefitAmountCalculation

---

## 5. BenefitDuration

**Decision:** Determine maximum benefit duration

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| benefit.previous_periods | Integer | Unemployment fund / Kela | Section 6.7 |
| person.age | Integer | Population register | Section 6.9 |
| employment.total_years | Integer | Employment history | Section 6.9 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: BenefitDuration

---

## 6. AdjustedBenefit

**Decision:** Calculate adjusted benefit when working

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| work.hours_per_week | Decimal | Employer | Section 4.1a |
| earnings.monthly | Decimal | Payslips | Section 4.4 |
| earnings.below_limit | Boolean | Calculated | Section 4.4 |
| benefit.full_amount | Decimal | Calculation | Section 4.5 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: AdjustedBenefit

---

## 7. LabourMarketPolicyConditions

**Decision:** Verify labour market policy conditions

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| jobseeker.registered | Boolean | TE services | Section 2.1 |
| jobseeker.available | Boolean | TE services | Section 2.1 |
| jobseeker.actively_seeking | Boolean | Job applications | Section 2.1 |
| interview.attended | Boolean | TE services | Section 2.1 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: LabourMarketPolicyConditions

---

## 8. JobRefusalConsequences

**Decision:** Determine consequences of refusing suitable work

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| refusal.occurred | Boolean | TE services | Section 2a.4 |
| refusal.reason | Enum | Job seeker | Section 2a.2 |
| refusal.count_previous | Integer | Benefit history | Section 2a.10 |
| refusal.without_acceptable | Boolean | TE services | Section 2a.2 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: JobRefusalConsequences

---

## 9. AcceptableReasonsForRefusal

**Decision:** Determine if reason for refusal is acceptable

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| reason.health | Boolean | Medical certificate | Section 2a.5 |
| reason.family | Boolean | Self-declaration | Section 2a.5 |
| reason.education | Boolean | Enrollment | Section 2a.5 |
| reason.distance | Decimal | Distance calculation | Section 2a.7 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: AcceptableReasonsForRefusal

---

## 10. SelfEmploymentConditions

**Decision:** Conditions for entrepreneur benefits

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| business.ended | Boolean | Business registration | Section 2.5 |
| business.ended_date | Date | Registration | Section 2.5 |
| entrepreneur.family_member | Boolean | Tax records | Section 2.7 |
| income.verified | Boolean | Tax records | Section 5.7 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: SelfEmploymentConditions

---

## 11. StudyAndBenefit

**Decision:** Effect of studies on benefit

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| study.full_time | Boolean | Educational institution | Section 2.10 |
| study.part_time | Boolean | Self-declaration | Section 2.10 |
| study.vocational | Boolean | Program type | Section 2.13 |
| study.ended | Boolean | Completion / Dropout | Section 2.11 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: StudyAndBenefit

---

## 12. RestrictionsOnBenefit

**Decision:** General restrictions on benefit

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| person.incarcerated | Boolean | Prison register | Section 3.1 |
| person.abroad | Boolean | Exit / Entry records | Section 3.1 |
| person.striking | Boolean | Union / Employer | Section 3.1 |
| income.other | Decimal | Tax records | Section 3.7 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: RestrictionsOnBenefit

---

## 13. WaitingPeriod

**Decision:** Determine waiting period

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| benefit.first_time | Boolean | History | Section 5.13 |
| employment.short | Boolean | Recent work | Section 5.13 |
| illness.during_wait | Boolean | Medical certificate | Section 5.13 |
| activation.program | Boolean | TE services | Section 5.13 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: WaitingPeriod

---

## 14. LabourMarketSupport

**Decision:** Labour market support conditions

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| person.no_earnings_related | Boolean | Fund membership | Section 7.1 |
| income.household | Decimal | Tax records | Section 7.6 |
| employment.meets_condition | Boolean | Work history | Section 7.1 |
| person.age | Integer | Population register | Section 7.1 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: LabourMarketSupport

---

## 15. MobilitySupport

**Decision:** Mobility support conditions

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| move.distance_km | Decimal | Address change | Section 8.1 |
| job.permanent | Boolean | Employment contract | Section 8.1 |
| job.duration_months | Integer | Contract | Section 8.1 |
| previous.residence | String | Population register | Section 8.1 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: MobilitySupport

---

## 16. RedundancyPayment

**Decision:** Redundancy payment conditions

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| employer.bankruptcy | Boolean | Bankruptcy register | Section 9.1 |
| layoff.duration_days | Integer | Employer notice | Section 9.1 |
| employment.tenure_years | Integer | Employer / Tax | Section 9.1 |
| refused.reemployment | Boolean | TE services | Section 9.3 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: RedundancyPayment

---

## 17. EmploymentServicesBenefit

**Decision:** Benefit during employment services

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| service.type | Enum | TE services | Section 10.1 |
| service.start_date | Date | TE services | Section 10.1 |
| attendance.required | Boolean | Service plan | Section 10.3 |
| absence.reason | Enum | Self-declaration | Section 10.3 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: EmploymentServicesBenefit

---

## 18. ApplicationAndPayment

**Decision:** Application and payment procedures

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| application.submitted | Boolean | Application form | Section 11.1 |
| applicant.fund_or_kela | Enum | Application | Section 11.1 |
| bank.account_finnish | Boolean | Bank connection | Section 11.5 |
| payment.frequency | Enum | System default | Section 11.5 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: ApplicationAndPayment

---

## 19. RecoveryOfOverpayment

**Decision:** Recovery of incorrectly paid benefit

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| overpayment.amount | Decimal | Calculation | Section 11.10 |
| overpayment.intentional | Boolean | Investigation | Section 11.10 |
| overpayment.negligent | Boolean | Investigation | Section 11.10 |
| person.financial_situation | Enum | Assessment | Section 11.10 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: RecoveryOfOverpayment

---

## 20. AppealProcedure

**Decision:** Right to appeal benefit decisions

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| appeal.submitted | Boolean | Appeal form | Section 12.1 |
| decision.received_date | Date | Notice | Section 12.1 |
| appeal.within_30_days | Boolean | Date calculation | Section 12.1 |
| decision.type | Enum | Decision notice | Section 12.1 |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: AppealProcedure

---

## 21. InternationalCoordination

**Decision:** EU and international coordination

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| work.country_eu | Boolean | Employment | Section 8a |
| insurance.periods_other_country | Boolean | Foreign records | Section 5.9 |
| job.search_eu | Boolean | Application | Section 8b |
| return.finland | Boolean | Population register | Section 8b |

### Rule Reference
- `unemployment_protection_dmn_rules.json` - Decision: InternationalCoordination

---

## Summary: All Data Points

### Person Data
- person.type
- person.age
- person.employee
- person.entrepreneur
- person.unemployment_fund_member
- person.incarcerated
- person.abroad
- person.striking

### Job Seeker Data
- jobseeker.registered
- jobseeker.available
- jobseeker.actively_seeking

### Employment Data
- employment.months_last_24
- employment.hours_per_week
- employment.ended_reason
- employment.date_ended
- employment.total_years

### Entrepreneur Data
- entrepreneur.months_last_48
- entrepreneur.annual_income
- entrepreneur.tyel_insured
- entrepreneur.active_business

### Business Data
- business.ended
- business.ended_date
- entrepreneur.family_member

### Wages/Income Data
- wages.12_month_total
- wages.daily_average
- income.household
- income.other
- earnings.monthly
- earnings.below_limit
- income.verified

### Children Data
- children.count
- children.ages

### Work Data
- work.hours_per_week

### Refusal Data
- refusal.occurred
- refusal.reason
- refusal.count_previous
- refusal.without_acceptable

### Reason Data
- reason.health
- reason.family
- reason.education
- reason.distance

### Study Data
- study.full_time
- study.part_time
- study.vocational
- study.ended

### Benefit Data
- benefit.first_time
- benefit.previous_periods
- benefit.full_amount

### Illness Data
- illness.during_wait

### Activation Data
- activation.program

### Service Data
- service.type
- service.start_date
- attendance.required
- absence.reason

### Mobility Data
- move.distance_km
- job.permanent
- job.duration_months
- previous.residence

### Employer Data
- employer.bankruptcy

### Layoff Data
- layoff.duration_days

### Redundancy Data
- refused.reemployment

### Application Data
- application.submitted
- applicant.fund_or_kela

### Bank Data
- bank.account_finnish

### Payment Data
- payment.frequency

### Overpayment Data
- overpayment.amount
- overpayment.intentional
- overpayment.negligent
- person.financial_situation

### Appeal Data
- appeal.submitted
- decision.received_date
- appeal.within_30_days
- decision.type

### International Data
- work.country_eu
- insurance.periods_other_country
- job.search_eu
- return.finland

### Legal Basis
- Sections: 1, 2.1-2.13, 3.1-3.7, 4.1a, 4.2-4.5, 5.1-5.13, 5a, 6.1-6.10, 7.1-7.8, 8.1-8.5, 8a-8b, 9.1-9.3, 9a, 10.1-10.6, 11.1-11.13, 12.1-12.9
