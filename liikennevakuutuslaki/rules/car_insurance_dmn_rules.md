# Liikennevakuutuslaki DMN Rules - Complete Hierarchical Structure

## Finnish Traffic Insurance Act (460/2016) - Full Rule Set

---

## HIERARCHY OVERVIEW

### Level 1: NEGATIVE CLAIMS (What is NOT Covered - Check FIRST)

| Category | Decisions | Sections |
|----------|-----------|----------|
| Full Denial | N1-N9 | §§41, 41a, 43, 44, 46-50 |
| Reduced Compensation | N10-N11 | §§47-48 |
| Conditional Compensation | N12-N17 | §§41, 41a, 43, 44, 46, 48 |

**Total: 17 negative claim decisions**

### Level 2: ELIGIBILITY (Positive - What IS Covered)

| Category | Decisions | Sections |
|----------|-----------|----------|
| Coverage Determination | E1-E4 | §§5-6, 10-12 |
| Compensation Calculation | E5-E8 | §§3, 34-35, 54 |
| Benefit Entitlement | E9-E10 | §§36-38 |
| Premium Calculation | E11 | §§89-92 |
| Time Limits | E12-E13 | §§74, 77 |

**Total: 13 eligibility decisions**

---

## DECISION FLOW DIAGRAM

```
Claim Received
       │
       ▼
┌─────────────────────┐
│ 1. NEGATIVE CLAIMS │───→ N1-N17
│ (Exclusions,        │     Full Denial
│  Denials,          │     Reduced Compensation
│  Reductions)       │     Conditional
└──────────┬──────────┘
           │ Pass (No exclusion)
           ▼
┌─────────────────────┐
│ 2. ELIGIBILITY     │───→ E1-E13
│ (Coverage, Calc,   │     Coverage Determination
│  Benefits, Time)   │     Compensation Calculation
└──────────┬──────────┘
           │ Eligible
           ▼
    COMPENSATION PAID
```

---

## SECTION 1: NEGATIVE CLAIMS RULES (Check First)

### 1.1 Full Denial

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

### 1.2 Reduced Compensation

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

### 1.3 Conditional Compensation

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

## SECTION 2: ELIGIBILITY RULES (Check After Negative Claims)

### 2.1 Coverage Determination

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

### 2.2 Compensation Calculation

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

### 2.3 Benefit Entitlement

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

### 2.4 Premium Calculation

#### E11: Premium Calculation (§§89-92)

| vehicle.vehicleType | driver.age | claim.historyClaimCount | vehicle.usagePurpose | Output |
|--------------------|------------|------------------------|---------------------|--------|
| PrivateCar | over_25 | 0 | Private | **BasePremium** |
| PrivateCar | under_25 | 0 | Private | BasePremium×1.5 |
| PrivateCar | any | positive | any | BasePremium+ClaimLoading |
| Commercial | any | any | Commercial | **CommercialRate** |

---

### 2.5 Time Limits

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

## VARIABLE NAMING CONVENTION

All variables follow `entity.attribute` format matching the business ontology:

| Entity | Attributes |
|--------|-----------|
| **vehicle** | registrationCountry, requiresInsurance, vehicleType, isExempt, exemptType, usedWithoutPermission, ownerConsent, isUnknown, theft.reported |
| **driver** | isAuthorized, isInsane, inEmergency, isResponsible, isCompetitionParticipant, licenseValid, bloodAlcoholLevel, contributionDegree |
| **damage** | damageType, isPersonalInjury, isPropertyDamage, severity |
| **injury** | isPermanent, permanentDisabilityPercentage, workAbilityLostDays, affectsWorkAbility |
| **insurance** | policyStatus, exists, obligationMet |
| **person** | incomeType, netMonthlyIncome, annualIncome, ageAtInjury |
| **survivor** | relationship, isDependent |
| **accident** | locationCountry, occurredAfterTheft |
| **claim** | damageType, submissionDate, isPending |
| **greenCard** | valid |
| **police** | reportFiled |
| **event** | isAuthorized |

---

## METADATA

- **Law**: Liikennevakuutuslaki (Traffic Insurance Act) 460/2016
- **Source**: finlex.fi/fi/lainsaadanto/2016/460
- **Version**: 1.3 (Negative Claims First)
- **Total Decisions**: 30 (17 Negative Claims + 13 Eligibility)
- **Decision Order**: Negative Claims → Eligibility → Compensation
- **Variable Convention**: entity.attribute (ontology-aligned)


---

## SECTION 2: ELIGIBILITY RULES

### 2.1 Coverage Determination (Positive Rules)

#### E15: Scope of Application (§1)

| vehicle.inTraffic | vehicle.purpose | vehicle.location | Output |
|-------------------|-----------------|-----------------|--------|
| false | construction_other | any | **NOT_IN_SCOPE** |
| false | repair_maintenance | any | **NOT_IN_SCOPE** |
| true | transport | any | **IN_SCOPE** |

#### E16: Definition - Vehicle Types (§2)

| vehicle.mechanical | vehicle.speed | vehicle.weight | Output |
|-------------------|---------------|----------------|--------|
| true | >25_kmh | any | **COVERED_VEHICLE** |
| true | any | >25_kg | **COVERED_VEHICLE** |
| false | any | any | **NOT_COVERED** |

#### E17: Mandatory Nature (§3)

| contract.contrary_to_law | party.damaged | Output |
|--------------------------|---------------|--------|
| true | true | **VOID_CONTRACT** |
| false | any | **VALID_CONTRACT** |

#### E18: Liikennevakuutuskeskus Role (§4)

| entity.type | function.requested | Output |
|-------------|-------------------|--------|
| Centre | funding | **CENTRE_RESPONSIBLE** |
| Centre | administration | **CENTRE_RESPONSIBLE** |

#### E19: Insurance Contract Act Application (§4a)

| section.applied | Output |
|-----------------|--------|
| 3 | **APPLIES** |
| 4b | **APPLIES** |
| 5 | **APPLIES** |

#### E20: Consumer Protection Application (§4b)

| policyholder.type | Output |
|------------------|--------|
| consumer | **CONSUMER_PROTECTION_APPLIES** |
| business | **NOT_APPLIES** |

#### E21: Vehicles to Insure (§5)

| vehicle.permanent_location | vehicle.type | Output |
|---------------------------|--------------|--------|
| Finland | covered_type | **MUST_INSURE** |
| Finland | exempt_type | **EXEMPT** |

#### E22: Insurance Obligation Begins (§6)

| ownership_date | delivery_date | Output |
|---------------|---------------|--------|
| date | any | **OBLIGATION_STARTS** |
| future | date | **OBLIGATION_STARTS** |

#### E23: Import from EEA (§6a)

| vehicle.imported_from | registration.country | Output |
|----------------------|---------------------|--------|
| EEA | Finland | **CAN_CHOOSE_FINLAND** |
| EEA | origin_country | **MUST_INSURE_ORIGIN** |

#### E24: Border Traffic Insurance (§7)

| vehicle.permanent_country | green_card | accident.country | Output |
|--------------------------|------------|-----------------|--------|
| third_country | false | Finland | **MUST_INSURE** |
| third_country | true | any | **GREEN_CARD_OK** |

#### E25: Exemptions from Insurance (§8)

| vehicle.type | vehicle.speed | vehicle.purpose | Output |
|-------------|---------------|-----------------|--------|
| tractor | <=15_kmh | agricultural | **EXEMPT** |
| trailer | not_registered | any | **EXEMPT** |
| wheelchair | any | disability | **EXEMPT** |

#### E26: Information to Transport Agency (§9)

| information.type | timeliness | Output |
|-----------------|------------|--------|
| new_policy | <=7_days | **MUST_REPORT** |
| premium_default | any | **MUST_REPORT** |

#### E27: Vehicle Identification (§10)

| vehicle.registered | vehicle.identified | notification.days | Output |
|-------------------|-------------------|-------------------|--------|
| true | false | >7 | **LIABILITY_EXPIRES** |
| true | true | <=7 | **LIABILITY_VALID** |

#### E28: Policy Document (§11)

| document.contains_key_terms | terms.provided | Output |
|---------------------------|-----------------|--------|
| true | true | **VALID_DOCUMENT** |
| false | any | **INCOMPLETE** |

#### E29: Validity Period (§12)

| acceptance.date | policy.period | Output |
|-----------------|---------------|--------|
| date | any | **COVERAGE_STARTS** |
| any | 13_months | **FIRST_PERIOD_13_MONTHS** |

#### E30: Geographical Scope (§13)

| country | green_card | Output |
|---------|------------|--------|
| EEA | true | **COVERED** |
| EEA | false | **COVERED_MINIMUM** |

### 2.2 Premium Calculation

#### E31: Information Withholding (§14)

| information.withheld | years_back | Output |
|---------------------|-------------|--------|
| true | <=5 | **RETROACTIVE_5_YEARS** |
| false | any | **NO_RETROACTIVE** |

#### E32: Risk Increase (§15)

| risk.increased | years_back | Output |
|---------------|-------------|--------|
| true | <=5 | **RETROACTIVE_5_YEARS** |
| false | any | **NO_RETROACTIVE** |

#### E33: Cancellation Right (§16)

| cancellation.reason | new_insurance.exists | Output |
|---------------------|---------------------|--------|
| new_insurer | true | **CANCELLATION_ALLOWED** |
| theft | true | **CANCELLATION_ALLOWED** |

#### E34: Insurer Obligation (§17)

| vehicle.type | insurer.licensed | Output |
|-------------|------------------|--------|
| covered_type | true | **MUST_PROVIDE** |

#### E35: Owner/Holder Change (§18)

| transfer.date | new_insurance.date | days_elapsed | Output |
|--------------|-------------------|--------------|--------|
| date | none | <=7 | **OLD_POLICY_COVERS** |
| date | date | >7 | **NEW_POLICY_REQUIRED** |

#### E36: Damage History (§19)

| history.years | history.claims | Output |
|--------------|-----------------|--------|
| <=5 | any | **HISTORY_RELEVANT** |
| >5 | any | **HISTORY_EXPIRED** |

#### E37: Premium Calculation Factors (§20)

| vehicle.type | driver.age | claims.count | Output |
|-------------|-----------|--------------|--------|
| private_car | >25 | 0 | **BASE_PREMIUM** |
| private_car | <25 | any | **YOUNG_DRIVER_LOADING** |
| motorcycle | any | any | **MOTORCYCLE_RATE** |

#### E38: History Transfer (§21)

| policy.new_company | history.exists | Output |
|-------------------|----------------|--------|
| true | true | **MUST_TRANSFER** |

#### E39: Usage During Removal Period (§22)

| registered_removed | used_in_traffic | Output |
|-------------------|-----------------|--------|
| true | true | **TRIPLE_PREMIUM** |
| true | false | **NORMAL_PREMIUM** |

#### E40: Premium Refund (§23)

| refund.amount | Output |
|--------------|--------|
| >8 | **REFUND_PROCESSED** |
| <=8 | **NO_REFUND** |

#### E41: Late Payment Interest (§24)

| overdue | Output |
|---------|--------|
| true | **INTEREST_CHARGED** |

#### E42: Liability Continues (§25)

| premium.unpaid | Output |
|--------------|--------|
| true | **LIABILITY_CONTINUES** |

#### E43: Limitation (§26)

| claim.year | billing.year | Output |
|-----------|--------------|--------|
| >5 | any | **TIME_BARRED** |

#### E44: Payment When Uninsured (§27)

| obligation_violated | period_months | Output |
|--------------------|---------------|--------|
| true | <=60 | **REASONABLE_PREMIUM** |

#### E45: Penalty Fee (§28)

| laiminlynti.type | multiplier | Output |
|------------------|------------|--------|
| first_time | 1 | **SINGLE_FEE** |
| repeated | 3 | **TRIPLE_FEE** |

#### E46: Penalty Determination (§29)

| proposal.made | Output |
|--------------|--------|
| true | **PROCEED_PENALTY** |

#### E47: Usage Ban (§30)

| insurance.obligation | Output |
|---------------------|--------|
| violated | **USAGE_BANNED** |

### 2.3 Compensation Calculation

#### E48: Strict Liability (§31)

| accident.occurred | vehicle.insured | driver.fault | Output |
|------------------|-----------------|--------------|--------|
| true | true | any | **STRICT_LIABILITY** |

#### E49: Insurer Liability Period (§32)

| policy.active | accident.date | Output |
|--------------|--------------|--------|
| true | within_term | **INSURER_LIABLE** |
| false | any | **NOT_LIABLE** |

#### E50: Two or More Vehicles (§33)

| accident.vehicles | fault.determined | Output |
|-----------------|-----------------|--------|
| two_or_more | first_vehicle | **FIRST_NOT_LIABLE** |
| two_or_more | second_vehicle | **SECOND_NOT_LIABLE** |
| two_or_more | both | **SHARED_LIABILITY** |

#### E51: Rented E-Scooter (§34a)

| vehicle.type | rental.business | Output |
|-------------|-----------------|--------|
| e_scooter | rented | **LIMITED_COVERAGE** |

#### E52: Property Damage (§37)

| property.type | repair.possible | total_loss | Output |
|--------------|-----------------|------------|--------|
| vehicle | true | false | **REPAIR_COST** |
| vehicle | false | true | **MARKET_VALUE** |

#### E53: Maximum Property Damage (§38)

| damage.amount | claimants | Output |
|--------------|-----------|--------|
| >5000000 | 1 | **MAX_5000000** |
| >5000000 | >1 | **PROPORTIONAL** |

#### E54: Rescuer Compensation (§39)

| person.helped | helper.is_professional | Output |
|--------------|----------------------|--------|
| true | false | **COVERED** |
| true | true | **NOT_COVERED** |

#### E55: Vehicle Combinations (§39a)

| combination.towing | combination.trailer | Output |
|-------------------|--------------------|--------|
| identified | any | **TOWING_INSURER** |
| not_identified | identified | **TRAILER_INSURER** |

#### E56: Property Exclusions (§40)

| damage.to_own | damage.to_connected | Output |
|---------------|---------------------|--------|
| true | any | **NOT_COVERED** |
| false | true | **NOT_COVERED** |

#### E57: Work Performance (§42)

| vehicle.status | work.type | Output |
|---------------|-----------|--------|
| stationary | loading_unloading | **NOT_COVERED** |

#### E58: Outside Finland (§45)

| accident.country | vehicle.home | Output |
|-----------------|-------------|--------|
| EEA_not_Finland | Finland | **COVERED_GUARANTEE** |

#### E59: Liability Distribution (§51)

| insurers.multiple | fault.distribution | Output |
|------------------|-------------------|--------|
| true | shared | **JOINT_SEVERAL** |
| true | identified | **SPECIFIC_SOLE** |

#### E60: Rail Liability Division (§52)

| accident.involves_rail | fault.rail | fault.road | Output |
|------------------------|-----------|-----------|--------|
| true | sole | no_fault | **RAIL_SOLE** |
| true | shared | shared | **PROPORTIONAL** |
| true | no_fault | sole | **ROAD_SOLE** |

### 2.4 Medical Care

#### E61: Public Healthcare (§54)

| care.provider.public | Output |
|---------------------|--------|
| true | **PATIENT_FEE_COVERED** |

#### E62: Full Cost Payment (§55)

| care.provided | authority.reported | Output |
|--------------|-------------------|--------|
| true | true | **FULL_COST** |

#### E63: Reporting Requirement (§56)

| report.submitted | content.complete | Output |
|-----------------|------------------|--------|
| true | true | **VALID_REPORT** |

#### E64: Direct to Provider (§57)

| directed | provider.appropriate | Output |
|----------|----------------------|--------|
| true | true | **DIRECTION_VALID** |

#### E65: Private Without Authorization (§58)

| care.type | urgency | Output |
|----------|---------|--------|
| emergency | true | **COVERED** |
| visit | any | **COVERED** |

#### E66: Private With Authorization (§59)

| authorization.given | provider.appropriate | Output |
|--------------------|---------------------|--------|
| true | true | **FULL_COVERED** |

### 2.5 Claims Procedure

#### E67: Right to Compensation (§60)

| claim.submitted | damage.proven | Output |
|----------------|--------------|--------|
| true | true | **RIGHT_ESTABLISHED** |
| true | false | **RIGHT_NOT_ESTABLISHED** |

#### E68: Claim Timing (§61)

| claim.timing | limitation.period | Output |
|-------------|-------------------|--------|
| within_3_years | not_expired | **ACCEPTED** |
| within_10_years | expired | **EXCEPTIONAL** |
| after_10_years | expired | **TIME_BARRED** |

#### E69: Decision Deadline (§62)

| claim.type | complexity | Output |
|-----------|------------|--------|
| property | simple | **30_DAYS** |
| personal | any | **90_DAYS** |

#### E70: Registered Rights Limitation (§62a)

| data_subject.request | processing.lawful | Output |
|---------------------|------------------|--------|
| restrict | legitimate | **REQUEST_DENIED** |

#### E71: Decision & Reasoning (§63)

| decision.type | reasoning.provided | Output |
|--------------|--------------------|--------|
| approval | true | **VALID_DECISION** |
| rejection | true | **MUST_EXPLAIN** |

#### E72: Board (§64)

| board.requested | Output |
|-----------------|--------|
| true | **BOARD_CAN_ADVISE** |

#### E73: Board Recommendation (§65)

| party.requested | Output |
|-----------------|--------|
| injured | **CAN_REQUEST** |
| policyholder | **CAN_REQUEST** |

#### E74: Board Recommendation Obligation (§66)

| claim.type | severity | Output |
|-----------|----------|--------|
| permanent_loss | any | **MUST_REQUEST** |
| death | any | **MUST_REQUEST** |
| severe_disability | any | **MUST_REQUEST** |

#### E75: Delayed Compensation (§67)

| compensation.type | delay.reason | Output |
|------------------|--------------|--------|
| personal_injury | insurer_fault | **ENHANCED_INTEREST** |
| property | insurer_fault | **STANDARD_INTEREST** |

#### E76: Claimant Notification Duty (§68)

| change.occurred | notification.made | Output |
|-----------------|-------------------|--------|
| true | false | **NOTIFICATION_REQUIRED** |

#### E77: Representative (§69)

| company.type | eea_operation | Output |
|-------------|---------------|--------|
| insurer | true | **MUST_NOMINATE** |

#### E78: Right to Claim from Representative (§70)

| accident.country | victim.residence | Output |
|-----------------|------------------|--------|
| EEA | Finland | **CAN_CLAIM_REP** |

#### E79: Liability Handling Delay (§71)

| insurer.delayed | victim.residence | Output |
|-----------------|------------------|--------|
| true | Finland | **CENTRE_CAN_INTERVENE** |

#### E80: Right to Info from Centre (§72)

| info.requested | accident.country | Output |
|----------------|------------------|--------|
| owner_info | Finland | **MUST_PROVIDE** |

#### E81: Subrogation (§73)

| insurer.paid | third_party.liable | Output |
|-------------|-------------------|--------|
| true | true | **SUBROGATION_EXISTS** |

### 2.6 Distribution System

#### E82: Distribution System (§75)

| company.type | participation | Output |
|-------------|---------------|--------|
| insurer | mandatory | **MUST_PARTICIPATE** |

#### E83: Contribution Amount (§76)

| costs.total | method.calculation | Output |
|-------------|-------------------|--------|
| any | proportional | **CONTRIBUTION_OWED** |

#### E84: Portfolio Transfer (§78)

| transfer.type | effect | Output |
|--------------|--------|--------|
| merger | adjusts_contribution | **ADJUSTED** |

### 2.7 Miscellaneous

#### E85: Limitation Period (§79)

| claim.type | years_elapsed | Output |
|-----------|---------------|--------|
| any | <=3 | **WITHIN_PERIOD** |
| any | >3 | **TIME_BARRED** |

#### E86: Court Proceedings (§80)

| court.claimed | Output |
|--------------|--------|
| damages | **COURT_CAN_DECIDE** |

#### E87: Authority Appeal Right (§81)

| authority.type | Output |
|---------------|--------|
| welfare | **CAN_APPEAL** |

#### E88: Information Right (§82)

| info.type | requester.type | Output |
|----------|---------------|--------|
| employment | insurer | **MUST_PROVIDE** |
| medical | insurer | **MUST_PROVIDE** |

#### E89: (Repealed) (§83)

| N/A | N/A | N/A | Output |
|------|-----|-----|--------|
| N/A | N/A | N/A | **NOT_APPLICABLE** |

#### E90: Right to Information (§84)

| info.type | legitimate_interest | Output |
|----------|---------------------|--------|
| policy | true | **MUST_PROVIDE** |

#### E91: Document Retention (§85)

| document.type | retention.period | Output |
|--------------|------------------|--------|
| personal_injury | 100_years | **MUST_RETAIN** |
| appeals | 50_years | **MUST_RETAIN** |

#### E92: Info Centre (§86)

| centre.function | Output |
|----------------|--------|
| information | **CENTRE_OPERATES** |

#### E93: Centre Duties (§87)

| duty.type | Output |
|----------|--------|
| statistics | **MUST_COMPILE** |
| guarantee | **MUST_ADMINISTER** |

#### E94: Information to Centre (§88)

| info.type | timeliness | Output |
|----------|------------|--------|
| statistics | annual | **MUST_REPORT** |

#### E95: Finanssivalvonta (§90)

| authority.function | Output |
|-------------------|--------|
| supervision | **SUPERVISES** |

#### E96: Customs Duties (§91)

| vehicle.imported | customs.duties | Output |
|-----------------|---------------|--------|
| temporary | border_insurance | **MUST_ENSURE** |

#### E97: Insolvency (§91a)

| insolvency.type | victim.residence | Output |
|----------------|------------------|--------|
| company | Finland | **CENTRE_CAN_PAY** |

#### E98: Insolvency Duties (§91b)

| action.type | Output |
|-------------|--------|
| notify_eea | **MUST_NOTIFY** |

#### E99: Insolvency & Bankruptcy (§92)

| status.type | output |
|------------|--------|
| liquidation | policy_terminates |

#### E100: Additional Payment (§93)

| situation.type | Output |
|---------------|--------|
| shortfall | **ADDITIONAL_DUE** |

#### E101: Joint Guarantee (§94)

| default.company | Output |
|----------------|--------|
| insolvent | **GUARANTEE_ASSESSES** |

#### E102: Official Liability (§95)

| official.type | Output |
|--------------|--------|
| company_personnel | **OFFICIAL_LIABILITY** |

