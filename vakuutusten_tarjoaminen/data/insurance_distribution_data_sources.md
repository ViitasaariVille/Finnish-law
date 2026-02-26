# Insurance Distribution (Laki vakuutusten tarjoamisesta 234/2018) - Data Sources

This file maps **data points** to their **sources** for the Insurance Distribution Act business rules.

---

## 1. Government Registers

### FIN-FSA (Financial Supervisory Authority)
| Data Point | Register | Access |
|-----------|----------|--------|
| broker.registration_number | Insurance Distribution Register | Public |
| broker.registration_status | Insurance Distribution Register | Public |
| entity.registration_status | Insurance Distribution Register | Public |
| insurer.license_status | Insurance Distribution Register | Public |
| violation.severity | Sanctions register | Public |

**Website:** www.finanssivalvonta.fi

### Criminal Record (Rikosrekisteri)
| Data Point | Register | Access |
|-----------|----------|--------|
| person.conviction.type | Criminal record | Police |
| person.conviction.date | Criminal record | Police |

**Website:** www.poliisi.fi/rikosrekisteri

### Bankruptcy Register (Konkurssirekisteri)
| Data Point | Register | Access |
|-----------|----------|--------|
| person.bankruptcy_status | Bankruptcy register | National |
| broker.bankruptcy_status | Bankruptcy register | National |

**Website:** www.konkurssirekisteri.fi

### Trade Register (Kaupparekisteri)
| Data Point | Register | Access |
|-----------|----------|--------|
| broker.registered_in_finland | Trade register | Public |
| company.type | Trade register | Public |
| company.finland_registration | Trade register | Public |

**Website:** www.kaupparekisteri.fi

### Business Ban Register (Liiketoimintakieltorekisteri)
| Data Point | Register | Access |
|-----------|----------|--------|
| person.business_ban | Business ban register | Public |

---

## 2. Insurance Industry Sources

### Finnish Insurance Association (Finanss Finland)
| Data Point | Source | Access |
|-----------|--------|--------|
| broker.liability_insurance | Insurance policy | Policy document |
| insurance.coverage.per_claim | Insurance policy | Policy document |
| insurance.coverage.annual | Insurance policy | Policy document |
| insurance.geographic_coverage | Insurance policy | Policy document |

### Individual Insurance Companies
| Data Point | Source | Access |
|-----------|--------|--------|
| broker.principals | Agency agreement | Contract |
| insurer.name | Business registration | Certificate |

---

## 3. Internal Business Records

### Broker/Company Internal Systems
| Data Point | Source | System |
|-----------|--------|--------|
| broker.staff.registered_ratio | HR records | HR system |
| broker.client_assets_system | Client funds | Accounting |
| professional.training.hours_per_year | Training records | LMS |
| professional.training.certificates | Training records | LMS |
| customer.existing_insurance | Customer data | CRM |
| customer.risk_profile | Needs assessment | Sales system |
| customer.financial_situation | Customer interview | CRM |
| customer.objectives | Customer interview | Sales system |
| broker.recommendation.given | Sales record | Sales system |
| communication.content | Marketing materials | Marketing |
| document.type | Document classification | DMS |
| document.date | Document metadata | DMS |

---

## 4. Customer Information

### Customer Interview
| Data Point | Method |
|-----------|--------|
| customer.type | Application form |
| customer.experience.level | Interview |
| customer.knowledge.level | Interview |
| customer.financial.situation | Interview |
| customer.objectives | Interview |
| customer.risk_tolerance | Risk questionnaire |
| customer.professional_status | Application |

### Customer Classification
| Data Point | Classification Criteria |
|-----------|------------------------|
| customer.type = "Consumer" | Natural person, non-business |
| customer.type = "Professional" | Per Section 5(13) |
| customer.type = "Commercial" | Business customer |

---

## 5. Regulatory Sources

### Finnish Legislation
| Data Point | Source |
|-----------|--------|
| entity.type | This Act (234/2018) |
| activity.level | This Act Section 4 |
| annual_premium | This Act Section 4 |
| broker.not_employed_by_insurer | This Act Section 8(1) |

### EU Sources
| Data Point | Source |
|-----------|--------|
| insurance.geographic_coverage = "EEA" | EU membership |
| intermediary.EEA_plans | EU Single Market |

---

## 6. Investigation & Compliance

### Compliance Investigation
| Data Point | Source |
|-----------|--------|
| broker.breach.type | Internal investigation |
| violation.count | Compliance records |
| broker.professional_conduct | Compliance review |

### Claims Investigation
| Data Point | Source |
|-----------|--------|
| customer.damage.proven | Claims investigation |
| customer.damage.amount | Loss assessment |

---

## Data Access Summary

| Source Type | Examples | Typical Access |
|-------------|----------|----------------|
| Public Registers | Trade register, FIN-FSA | Online / API |
| Government | Criminal record, Bankruptcy | Authorized request |
| Insurance Companies | Policy details | Contract review |
| Internal Records | Training, Sales, CRM | Direct access |
| Customer | Interview, Application | Direct collection |
| Regulatory | Finnish law, EU directives | Published |

---

## Key Authorities

| Authority | Finnish Name | Role |
|-----------|--------------|------|
| FIN-FSA | Finanssivalvonta | Supervision, registration |
| Police | Poliisi | Criminal records |
| Ministry | Sosiaali- ja terveysministeriö | Policy |
| EIOPA | Euroopan vakuutusviranomainen | EU coordination |
