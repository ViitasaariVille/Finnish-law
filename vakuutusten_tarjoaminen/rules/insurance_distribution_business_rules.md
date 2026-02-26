# Insurance Distribution (Laki vakuutusten tarjoamisesta 234/2018) - Business Rules

This file documents the **business rules** extracted from the Insurance Distribution Act (234/2018).

---

## 1. RegistrationRequirement

**Decision:** Determine if entity must register as insurance intermediary

### Rule
```
IF entity_type = "InsuranceBroker" AND activity = "primary"
THEN must_register = TRUE

IF entity_type = "InsuranceAgent" AND activity = "any"
THEN must_register = TRUE

IF entity_type = "InsuranceCompany"
THEN must_register = FALSE (exempt)

IF entity_type = "PartTimeAgent" AND premium <= 600 EUR/year
THEN must_register = TRUE (limited)
```

### Legal Basis
- Section 6

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| entity.type | Enum | Business registration |
| activity.level | Enum | Primary/ancillary |
| annual_premium | Number | Financial records |

---

## 2. BrokerRegistrationConditions

**Decision:** Determine if broker meets registration conditions

### Rule
```
IF broker.not_employed_by_insurer = TRUE
AND broker.registered_in_finland = TRUE
AND broker.not_bankrupt = TRUE
AND broker.good_reputation = TRUE
AND broker.professional_qualification = TRUE
AND broker.liability_insurance = TRUE
AND broker.client_assets_system = TRUE
AND broker.staff_30percent_registered = TRUE
THEN registration_allowed = TRUE
ELSE registration_allowed = FALSE
```

### Legal Basis
- Section 8

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| broker.employment_status | Boolean | Employment contract |
| broker.registration.country | String | Trade register |
| broker.bankruptcy_status | Boolean | Bankruptcy register |
| broker.conviction_record | Boolean | Criminal record |
| broker.exam_passed | Boolean | Exam certificate |
| broker.liability_insurance.coverage | Number | Insurance policy |
| broker.client_funds_system | Boolean | Internal systems |
| broker.staff.registered_ratio | Number | HR records |

---

## 3. GoodReputation

**Decision:** Determine if person meets good reputation requirement

### Rule
```
IF person.conviction.relevant = FALSE
THEN good_reputation = TRUE

IF person.conviction.prison WITHIN 5 years
THEN good_reputation = FALSE

IF person.conviction.fine WITHIN 3 years
THEN good_reputation = FALSE

IF person.bankruptcy = ACTIVE
THEN good_reputation = FALSE

IF person.business_ban = ACTIVE
THEN good_reputation = FALSE
```

### Legal Basis
- Section 16

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| person.conviction.type | Enum | Criminal record |
| person.conviction.date | Date | Criminal record |
| person.bankruptcy_status | Boolean | Bankruptcy register |
| person.business_ban | Boolean | Business ban register |

---

## 4. ProfessionalQualification

**Decision:** Determine if person has required professional qualification

### Rule
```
IF person.broker_exam = PASSED
OR person.equivalent_qualification = APPROVED
THEN qualified = TRUE

IF person.no_qualification = TRUE
THEN qualified = FALSE
```

### Legal Basis
- Section 18

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| person.broker_exam.status | Enum | Exam certificate |
| person.equivalent_qualification | Boolean | Competence assessment |

---

## 5. ContinuingEducation

**Decision:** Determine compliance with continuing education requirements

### Rule
```
IF professional.training_hours >= 15 per year
THEN continuing_education.compliant = TRUE

IF professional.training_hours < 15 per year
THEN continuing_education.compliant = FALSE
```

### Legal Basis
- Section 20

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| professional.training.hours_per_year | Number | Training records |
| professional.training.certificates | List | Training provider |

---

## 6. DisclosureObligationsInsurer

**Decision:** Determine what information insurer must disclose

### Rule
```
IF transaction.type = "insurance_contract"
THEN disclose(insurer.name)
THEN disclose(insurer.contact_info)
THEN disclose(insurer.licensing_status)
THEN disclose(insurer.advisory_services)
THEN disclose(complaint_procedures)
```

### Legal Basis
- Section 32

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| transaction.type | Enum | Sales record |
| insurer.name | String | Business registration |
| insurer.license_status | Boolean | FIN-FSA register |

---

## 7. DisclosureObligationsBroker

**Decision:** Determine what information broker must disclose

### Rule
```
IF entity.type = "Broker"
THEN disclose(registration_number)
THEN disclose(register_verification)
THEN disclose(principals_represented)
THEN disclose(commission_structure)
THEN disclose(conflicts_of_interest)
THEN disclose(ownership_10percent)

IF broker.recommendation_given
THEN disclose(recommendation_basis)
```

### Legal Basis
- Sections 33, 36-37

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| broker.registration_number | String | FIN-FSA register |
| broker.principals | List | Agency agreements |
| broker.commission.amount | Number | Commission schedule |
| broker.ownership.interests | List | Shareholder register |
| broker.recommendation.given | Boolean | Sales record |

---

## 8. NeedsAssessment

**Decision:** Determine if broker must assess customer needs

### Rule
```
IF broker.offers_insurance = TRUE
THEN broker.must_assess_needs = TRUE

IF customer.type = "any"
THEN collect(customer.existing_coverage)
THEN collect(customer.risk_profile)
THEN collect(customer.financial_situation)
```

### Legal Basis
- Section 35

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| customer.existing_insurance | List | Customer interview |
| customer.risk_profile | Enum | Needs assessment |
| customer.financial_situation | Object | Customer interview |
| customer.objectives | List | Customer interview |

---

## 9. ProductGovernance

**Decision:** Determine product governance requirements

### Rule
```
IF insurer.offers_products = TRUE
THEN insurer.must_have.product_governance = TRUE
THEN define_target_market(each_product)
THEN assess_risks(each_product)
THEN create_distribution_plan(each_product)
THEN review_products_regularly
```

### Legal Basis
- Section 42

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| product.target_market | Object | Product design |
| product.risk_assessment | Object | Risk analysis |
| product.distribution_plan | Object | Distribution strategy |
| product.review_date | Date | Monitoring system |

---

## 10. InvestmentInsuranceSuitability

**Decision:** Determine suitability assessment requirements

### Rule
```
IF product.type = "InvestmentInsurance"
AND broker.provides_recommendation = TRUE
THEN assess_suitability(customer)
THEN assess(customer.experience)
THEN assess(customer.knowledge)
THEN assess(customer.financialSituation)
THEN assess(customer.objectives)
THEN assess(customer.riskTolerance)

IF customer.professional = TRUE
THEN suitability_exempt = TRUE
```

### Legal Basis
- Sections 49-50, 54

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| product.type | Enum | Product classification |
| customer.experience.level | Enum | Customer interview |
| customer.knowledge.level | Enum | Customer interview |
| customer.financial.situation | Object | Customer interview |
| customer.objectives | List | Customer interview |
| customer.risk_tolerance | Enum | Risk assessment |
| customer.professional_status | Boolean | Customer classification |

---

## 11. ProfessionalLiabilityInsurance

**Decision:** Determine liability insurance requirements

### Rule
```
IF broker.registers = TRUE
THEN liability_insurance.minimum_coverage = 1,564,610 EUR per claim
THEN liability_insurance.aggregate = 2,315,610 EUR per year
THEN coverage.area = "entire_EEA"
THEN cancellation_notice >= 2 months
```

### Legal Basis
- Section 58

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| broker.registration.status | Boolean | FIN-FSA register |
| insurance.coverage.per_claim | Number | Policy |
| insurance.coverage.annual | Number | Policy |
| insurance.geographic_coverage | List | Policy |
| insurance.cancellation_terms | Object | Policy |

---

## 12. ClientAssetSegregation

**Decision:** Determine client asset handling requirements

### Rule
```
IF broker.holds_client_funds = TRUE
THEN segregate_assets = TRUE
THEN bank_account.separate = TRUE
THEN record_keeping.detailed = TRUE
THEN transfer_to_beneficiary = prompt

IF customer.type = "Consumer"
THEN broker.must_not_hold_funds = TRUE
```

### Legal Basis
- Section 59

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| broker.holds_client_funds | Boolean | Business model |
| client_funds.account_type | Enum | Bank records |
| customer.type | Enum | Customer classification |

---

## 13. CrossBorderNotification

**Decision:** Determine cross-border notification requirements

### Rule
```
IF intermediary.plans_EEA_operations = TRUE
THEN notify_home_state_authority
THEN provide(registered_details)
THEN provide(principals)
THEN provide(insurance_types)
THEN provide(target_countries)

IF establishment.planned = TRUE
THEN provide(branch_address)
THEN provide(responsible_person)
```

### Legal Basis
- Sections 22-23

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| intermediary.EEA_plans | Boolean | Business plan |
| intermediary.countries_targeted | List | Business plan |
| intermediary.establishment_type | Enum | Business plan |

---

## 14. AdministrativeSanctions

**Decision:** Determine available sanctions

### Rule
```
IF entity.operates_without_registration = TRUE
THEN sanction = PROHIBITION

IF entity.violation = SIGNIFICANT
THEN sanction = ADMINISTRATIVE_FINE

IF entity.violations = REPEATED
THEN sanction = DEREGISTRATION

IF entity.violation.caused_damage = TRUE
THEN sanction = COMPENSATION
```

### Legal Basis
- Sections 70-73

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| entity.registration_status | Boolean | FIN-FSA register |
| violation.severity | Enum | Investigation |
| violation.count | Number | Compliance records |
| violation.damage_amount | Number | Claims records |

---

## 15. CompensationLiability

**Decision:** Determine compensation liability

### Rule
```
IF broker.breach_of_duty = TRUE
AND customer.damage = TRUE
THEN customer.entitled_to_compensation = TRUE

IF broker.information_omission = TRUE
THEN compensate(difference_from_expectation)

IF insurer.breach_sections_30_34_45_46 = TRUE
THEN insurer.liable = TRUE
```

### Legal Basis
- Sections 74-75

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| broker.breach.type | Enum | Investigation |
| customer.damage.proven | Boolean | Claims investigation |
| customer.damage.amount | Number | Assessment |
| broker.professional_conduct | Boolean | Compliance review |

---

## 16. ConfidentialityObligations

**Decision:** Determine confidentiality requirements

### Rule
```
IF employee.accessed_customer_data = TRUE
THEN maintain_confidentiality = TRUE

IF authority.request = LEGITIMATE
THEN disclose_to_authority = ALLOWED

IF legal_proceedings = REQUIRED
THEN disclose_for_investigation = ALLOWED

IF researcher.request = LEGITIMATE
AND no_individual_harm = TRUE
THEN disclose_for_research = ALLOWED
```

### Legal Basis
- Sections 79-80

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| employee.accessed_data.types | List | Access logs |
| authority.request.type | Enum | Official request |
| disclosure.purpose | Enum | Request documentation |

---

## 17. DocumentRetention

**Decision:** Determine document retention requirements

### Rule
```
IF document.type = "qualification_records"
THEN retain >= 5 years

IF document.type = "customer_contracts"
THEN retain >= 5 years

IF document.type = "training_records"
THEN retain >= 5 years
```

### Legal Basis
- Section 78

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| document.type | Enum | Document classification |
| document.date | Date | Document metadata |
| retention.start_date | Date | Expiry calculation |

---

## 18. MarketingRequirements

**Decision:** Determine marketing compliance

### Rule
```
IF communication.type = "marketing"
THEN identify_as_marketing = TRUE
THEN information.accurate = TRUE
THEN information.non_misleading = TRUE
IF communication.omits_material = TRUE
THEN practice = PROHIBITED
```

### Legal Basis
- Section 34

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| communication.type | Enum | Communication classification |
| communication.content | Object | Marketing materials |
| information.accuracy | Boolean | Compliance review |

---

## 19. TyingProhibition

**Decision:** Determine tying and bundling rules

### Rule
```
IF customer.type = "Consumer"
AND product.tied_to_other = TRUE
THEN tying = PROHIBITED
THEN offer_separately = REQUIRED

IF customer.type = "Business"
AND product.bundled = TRUE
THEN disclose_separate_pricing = REQUIRED
```

### Legal Basis
- Sections 40-41

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| customer.type | Enum | Customer classification |
| product.bundling.type | Enum | Product design |
| product.separate_pricing | Boolean | Pricing structure |

---

## 20. WhistleblowingProcedure

**Decision:** Determine whistleblowing requirements

### Rule
```
IF company.type = "legal_entity"
THEN establish_reporting_channel = TRUE
THEN protect_reporter_identity = TRUE
THEN handle_properly = TRUE
THEN retain_records >= 5 years
```

### Legal Basis
- Section 72

### Data Points Needed
| Data Point | Type | Source |
|-----------|------|--------|
| company.type | Enum | Business registration |
| channel.independent | Boolean | Internal systems |
| protection.measures | List | Policy documents |
