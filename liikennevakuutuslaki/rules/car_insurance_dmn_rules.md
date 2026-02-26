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
| Time Limits | E12-E13 | §§74-77 |
| Rail-Road Liability | E14-E15 | §52 |

**Total: 15 eligibility decisions**

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
│ 2. ELIGIBILITY     │───→ E1-E15
│ (Coverage, Calc,   │     Coverage Determination
│  Benefits, Time,   │     Compensation Calculation
│  Rail-Road Liab.)  │     Rail-Road Apportionment
└──────────┬──────────┘
           │ Eligible
           ▼
    COMPENSATION PAID
```

---

## SECTION 1: NEGATIVE CLAIMS RULES (Check First)

### 0.1 Contract Validity - Mandatory Provisions (§3)

#### VAL-001: Mandatory Nature of Provisions (§3)

| contract.term.deviatesFromLaw | party.affected | term.detrimentalToParty | Output |
|------------------------------|----------------|------------------------|--------|
| true | Policyholder | true | **VOID** |
| true | Insured | true | **VOID** |
| true | Victim | true | **VOID** |
| true | EntitledParty | true | **VOID** |
| false | any | any | **VALID** |
| true | any | false | **VALID** |

**§3:** "Sopimusehto, joka poikkeaa tämän lain säännöksistä vakuutuksenottajan, vakuutetun, vahinkoa kärsineen tai muun korvaukseen oikeutetun vahingoksi, on mitätön."

**Purpose:** Any contract term that deviates from mandatory provisions to the detriment of protected parties is automatically void.

---

### 0.2 Liikennevakuutuskeskus (LVK) Scope and Application (§4)

#### LVK-000: LVK Scope and Application (§4)

| scenario.type | vehicle.homeCountry | vehicle.insuranceStatus | insurer.identifiable | lvk.appliesAs | applicableSections |
|--------------|--------------------|----------------------|---------------------|---------------|-------------------|
| ForeignVehicleAccident | Non-Finland | any | false | InsurerSubstitute | §32(3) |
| ExemptVehicle | Finland | Exempt | N/A | InsurerSubstitute | §43 |
| UnknownVehicle | any | Unknown | false | InsurerSubstitute | §44 |
| UninsuredObligation | Finland | NoInsurance | N/A | InsurerSubstitute | §46 |
| NormalCase | any | Insured | true | NotApplicable | N/A |

**§4:** "Liikennevakuutuskeskuksesta ja sen toiminnan rahoituksesta ja hallinnosta säädetään Liikennevakuutuskeskuksesta annetussa laissa (461/2016)."

**§4 Cross-Reference:** When LVK applies, provisions of §§9, 11, 12, 14, 15, 20, 24, 25, 33-39, 49-52, 55-68, 73, 79-85, 95 apply to LVK as if it were the insurer.

**Key Provisions:**
- LVK replaces insurer in specific situations
- LVK covers damages when:
  - Foreign vehicle causes damage in Finland (§32(3))
  - Exempt vehicle causes damage (§43)
  - Unknown vehicle causes damage (§44)
  - Insurance obligation neglected (§46)

---

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

#### N19: Rescue Assistance Coverage (§39)

| person.renderedAid | rescue.professional | damage.type | Output |
|-------------------|---------------------|-------------|--------|
| true | false | PersonalInjury | **COVERED** |
| true | false | PropertyDamage | **COVERED** |
| true | true | any | **NOT_COVERED** |
| false | any | any | **N/A** |

**§39:** "Jos joku on liikenneonnettomuuden seurauksena joutunut sellaiseen tilaan, että hänelle on välttämätöntä heti antaa ensiapua tai kuljettaa hänet saamaan hoitoa, liikennevahingosta vastuussa oleva vakuutusyhtiö on velvollinen korvaamaan vahinkoa kärsinyttä auttaneelle henkilölle auttamisesta aiheutuneen välittömän henkilö- ja esinevahingon."

**Exception:** "Vahinkoja, jotka ovat aiheutuneet pelastustointa ammattimaisesti hoitavalle henkilölle tai tähän toimintaan liittyvälle omaisuudelle, ei kuitenkaan korvata."

---

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

### 0.2 Border Traffic Insurance (§7)

#### BORDER-001: Third-Country Vehicle Border Insurance (§7)

| vehicle.homeCountry | greenCard.valid | lvk.commitment | accident.location | Output |
|--------------------|-----------------|----------------|-------------------|--------|
| ThirdCountry | false | false | Finland | **InsuranceRequired_BorderTraffic** |
| ThirdCountry | false | false | Sweden | **InsuranceRequired_BorderTraffic** |
| ThirdCountry | false | false | Norway | **InsuranceRequired_BorderTraffic** |
| ThirdCountry | false | false | any | **InsuranceNotRequired** |
| ThirdCountry | true | any | any | **Covered_ByGreenCard** |
| ThirdCountry | any | true | any | **Covered_ByLVK** |
| EEA | N/A | N/A | any | **Covered_ByEEA** |
| Finland | N/A | N/A | any | **DomesticRules** |

**BORDER-002: Driver Injury Coverage Limitation (§7(3))**

| vehicle.homeCountry | accident.location | damage.type | Output |
|--------------------|-------------------|-------------|--------|
| ThirdCountry | Finland | PersonalInjury_Driver | **COVERED** |
| ThirdCountry | Sweden | PersonalInjury_Driver | **COVERED** |
| ThirdCountry | Norway | PersonalInjury_Driver | **COVERED** |
| ThirdCountry | any | PersonalInjury_Driver | **NOT_COVERED** |
| ThirdCountry | any | PropertyDamage | **COVERED** |
| ThirdCountry | any | PersonalInjury_Passenger | **COVERED** |

**§7:** "Sen, joka tuo Suomeen tilapäistä käyttöä varten ajoneuvon, jonka pysyvä kotipaikka on kolmannessa maassa, tulee ottaa tälle ajoneuvolle rajaliikennevakuutus."

**§7(3):** "Ajoneuvon rajaliikennevakuutuksesta korvataan tämän ajoneuvon kuljettajalle aiheutunut henkilövahinko vain, jos vahinkotapahtuma on sattunut Suomessa, Ruotsissa tai Norjassa."

---

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

#### E3b: Guarantee Fund Coverage Outside Finland (§45)

| accident.locationCountry | victim.residenceCountry | vehicle.ownerCountry | vehicle.identified | response.twoMonths | Output |
|-------------------------|------------------------|----------------------|-------------------|-------------------|--------|
| EEA (not FI) | Finland | any | any | any | **Covered_ByLVK** |
| EEA (not FI) | Finland | unknown | unknown | any | **Covered_ByLVK** |
| Non-EEA | Finland | EEA | any | no_insurer | **Covered_ByLVK** |
| Non-EEA (GreenCard) | Finland | any | any | any | **Covered_ByLVK** |

**§45(1):** "Liikennevakuutuskeskus korvaa 43 §:n 1 momentissa tarkoitetun ajoneuvon liikenteeseen käyttämisestä aiheutuneen liikennevahingon silloin, kun se on sattunut muussa ETA-valtiossa kuin Suomessa..."

**§45(2):** "Jos tuntemattomaksi jääneen ajoneuvon... vahinkoa kärsinyt, jolla on kotipaikka Suomessa, voi esittää korvausvaatimuksensa Liikennevakuutuskeskukselle."

#### E4: Insurance Obligation Liable Party (§6)

| person.owner.exists | person.holder.exists | vehicle.ownershipTransferred | Output |
|---------------------|----------------------|------------------------------|--------|
| true | true | true | **OwnerAndHolderJointlyLiable** |
| true | false | true | **OwnerLiable** |
| false | true | true | **HolderLiable** |
| true | false | false | **OwnerLiableFromOwnership** |

#### OBL-001: Joint Liability of Owner and Holder (§6)

| party.type | party.relationship | otherObligatedParty.exists | jointLiability.applies | Output |
|-----------|-------------------|---------------------------|----------------------|--------|
| Owner | RegisteredOwner | Holder | Yes | **JointlyLiable_Yhteisvastuu** |
| Holder | RegisteredHolder | Owner | Yes | **JointlyLiable_Yhteisvastuu** |
| Owner | RegisteredOwner | none | No | **SolelyLiable** |
| Holder | RegisteredHolder | none | No | **SolelyLiable** |

**§6(1):** "Jos vakuuttamisvelvollisia on enemmän kuin yksi, he ovat yhteisvastuussa vakuutuksen ottamisesta."

**Joint Liability Rule:**
- If both Owner AND Holder exist → both are yhteisvastuussa (jointly liable)
- Either can be held responsible for full obligation
- Payment by one discharges the other's obligation

#### OBL-002: EEA Import Immediate Coverage (§6(2))

| vehicle.importType | delivery.accepted | registration.completed | insurance.obligationStarts | effectiveDate |
|-------------------|-------------------|----------------------|---------------------------|---------------|
| EEAImport | true | false | Immediately | delivery.acceptanceDate |
| EEAImport | true | true | Standard | registration.date |
| Domestic | N/A | true | Standard | ownership.transferDate |

**§6(2):** "Edellä 1 momentista poiketen toisesta ETA-maasta Suomeen tuotavan ajoneuvon vakuuttamisvelvollisuus alkaa välittömästi, kun ajoneuvon ostaja on sopimuksessa hyväksynyt ajoneuvon toimituksen, vaikka ajoneuvoa ei ole vielä rekisteröity Suomessa."

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

### 0.3 Policy Termination (§16)

#### TERM-001: Policyholder Termination Rights (§16(1))

| termination.reason | newInsurance.exists | theft.reported | Output |
|-------------------|---------------------|----------------|--------|
| NewInsurance | true | N/A | **TerminationAllowed** |
| Theft | N/A | true | **TerminationAllowed** |
| any | false | false | **TerminationDenied** |

**§16(1):** "Vakuutuksenottajalla, jonka vakuuttamisvelvollisuus ei ole päättynyt, on oikeus irtisanoa rekisteröidyn ajoneuvon vakuutus ainoastaan silloin, kun vakuutuksenottaja on ottanut vakuutuksen toisesta vakuutusyhtiöstä tai ajoneuvo on anastettu ja siitä on tehty ilmoitus poliisille ja vakuutusyhtiölle."

#### TERM-002: Automatic Termination Events (§16(2))

| termination.event | Output |
|-------------------|--------|
| PermanentRemoval | **Terminates_Immediate** |
| OwnershipTransfer | **Terminates_Immediate** |
| HolderReturnsToOwner | **Terminates_Immediate** |
| NewInsuranceTaken | **Terminates_Immediate** |

**§16(2):** "Vakuutuksen voimassaolo päättyy ilmoituksessa mainittuna päivänä" when:
1) ajoneuvo on poistettu lopullisesti liikennekäytöstä
2) ajoneuvo on siirtynyt oikeustoimen johdosta muulle uudelle omistajalle tai haltijalle
3) ajoneuvon hallinta palautuu omistajalle tai hallinta siirtyy uudelle haltijalle
4) vakuutus on otettu toisesta vakuutusyhtiöstä

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

### 2.8 Mandatory Opinion Requirements (§66)

#### MOP-001: Mandatory Liikennevahinkolautakunta Opinion Triggers (§66)

| claim.compensationType | injury.severity | claim.isCorrection | correction.partyAgreed | Output |
|-----------------------|-----------------|-------------------|----------------------|--------|
| ContinuousCompensation_Permanent | any | false | N/A | **OpinionMandatory** |
| ContinuousCompensation_Death | any | false | N/A | **OpinionMandatory** |
| ContinuousCompensation_Increase | any | false | N/A | **OpinionMandatory** |
| ContinuousCompensation_Decrease | any | false | N/A | **OpinionMandatory** |
| PainSuffering | Severe | false | N/A | **OpinionMandatory** |
| PainSuffering | any | true | false | **OpinionMandatory** (unless obvious error) |
| PainSuffering | any | true | true | **OpinionNotRequired** |
| any | any | true | N/A | **OpinionNotRequired** |

**§66 Mandatory Triggers:**
1) Pysyvän ansionmenetyksen taikka kuoleman perusteella suoritettavaa jatkuvaa korvausta tai sen sijasta suoritettavaa kertakaikkista pääoma-arvoa
2) Jatkuvan korvauksen korottamista tai alentamista vahingonkorvauslain 5 luvun 8 §:n perusteella
3) Haitan perusteella suoritettavaa korvausta, jos vamma on vaikea
4) Virheellisen päätöksen oikaisua asianosaisen vahingoksi, jos asianosainen ei suostu virheen korjaamiseen (ellei virhe ole ilmeinen ja aiheutunut asianosaisen omasta menettelystä)

---

### 2.9 Foreign Claims Representative Rules (§70)

#### FCR-001: Foreign Representative 3-Month Deadline (§70)

| accident.locationCountry | vehicle.homeCountry | victim.residenceCountry | daysSinceClaim | claim.status | Output |
|------------------------|--------------------|------------------------|-----------------|--------------|--------|
| EEA | EEA | Finland | ≤90 | ClaimComplete | **ResponseRequired** |
| EEA | EEA | Finland | ≤90 | LiabilityDisputed | **JustifiedResponseRequired** |
| EEA | EEA | Finland | >90 | NoResponse | **LVK_TakesOver** |
| GreenCard | GreenCard | Finland | ≤90 | ClaimComplete | **ResponseRequired** |
| GreenCard | GreenCard | Finland | ≤90 | LiabilityDisputed | **JustifiedResponseRequired** |
| GreenCard | GreenCard | Finland | >90 | NoResponse | **LVK_TakesOver** |
| Finland | any | any | any | any | **DomesticRulesApply** |

**§70(2):** "Korvausedustajan on kolmen kuukauden kuluessa päivästä, jona vahinkoa kärsinyt on esittänyt korvausvaatimuksensa, korvattava 1 momentissa tarkoitettu liikennevahinko tai tehtävä perusteltu korvaustarjous, jos korvausvastuuta ei kiistetä ja jos vahinkojen suuruus on määritelty."

**§71:** If representative fails to respond within 3 months, victim can demand compensation from Liikennevakuutuskeskus.

#### FCR-002: Representative Appointment Requirements (§69)

| insurer.operatesInEEAState | representative.appointed | representative.residesInState | rep.speaksLocalLanguage | rep.contactReported | Output |
|-------------------------|-------------------------|-------------------------------|------------------------|---------------------|--------|
| true | true | true | true | true | **Compliant** |
| true | false | any | any | any | **NonCompliant_MustAppoint** |
| true | true | false | any | any | **NonCompliant_MustReside** |
| true | true | true | false | any | **NonCompliant_Language** |
| true | true | true | true | false | **NonCompliant_MustReport** |
| false | any | any | any | any | **NotApplicable** |

**§69:** Insurer must appoint representative in each EEA state where operating. Representative must reside/be established in that state, be able to operate in official languages, and report names/contact info to information centers.

#### FCR-003: LVK Backup Liability (§71)

| daysSinceClaim | representative.responded | response.justified | victim.demandedFromLVK | lvk.mustProcess |
|---------------|------------------------|-------------------|----------------------|-----------------|
| >90 | false | N/A | true | ProcessWithin2Months |
| >90 | true | true | any | LVKStopsProcessing |
| ≤90 | any | any | false | AwaitingRepresentative |
| ≤90 | any | any | true | AwaitingRepresentative |

**§71:** If representative doesn't respond within 3 months, victim can demand from LVK. LVK must act within 2 months of receiving claim. LVK stops processing if insurer/representative provides justified response.

#### FCR-004: 7-Year Information Limitation (§72)

| info.requested | accident.date | yearsSinceAccident | lvk.mustProvideInfo |
|----------------|---------------|--------------------|---------------------|
| OwnerHolderDetails | any | ≤7 | Provide |
| InsurerDetails | any | ≤7 | Provide |
| RepresentativeInfo | any | ≤7 | Provide |
| OwnerHolderDetails | any | >7 | NotRequired |
| InsurerDetails | any | >7 | NotRequired |
| RepresentativeInfo | any | >7 | NotRequired |

**§72:** LVK must provide owner/holder name and address, insurer info, and representative details. 7-year limitation: No duty to provide info for accidents >7 years ago.

---

### 2.10 Subrogation Rights (§73)

#### SUB-001: Insurer Subrogation - Individual vs Corporation (§73)

| responsibleParty.type | responsibleParty.relationship | cause.intentional | cause.grossNegligence | driver.condition_§48 | subrogation.applies | Output |
|----------------------|------------------------------|-------------------|----------------------|---------------------|---------------------|--------|
| PrivateIndividual | any | false | false | any | **NoSubrogation** | **SubrogationDenied** |
| PrivateIndividual | Owner/Holder/Driver/Passenger | true | any | any | **SubrogationAllowed** | **SubrogationAllowed** |
| PrivateIndividual | Owner/Holder/Driver/Passenger | false | true | any | **SubrogationAllowed** | **SubrogationAllowed** |
| PrivateIndividual | Owner/Holder/Driver/Passenger | false | false | any | **SubrogationAllowed** | **SubrogationAllowed** (if §48 applies) |
| Corporation | any | false | false | any | **SubrogationAllowed** | **SubrogationAllowed** |
| Corporation | any | true | any | any | **SubrogationAllowed** | **SubrogationAllowed** |
| ThirdParty | any | any | any | any | **SubrogationAllowed** | **SubrogationAllowed** |

**§73 Key Distinction:**
- **Private individuals** (yksityishenkilö): Subrogation only if caused intentionally or with gross negligence, OR if driver was in §48(1) conditions
- **Corporations/entities**: Subrogation allowed in all cases
- **Employees, officials**: Treated as private individuals (§73 limits subrogation)

**Protected persons under §73:**
- Työntekijä (employee)
- Virkamies (official)  
- Other persons equated under Tort Liability Act §3:1
- Ajoneuvon omistaja, haltija, kuljettaja, matkustaja

---

### 2.11 Liikennevakuutuskeskus Recourse (§74)

#### LVK-001: LVK Recourse Scenarios (§74)

| vehicle.insuranceRequired | vehicle.ownerFound | vehicle.identified | vehicle.homeCountry | recourse.target | Output |
|-------------------------|-------------------|-------------------|---------------------|-----------------|--------|
| false | N/A | any | EEA | **NationalGuaranteeFund_HomeCountry** | **RecourseToGuaranteeFund** |
| true | false | true | EEA | **NationalGuaranteeFund_AccidentCountry** | **RecourseToGuaranteeFund** |
| true | false | false | any | **NationalGuaranteeFund_AccidentCountry** | **RecourseToGuaranteeFund** |
| any | any | any | Non-EEA | **NationalGuaranteeFund_AccidentCountry** | **RecourseToGuaranteeFund** |
| true | true | any | any | **NotApplicable** | **NoRecourse** |

**§74 Recourse Triggers:**
1) Ajoneuvoa ei ole velvollisuus vakuuttaa → ETA-valtion takuurahasto (kotipaikka)
2) Vakuutusyhtiötä ei saada selville → ETA-valtion takuurahasto (kotipaikka)
3) Ajoneuvo jää tunnistamatta → ETA-valtion takuurahasto (vahinkomaa)
4) Kolmannesta maasta peräisin oleva ajoneuvo → ETA-valtion takuurahasto (vahinkomaa)
5) Vakuuttamisvelvollisuus laiminlyöty → ETA-valtion takuurahasto (kotipaikka)

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

---

### 2.12 Insurer Cannot Refuse Insurance (§17)

#### INS-001: Mandatory Insurance Acceptance (§17)

| insurer.licenseType | vehicle.vehicleType | insurer.licenseCovers | application.received | Output |
|--------------------|--------------------|---------------------|---------------------|--------|
| vahinkovakuutusluokka_10 | MotorVehicle | true | true | **MustAccept** |
| vahinkovakuutusluokka_10 | Trailer | true | true | **MustAccept** |
| vahinkovakuutusluokka_10 | any | false | true | **CannotAccept** |
| any | any | any | false | **ApplicationNotReceived** |

**§17(2):** "Vakuutusyhtiö, joka harjoittaa liikennevakuutustoimintaa, ei saa kieltäytyä antamasta ja voimassa pitämästä siltä haettua vakuutusta, jos vakuutus koskee sellaista ajoneuvoa, jota varten yhtiöllä toimilupansa sekä vahvistetun yhtiöjärjestyksensä mukaan on oikeus antaa vakuutus."

**§17(3):** "Mitä 2 momentissa säädetään, ei koske raja- ja siirtoliikennevakuutuksia."

**Exceptions:**
- Border traffic insurance (§7) - separate rules
- Transfer traffic insurance (§12(3)) - separate rules

---

### 2.13 Document Retention Requirements (§85)

#### DOC-001: Document Retention Periods (§85)

| document.type | document.category | retention.periodYears | retention.startDate | Output |
|--------------|------------------|---------------------|-------------------|--------|
| Policy_Documents | Voimassaolo | 100 | PolicyTermination | **Retain_100Years** |
| PersonalInjury_Claims | Henkilövahinko | 100 | ClaimSettlement | **Retain_100Years** |
| Appeal_Documents | Muutoksenhaku | 50 | CaseResolution | **Retain_50Years** |
| Administrative_Documents | Toimeenpano | 10 | DocumentReceipt | **Retain_10Years** |

**§85 Document Retention Requirements:**
1) vakuutuksen voimassaoloa ja henkilövahinkoa koskevat asiakirjat vähintään 100 vuoden ajan
2) muutoksenhakua koskevat asiakirjat vähintään 50 vuoden ajan
3) muut tämän lain toimeenpanoa koskevat asiakirjat vähintään 10 vuoden ajan

**§85(2):** "Korvausasiaa koskevan asiakirjan säilytysaika alkaa siitä, kun korvausasia on tullut vakuutusyhtiössä vireille. Vakuuttamiseen liittyvän asiakirjan säilytysaika alkaa siitä, kun asiakirja saapui vakuutusyhtiölle."

---

### 2.14 Customs Border Insurance Enforcement (§90/§91)

#### CUST-001: Customs Border Insurance Requirement (§91)

| vehicle.importType | vehicle.homeCountry | vehicle.temporaryUse | customs.controlPoint | greenCard.valid | borderInsurance.valid | Output |
|-------------------|--------------------|--------------------|--------------------|-----------------|---------------------|--------|
| TemporaryImport | ThirdCountry | true | BorderCrossing | false | false | **InsuranceRequired_CustomsEnforced** |
| TemporaryImport | ThirdCountry | true | BorderCrossing | true | any | **Covered_ByGreenCard** |
| TemporaryImport | ThirdCountry | true | BorderCrossing | false | true | **Covered_ByBorderInsurance** |
| PermanentImport | any | false | any | any | any | **DomesticRulesApply** |
| EEA_Import | EEA | any | any | any | any | **DomesticRulesApply** |

**§91(1):** "Tulli valvoo, että kolmannesta maasta Suomeen tilapäistä käyttöä varten tuodun ajoneuvon omistaja tai haltija on täyttänyt 7 §:ssä säädetyn velvollisuutensa ottaa ajoneuvolle rajaliikennevakuutus."

**§91(2):** "Jos 1 momentissa tarkoitetulla ajoneuvolla ei sitä maahan tuotaessa ole vihreää korttia tai rajaliikennevakuutusta, Tulli kantaa vakuutusmaksun siltä ajalta, jona ajoneuvoa on tarkoitus käyttää Suomessa tai muussa ETA-valtiossa, ja antaa vakuutusyhtiöiden puolesta ajoneuvolle ETA-valtioissa voimassa oleva vakuutustodistus."

#### CUST-002: Customs Insurance Collection (§91)

| customs.situation | vehicle.usagePeriod | payment.status | customs.action | Output |
|------------------|-------------------|----------------|---------------|--------|
| NoInsurance_AtImport | Known | Unpaid | Collect_PremiumForPeriod | **PremiumCollected_CertificateIssued** |
| NoInsurance_AtImport | Unknown | Unpaid | Collect_1MonthPremium | **PremiumCollected_MonthlyCertificate** |
| NoInsurance_Export | any | Unpaid | Collect_1MonthPremium | **PremiumCollected_ExportCertificate** |
| Insurance_Valid | any | Paid | NoAction | **NoActionRequired** |

**§91(3):** "Jos vakuutusmaksua ei ole suoritettu koko siltä ajalta kuin 2 momentissa edellytetään, Tulli kantaa ajoneuvon maastaviennin yhteydessä yhden kuukauden vakuutusmaksun ja antaa tätä koskevan uuden vakuutustodistuksen."

#### CUST-003: Temporary Import from Another EEA State (§91)

| vehicle.homeCountry | vehicle.importType | customs.controlPoint | insurance.status | Output |
|--------------------|-------------------|--------------------|-----------------|--------|
| ThirdCountry | TemporaryImport | EEA_Border | NoInsurance | **CustomsEnforcement_Required** |
| ThirdCountry | TemporaryImport | Finland_Border | NoInsurance | **CustomsEnforcement_Required** |
| ThirdCountry | TemporaryImport | any | ValidInsurance | **NoEnforcement** |
| EEA | TemporaryImport | any | any | **DomesticRulesApply** |

**§91(4):** "Tulli valvoo osana suorittamaansa tullivalvontaa myös, että toisesta ETA-valtiosta Suomeen tilapäistä käyttöä varten tuodulla ajoneuvolla, jonka kotipaikka on kolmannessa maassa, on voimassa oleva liikenne- tai rajaliikennevakuutus."

**§91(5):** "Tulli tilittää tämän pykälän nojalla kantamansa maksut Liikennevakuutuskeskukselle."

---

## §52: Rail Traffic Liability Sharing Rules

### 2.15 Rail-Road Liability Apportionment (§52)

#### RAIL-001: Rail-Road Liability Apportionment (§52)

| accident.involvesRailVehicle | accident.involvesRoadVehicle | fault.railContributingFactors | fault.roadContributingFactors | Output |
|------------------------------|------------------------------|-------------------------------|-------------------------------|--------|
| true | true | Present | Present | **ProportionalSharing_ByNegligence** |
| true | true | None | Present | **RoadOnlyLiable** |
| true | true | Present (§5 rail act) | None | **RailOnlyLiable** |
| true | true | None | None | **Proportional_ByOtherFactors** |

**§52(1):** "Jos vahinkoa kärsineellä on oikeus saada saman vahinkotapahtuman johdosta korvausta sekä tämän lain että raideliikennevastuulain (113/1999) nojalla, vastuu vakuutusyhtiön ja raideliikennevastuulain mukaan korvausvelvollisen kesken jaetaan sen mukaan kuin ilmenneeseen huolimattomuuteen ja muihin vahingon aiheuttaneisiin seikkoihin nähden on kohtuullista."

**§52(2):** "Jos kuitenkin vahinko on aiheutunut yksinomaan tämän lain 33 §:n 1 momentissa tai raideliikennevastuulain 5 §:ssä mainitusta seikasta, korvaus jää kokonaan vahingon aiheuttaneen osapuolen suoritettavaksi."

#### RAIL-002: Overpayment Subrogation (§52)

| insurer.paymentAmount | insurer.apportionedShare | overpayment.exists | Output |
|----------------------|--------------------------|-------------------|--------|
| any | calculatedShare | true | **Subrogation_RightToRecover** |
| shareAmount | sameAmount | false | **NoSubrogation** |

**§52(3):** "Jos liikennevakuutusyhtiö on maksanut vahingonkorvausta yli oman osuutensa, sillä on oikeus saada raideliikennevastuulain mukaan korvausvelvolliselta, mitä se on tämän osalta maksanut."

---

## §81: Municipality Appeal Rights

### 2.15b Municipality Appeal Rights (§81)

#### MUN-001: Municipality Party Status (§81)

| entity.type | claim.type | municipality.providedCare | Output |
|------------|-----------|--------------------------|--------|
| municipality | victim_compensation | any | **NotParty** |
| municipality | full_cost_payment | true | **CanAppeal** |

**§81(1):** "Kunta tai kuntayhtymä ei ole asianosainen asiassa, joka koskee vahinkoa kärsineen oikeutta tämän lain mukaiseen korvaukseen..."

**§81(2):** "Kunta tai kuntayhtymä saa hakea muutosta täyskustannusmaksua koskevaan päätökseen..."

---

## §82-83: Information Access Rights

### 2.16 Information Access from Employers (§82)

#### INFO-001: Employer Information Request (§82)

| request.authority | request.purpose | request.necessary | information.type | Output |
|------------------|-----------------|-----------------|-----------------|--------|
| insurer | claim_processing | true | employment_details | **MustProvide** |
| insurer | claim_processing | true | salary_payments | **MustProvide** |
| insurer | claim_processing | true | benefits_received | **MustProvide** |
| insurer | other | any | any | **CannotRequest** |
| lvk | enforcement | true | uninsured_vehicles | **MustProvide** |

**§82(1):** "Vakuutusyhtiöllä on oikeus saada tiedot vahinkoa kärsineen tai korvaukseen oikeutetun työsuhteista, yrittäjätyöstä ja ansioista, hänelle maksetuista etuuksista sekä muista näihin verrattavista seikoista."

#### INFO-002: Medical Information Request (§82)

| request.authority | request.purpose | request.necessary | patient.consent | Output |
|------------------|-----------------|-----------------|-----------------|--------|
| insurer | claim_processing | true | implicit | **MustProvide_MedicalRecords** |
| insurer | claim_processing | true | explicit | **MustProvide_Full** |
| insurer | claim_processing | false | any | **CannotRequest** |
| lvk | enforcement | any | any | **MustProvide_Anonymous** |

**§82(1):** "Lääkäriltä ja muulta terveydenhuollon ammattihenkilöistä annetussa laissa tarkoitetulta ammattihenkilöltä... tiedot potilasasiakirjoista, terveydentilasta, työkyvystä, hoidosta ja kuntoutuksesta."

### 2.17 Technical Data Access (§83)

#### INFO-003: Technical Connection for Data Retrieval (§83)

| data.system | connection.authorized | technical_access_available | request.purpose | Output |
|------------|---------------------|-------------------------|-----------------|--------|
| traffic_register | true | true | enforcement | **AutomatedAccess_Granted** |
| vehicle_registry | true | true | insurance_obligation | **AutomatedAccess_Granted** |
| customs | true | true | border_control | **AutomatedAccess_Granted** |
| any | false | any | any | **AccessDenied** |

**§83:** "Tässä pykälässä tarkoitettuja tietoja saa hakea teknisen käyttöyhteyden avulla ilman sen suostumusta, jonka etujen suojaamiseksi salassapitovelvollisuus on säädetty."

### 2.18 LVK Enforcement Information (§82(4))

#### INFO-004: LVK Right to Uninsured Vehicle Data (§82)

| data.category | enforcement.purpose | lvk.request | Output |
|--------------|-------------------|-------------|--------|
| traffic_removal | 29_section | true | **MustProvide** |
| vehicle_modification | enforcement | true | **MustProvide** |
| private_to_professional | license_check | true | **MustProvide** |
| any | other | true | **CannotRequest** |

**§82(4):** "Liikennevakuutuskeskuksella on oikeus... saada viranomaisilta ja vakuutusyhtiöiltä tiedot vakuuttamattomista ajoneuvoista..."

---

### 2.19 Traficom Reporting Obligations (§90)

#### TRAF-001: Traficom Reporting Events (§90)

| event.type | event.occurred | insurance.exists | daysSinceOwnershipChange | traficom.mustReport | lvk.notification |
|-----------|---------------|-----------------|------------------------|-------------------|-----------------|
| PermanentRemoval | true | any | N/A | true | ReportToLVK |
| InsuranceTransfer | true | N/A | N/A | true | ReportToLVK |
| OwnerHolderChange | true | true | ≤7 | true | StandardReport |
| OwnerHolderChange | true | false | >7 | true | PenaltyAssessmentNotice |
| TrafficUseStart | true | any | N/A | true | ReportToLVK |
| TrafficUseEnd | true | any | N/A | true | ReportToLVK |

**§90(1):** Liikenteen turvallisuusviraston on ilmoitettava Liikennevakuutuskeskukselle:
1) ajoneuvon lopullinen poisto rekisteristä;
2) ajoneuvon vakuutuksen siirtyminen toiseen vakuutusyhtiöön;
3) ajoneuvon omistajan ja haltijan vaihtuminen; ja
4) ajoneuvon liikennekäyttöön ottaminen ja liikennekäytöstä poisto.

#### TRAF-002: Uninsured Vehicle Penalty Trigger (§90(2))

| ownership.changed | insurance.taken | daysElapsed | traficom.action | lvk.action |
|------------------|-----------------|-------------|----------------|------------|
| true | false | >7 | NotifyLVK | InitiatePenaltyAssessment_§27-28 |
| true | true | ≤7 | None | None |
| false | any | any | None | None |

**§90(2):** "Jos ajoneuvoa varten ei ole otettu vakuutusta 7 päivän kuluessa ajoneuvon omistusoikeuden alkamisesta tai hallintaoikeuden vaihtumisesta, Liikenteen turvallisuusviraston on ajoneuvoa rekisteröidessään lähetettävä ilmoitus siitä, ettei vakuutusta ole otettu Liikennevakuutuskeskukselle 27 ja 28 §:ssä tarkoitettujen maksujen määräämistä varten."

---

## METADATA

- **Law**: Liikennevakuutuslaki (Traffic Insurance Act) 460/2016
- **Source**: finlex.fi/fi/lainsaadanto/2016/460
- **Version**: 1.5 (Added §52 Rail Traffic Liability Sharing Rules)
- **Total Decisions**: 35 (17 Negative Claims + 18 Eligibility)
- **Decision Order**: Negative Claims → Eligibility → Compensation
- **Variable Convention**: entity.attribute (ontology-aligned)
