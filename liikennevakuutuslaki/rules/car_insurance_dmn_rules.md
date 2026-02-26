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

**Blood Alcohol Concentration (BAC) Thresholds:**
- Blood: ≥1.2‰ (≥0.53 mg/L breath)
- "Verensä alkoholipitoisuus on ajon aikana tai sen jälkeen vähintään 1,2 promillea"
- "Vähintään 0,53 milligrammaa alkoholia litrassa uloshengitysilmaa"

| driver.bloodAlcoholLevel | driver.breathAlcoholLevel | driver.contributionDegree | victim.isAtFault | Output |
|-------------------------|--------------------------|--------------------------|-----------------|--------|
| >=1.2_permille | any | SoleFault | false | **NOT_COVERED** |
| any | >=0.53_mg_per_L | SoleFault | false | **NOT_COVERED** |

**Drug Impairment (§48):**
- "Kykynsä tehtävän vaatimiin suorituksiin on tuntuvasti huonontunut muun huumaavan aineen kuin alkoholin vaikutuksesta"
- Combined alcohol + drugs: enhanced reduction applies

---

### 1.2 Reduced Compensation

#### N10: Victim Contribution (§47)

| victim.causedDamage | victim.contributionDegree | damage.damageType | Output |
|--------------------|--------------------------|-------------------|--------|
| true | Negligence | PropertyDamage | **50_PERCENT** |
| true | Slight | any | **75_PERCENT** |
| true | Moderate | any | **50_PERCENT** |

#### N11: Alcohol Impairment (§48)

**BAC Thresholds (Blood & Breath):**
- Blood ≥1.2‰ OR Breath ≥0.53 mg/L: Significant reduction/denial
- Blood 0.5-1.19‰ OR Breath 0.22-0.52 mg/L: Proportional reduction

| driver.bloodAlcoholLevel | driver.breathAlcoholLevel | driver.contributionDegree | victim.isAtFault | Output |
|--------------------------|--------------------------|--------------------------|-----------------|--------|
| >=1.2_permille | any | PartialFault | false | **50_PERCENT** |
| any | >=0.53_mg_per_L | PartialFault | false | **50_PERCENT** |
| 0.5-1.19_permille | 0.22-0.52_mg_per_L | PartialFault | false | **75_PERCENT** |
| 0.5-1.19_permille | 0.22-0.52_mg_per_L | SoleFault | false | **NOT_COVERED** |

**Drug Impairment (§48):**
- "Kykynsä tehtävän vaatimiin suorituksiin on huonontunut muun huumaavan aineen kuin alkoholin vaikutuksesta"
- Combined alcohol + drug impairment: applies same reduction rules

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

**Third parties are protected from alcohol-based reductions (§48):**
- Blood ≥1.2‰ OR Breath ≥0.53 mg/L: Full coverage for third parties
- Blood 0.5-1.19‰ OR Breath 0.22-0.52 mg/L: Full coverage for third parties
- <0.5‰ BAC: Full coverage

| driver.bloodAlcoholLevel | driver.breathAlcoholLevel | victim.relationshipType | victim.isAtFault | Output |
|--------------------------|--------------------------|-------------------------|-----------------|--------|
| >=1.2_permille | any | ThirdParty | false | **COVERED** |
| any | >=0.53_mg_per_L | ThirdParty | false | **COVERED** |
| 0.5-1.19_permille | 0.22-0.52_mg_per_L | ThirdParty | false | **COVERED** |
| <0.5_permille | any | any | false | **COVERED** |

**§48 Note:** Reductions for alcohol impairment do NOT apply to third party victims

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

**Treatment Authorization Requirements:**
- §53: Treatment must be necessary ("vahingon vuoksi tarpeellinen")
- §54: Public healthcare = customer fee only (asiakasmaksu)
- §56: Notification within 4 business days ("neljän arkipäivän kuluessa")
- §57: Insurer can direct to specific facility (maksusitoumus)
- §58-59: Private care requires prior approval (except emergency)

| medicalExpense.treatmentType | medicalExpense.isNecessary | medicalExpense.providerType | medicalExpense.maksusitoumusRequired | medicalExpense.notificationWithin4Days | Output |
|------------------------------|---------------------------|---------------------------|-------------------------------------|----------------------------------------|--------|
| Emergency | true | public | N/A | N/A | **100_PERCENT** |
| Emergency | true | private | No | N/A | **100_PERCENT_REIMBURSEMENT** |
| NonEmergency | true | public | N/A | Yes | **100_PERCENT** |
| NonEmergency | true | private | Yes | Yes | **100_PERCENT_REIMBURSEMENT** |
| NonEmergency | true | private | No | Yes | **CustomerFeeOnly** |
| NonEmergency | true | any | any | No | **NotificationRequired** |
| any | false | any | any | any | **NOT_COVERED** |

**Treatment Types Covered:**
- Surgery (leikkaus)
- Medicines (lääkkeet)
- Rehabilitation (kuntoutus)
- Dental treatment (hammashoito)
- Prosthesis (proteesi)
- Travel to treatment (hoitomatkat)

**§55 Täyskustannusmaksu:** Full cost payment to municipality for public healthcare

---

### 2.7 Medical Treatment Workflow (§§56-59)

#### M1: Healthcare Provider Notification (§56)

| treatment.decisionDate | notification.sentDate | notification.recipient | Output |
|------------------------|----------------------|------------------------|--------|
| any | within 4 business days | Insurer | **Compliant** |
| any | after 4 business days | Insurer | **NotificationDelayed** |
| emergency | immediate | Insurer | **EmergencyException** |

**§56:** Healthcare provider must notify insurer within 4 business days of treatment decision.

#### M2: Maksusitoumus Requirement (§57, §59)

| treatment.type | treatment.provider | maksusitoumus.obtained | Output |
|----------------|-------------------|------------------------|--------|
| Emergency | private | N/A | **Covered_NoPriorApproval** |
| NonEmergency | private | Yes | **Covered_WithMaksusitoumus** |
| NonEmergency | private | No | **CustomerFeeOnly** |
| any | public | N/A | **FullCoverage** |

**§57:** Insurer has right to direct patient to specific facility via maksusitoumus.
**§59:** Non-emergency private care requires maksusitoumus for full coverage.

#### E6: Lost Wages Compensation (§34)

| person.incomeType | person.netMonthlyIncome | person.annualIncome | injury.workAbilityLostDays | Output |
|-------------------|------------------------|---------------------|----------------------------|--------|
| Employed | any | null | any | Calculate_NetMonthly/30×Days |
| SelfEmployed | null | any | any | Calculate_Annual/365×Days |
| Unemployed | any | null | any | **Minimum_36.90_PerDay** |
| Student | any | null | any | StudentGrant_Adjustment |

#### E7: Pain and Suffering Compensation (§35)

**Index Adjustment for Continuous Compensation (§35):**
- Annual adjustment using Työeläkeindeksi (Employee Pension Index)
- Ansiotulot adjusted using Palkkakerroin (Wage Coefficient)

| injury.isPermanent | injury.permanentDisabilityPercentage | painSuffering.level | compensation.type | Output |
|-------------------|---------------------------------------|---------------------|-------------------|--------|
| true | 1-10_PERCENT | moderate | Continuous | Scale_1_10_Percent × Työeläkeindeksi |
| true | 11-20_PERCENT | moderate | Continuous | Scale_11_20_Percent × Työeläkeindeksi |
| true | 21-50_PERCENT | significant | Continuous | Scale_21_50_Percent × Työeläkeindeksi |
| true | 51-100_PERCENT | severe | Continuous | Scale_51_100_Percent × Työeläkeindeksi |
| false | null | any | OneTime | TemporaryPain_Scale |
| true | any | any | LumpSum | FixedAmount (erityisen painava syy) |

**§35:** "Tämän lain ja liikennevakuutuslain perusteella korvattavasta kuntoutuksesta annetun lain nojalla henkilövahingon johdosta suoritettavat jatkuvat korvaukset tarkistetaan kalenterivuosittain työntekijän eläkelain (395/2006) 98 §:ssä tarkoitetulla työeläkeindeksillä."

#### E8: Property Damage Compensation (§3, §38)

| property.type | property.marketValue | damage.severity | Output |
|---------------|---------------------|-----------------|--------|
| Vehicle | any | TotalLoss | **MarketValue** |
| Vehicle | any | PartialDamage | **RepairCost** |
| ThirdPartyProperty | any | any | **ActualValue** |
| Clothing | any | any | **ReplacementValue** |

**Maximum Compensation (§38):** €5,000,000 per insurance policy

| totalClaimsAmount | Output |
|-------------------|--------|
| <= 5,000,000 EUR | **FullCompensation** |
| > 5,000,000 EUR | **ProRataDistribution** |

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

### 2.6 Time Limits and Deadlines (§§61, 62, 79)

#### T1: Claim Filing Deadline (§61)

| claim.knowledgeDate | claim.submissionDate | Output |
|---------------------|----------------------|--------|
| known | within 3 years of knowledge | **ValidClaim** |
| known | after 3 years of knowledge | **TimeBarred** |
| unknown | within 10 years of accident | **ValidClaim** |
| unknown | after 10 years of accident | **AbsolutelyTimeBarred** |

**§61:** Korvausvaatimus on esitettävä kolmen vuoden kuluessa siitä, kun korvauksen hakija on saanut tietää vahinkotapahtumasta. Korvausvaatimus on joka tapauksessa esitettävä kymmenen vuoden kuluessa vahinkoseuraamuksen aiheutumisesta.

#### T2: Investigation Start Deadline (§62)

| claim.receivedDate | investigation.startDate | Output |
|--------------------|------------------------|--------|
| any | within 7 business days | **Compliant** |
| any | after 7 business days | **InvestigationDelayed** |

**§62:** Vakuutusyhtiön on aloitettava korvausasian selvittäminen viipymättä ja viimeistään seitsemän arkipäivän kuluessa vireilletulosta.

#### T3: Payment Deadline (§62)

| documents.completeDate | payment.date | Output |
|------------------------|--------------|--------|
| any | within 1 month | **Compliant** |
| any | after 1 month | **PaymentDelayed** |

**§62:** Vakuutusyhtiön on suoritettava korvaus tai ilmoitettava, ettei korvausta suoriteta, joutuisasti ja viimeistään kuukauden kuluttua siitä, kun se on saanut riittävän selvityksen.

#### T4: Court Action Deadline (§79)

| decision.notificationDate | courtAction.filingDate | Output |
|---------------------------|------------------------|--------|
| any | within 3 years | **ValidAction** |
| any | after 3 years | **ActionTimeBarred** |

**§79:** Kanne on oikeuden menettämisen uhalla nostettava vakuutusyhtiötä vastaan kolmen vuoden kuluessa siitä, kun asianosainen on saanut kirjallisen tiedon vakuutusyhtiön päätöksestä.

---

### 2.7 Premium Calculation Rules (§§20-28)

#### P6: Traffic Removal Violation Premium (§22)

| vehicle.isRemovedFromTraffic | vehicle.usedDuringTrafficRemoval | vehicle.removalPeriodDays | specialReason.exists | Output |
|------------------------------|----------------------------------|--------------------------|---------------------|--------|
| true | true | >0 | false | **Premium×3** |
| true | true | >0 | true | **Premium×1** (exemption applies) |
| false | any | any | any | **NormalPremium** |
| true | false | any | any | **NormalPremium** |

**§22:** "Jos vakuutettua ajoneuvoa on käytetty liikenteessä sinä aikana, jona se on ollut ilmoitettuna rekisteriin liikennekäytöstä poistetuksi, vakuutuksenottajan on suoritettava vakuutusyhtiölle vakuutusehdoissa määritelty enintään kolminkertainen vakuutusmaksu."

#### P7: Premium Claim Statute of Limitations (§26)

| invoice.sent | invoice.date | claimYearEnd | insurancePeriodEnd | yearsElapsed | Output |
|--------------|--------------|--------------|-------------------|--------------|--------|
| true | any | known | N/A | <5 | **ValidClaim** |
| true | any | known | N/A | >=5 | **TimeBarred** |
| false | N/A | N/A | known | <5 | **ValidClaim** |
| false | N/A | N/A | known | >=5 | **TimeBarred** |

**§26:** "Vakuutusmaksusaatava vanhentuu lopullisesti viiden vuoden kuluttua sitä seuraavan kalenterivuoden päättymisestä, jona se on määrätty tai maksuunpantu. Jos laskua ei ole lähetetty, vakuutusmaksusaatava vanhentuu viiden vuoden kuluttua kunkin vakuutuskauden päättymisestä."

---

### 1.1.1 Extended Exemptions (§8)

#### N5a: Complete Vehicle Exemptions (§8)

| vehicle.registrationRequired | vehicle.maxSpeed | vehicle.vehicleType | vehicle.usagePurpose | vehicle.ownerType | insurance.exemptType | Output |
|------------------------------|------------------|---------------------|---------------------|-------------------|----------------------|--------|
| false | ≤15 km/h | MotorWorkMachine | any | any | **Exempt** |
| false | any | Harvester | Agriculture | any | **Exempt** |
| false | any | Trailer | any | any | **Exempt** |
| false | any | ChildVehicle | ChildTransport | any | **Exempt** |
| false | any | Wheelchair | DisabledUse | any | **Exempt** |
| false | any | any | any | any | **Exempt** |
| any | any | any | any | FinnishState | **Exempt** |
| any | any | any | any | OtherState | **Exempt** (diplomatic) |
| true | any | any | any | any | TempRemovedFromTraffic | **ExemptIfNotUsed** |
| true | any | any | any | any | PermanentlyRemoved | **Exempt** |

**§8(2):** "Ajoneuvon omistajalla ja haltijalla on kuitenkin oikeus vakuuttaa 1 momentin 6, 7 ja 9 kohdassa tarkoitettu ajoneuvo."

---

## VARIABLE NAMING CONVENTION

All variables follow `entity.attribute` format matching the business ontology:

| Entity | Attributes |
|--------|-----------|
| **vehicle** | registrationCountry, requiresInsurance, vehicleType, isExempt, exemptType, usedWithoutPermission, ownerConsent, isUnknown, theft.reported, maxSpeed, registrationRequired, usagePurpose, ownerType, isRemovedFromTraffic, usedDuringTrafficRemoval, removalPeriodDays |
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
| **specialReason** | exists |
| **invoice** | sent, date |
| **insurancePeriod** | end |

---

## SECTION 3: PROCEDURAL RULES (§§60-72, 19)

### 3.1 Claims Submission and Processing

#### P1: Direct Claim Right (§60)

| claimant.type | claim.submittedTo | Output |
|---------------|-------------------|--------|
| ThirdParty | Insurer | **DirectClaimAllowed** |
| Passenger | AnyInvolvedVehicleInsurer | **DirectClaimAllowed** |
| Pedestrian | AnyInvolvedVehicleInsurer | **DirectClaimAllowed** |
| Driver | OwnVehicleInsurer | **DirectClaimAllowed** |

**§60:** "Vahinkoa kärsineellä on oikeus vaatia korvausta suoraan vakuutusyhtiöltä."

#### P2: Claims History Certificate (§19)

| certificate.requestDate | certificate.issuedDate | policy.endDate | Output |
|------------------------|------------------------|----------------|--------|
| any | within 15 days | any | **Compliant** |
| any | after 15 days | any | **CertificateDelayed** |
| any | N/A | >5 years ago | **CertificateNotRequired** |

**§19:** "Vakuutusyhtiön on toimitettava todistus vakuutuksenottajalle 15 päivän kuluessa pyynnöstä."

#### P3: Decision Justification Requirements (§63)

| decision.type | justification.includesMedicalAssessment | justification.includesKeyFactors | Output |
|---------------|----------------------------------------|----------------------------------|--------|
| Reduction | Yes | Yes | **Compliant** |
| Denial | Yes | Yes | **Compliant** |
| any | No | Yes | **IncompleteJustification** |

**§63:** If decision is based on medical factors, justification must include key factors and conclusions.

#### P4: Liikennevahinkolautakunta Opinion Right (§65)

| decision.notificationDate | opinion.requestDate | request.within1Year | Output |
|---------------------------|--------------------|---------------------|--------|
| any | within 1 year | Yes | **OpinionRequestValid** |
| any | after 1 year | No | **OpinionRequestTimeBarred** |

**§65:** Parties can request Liikennevahinkolautakunta opinion within 1 year of decision.

#### P5: Delay Interest Calculation (§67)

| payment.dueDate | payment.actualDate | interest.rate | Output |
|-----------------|--------------------|---------------|--------|
| any | on time | N/A | **NoInterest** |
| any | delayed | Korkolaki + increase | **DelayInterestApplied** |
| any | duringLautakuntaReview | 0 | **InterestPaused** |

**§67:** "Henkilövahingosta suoritettavan korvauksen viivästyessä vakuutusyhtiön on maksettava viivästynyt korvaus viivästysajalta korotettuna (viivästyskorotus)."

**Minimum interest:** €7.28 (adjusted annually by palkkakerroin)

---

## METADATA

- **Law**: Liikennevakuutuslaki (Traffic Insurance Act) 460/2016
- **Source**: finlex.fi/fi/lainsaadanto/2016/460
- **Version**: 1.3 (Negative Claims First)
- **Total Decisions**: 30 (17 Negative Claims + 13 Eligibility)
- **Decision Order**: Negative Claims → Eligibility → Compensation
- **Variable Convention**: entity.attribute (ontology-aligned)
