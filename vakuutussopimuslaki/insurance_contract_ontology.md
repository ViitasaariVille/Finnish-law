# Finnish Insurance Contract Act - Ontology

**Based on:** Vakuutussopimuslaki (Insurance Contract Act) 543/1994  
**Version:** 1.1  
**Source:** https://www.finlex.fi/fi/lainsaadanto/1994/543

---

## 1. Core Entities

### InsuranceContract (Vakuutussopimus)
- **Description:** Contract between insurer and policyholder
- **Legal Basis:** Section 1
- **Subclasses:**
  - **LifeInsurance (Henkilövakuutus):** Insurance with natural person as subject (§2.1)
  - **NonLifeInsurance (Vahinkovakuutus):** Insurance for property damage or liability (§2.2)
  - **InvestmentInsurance (Sijoitusvakuutus):** Life insurance with investment component (§2.2a)
  - **CapitalRedemptionContract (Kapitalisaatiosopimus):** Investment without insured person (§4a)
  - **GroupInsurance (Ryhmävakuutus):** Insurance for group members (§2.6)
  - **GroupBenefitInsurance (Ryhmäetuvakuutus):** Group insurance where members pay premium

### Insurer (Vakuutuksenantaja)
- **Description:** Entity granting insurance
- **Legal Basis:** Section 2(3)

### Policyholder (Vakuutuksenottaja)
- **Description:** Party making insurance contract with insurer
- **Legal Basis:** Section 2(4)

### Insured (Vakuutettu)
- **Description:** Person who is subject of life insurance or beneficiary of non-life insurance
- **Legal Basis:** Section 2(5)

### Beneficiary (Edunsaaja)
- **Description:** Person entitled to insurance benefit
- **Legal Basis:** Section 47

---

## 2. Financial Entities

### InsurancePremium (Vakuutusmaksu)
- **Description:** Payment for insurance
- **Legal Basis:** Section 38

### InsuranceSum (Vakuutusmäärä)
- **Description:** Maximum insurance amount
- **Legal Basis:** Section 57

### SurrenderValue (Takaisinostoarvo)
- **Description:** Cash value of life insurance
- **Legal Basis:** Section 13

### FreePolicy (Vapaakirja)
- **Description:** Paid-up insurance policy
- **Legal Basis:** Section 13

### InsurancePeriod (Vakuutuskausi)
- **Description:** Insurance contract period
- **Legal Basis:** Section 12

---

## 3. Document Entities

### PolicyDocument (Vakuutuskirja)
- **Description:** Document with key contract terms
- **Legal Basis:** Section 6

### InsuranceTerms (Vakuutusehdot)
- **Description:** Terms and conditions of insurance
- **Legal Basis:** Section 6

### AnnualNotice (Vuositiedote)
- **Description:** Annual notice to policyholder
- **Legal Basis:** Section 7

---

## 4. Claim & Event Entities

### Claim (Korvausvaatimus)
- **Description:** Insurance compensation claim
- **Legal Basis:** Section 69

### InsuranceEvent (Vakuutustapahtuma)
- **Description:** Event triggering insurance coverage
- **Legal Basis:** Section 2

### ThirdPartyClaim (Kolmannen osapuolen korvausvaatimus)
- **Description:** Third party right to compensation
- **Legal Basis:** Section 67

---

## 5. Rights & Duties

### DutyOfDisclosure (Tiedonantovelvollisuus)
- **Description:** Duty to provide information
- **Legal Basis:** Sections 22-24
- **Subclasses:**
  - **NonLifeDisclosure:** Non-life insurance disclosure (§23)
  - **LifeDisclosure:** Life insurance disclosure (§24)

### RightToCancel (Peruutusoikeus)
- **Description:** Right to cancel insurance
- **Legal Basis:** Section 13a

### RightToTerminate (Irtisanoisoikeus)
- **Description:** Right to terminate insurance
- **Legal Basis:** Section 12

### ContinuationInsurance (Jatkovakuutus)
- **Description:** Right to continue insurance after surrender
- **Legal Basis:** Section 14

### SafetyInstructions (Suojeluohjeet)
- **Description:** Safety instructions to follow
- **Legal Basis:** Section 31

### SalvageDuty (Pelastamisvelvollisuus)
- **Description:** Duty to prevent or reduce loss
- **Legal Basis:** Section 32

### RightToAppeal (Muutoksenhaku)
- **Description:** Right to appeal compensation decision
- **Legal Basis:** Section 68

---

## 6. Risk Entities

### RiskIncrease (Vaaran lisääntyminen)
- **Description:** Increase in risk
- **Legal Basis:** Sections 26-27
- **Subclasses:**
  - **NonLifeRiskIncrease:** Risk increase in non-life (§26)
  - **LifeRiskIncrease:** Risk increase in life (§27)

### OverInsurance (Ylivakuutus)
- **Description:** Insurance exceeding actual value
- **Legal Basis:** Section 57

### UnderInsurance (Alivakuutus)
- **Description:** Insurance less than actual value
- **Legal Basis:** Section 58

### MultipleInsurance (Monivakuutus)
- **Description:** Multiple insurance for same risk
- **Legal Basis:** Section 59

### SalvageCosts (Pelastamiskustannukset)
- **Description:** Costs to prevent or reduce loss
- **Legal Basis:** Section 61

---

## 7. Legal Process Entities

### Distraint (Ulosmittaus)
- **Description:** Distraint of insurance benefits
- **Legal Basis:** Sections 54-55
- **Subclasses:**
  - **LifeInsuranceDistraint:** Distraint of life insurance (§54)
  - **AccidentInsuranceDistraint:** Distraint of accident insurance (§55)

### BankruptcyRecovery (Takaisinsaanti konkurssissa)
- **Description:** Recovery in bankruptcy
- **Legal Basis:** Section 56

### ThirdPartyRights (Kolmannen osapuolen oikeudet)
- **Description:** Third party rights in non-life insurance
- **Legal Basis:** Section 62

---

## 8. Information Entities

### InformationDuty (Tiedottamisvelvollisuus)
- **Description:** Duty to provide pre-contract information
- **Legal Basis:** Section 5

### PreContractInformation
- **Description:** Information before contract (§5)
- **Includes:** Insurance forms, premiums, terms, needs assessment

### InformationDeliveryMethod
- **Description:** How information must be delivered (§5a)
- **Methods:** Paper, durable medium, website

---

## 9. Group Insurance Entities

### GroupInsurancePolicy (Ryhmävakuutussopimus)
- **Description:** Group insurance contract
- **Legal Basis:** Section 2(6)

### GroupRepresentative (Ryhmän edustaja)
- **Description:** Representative of insurance group
- **Legal Basis:** Section 76

### ContinuationAfterGroup (Jatkovakuutus ryhmän jälkeen)
- **Description:** Right to continue individually after group ends
- **Legal Basis:** Section 80

---

## Relationships

| From | To | Type |
|------|----|------|
| Policyholder | Insurer | makes_contract_with |
| LifeInsurance | Insured | covers |
| NonLifeInsurance | Insured | covers |
| Beneficiary | LifeInsurance | entitled_to_benefit |
| Policyholder | InsurancePremium | pays |
| Claim | InsuranceEvent | arises_from |
| Insurer | Claim | processes |
| LifeInsurance | SurrenderValue | has |
| LifeInsurance | FreePolicy | can_become |
| NonLifeInsurance | ThirdPartyRights | grants |
| Insured | DutyOfDisclosure | owes |

---

## Key Legal References

| Section | Topic | Entity |
|---------|-------|--------|
| §1 | Scope | InsuranceContract |
| §2 | Definitions | All core entities |
| §3 | Mandatory terms | InsuranceContract |
| §5-9 | Information duties | InformationDuty |
| §10-21 | Insurance validity | InsurancePeriod |
| §12 | Termination | RightToTerminate |
| §13 | Surrender value | SurrenderValue |
| §13a | Cancellation | RightToCancel |
| §14 | Continuation | ContinuationInsurance |
| §22-24 | Disclosure duty | DutyOfDisclosure |
| §26-27 | Risk increase | RiskIncrease |
| §31-32 | Safety/Salvage | SafetyInstructions, SalvageDuty |
| §34-37 | Liability limits | Various |
| §38-46 | Premium | InsurancePremium |
| §47-53 | Beneficiaries | Beneficiary |
| §54-56 | Distraint/Bankruptcy | Distraint, BankruptcyRecovery |
| §57-61 | Compensation | Claim, OverInsurance, UnderInsurance |
| §62-68 | Third party | ThirdPartyClaim, ThirdPartyRights |
| §69-75 | Claims | Claim |
| §76-80 | Group insurance | GroupInsurance |

---

*Total: 30+ entities covering Vakuutussopimuslaki (543/1994)*
