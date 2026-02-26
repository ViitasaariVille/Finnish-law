# Liikennevakuutuslaki DMN Rules - Complete Hierarchical Structure

## Finnish Traffic Insurance Act (460/2016) - Full Rule Set

---

## HIERARCHY OVERVIEW

### Level 1: ELIGIBILITY (Positive - What IS Covered)

| Category | Decisions | Sections |
|----------|-----------|----------|
| Coverage Determination | E1-E4 | §§5-6, 10-12 |
| Compensation Calculation | E5-E8 | §§3, 34-35, 54 |
| Benefit Entitlement | E9-E10 | §§36-38 |
| Premium Calculation | E11 | §§89-92 |
| Time Limits | E12-E13 | §§74, 77 |

**Total: 13 eligibility decisions**

### Level 2: NEGATIVE CLAIMS (What is NOT Covered)

| Category | Decisions | Sections |
|----------|-----------|----------|
| Full Denial | N1-N9 | §§41, 41a, 43, 44, 46-50 |
| Reduced Compensation | N10-N11 | §§47-48 |
| Conditional Compensation | N12-N17 | §§41, 41a, 43, 44, 46, 48 |

**Total: 17 negative claim decisions**

---

## SECTION 1: ELIGIBILITY RULES

### 1.1 Coverage Determination

#### E1: Vehicle Insurance Requirement (§5)

| vehicle.registrationCountry | vehicle.requiresInsurance | vehicle.vehicleType | Output |
|----------------------------|---------------------------|---------------------|--------|
| FI | true | MotorVehicle | **MandatoryTrafficInsurance** |
| FI | true | Trailer | **MandatoryTrafficInsurance** |
| EEA | true | any | CheckRegistrationCountry |
| Non-EEA | true | any | **MandatoryTrafficInsurance** |

#### E2: Damage Coverage (§§12-16)

| damage.damageType | damage.isPersonalInjury | damage.isPropertyDamage | Output |
|-------------------|-------------------------|------------------------|--------|
| PersonalInjury | true | false | **COVERED_100** |
| PersonalInjury | true | true | **COVERED_100** |
| PropertyDamage | false | true | **COVERED_100** |
| VehicleDamage | false | true | **COVERED_100** |
| EnvironmentalDamage | false | true | **COVERED_100** |

#### E3: International Coverage (§§10-11)

| accident.locationCountry | greenCard.valid | vehicle.registeredCountry | Output |
|--------------------------|-----------------|-------------------------|--------|
| Finland | any | FI | **FullCoverage** |
| EEA | true | any | **FullCoverage_GreenCard** |
| EEA | false | any | LimitedCoverage_BureauGuarantee |
| Non-EEA | any | any | CheckBilateralAgreement |

#### E4: Insurance Obligation Liable Party (§6)

| person.owner.exists | person.holder.exists | vehicle.ownershipTransferred | Output |
|---------------------|----------------------|------------------------------|--------|
| true | true | true | **OwnerAndHolderJointlyLiable** |
| true | false | true | **OwnerLiable** |
| false | true | true | **HolderLiable** |
| true | false | false | **OwnerLiableFromOwnership** |

---

### 1.2 Compensation Calculation

#### E5: Medical Expense Compensation (§§53-59)

| medicalExpense.treatmentType | medicalExpense.isNecessary | medicalExpense.providerType | Output |
|------------------------------|---------------------------|---------------------------|--------|
| Emergency | true | public | **100_PERCENT** |
| Emergency | true | private | **100_PERCENT_REIMBURSEMENT** |
| Surgery | true | any | **100_PERCENT** |
| Medicines | true | pharmacy | **100_PERCENT** |
| Rehabilitation | true | any | **100_PERCENT** |
| DentalTreatment | true | any | **100_PERCENT** |
| Prosthesis | true | any | **100_PERCENT** |
| TravelToTreatment | true | any | **100_PERCENT** |

#### E6: Lost Wages Compensation (§34)

| person.incomeType | person.netMonthlyIncome | person.annualIncome | injury.workAbilityLostDays | Output |
|-------------------|------------------------|---------------------|----------------------------|--------|
| Employed | any | null | any | Calculate_NetMonthly/30×Days |
| SelfEmployed | null | any | any | Calculate_Annual/365×Days |
| Unemployed | any | null | any | **Minimum_36.90_PerDay** |
| Student | any | null | any | StudentGrant_Adjustment |

#### E7: Pain and Suffering Compensation (§35)

| injury.isPermanent | injury.permanentDisabilityPercentage | painSuffering.level | Output |
|-------------------|---------------------------------------|---------------------|--------|
| true | 1-10_PERCENT | moderate | Scale_1_10_Percent |
| true | 11-20_PERCENT | moderate | Scale_11_20_Percent |
| true | 21-50_PERCENT | significant | Scale_21_50_Percent |
| true | 51-100_PERCENT | severe | Scale_51_100_Percent |
| false | null | any | TemporaryPain_Scale |

#### E8: Property Damage Compensation (§3)

| property.type | property.marketValue | damage.severity | Output |
|---------------|---------------------|-----------------|--------|
| Vehicle | any | TotalLoss | **MarketValue** |
| Vehicle | any | PartialDamage | **RepairCost** |
| ThirdPartyProperty | any | any | **ActualValue** |
| Clothing | any | any | **ReplacementValue** |

---

### 1.3 Benefit Entitlement

#### E9: Death Compensation (§§36-38)

| deceased.hasIncome | survivor.relationship | survivor.isDependent | Output |
|-------------------|----------------------|---------------------|--------|
| true | Spouse | true | **SpousePension_Plus_LumpSum** |
| true | Child | true | **ChildPension** |
| false | Dependent | true | **LumpSum** |
| any | Parent | true | FuneralExpenses_Plus_Compensation |

#### E10: Disability Compensation (§35)

| injury.permanentDisabilityPercentage | injury.affectsWorkAbility | person.ageAtInjury | Output |
|--------------------------------------|---------------------------|-------------------|--------|
| 1-10_PERCENT | true | any | **DisabilityPension_Low** |
| 11-30_PERCENT | true | any | **DisabilityPension_Medium** |
| 31-100_PERCENT | true | any | **DisabilityPension_High** |

---

### 1.4 Premium Calculation

#### E11: Premium Calculation (§§89-92)

| vehicle.vehicleType | driver.age | claim.historyClaimCount | vehicle.usagePurpose | Output |
|--------------------|------------|------------------------|---------------------|--------|
| PrivateCar | over_25 | 0 | Private | **BasePremium** |
| PrivateCar | under_25 | 0 | Private | BasePremium×1.5 |
| PrivateCar | any | positive | any | BasePremium+ClaimLoading |
| Commercial | any | any | Commercial | **CommercialRate** |

---

### 1.5 Time Limits

#### E12: Claim Time Limit (§74)

| claim.damageType | accident.date | claim.submissionDate | Output |
|------------------|---------------|----------------------|--------|
| PersonalInjury | any | any | Within_3_Years_From_Injury |
| PropertyDamage | any | within_1_year | Within_1_Year_From_Accident |
| PropertyDamage | any | after_1_year | **ClaimTimeBarred** |

#### E13: Insolvency Protection (§77)

| insuranceCompany.status | insurance.policyActive | claim.isPending | Output |
|------------------------|----------------------|-----------------|--------|
| Insolvent | true | true | **FinnishGuaranteeFund_Pays** |
| Insolvent | true | false | TransferToAnotherInsurer |
| Healthy | true | true | NormalClaimsProcess |

---

## SECTION 2: NEGATIVE CLAIMS RULES

### 2.1 Full Denial

#### N1: Unauthorized Use (§49)

| vehicle.usedWithoutPermission | vehicle.ownerConsent | driver.isAuthorized | Output |
|------------------------------|----------------------|-------------------|--------|
| true | false | false | **NOT_COVERED** |

#### N2: Insanity/Emergency (§50)

| driver.isInsane | driver.inEmergency | driver.isResponsible | Output |
|----------------|-------------------|---------------------|--------|
| true | false | false | **NOT_COVERED** |
| false | true | false | **NOT_COVERED** |

#### N3: Theft Property Damage (§41)

| vehicle.theft.reported | accident.occurredAfterTheft | insurance.policyStatus | damage.damageType | Output |
|------------------------|----------------------------|----------------------|-------------------|--------|
| true | true | terminated | PropertyDamage | **NOT_COVERED** |

#### N4: Unauthorized Competition (§41a)

| driver.isCompetitionParticipant | event.isAuthorized | driver.licenseValid | Output |
|--------------------------------|-------------------|---------------------|--------|
| true | false | any | **NOT_COVERED** |
| true | true | false | **NOT_COVERED** |

#### N5: Exempt Vehicle Property (§43)

| vehicle.isExempt | vehicle.exemptType | damage.damageType | Output |
|-----------------|-------------------|-------------------|--------|
| true | Military | PropertyDamage | **NOT_COVERED** |
| true | Diplomatic | PropertyDamage | **NOT_COVERED** |
| true | Government | PropertyDamage | **NOT_COVERED** |

#### N6: Unknown Vehicle No Report (§44)

| vehicle.isUnknown | police.reportFiled | damage.damageType | Output |
|------------------|-------------------|-------------------|--------|
| true | false | PropertyDamage | **NOT_COVERED** |

#### N7: No Insurance Property (§46)

| insurance.obligationMet | insurance.exists | damage.damageType | Output |
|------------------------|-----------------|-------------------|--------|
| false | false | PropertyDamage | **NOT_COVERED** |

#### N8: Victim Gross Negligence (§47)

| victim.causedDamage | victim.contributionDegree | Output |
|--------------------|-------------------------|--------|
| true | GrossNegligence | **NOT_COVERED** |

#### N9: Drunk Driver Sole Fault (§48)

| driver.bloodAlcoholLevel | driver.contributionDegree | victim.isAtFault | Output |
|-------------------------|--------------------------|-----------------|--------|
| >=1.2_permille | SoleFault | false | **NOT_COVERED** |

---

### 2.2 Reduced Compensation

#### N10: Victim Contribution (§47)

| victim.causedDamage | victim.contributionDegree | damage.damageType | Output |
|--------------------|--------------------------|-------------------|--------|
| true | Negligence | PropertyDamage | **50_PERCENT** |
| true | Slight | any | **75_PERCENT** |
| true | Moderate | any | **50_PERCENT** |

#### N11: Alcohol Impairment (§48)

| driver.bloodAlcoholLevel | driver.contributionDegree | victim.isAtFault | Output |
|--------------------------|--------------------------|-----------------|--------|
| >=1.2_permille | PartialFault | false | **50_PERCENT** |
| 0.5-1.19_permille | PartialFault | false | **75_PERCENT** |
| 0.5-1.19_permille | SoleFault | false | **NOT_COVERED** |

---

### 2.3 Conditional Compensation

#### N12: Theft Personal Injury (§41)

| vehicle.theft.reported | accident.occurredAfterTheft | insurance.policyStatus | damage.damageType | Output |
|------------------------|----------------------------|----------------------|-------------------|--------|
| true | true | active | PersonalInjury | **COVERED** |
| false | any | active | any | **COVERED** |

#### N13: Authorized Competition (§41a)

| driver.isCompetitionParticipant | event.isAuthorized | driver.licenseValid | damage.damageType | Output |
|--------------------------------|-------------------|---------------------|-------------------|--------|
| true | true | true | PersonalInjury | **COVERED** |
| true | true | true | PropertyDamage | **COVERED** |
| false | any | any | any | **COVERED** |

#### N14: Exempt Vehicle Personal Injury (§43)

| vehicle.isExempt | damage.damageType | Output |
|-----------------|-------------------|--------|
| true | PersonalInjury | **COVERED** |

#### N15: Unknown Vehicle Personal Injury (§44)

| vehicle.isUnknown | police.reportFiled | damage.damageType | Output |
|------------------|-------------------|-------------------|--------|
| true | true | PersonalInjury | **COVERED** |
| true | true | PropertyDamage | **COVERED_GuaranteeFund** |

#### N16: No Insurance Personal Injury (§46)

| insurance.exists | damage.damageType | Output |
|-----------------|-------------------|--------|
| false | PersonalInjury | **COVERED_GuaranteeFund** |
| true | any | **COVERED** |

#### N17: Third Party Victim (§48)

| driver.bloodAlcoholLevel | victim.relationshipType | victim.isAtFault | Output |
|--------------------------|-------------------------|-----------------|--------|
| >=1.2_permille | ThirdParty | false | **COVERED** |
| 0.5-1.19_permille | ThirdParty | false | **COVERED** |
| <0.5_permille | any | false | **COVERED** |

---

## DECISION FLOW DIAGRAM

```
Claim Received
       │
       ▼
┌─────────────────────┐
│ Check Eligibility  │───→ E1-E13
│ (Coverage, Calc,   │
│  Benefits, Time)   │
└──────────┬──────────┘
           │ Eligible
           ▼
┌─────────────────────┐
│ Check Negative     │───→ N1-N17
│ Claims             │
│ (Denial, Reduce,   │
│  Conditional)      │
└──────────┬──────────┘
           │ Approved
           ▼
    COMPENSATION PAID
```

---

## VARIABLE NAMING CONVENTION

All variables follow `entity.attribute` format matching the business ontology:

| Entity | Attributes |
|--------|-----------|
| **vehicle** | registrationCountry, requiresInsurance, vehicleType, isExempt, exemptType, usedWithoutPermission, ownerConsent, isUnknown, theft.reported |
| **driver** | isAuthorized, isInsane, inEmergency, isResponsible, isCompetitionParticipant, licenseValid, bloodAlcoholLevel, contributionDegree |
| **damage** | damageType, isPersonalInjury, isPropertyDamage, severity |
| **person** | incomeType, netMonthlyIncome, annualIncome, ageAtInjury |
| **injury** | isPermanent, permanentDisabilityPercentage, workAbilityLostDays, affectsWorkAbility |
| **insurance** | policyStatus, exists, obligationMet |
| **claim** | damageType, submissionDate, isPending |
| **survivor** | relationship, isDependent |
| **accident** | locationCountry, occurredAfterTheft |
| **greenCard** | valid |
| **police** | reportFiled |
| **event** | isAuthorized |

---

## METADATA

- **Law**: Liikennevakuutuslaki (Traffic Insurance Act) 460/2016
- **Source**: finlex.fi/fi/lainsaadanto/2016/460
- **Version**: 1.2 (Complete Hierarchical)
- **Total Decisions**: 30 (13 Eligibility + 17 Negative Claims)
- **Variable Convention**: entity.attribute (ontology-aligned)
