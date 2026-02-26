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

| vehicle.usedWithoutPermission | victim.knewUnauthorized | specialReason.exists | Output |
|------------------------------|------------------------|---------------------|--------|
| true | false | N/A | **NOT_COVERED** |
| true | true | false | **NOT_COVERED** |
| true | true | true | **COVERED_SpecialReason** |

**§49:** "Jos liikennevahinko on aiheutunut vahinkoa kärsineen ollessa luvattomasti käyttöön otetussa ajoneuvossa ja vakuutusyhtiö voi osoittaa hänen tienneen ajoneuvon käyttöönoton luvattomuudesta, hänelle suoritetaan korvausta ajoneuvon vakuutuksesta vain erityisestä syystä."

**Examples of "Special Reason" (erityinen syy):**
- Emergency situation
- Coercion/duress
- Minor without capacity to understand
- Other compelling circumstances

#### N2: Insanity/Emergency (§50)

| driver.isInsane | driver.inEmergency | driver.isResponsible | Output |
|----------------|-------------------|---------------------|--------|
| true | false | false | **NOT_COVERED** |
| false | true | false | **NOT_COVERED** |

#### N2a: Work Performance Damage (§42)

| vehicle.isStationary | person.performingWork | person.relationshipToVehicle | damage.targetProperty | Output |
|--------------------|---------------------|---------------------------|---------------------|--------|
| true | true | Owner | InsuredVehicle | **NOT_COVERED** |
| true | true | Driver | InsuredVehicle | **NOT_COVERED** |
| true | true | any | WorkTargetProperty | **NOT_COVERED** |
| true | true | any | OtherVehicleInvolved | **NOT_COVERED** |
| true | false | any | any | **COVERED** |
| false | any | any | any | **COVERED** |

**§42:** "Vakuutuksesta ei korvata vahinkoa, joka on aiheutunut: 1) ajoneuvon ollessa liikkumattomana ajoneuvon omistajalle, kuljettajalle tai muulle henkilölle, joka suorittaa tässä tarkoitettua työtä; eikä 2) työsuorituksen kohteena olevalle omaisuudelle taikka tähän toimintaan osalliselle toiselle ajoneuvolle."

**Excluded Scenarios:**
- Vehicle owner injured while working on their own stationary vehicle
- Driver injured while performing work on the stationary vehicle
- Damage to the property being worked on
- Damage to another vehicle involved in the work activity

**Covered Scenarios:**
- Injuries to third parties
- Damage to property not involved in the work

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

#### N18: Owner/Holder Property Exclusion with Passenger Exception (§40)

| property.location | property.ownerRelationship | property.type | property.isAttachedToVehicle | Output |
|-------------------|---------------------------|---------------|------------------------------|--------|
| InsuredVehicle | Owner | any | true | **NOT_COVERED** |
| InsuredVehicle | Holder | any | true | **NOT_COVERED** |
| InsuredVehicle | Driver | any | false | **NOT_COVERED** |
| InsuredVehicle | Owner | OtherVehicle | true | **NOT_COVERED** |
| InsuredVehicle | Owner | OtherProperty | false | **NOT_COVERED** |
| InsuredVehicle | Passenger-NotOwnerHolder | Clothing | false | **COVERED** (passenger exception) |
| InsuredVehicle | Passenger-NotOwnerHolder | PersonalItems | false | **COVERED** (passenger exception) |
| InsuredVehicle | Passenger-NotOwnerHolder | OtherProperty | false | **NOT_COVERED** |

**§40:** "Vakuutuksesta korvataan kuitenkin vahinko, joka on aiheutunut muun matkustajan kuin ajoneuvon omistajan tai haltijan yllä tai mukana olleiden vaatteiden ja henkilökohtaisten käyttöesineiden vahingoittumisesta."

**Special Case (§40(3)):** If owner/holder owns ANOTHER vehicle involved, that vehicle's damage IS covered.

---

### 1.2 Reduced Compensation

#### N10: Victim Contribution (§47)

| victim.causedDamage | victim.contributionDegree | compensation.type | damage.damageType | Output |
|--------------------|--------------------------|-------------------|-------------------|--------|
| true | Negligence | Rehabilitation | any | **COVERED_100** |
| true | GrossNegligence | Rehabilitation | any | **COVERED_100** |
| true | Slight | any | PropertyDamage | **75_PERCENT** |
| true | Moderate | any | PropertyDamage | **50_PERCENT** |
| true | Negligence | any | PropertyDamage | **50_PERCENT** |

**§47(3):** "Liikennevakuutuslain perusteella korvattavasta kuntoutuksesta annetun lain mukaisiin korvauksiin ei tehdä 1 momentissa tarkoitettua vähennystä. Jos korvaus evätään kokonaan, ei kuntoutustakaan korvata."

#### N11: Alcohol Impairment (§48)

**BAC Thresholds (Blood & Breath):**
- Blood ≥1.2‰ OR Breath ≥0.53 mg/L: Significant reduction/denial
- Blood 0.5-1.19‰ OR Breath 0.22-0.52 mg/L: Proportional reduction

| driver.bloodAlcoholLevel | driver.breathAlcoholLevel | driver.contributionDegree | compensation.type | victim.isAtFault | Output |
|--------------------------|--------------------------|--------------------------|-------------------|-----------------|--------|
| >=1.2_permille | any | PartialFault | Rehabilitation | false | **COVERED_100** |
| any | >=0.53_mg_per_L | PartialFault | Rehabilitation | false | **COVERED_100** |
| 0.5-1.19_permille | 0.22-0.52_mg_per_L | PartialFault | Rehabilitation | false | **COVERED_100** |
| >=1.2_permille | any | PartialFault | any | false | **50_PERCENT** |
| any | >=0.53_mg_per_L | PartialFault | any | false | **50_PERCENT** |
| 0.5-1.19_permille | 0.22-0.52_mg_per_L | PartialFault | any | false | **75_PERCENT** |
| 0.5-1.19_permille | 0.22-0.52_mg_per_L | SoleFault | any | false | **NOT_COVERED** |

**§48(3):** "Liikennevakuutuslain perusteella korvattavasta kuntoutuksesta annetun lain mukaisiin korvauksiin ei tehdä 1 ja 2 momenteissa tarkoitettua vähennystä."

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

#### E15: Coverage During Ownership Transfer (§18)

| insurance.status | ownership.transferOccurred | daysSinceTransfer | newOwner.hasInsurance | Output |
|------------------|---------------------------|-------------------|----------------------|--------|
| Terminated | true | ≤7 | false | **COVERED** (7-day extension) |
| Terminated | true | ≤7 | true | **NOT_COVERED** (new insurance applies) |
| Terminated | true | >7 | any | **NOT_COVERED** |
| Active | false | any | any | **COVERED** |

**§18:** "Korvataan päättyneestä vakuutuksesta myös ne vahingot, jotka ovat sattuneet seitsemän päivän kuluessa omistusoikeuden siirtymisestä taikka ajoneuvon hallinnan vaihtumisesta tai palautumisesta omistajalle, jollei ajoneuvon seuraava omistaja tai haltija ole ottanut vakuutusta mainitun ajan kuluessa."

**Variables:**
- `ownership.transferDate`: Date of ownership/holdership transfer
- `newOwner.insuranceStartDate`: Date new owner took insurance (if any)
- `daysSinceTransfer`: Calculated from transfer date |

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
| Vehicle | PartialDamage | any | **RepairCost** |
| ThirdPartyProperty | any | any | **ActualValue** |
| Clothing | any | any | **ReplacementValue** |

#### E8b: Property Damage Maximum Cap (§38)

| totalClaimsAmount | cap | ratio | Output |
|-------------------|-----|-------|--------|
| ≤ €5,000,000 | €5,000,000 | ≤ 100% | **FullCompensation** |
| > €5,000,000 | €5,000,000 | > 100% | **ProRataDistribution** |

**§38:** "Esinevahinkona korvataan enintään 5 000 000 euroa kutakin vahingosta vastuussa olevaa liikennevakuutusta kohden."

#### E8c: Pro-Rata Distribution (§38(2))

| claim.amount | totalClaims | cap | calculation | payout |
|--------------|-------------|-----|-------------|--------|
| any | any | €5,000,000 | claim.amount / totalClaims × cap | **proRataAmount** |

**§38(2):** "Jos 1 momentissa tarkoitettu enimmäismäärä ei riitä täyteen korvaukseen, jaetaan maksettava korvaus korvattavien vahinkojen suuruuden osoittamassa suhteessa."

#### E8d: Late Claimant Protection (§38(3))

| claimant.filedLate | claimant.hasRight | payouts.finalized | originalRatio | Output |
|-------------------|-------------------|------------------|---------------|--------|
| true | true | false | any | **FullProRataShare_Guaranteed** |
| true | true | true | ≤ original share | **AdditionalPayment_EvenIfExceedsCap** |
| false | any | any | any | **StandardProcessing** |

**§38(3):** "Jos korvausvaatimusten tultua ratkaistuiksi osoittautuu, että jollakulla, joka ei ole vielä saanut korvausta, on siihen oikeus, korvataan hänen vahinkonsa siinäkin tapauksessa, että korvauksen enimmäismäärä siten ylittyy. Korvauksen määrä ei kuitenkaan saa tällöin ylittää sitä suhteellista osuutta korvauksista, jonka korvaukseen oikeutettu olisi saanut, jos hän olisi alun perin ollut korvauksensaajien joukossa."

#### E8a: Loss of Use / Vehicle Downtime (§37)

| vehicle.damage.severity | vehicle.repair.days | vehicle.repair.isOngoing | rental.substitutionAvailable | Output |
|-----------------------|--------------------|-------------------------|-----------------------------|--------|
| TotalLoss | any | N/A | any | **LossOfUse_UpToReasonablePeriod** |
| PartialDamage | ≤30 days | true | true | **RentalCovered** |
| PartialDamage | ≤30 days | true | false | **LossOfUse_UpToRepairDays** |
| PartialDamage | >30 days | true | any | **LossOfUse_ExtendedReview** |
| PartialDamage | any | false | any | **NoLossOfUse** |
| NoDamage | any | any | any | **NotApplicable** |

**§37:** "Ajoneuvolle aiheutuneena vahinkona korvataan korjauskustannus tai sitä vastaava määrä. Ajoneuvon arvon alentumista ei korvata."

**Loss of Use Coverage:**
- While vehicle is being repaired or awaiting repair
- Maximum reasonable period based on repair complexity
- Substitution vehicle (rental) if available and reasonable
- Not covered if damage is minimal or repair is delayed unreasonably

**Variables:**
- `vehicle.repair.days`: Estimated or actual repair duration
- `rental.substitutionAvailable`: Whether rental vehicle is available

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

#### E12: Claim Filing Time Limit (§61)

| claim.knowledgeDate | claim.submissionDate | daysSinceKnowledge | daysSinceDamage | Output |
|---------------------|---------------------|---------------------|-----------------|--------|
| known | any | ≤ 1095 (≤3 years) | any | **ValidClaim** |
| known | any | > 1095 (>3 years) | any | **TimeBarred** |
| unknown | any | N/A | ≤ 3650 (≤10 years) | **ValidClaim** |
| unknown | any | N/A | > 3650 (>10 years) | **AbsolutelyTimeBarred** |

**§61:** "Korvausvaatimus on esitettävä vakuutusyhtiölle kolmen vuoden kuluessa siitä, kun korvauksen hakija on saanut tietää vahinkotapahtumasta ja siitä aiheutuneesta vahinkoseuraamuksesta. Korvausvaatimus on joka tapauksessa esitettävä kymmenen vuoden kuluessa vahinkoseuraamuksen aiheutumisesta."

**Exception:** "Erityisen painava syy" (particularly weighty reason) - claim can be processed after deadline

#### E12b: Claim Deadline (§62)

 Investigation| claim.filingDate | daysElapsed | output.required | Output |
|------------------|-------------|-----------------|--------|
| any | ≤ 7 days | Investigation | **InvestigationStarted** |
| any | ≤ 30 days | Payment | **PaymentDue** |
| any | ≤ 90 days | ResponseOnDispute | **ResponseDue** |
| any | > 30 days | Payment | **PaymentOverdue** |

**§62:** "Vakuutusyhtiön on aloitettava korvausasian selvittäminen viipymättä ja viimeistään seitsemän arkipäivän kuluessa vireilletulosta."

#### E12c: Court Action Time Limit (§79)

| decision.receiptDate | court.filingDate | daysSinceDecision | dispute.body | tolling.previouslyExtended | Output |
|---------------------|------------------|-------------------|--------------|---------------------------|--------|
| any | ≤ 1095 days (≤3 years) | ≤ 1095 | any | any | **TimelyFiling** |
| any | > 1095 days | > 1095 | any | any | **ClaimTimeBarred** |
| any | any | any | Vakuutuslautakunta/TrafficDamageBoard | false | **StatuteOfLimitationsTolled** |
| any | any | any | ConsumerDisputeBody | false | **StatuteOfLimitationsTolled** |
| any | > 365 days | any | any | false | **OneYearSafetyNet_Valid** (can extend once) |
| any | any | any | any | true | **ExtensionAlreadyUsed** |

**§79 Tolling Rules:**
- Filing with Vakuutuslautakunta/TrafficDamageBoard tolls the statute (§79(2))
- If proceedings end prematurely, minimum 1-year deadline applies (§79(3))
- Extension can only be used ONE TIME (§79(4))

**§79(3) 1-Year Safety Net:** "Kanneaika katsotaan katkenneeksi...Kanneaikaa voidaan pidentää tällä tavoin vain yhden kerran."

#### E13: Insolvency Protection (§92)

| insuranceCompany.status | insurance.policyActive | claim.isPending | Output |
|------------------------|----------------------|-----------------|--------|
| Insolvent | true | true | **FinnishGuaranteeFund_Pays** |
| Insolvent | true | false | TransferToAnotherInsurer |
| Healthy | true | true | NormalClaimsProcess |

---

### 2.7 Large Loss Distribution System (§75)

#### S1: Large Loss Distribution System (§75)

| totalClaimAmount | threshold.exceeded | amountOverThreshold | costType | yearsSinceAccident | distribution.applies | Output |
|------------------|-------------------|---------------------|----------|-------------------|---------------------|--------|
| ≤ €75M | false | 0 | any | any | false | **NormalCoverage** |
| > €75M | true | >0 | LVKCosts | any | true | **Distribute(amountOverThreshold)** |
| > €75M | true | >0 | IndexAdjustment | any | true | **Distribute(amountOverThreshold)** |
| > €75M | true | >0 | Healthcare | ≤9 | false | **NormalCoverage** |
| > €75M | true | >0 | Healthcare | >9 | true | **Distribute(amountOverThreshold)** |
| > €75M | true | >0 | Rehabilitation | ≤9 | false | **NormalCoverage** |
| > €75M | true | >0 | Rehabilitation | >9 | true | **Distribute(amountOverThreshold)** |
| > €75M | true | >0 | Täyskustannusmaksu | ≤9 | false | **NormalCoverage** |
| > €75M | true | >0 | Täyskustannusmaksu | >9 | true | **Distribute(amountOverThreshold)** |
| > €75M | true | >0 | LargeLoss | any | true | **Distribute(amountOverThreshold)** |

**Distribution Formula:**
```
insurerShare = (insurerPremiumIncome / totalPremiumIncome) × amountOverThreshold
```

**§75:** "Suurvahingolla tarkoitetaan ajallisesti ja paikallisesti rajoittunutta tapahtumaa tai samaa alkuperää olevaa tapahtumasarjaa, jonka seurauksena liikennevakuutuksen perusteella maksettuja korvauksia maksetaan yhdelle tai useammalle vahinkoa kärsineelle tai muulle korvaukseen oikeutetulle yhteensä yli 75 000 000 euroa (suurvahinkoraja)."

**Key Points:**
- Large loss threshold: €75,000,000
- Distribution applies only to amounts EXCEEDING the threshold
- Certain costs (Healthcare, Rehabilitation, Täyskustannusmaksu) only enter distribution after 9 years
- Distribution is proportional based on premium income

**Variables:**
- `totalClaimAmount`: Sum of all claims from the event
- `threshold.value`: €75,000,000 (adjustable)
- `yearsSinceAccident`: Years from accident date
- `insurer.premiumIncome`: Insurance premium income for distribution calculation

**Related Sections:**
- §76: Jakojärjestelmämaksun suuruus (calculation details)
- §77: Jakojärjestelmämaksun suorittaminen (payment)
- §78: Vakuutuskannan siirron vaikutus (portfolio transfer effects)

---

### 2.6 Time Limits and Deadlines (§§61, 62, 79)

#### T1: Claim Filing Deadline (§61)

| claim.knowledgeDate | claim.submissionDate | accident.date | specialReason.exists | Output |
|---------------------|----------------------|---------------|---------------------|--------|
| known | within 3 years of knowledge | any | any | **ValidClaim** |
| known | after 3 years of knowledge | within 10 years | true | **ProcessUnderException** |
| known | after 3 years of knowledge | within 10 years | false | **TimeBarred** |
| known | any | after 10 years | any | **AbsolutelyTimeBarred** |
| unknown | within 10 years of accident | any | any | **ValidClaim** |
| unknown | after 10 years of accident | any | any | **AbsolutelyTimeBarred** |

**§61:** Korvausvaatimus on esitettävä kolmen vuoden kuluessa siitä, kun korvauksen hakija on saanut tietää vahinkotapahtumasta. Korvausvaatimus on joka tapauksessa esitettävä kymmenen vuoden kuluessa vahinkoseuraamuksen aiheutumisesta. Erityisen painavasta syystä korvausvaatimus voidaan käsitellä myös määräajan jälkeen.

**Examples of "Special Reason" (erityisen painava syy):**
- Military service
- Prolonged unconsciousness
- Minority with no legal guardian
- Other compelling circumstances preventing timely filing

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

#### T3b: Undisputed Portion Payment (§62(3))

| claim.isDisputed | undisputed.amount | payment.date | documents.completeDate | Output |
|-----------------|-------------------|--------------|----------------------|--------|
| false | N/A | within 1 month | any | **FullPayment_Required** |
| true | > 0 | within 1 month | complete | **UndisputedPortion_Paid** |
| true | > 0 | after 1 month | complete | **UndisputedPortion_Delayed** |
| true | 0 | any | any | **FullDispute_NoPartialPayment** |
| true | > 0 | N/A | incomplete | **AwaitingCompleteDocuments** |

**§62(3):** "Jos korvauksen määrä ei ole riidaton, vakuutusyhtiö on kuitenkin velvollinen suorittamaan 2 momentissa mainitussa ajassa korvauksen riidattoman osan."

#### T4: Court Action Deadline (§79)

| decision.notificationDate | courtAction.filingDate | tolling.active | tolling.endedPrematurely | extension.used | Output |
|---------------------------|------------------------|---------------|------------------------|---------------|--------|
| any | within 3 years | false | any | any | **ValidAction** |
| any | after 3 years | false | any | any | **ActionTimeBarred** |
| any | within 3 years | true | any | any | **Tolled_Valid** |
| any | > 1 year after tolling ends | any | true | false | **OneYearSafetyNet_Valid** |
| any | any | any | any | true | **ExtensionAlreadyUsed** |

**§79(3) 1-Year Safety Net:** If proceedings end prematurely, deadline extends to min 1 year from end date.
**§79(4) One-Time Limit:** This extension can only be used once.

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

### 2.8 Penalty Rules (§§27-28)

#### P8: Insurance Obligation Failure Penalty (§27)

| obligation.failure | failure.durationYears | reasonablePremium | daysUninsured | Output |
|-------------------|----------------------|-------------------|----------------|--------|
| true | ≤5 | any | any | **BasePenalty = reasonablePremium × daysUninsured / 365** |
| true | >5 | any | any | **5YearLimit** (retroactive penalty limited to current + 5 years) |

**§27:** "Se, joka on laiminlyönyt 6 §:n mukaisen vakuuttamisvelvollisuutensa, on velvollinen maksamaan maksun, joka vastaa kohtuulliseksi katsottavaa vakuutusmaksua siltä ajalta, jota laiminlyönti koskee, ei kuitenkaan pitemmältä ajalta kuin kulumassa olevalta ja viideltä viimeksi kuluneelta kalenterivuodelta."

#### P9: Laiminlyöntimaksu Penalty Multiplier (§28)

| obligation.failure | failure.durationYears | failure.intentional | failure.repeated | vehicle.usedDuringFailure | penalty.multiplier | Output |
|-------------------|----------------------|--------------------|-----------------|--------------------------|-------------------|--------|
| true | ≤5 | false | false | false | 1.0 | **BasePenalty** |
| true | ≤5 | false | false | true | 1.5 | **Penalty×1.5** |
| true | ≤5 | true | false | false | 2.0 | **Penalty×2** |
| true | ≤5 | true | true | false | 2.5 | **Penalty×2.5** |
| true | ≤5 | true | true | true | 3.0 | **Penalty×3** (max) |
| true | >5 | any | any | any | N/A | **5YearLimit** |

**Total Penalty Calculation:**
```
basePenalty = reasonablePremium × daysUninsured / 365
totalPenalty = basePenalty × multiplier (max 3× base)
```

**§28:** "Laiminlyöntimaksun korotuskerrointa määrättäessä otetaan huomioon laiminlyöntiajan pituus, laiminlyönnin tahallisuus ja toistuvuus sekä se, onko ajoneuvoa käytetty liikenteessä."

**Variables:**
- `obligation.failure`: Boolean if insurance obligation was not met
- `failure.durationYears`: Years of non-compliance
- `failure.intentional`: Boolean for intentional failure
- `failure.repeated`: Boolean for repeated violations
- `vehicle.usedDuringFailure`: Boolean if vehicle was used uninsured
- `reasonablePremium`: Reasonable premium for the vehicle type
- `daysUninsured`: Number of days without insurance

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

| certificate.requested | certificate.requestDate | certificate.responseDate | policy.endDate | yearsSinceEnd | Output |
|---------------------|------------------------|-------------------------|----------------|---------------|--------|
| true | any | ≤15 days from request | any | ≤5 | **Compliant** |
| true | any | >15 days from request | any | ≤5 | **CertificateDelayed** (15-day deadline violated) |
| true | any | any | any | >5 | **NotRequired** (5-year statute) |
| true | any | any | unknown | any | **ProvideIfAvailable** |
| false | any | any | any | any | **NotRequested** |

**§19:** "Vakuutusyhtiön on toimitettava todistus vakuutuksenottajalle **15 päivän kuluessa pyynnöstä**. Vakuutusyhtiöllä ei kuitenkaan ole velvollisuutta antaa todistusta vakuutuksesta, jonka päättymisestä on kulunut yli viisi vuotaa."

**Required Certificate Contents (§19):**
1. Policy validity period (voimassaoloaika)
2. List of covered vehicles (kattamat ajoneuvot)
3. List of claims paid (vahingot joiden perusteella korvaus maksettu)

| certificate.requested | certificate.includesValidityPeriod | certificate.includesVehicles | certificate.includesClaims | Output |
|---------------------|-------------------------------------|------------------------------|----------------------------|--------|
| true | true | true | true | **Complete** |
| true | false | any | any | **Incomplete_MissingValidity** |
| true | true | false | any | **Incomplete_MissingVehicles** |
| true | true | true | false | **Incomplete_MissingClaims** |

**Variables:**
- `certificate.requestDate`: Date certificate was requested
- `certificate.responseDate`: Date certificate was provided
- `policy.endDate`: Policy end date (if ended)
- `yearsSinceEnd`: Years from policy end to request date

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

#### P4b: Mandatory Liikennevahinkolautakunta Consultation (§66)

| decision.type | compensation.category | disability.permanent | death.ongoing | correction.requestedByParty | Output |
|--------------|----------------------|---------------------|---------------|---------------------------|--------|
| Initial | ContinuousPension | Yes | N/A | N/A | **ConsultationRequired** |
| Initial | CapitalValue | N/A | Yes | N/A | **ConsultationRequired** |
| Initial | IncreasedCompensation | Yes | N/A | any | **ConsultationRequired** |
| Initial | DisabilityCompensation | Severe | N/A | any | **ConsultationRequired** |
| Correction | any | any | any | false | **ConsultationNotRequired** (no objection) |
| Correction | any | any | any | true | **ConsultationRequired** |
| Initial | any | No | No | N/A | **ConsultationOptional** |

**Mandatory Consultation Triggers (§66):**
- Persistent loss of earning capacity (§66(1)1)
- Death-related continuous compensation or capital value (§66(1)1)
- Increase/decrease of continuous compensation per Oikeusturva §5:8 (§66(1)2)
- Severe disability compensation (§66(1)3)
- Correction of erroneous decision against claimant's interest (§66(1)4)

**§66(2):** If insurer's decision differs from Lautakunta opinion against claimant, insurer must attach opinion to decision and notify Lautakunta.

**§66(3) Exceptions:** No consultation required if:
- Error is obvious and caused by party's own conduct
- Obvious clerical or calculation error

#### P5: Delay Interest Calculation (§67)

| interest.calculatedAmount | interest.currentMinimum | palkkakerroin.value | paymentDelay.cause | lautakunta.reviewActive | Output |
|---------------------------|------------------------|---------------------|--------------------|------------------------|--------|
| < €7.28 | €7.28 | current | any | false | **NoInterest** (below minimum) |
| ≥ €7.28 | €7.28 | current | Normal | false | **Interest = calculated × palkkakerroin** |
| any | €7.28 | current | VictimCaused | false | **NoInterest** |
| any | €7.28 | current | ForceMajeure | false | **NoInterestForDelayPeriod** |
| ≥ €7.28 | €7.28 | current | any | true | **InterestPaused** (during Lautakunta review) |

**Minimum Update Formula:**
```
newMinimum = €7.28 × palkkakerroin[currentYear]
newMinimum = Round(newMinimum, nearest cent)
```

**§67:** "Viivästyskorotusta tai viivästyskorkoa, jonka määrä on pienempi kuin 7,28 euroa, ei makseta. Rahamäärä tarkistetaan kalenterivuosittain työntekijän eläkelain 96 §:ssä tarkoitetulla palkkakertoimella. Tarkistettu euromäärä pyöristetään lähimmäksi sentiksi."

**Variables:**
- `interest.currentMinimum`: Current year threshold (default €7.28)
- `palkkakerroin.value`: Annual wage coefficient from Työeläkelaki
- `paymentDelay.cause`: Normal | VictimCaused | ForceMajeure
- `lautakunta.reviewActive`: Boolean

#### P6: Recipient Notification Obligation (§68)

| decision.notificationObligationStated | change.occurred | change.affectsCompensation | notification.timeliness | Output |
|--------------------------------------|-----------------|----------------------------|------------------------|--------|
| true | true | true | Immediate | **Compliant** |
| true | true | true | Delayed | **NonCompliant** |
| true | true | false | any | **NoObligation** |
| false | any | any | any | **NoObligation** |

**§68:** "Korvauksensaaja on velvollinen viipymättä ja oma-aloitteisesti ilmoittamaan vahingonkorvauslain 5 luvun 2, 2 d, 4 ja 4 b §:n sekä liikennevakuutuslain perusteella korvattavasta kuntoutuksesta annetun lain nojalla korvausta maksavalle vakuutusyhtiölle korvaukseen vaikuttavista muutoksista edellyttäen, että tästä velvollisuudesta on mainittu korvauspäätöksessä."

**Reportable Changes:**
- Employment status changes
- Recovery/improvement in condition
- Return to work
- Receipt of other compensation
- Change in disability status

---

## SECTION 4: RECOURSE & RECOVERY RULES

### 4.1 Insurer Subrogation

#### R1: Insurer Subrogation Rights (§73)

| thirdParty.type | damage.causeIntentional | damage.causedByGrossNegligence | driver.bloodAlcoholLevel | subrogation.applies |
|-----------------|------------------------|--------------------------------|-----------------------|---------------------|
| Individual | true | any | any | **Yes** |
| Individual | false | true | any | **Yes** |
| Individual | false | false | >= 1.2‰ | **Yes** |
| Individual | false | false | < 1.2‰ | **No** |
| Employee | true | any | any | **Yes** |
| Employee | false | true | any | **Yes** |
| VehicleOwner | true | any | any | **Yes** |
| VehicleOwner | false | true | any | **Yes** |
| VehicleDriver | true | any | any | **Yes** |
| VehicleDriver | false | true | any | **Yes** |
| Passenger | true | any | any | **Yes** |
| Passenger | false | true | any | **Yes** |
| Corporation | any | any | any | **Yes** |

**§73:** "Vahinkoa kärsineen oikeus vaatia kolmannelta henkilöltä korvaus määrän, jonka vakuutusyhtiö on hänelle suorittanut, siirtyy vakuutusyhtiölle. Jos kolmas henkilö on yksityishenkilö...oikeus siirtyy kuitenkin vain, jos hän on aiheuttanut vakuutustapahtuman tahallisesti tai törkeästä huolimattomuudesta tai jos kuljettaja on aiheuttanut vahingon kuljettaessaan ajoneuvoa 48 §:n 1 momentissa tarkoitetuissa olosuhteissa."

**Subrogation Limitations:**
- For individuals: Only if intentional, gross negligence, or §48(1) alcohol/drug impairment
- For corporations/businesses: Full subrogation applies
- For employees: Only if intentional or gross negligence

### 4.2 Traffic Insurance Centre Recourse

#### R2: Centre Recourse Rights (§74)

| payment.scenario | vehicle.homeCountry | insurer.identifiable | accident.locationCountry | recourse.target | recourse.applies |
|------------------|--------------------|----------------------|--------------------------|-----------------|---------------------|
| Uninsured_Vehicle | Finland | N/A | any | Finnish_Guarantee_Fund | **Yes** |
| Unknown_Insurer | EEA | false | any | Vehicle_HomeCountry_Fund | **Yes** |
| Unknown_Vehicle | any | false | EEA | AccidentLocation_Fund | **Yes** |
| Unknown_Vehicle | any | false | Non-EEA | AccidentLocation_Fund | **Yes** |
| ThirdCountry_Vehicle | Non-EEA | any | any | AccidentLocation_Fund | **Yes** |
| Insurance_Obligation_Neglected | Finland | any | any | Finnish_Guarantee_Fund | **Yes** |

**§74:** "Liikennevakuutuskeskuksella on oikeus vaatia takaisin 71 §:n perusteella maksamansa korvaus sen ETA-valtion korvauselimeltä, jossa vakuutussopimuksen tehneen vakuutusyhtiön toimipaikka on."

**Recourse Scenarios:**
1. Vehicle doesn't require insurance → National fund of vehicle's home country
2. Insurer unidentifiable → Fund of vehicle's home country
3. Vehicle unidentified → Fund of accident location
4. Third-country vehicle → Fund of accident location
5. Insurance obligation neglected → Fund of vehicle's home country

---

## METADATA

- **Law**: Liikennevakuutuslaki (Traffic Insurance Act) 460/2016
- **Source**: finlex.fi/fi/lainsaadanto/2016/460
- **Version**: 1.3 (Negative Claims First)
- **Total Decisions**: 30 (17 Negative Claims + 13 Eligibility)
- **Decision Order**: Negative Claims → Eligibility → Compensation
- **Variable Convention**: entity.attribute (ontology-aligned)
