# Insurance Distribution (Laki vakuutusten tarjoamisesta 234/2018) - Data Points

This file documents the **data points needed** to calculate each business rule in the DMN decision tables.

---

## 1. RegistrationRequirement

**Decision:** Determine if entity must register as insurance intermediary

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| entity.type | Enum | Business registration | Section 5 |
| activity.level | Enum | Business model | Section 6 |
| annual_premium | Number | Financial records | Section 4 |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: RegistrationRequirement

---

## 2. BrokerRegistrationConditions

**Decision:** Determine if broker meets registration conditions

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| broker.not_employed_by_insurer | Boolean | Employment contract | Section 8(1) |
| broker.registered_in_finland | Boolean | Trade register | Section 8(2) |
| broker.not_bankrupt | Boolean | Bankruptcy register | Section 8(3) |
| broker.good_reputation | Boolean | Criminal record | Section 8(4) |
| broker.professional_qualification | Boolean | Exam certificate | Section 8(5) |
| broker.liability_insurance | Boolean | Insurance policy | Section 8(6) |
| broker.client_assets_system | Boolean | Internal systems | Section 8(7) |
| broker.staff.registered_ratio | Number | HR records | Section 8(8) |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: BrokerRegistrationConditions

---

## 3. GoodReputation

**Decision:** Determine if person meets good reputation requirement

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| person.conviction.type | Enum | Criminal record | Section 16 |
| person.conviction.date | Date | Criminal record | Section 16 |
| person.bankruptcy_status | Boolean | Bankruptcy register | Section 16 |
| person.business_ban | Boolean | Business ban register | Section 16 |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: GoodReputation

---

## 4. ProfessionalQualification

**Decision:** Determine if person has required professional qualification

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| person.broker_exam.status | Enum | Exam certificate | Section 18 |
| person.equivalent_qualification | Boolean | Competence assessment | Section 18 |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: ProfessionalQualification

---

## 5. ContinuingEducation

**Decision:** Determine compliance with continuing education requirements

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| professional.training.hours_per_year | Number | Training records | Section 20 |
| professional.training.certificates | List | Training provider | Section 20 |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: ContinuingEducation

---

## 6. DisclosureObligationsInsurer

**Decision:** Determine what information insurer must disclose

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| transaction.type | Enum | Sales record | Section 32 |
| insurer.name | String | Business registration | Section 32(1) |
| insurer.license_status | Boolean | FIN-FSA register | Section 32 |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: DisclosureObligations

---

## 7. DisclosureObligationsBroker

**Decision:** Determine what information broker must disclose

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| broker.registration_number | String | FIN-FSA register | Section 33 |
| broker.principals | List | Agency agreements | Section 33 |
| broker.commission.amount | Number | Commission schedule | Section 38 |
| broker.ownership.interests | List | Shareholder register | Section 33 |
| broker.recommendation.given | Boolean | Sales record | Section 37 |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: DisclosureObligations

---

## 8. NeedsAssessment

**Decision:** Determine if broker must assess customer needs

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| broker.offers_insurance | Boolean | Business registration | Section 35 |
| customer.existing_insurance | List | Customer interview | Section 35 |
| customer.risk_profile | Enum | Needs assessment | Section 35 |
| customer.financial_situation | Object | Customer interview | Section 35 |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: NeedsAssessment

---

## 9. ProductGovernance

**Decision:** Determine product governance requirements

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| insurer.offers_products | Boolean | Product portfolio | Section 42 |
| product.target_market | Object | Product design | Section 42(2) |
| product.risk_assessment | Object | Risk analysis | Section 42(3) |
| product.distribution_plan | Object | Distribution strategy | Section 42(4) |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: ProductGovernance

---

## 10. InvestmentInsuranceSuitability

**Decision:** Determine suitability assessment requirements

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| product.type | Enum | Product classification | Section 5(12) |
| broker.provides_recommendation | Boolean | Sales record | Section 49 |
| customer.experience.level | Enum | Customer interview | Section 49 |
| customer.knowledge.level | Enum | Customer interview | Section 49 |
| customer.financial.situation | Object | Customer interview | Section 50 |
| customer.objectives | List | Customer interview | Section 50 |
| customer.risk_tolerance | Enum | Risk assessment | Section 50 |
| customer.professional_status | Boolean | Customer classification | Section 54 |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: InvestmentInsuranceSuitability

---

## 11. ProfessionalLiabilityInsurance

**Decision:** Determine liability insurance requirements

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| broker.registration.status | Boolean | FIN-FSA register | Section 58 |
| insurance.coverage.per_claim | Number | Policy | Section 58(1) |
| insurance.coverage.annual | Number | Policy | Section 58(1) |
| insurance.geographic_coverage | List | Policy | Section 58(2) |
| insurance.cancellation_terms | Object | Policy | Section 58(2) |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: ProfessionalLiabilityInsurance

---

## 12. ClientAssetSegregation

**Decision:** Determine client asset handling requirements

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| broker.holds_client_funds | Boolean | Business model | Section 59 |
| client_funds.account_type | Enum | Bank records | Section 59 |
| customer.type | Enum | Customer classification | Section 59 |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: ClientAssetSegregation

---

## 13. CrossBorderNotification

**Decision:** Determine cross-border notification requirements

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| intermediary.EEA_plans | Boolean | Business plan | Section 22 |
| intermediary.countries_targeted | List | Business plan | Section 22 |
| intermediary.establishment_type | Enum | Business plan | Section 22(2) |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: CrossBorderNotification

---

## 14. AdministrativeSanctions

**Decision:** Determine available sanctions

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| entity.registration_status | Boolean | FIN-FSA register | Section 70 |
| violation.severity | Enum | Investigation | Section 71 |
| violation.count | Number | Compliance records | Section 73 |
| violation.damage_amount | Number | Claims records | Section 74 |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: SanctionPowers

---

## 15. CompensationLiability

**Decision:** Determine compensation liability

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| broker.breach.type | Enum | Investigation | Section 74 |
| customer.damage.proven | Boolean | Claims investigation | Section 74 |
| customer.damage.amount | Number | Assessment | Section 74 |
| broker.professional_conduct | Boolean | Compliance review | Section 74 |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: CompensationLiability

---

## 16. ConfidentialityObligations

**Decision:** Determine confidentiality requirements

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| employee.accessed_customer_data | Boolean | Access logs | Section 79 |
| authority.request.legitimate | Boolean | Official request | Section 80 |
| disclosure.purpose | Enum | Request documentation | Section 80 |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: ConfidentialityObligations

---

## 17. DocumentRetention

**Decision:** Determine document retention requirements

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| document.type | Enum | Document classification | Section 78 |
| document.date | Date | Document metadata | Section 78 |
| retention.start_date | Date | Expiry calculation | Section 78 |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: DocumentRetention

---

## 18. MarketingRequirements

**Decision:** Determine marketing compliance

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| communication.type | Enum | Communication classification | Section 34 |
| communication.content | Object | Marketing materials | Section 34 |
| information.accuracy | Boolean | Compliance review | Section 34 |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: MarketingRequirements

---

## 19. TyingProhibition

**Decision:** Determine tying and bundling rules

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| customer.type | Enum | Customer classification | Sections 40-41 |
| product.bundling.type | Enum | Product design | Section 41 |
| product.separate_pricing | Boolean | Pricing structure | Section 41 |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: TyingAndBundling

---

## 20. WhistleblowingProcedure

**Decision:** Determine whistleblowing requirements

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| company.type | Enum | Business registration | Section 72 |
| channel.independent | Boolean | Internal systems | Section 72 |
| protection.measures | List | Policy documents | Section 72 |

### Rule Reference
- `insurance_distribution_dmn_rules.json` - Decision: WhistleblowingRequirement

---

## Data Sources Summary

| Source | Type | Contains |
|--------|------|-----------|
| FIN-FSA Register | Government | Registration status, sanctions |
| Criminal Record | Government | Conviction history |
| Bankruptcy Register | Government | Bankruptcy status |
| Trade Register | Government | Business registration |
| Customer Interview | Primary | Needs, financial situation |
| Insurance Policy | Contract | Coverage terms |
| Training Records | Internal | Education hours |
| Sales Records | Internal | Recommendations |
