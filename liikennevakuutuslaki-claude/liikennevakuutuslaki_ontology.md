# Finnish Motor Vehicle Liability Insurance Ontology

**Effective date:** 2017-01-01  
**Version:** 1.0  
**Author:** Lumen ⚖️ — Finnish Legal Engineer  

## Table of Contents

**56 entities** across 8 categories.

- **👤 Person** (5)
  - [Policyholder / Vakuutuksenottaja](#policyholder)
  - [Insured Person / Vakuutettu](#insuredperson)
  - [Injured Party / Claimant / Vahinkoa kärsinyt / Korvaukseen oikeutettu](#claimantperson)
  - [Compensation Representative / Korvausedustaja](#compensationrepresentative)
  - [Compensation Agent / Korvausasiamies](#compensationagent)
- **🏛️ Organization** (5)
  - [Insurer / Insurance Company / Vakuutusyhtiö](#insurer)
  - [Finnish Motor Insurers' Centre / Liikennevakuutuskeskus](#liikennevakuutuskeskus)
  - [State Treasury (Valtiokonttori) / Valtiokonttori](#valtiokonttori)
  - [Traffic Accident Board / Liikennevahinkolautakunta](#liikennevahinkolautakunta)
  - [Financial Supervisory Authority (Finanssivalvonta) / Finanssivalvonta](#finanssivalvonta)
- **🚗 Vehicle** (9)
  - [Motor Vehicle / Ajoneuvo (moottoriajoneuvo)](#motorvehicle)
  - [Trailer / Perävaunu](#trailer)
  - [Agricultural / Motor Work Machine (slow) / Moottorityökone / Traktori (hidas)](#agriculturalworkmachine)
  - [Combine Harvester / Farm Harvest Machine / Leikkuupuimuri / Sadonkorjuukone](#harvestcombine)
  - [Foreign Vehicle / Ulkomainen ajoneuvo](#foreignvehicle)
  - [ETA Foreign Vehicle / Toisessa ETA-valtiossa rekisteröity ajoneuvo](#etaforeignvehicle)
  - [Third-Country Vehicle / Kolmannen maan ajoneuvo](#thirdcountryvehicle)
  - [Uninsured Vehicle / Vakuuttamaton ajoneuvo](#uninsuredvehicle)
  - [Unknown / Hit-and-Run Vehicle / Tuntemattomaksi jäänyt ajoneuvo](#unknownvehicle)
- **⚡ Event** (4)
  - [Traffic Accident / Traffic Damage Event / Liikennevahinko / Vahinkotapahtuma](#trafficaccident)
  - [Personal Injury Event / Henkilövahinkotapahtuma](#personalinjuryevent)
  - [Property Damage Event / Esinevahinkotapahtuma](#propertydamageevent)
  - [Major Accident (Suurvahinko) / Suurvahinko](#majoraccident)
- **💶 Compensation** (10)
  - [Personal Injury Compensation / Henkilövahingon korvaus](#personalinjurycompensation)
  - [Pain and Suffering / Temporary Disability Compensation / Kipu ja särky sekä muu tilapäinen haitta](#painandsufferingcompensation)
  - [Loss of Earnings Compensation / Ansionmenetyskorvaus](#lossofearningscompensation)
  - [Permanent Disability Compensation / Pysyvän haitan korvaus](#permanentdisabilitycompensation)
  - [Loss of Maintenance Compensation (Death) / Elatuksen menetyksen korvaus](#lossofmaintenancecompensation)
  - [Death Benefits / Kuoleman johdosta suoritettavat korvaukset](#deathbenefitscompensation)
  - [Rehabilitation Compensation / Kuntoutuskorvaus](#rehabilitationcompensation)
  - [Property Damage Compensation / Esinevahingon korvaus](#propertydamagecompensation)
  - [Medical / Healthcare Costs / Sairaanhoidon kustannukset](#medicalcarecosts)
  - [Rescuer's Compensation / Auttajalle aiheutuneen vahingon korvaus](#rescuercompensation)
- **📋 Rule** (17)
  - [Motor Vehicle Liability Insurance (Compulsory) / Liikennevakuutus](#motorliabilityinsurance)
  - [Border Traffic Insurance / Rajaliikennevakuutus](#bordertrafficinsurance)
  - [Transit Traffic Insurance / Siirtoliikennevakuutus](#transittrafficinsurance)
  - [Strict Liability (No-Fault) Rule / Ankara (tuottamuksesta riippumaton) vastuu](#strictliabilityrule)
  - [Fault-Based Allocation Between Vehicles / Tuottamusperusteinen korvausvastuun jako (useamman ajoneuvon vahingot)](#faultbasedallocationrule)
  - [Contributory Negligence — Personal Injury / Myötävaikutus — henkilövahinko](#contributorynegligencerule)
  - [Alcohol / Intoxicant Effect on Compensation / Alkoholin tai huumaavan aineen vaikutus korvaukseen](#alcoholrule)
  - [Unauthorised Vehicle Use (Theft etc.) / Luvattomasti käyttöön otettu ajoneuvo](#unauthoriseduserule)
  - [Subrogation / Right of Recourse / Takautumisoikeus](#subrogationrule)
  - [Claim Filing Deadline (Limitation) / Korvausvaatimuksen esittämisajankohta / Vanhentuminen](#claimfilingdeadline)
  - [Decision Deadline / Korvauksen suorittamisen määräaika](#decisiondeadline)
  - [Cross-Border Claim Deadline (Compensation Representative) / Korvausedustajan vastauksen määräaika](#crossborderclaimdeadline)
  - [Appeal Chain and Deadlines / Muutoksenhakuketju](#appealchain)
  - [Premium Non-Payment Consequences / Vakuutusmaksun laiminlyönnin seuraukset](#premiumnonpaymentconsequences)
  - [Penalty for Failure to Insure / Vakuutusmaksua vastaava maksu ja laiminlyöntimaksu](#penaltyforuninsuredvehicle)
  - [Distribution System (Jakojärjestelmä) / Jakojärjestelmä](#distributionsystem)
  - [Document Retention Requirements / Asiakirjojen säilyttäminen](#documentretention)
- **🔍 Scope** (5)
  - [Territorial Scope of Coverage / Vakuutuksen voimassaoloalue](#territorialscope)
  - [Vehicles Exempt from Insurance Obligation / Vakuuttamisvelvollisuudesta vapautetut ajoneuvot](#exemptvehicles)
  - [Green Card System / Vihreä kortti -järjestelmä](#greencardsystem)
  - [ETA State (European Economic Area State) / ETA-valtio](#etastate)
  - [Third Country / Kolmas maa](#thirdcountry)
- **🚫 Exclusion** (1)
  - [Excluded Property Damage / Korvaamatta jäävät esinevahingot](#excludedpropertydamage)

---

## 👤 Person

### 👤 Policyholder (`policyholder`)
**Finnish:** Vakuutuksenottaja  **Legal basis:** §6(1)  **Category:** person

The person or entity that has entered into the insurance contract with the insurer. The owner and keeper of a vehicle are both obliged to take out insurance; if more than one person is obliged, they are jointly and severally liable.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `hasInsuranceObligation` | boolean |  |  | §6(1) |
| `vehicleOwnerOrKeeper` | enum | owner, keeper, both |  | §6(1) |
| `businessId` | string |  | Yritys- ja yhteisötunnus; if present, vehicle-specific identification may be waived | §10(2) |

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `insurer` | contractsWith | §6 |  |
| `motorVehicle` | obligedToInsure | §6 |  |
| `claimantPerson` | mayAlsoBeInjuredParty | §60 |  |


### 👤 Insured Person (`insuredPerson`)
**Finnish:** Vakuutettu  **Legal basis:** §2(5)  **Category:** person

The person in whose favour the insurance is in force.

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `policyholder` | contractBeneficiary |  |  |
| `insurer` | coveredBy |  |  |


### 👤 Injured Party / Claimant (`claimantPerson`)
**Finnish:** Vahinkoa kärsinyt / Korvaukseen oikeutettu  **Legal basis:** §60(1)  **Category:** person

Person who has suffered personal injury or property damage as a result of a traffic accident and is entitled to compensation directly from the insurer.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `residenceInFinland` | boolean |  | Relevant for cross-border claims via LVK and choice-of-law | §13(4), §45, §70 |
| `ageUnder12` | boolean |  | Under 12 years → contributory negligence provisions (§47-49) cannot be invoked against them | §50 |

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `insurer` | makesClaimAgainst | §60 |  |
| `liikennevakuutuskeskus` | mayMakeClaimAgainst | §44, §45, §46, §71 |  |
| `trafficAccident` | sufferedDamageIn |  |  |


### 👤 Compensation Representative (`compensationRepresentative`)
**Finnish:** Korvausedustaja  **Legal basis:** §69(1)  **Category:** person

Representative named by a foreign insurer in each ETA state to handle claims arising from accidents in the insurer's home state.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `mustResideInNominatedState` | boolean | true |  | §69(2) |

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `insurer` | nominatedBy | §69(1) |  |


### 👤 Compensation Agent (`compensationAgent`)
**Finnish:** Korvausasiamies  **Legal basis:** §69(4)  **Category:** person

Representative appointed in Finland by a foreign ETA insurer operating via freedom-of-services from abroad.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `mustHavePermanentPlaceInFinland` | boolean | true |  | §69(4) |


---

## 🏛️ Organization

### 🏛️ Insurer / Insurance Company (`insurer`)
**Finnish:** Vakuutusyhtiö  **Legal basis:** §2(3), §17(1)  **Category:** organization

Insurance company authorised to carry on motor vehicle liability insurance (damage class 10) in Finland under the Insurance Companies Act or the Act on Foreign Insurance Companies.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `licenceToOperate` | boolean |  |  | §17(1) |
| `obligedToProvideInsurance` | boolean | true |  | §17(2) |
| `mustNameCompensationRepresentative` | boolean | true | Required in every other ETA state when operating cross-border | §69(1) |

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `policyholder` | contractsWith | §6 |  |
| `liikennevakuutuskeskus` | memberOf | §4 |  |
| `liikennevahinkolautakunta` | obligedToConsult | §66 |  |
| `finanssivalvonta` | supervisedBy |  |  |


### 🏛️ Finnish Motor Insurers' Centre (`liikennevakuutuskeskus`)
**Finnish:** Liikennevakuutuskeskus  **Legal basis:** §4  **Category:** organization

Statutory central body of motor vehicle liability insurers. Acts as national bureau, information centre, guarantee fund (last-resort compensation body), and statistical authority. Governed by separate Act 461/2016.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `roleAsGuaranteeFund` | boolean | true |  | §43, §44, §45, §46 |
| `roleAsNationalBureau` | boolean | true |  | §87(1) |
| `roleAsInformationCentre` | boolean | true |  | §86 |
| `roleInPenaltyCollection` | boolean | true |  | §29 |

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `insurer` | coordinatesInsurers |  |  |
| `valtiokonttori` | submitsProposalTo | §29(1) | Submits proposals for uninsured vehicle penalties |
| `finanssivalvonta` | reportsTo |  |  |


### 🏛️ State Treasury (Valtiokonttori) (`valtiokonttori`)
**Finnish:** Valtiokonttori  **Legal basis:** §32(2), §29(2)  **Category:** organization

Acts as insurer for state-owned vehicles not covered by commercial insurance. Also determines penalty payments for uninsured vehicles on LVK's proposal.

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `liikennevakuutuskeskus` | receivesProposalFrom | §29(1) |  |
| `claimantPerson` | compensates | §32(2) |  |


### 🏛️ Traffic Accident Board (`liikennevahinkolautakunta`)
**Finnish:** Liikennevahinkolautakunta  **Legal basis:** §64, §65, §66  **Category:** organization

Expert advisory body providing non-binding opinions on compensation cases. Governed by Act 441/2002. Insurers are obliged to request opinions in certain serious or contentious cases.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `opinionsBinding` | boolean | false |  |  |

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `insurer` | advisesOn | §65(3) |  |
| `claimantPerson` | canBeRequestedByClaimant | §65(1) |  |


### 🏛️ Financial Supervisory Authority (Finanssivalvonta) (`finanssivalvonta`)
**Finnish:** Finanssivalvonta  **Legal basis:** §70(4), §89  **Category:** organization

Finnish financial sector regulator; supervises insurers and can take enforcement action.


---

## 🚗 Vehicle

### 🚗 Motor Vehicle (`motorVehicle`)
**Finnish:** Ajoneuvo (moottoriajoneuvo)  **Legal basis:** §2(1)  **Category:** vehicle

Vehicle designed to travel by mechanical power on land but not on rails; includes a coupled or uncoupled trailer.

**Subclasses:** `trailer`, `agriculturalWorkMachine`, `harvestCombine`, `vehicleExclusivelyForChildTransport`, `electricWheelchairForDisabled`, `exportRegisteredVehicle`, `foreignVehicle`, `uninsuredVehicle`, `unknownVehicle`

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `permanentHomeState` | string |  | State of registration plate, insurance badge, or keeper's permanent residence | §2(9) |
| `registeredInFinland` | boolean |  |  | §5(1) |
| `mustBeRegistered` | boolean |  |  | §8 |
| `maxConstructionSpeed` | integer |  | Relevant for exemptions (≤15 km/h) | §8(1)(1) |
| `removedFromTrafficUse` | boolean |  |  | §2(10), §8(1)(9) |
| `permanentlyRemovedFromTrafficUse` | boolean |  |  | §2(11), §8(1)(10) |
| `ownedByFinnishState` | boolean |  |  | §8(1)(7) |

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `policyholder` | insuredBy | §6 |  |
| `insurer` | coveredUnder | §32(1) |  |


### 🚗 Trailer (`trailer`)
**Finnish:** Perävaunu  **Legal basis:** §2(1), §8(1)(3)  **Category:** vehicle

Coupled or uncoupled trailer forming part of the vehicle concept; exempt from insurance obligation if not required to be registered.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `mustBeRegistered` | boolean |  |  |  |


### 🚗 Agricultural / Motor Work Machine (slow) (`agriculturalWorkMachine`)
**Finnish:** Moottorityökone / Traktori (hidas)  **Legal basis:** §8(1)(1)  **Category:** vehicle

Motor work machine or tractor not required to be registered with max construction speed ≤ 15 km/h; exempt from insurance obligation.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `maxConstructionSpeed` | integer | 15 |  |  |


### 🚗 Combine Harvester / Farm Harvest Machine (`harvestCombine`)
**Finnish:** Leikkuupuimuri / Sadonkorjuukone  **Legal basis:** §8(1)(2)  **Category:** vehicle

Combine harvester or other farm harvest machine not required to be registered; exempt from insurance obligation.


### 🚗 Foreign Vehicle (`foreignVehicle`)
**Finnish:** Ulkomainen ajoneuvo  **Legal basis:** §2(9), §7, §32(4)  **Category:** vehicle

Vehicle whose permanent home state is a state other than Finland.

**Subclasses:** `etaForeignVehicle`, `thirdCountryVehicle`

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `liikennevakuutuskeskus` | LVKPrimarilyLiableFor | §32(4) | LVK is primarily liable for damage caused in Finland by a vehicle with permanent home outside Finland |


### 🚗 ETA Foreign Vehicle (`etaForeignVehicle`)
**Finnish:** Toisessa ETA-valtiossa rekisteröity ajoneuvo  **Legal basis:** §32(4), §43(2)  **Category:** vehicle

Vehicle registered in another ETA state; covered by green card system; LVK liable for accidents in Finland.


### 🚗 Third-Country Vehicle (`thirdCountryVehicle`)
**Finnish:** Kolmannen maan ajoneuvo  **Legal basis:** §7(1)  **Category:** vehicle

Vehicle whose permanent home is a non-ETA state; requires border traffic insurance (rajaliikennevakuutus) when brought temporarily to Finland.


### 🚗 Uninsured Vehicle (`uninsuredVehicle`)
**Finnish:** Vakuuttamaton ajoneuvo  **Legal basis:** §46  **Category:** vehicle

Vehicle that should have been insured but was not at the time of the accident.

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `liikennevakuutuskeskus` | compensatedBy | §46(1) |  |


### 🚗 Unknown / Hit-and-Run Vehicle (`unknownVehicle`)
**Finnish:** Tuntemattomaksi jäänyt ajoneuvo  **Legal basis:** §44  **Category:** vehicle

Vehicle that caused a traffic accident but could not be identified.

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `liikennevakuutuskeskus` | compensatedBy | §44 |  |


---

## ⚡ Event

### ⚡ Traffic Accident / Traffic Damage Event (`trafficAccident`)
**Finnish:** Liikennevahinko / Vahinkotapahtuma  **Legal basis:** §2(6), §31  **Category:** event

Personal injury or property damage caused by the traffic use of a motor vehicle. Compensation is payable regardless of whether any person is personally liable in damages (strict liability principle).

**Subclasses:** `personalInjuryEvent`, `propertyDamageEvent`, `majorAccident`

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `vehicleInTrafficUse` | boolean | true |  | §1 |
| `excludedUse_offRoadNonTransport` | boolean |  | Vehicle used off road essentially for purposes other than transport | §1(1) |
| `excludedUse_storedRepaired` | boolean |  | Vehicle stored, repaired, serviced or washed off road | §1(2) |
| `excludedUse_competitionOnClosedArea` | boolean |  | Vehicle used for competition/testing on traffic-isolated area | §1(3) |

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `motorVehicle` | causedBy |  |  |
| `claimantPerson` | injures |  |  |
| `insurer` | triggersLiabilityOf |  |  |


### ⚡ Personal Injury Event (`personalInjuryEvent`)
**Finnish:** Henkilövahinkotapahtuma  **Legal basis:** §34  **Category:** event

Traffic accident resulting in bodily injury or death to a natural person.


### ⚡ Property Damage Event (`propertyDamageEvent`)
**Finnish:** Esinevahinkotapahtuma  **Legal basis:** §37  **Category:** event

Traffic accident resulting in damage to or destruction of property.


### ⚡ Major Accident (Suurvahinko) (`majorAccident`)
**Finnish:** Suurvahinko  **Legal basis:** §75(3)  **Category:** event

A temporally and spatially limited event (or series of connected events) where total motor liability compensation paid exceeds 75 000 000 EUR threshold. Costs above threshold are pooled via the distribution system (jakojärjestelmä).

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `poolingThreshold` | MonetaryAmount | 75000000 |  | §75(3) |


---

## 💶 Compensation

### 💶 Personal Injury Compensation (`personalInjuryCompensation`)
**Finnish:** Henkilövahingon korvaus  **Legal basis:** §34(1)  **Category:** compensation

Compensation for personal injury determined in accordance with Chapter 5 of the Tort Liability Act (412/1974), including pain & suffering (if not minor), loss of earnings, loss of maintenance, permanent disability, and death benefits.

**Subclasses:** `painAndSufferingCompensation`, `lossOfEarningsCompensation`, `lossOfMaintenanceCompensation`, `permanentDisabilityCompensation`, `deathBenefitsCompensation`, `rehabilitationCompensation`

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `basisLaw` | string | Vahingonkorvauslaki 412/1974, §§5:2, 5:2a-2d, 5:3, 5:4, 5:4a, 5:4b, 5:7, 5:8, 7:3 |  | §34(1) |
| `painAndSufferingExcluded` | boolean |  | No entitlement to pain & suffering compensation if injury is minor | §34(1) |
| `lumpSumInsteadOfContinuing` | string | Only for compelling reason; STM decree sets calculation basis |  | §34(3), §34(4) |
| `indexAdjustment` | string | Annual adjustment by työeläkeindeksi (TEL earnings index, §98 TEL Act 395/2006) |  | §35(1) |
| `earningsIndexForHistoricalWages` | string | Annual adjustment to accident year level by palkkakerroin (wage coefficient, §96 TEL Act) |  | §35(2) |

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `personalInjuryEvent` | arisesFrom |  |  |
| `insurer` | paidBy |  |  |


### 💶 Pain and Suffering / Temporary Disability Compensation (`painAndSufferingCompensation`)
**Finnish:** Kipu ja särky sekä muu tilapäinen haitta  **Legal basis:** §34(1)  **Category:** compensation

Compensation for pain, suffering and other temporary disability. Not payable if injury is minor.


### 💶 Loss of Earnings Compensation (`lossOfEarningsCompensation`)
**Finnish:** Ansionmenetyskorvaus  **Legal basis:** §34(3), VahL §5:2  **Category:** compensation

Continuous compensation for loss of earnings; lump sum only for compelling reason.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `indexAdjusted` | boolean | true |  |  |
| `indexMechanism` | string | Työeläkeindeksi annually |  | §35(1) |


### 💶 Permanent Disability Compensation (`permanentDisabilityCompensation`)
**Finnish:** Pysyvän haitan korvaus  **Legal basis:** §66(1)(3), VahL §5:2  **Category:** compensation

Compensation for permanent functional impairment; LVL board opinion mandatory if serious impairment.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `boardOpinionMandatory` | boolean | true | Mandatory if vamma on vaikea (serious injury) | §66(1)(3) |


### 💶 Loss of Maintenance Compensation (Death) (`lossOfMaintenanceCompensation`)
**Finnish:** Elatuksen menetyksen korvaus  **Legal basis:** §34(1), VahL §5:4  **Category:** compensation

Continuous compensation for dependants who lose maintenance following victim's death.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `indexAdjusted` | boolean | true |  |  |
| `indexMechanism` | string | Työeläkeindeksi annually |  | §35(1) |


### 💶 Death Benefits (`deathBenefitsCompensation`)
**Finnish:** Kuoleman johdosta suoritettavat korvaukset  **Legal basis:** §34(1), VahL §§5:4a, 5:4b  **Category:** compensation

Funeral costs and compensation for survivors' grief (under VahL §5:4a-4b).


### 💶 Rehabilitation Compensation (`rehabilitationCompensation`)
**Finnish:** Kuntoutuskorvaus  **Legal basis:** §34(2), §47(2), §48(3)  **Category:** compensation

Compensation for rehabilitation costs under the separate Act on Rehabilitation Compensable under Motor Liability Insurance (626/1991). Not reducible under §47-48 contributory negligence rules even if other compensation is.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `notReducibleForContributoryNegligence` | boolean | true |  | §47(2), §48(3) |
| `governingAct` | string | Laki liikennevakuutuslain perusteella korvattavasta kuntoutuksesta 626/1991 |  |  |


### 💶 Property Damage Compensation (`propertyDamageCompensation`)
**Finnish:** Esinevahingon korvaus  **Legal basis:** §37  **Category:** compensation

Compensation for property damage determined per Tort Liability Act §5:5. For a vehicle: repair cost or equivalent; fair market value before accident if totalled. Vehicle value depreciation is not compensated.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `maxPerLiableInsurance` | MonetaryAmount | 5000000 |  | §38(1) |
| `vehicleDepreciationExcluded` | boolean | true |  | §37(2) |
| `titleTransfersOnTotalLoss` | boolean | true | On total loss, vehicle title transfers to insurer | §37(2) |

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `propertyDamageEvent` | arisesFrom |  |  |


### 💶 Medical / Healthcare Costs (`medicalCareCosts`)
**Finnish:** Sairaanhoidon kustannukset  **Legal basis:** §53, §54, §55, §58, §59  **Category:** compensation

Necessary medical treatment costs for injury. Public healthcare: patient co-payment (asiakasmaksu) to claimant + full cost (täyskustannusmaksu) to municipality/joint authority. Private: generally requires insurer's prior payment commitment (maksusitoumus).

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `publicHealthcarePatientCopayment` | string | asiakasmaksu per asiakasmaksulaki 734/1992 |  | §54(1) |
| `fullCostToMunicipality` | string | täyskustannusmaksu (full cost minus patient copayment) |  | §55(1) |
| `privateWithoutCommitment` | string | Emergency and first visit covered without commitment; other private requires maksusitoumus |  | §58, §59 |


### 💶 Rescuer's Compensation (`rescuerCompensation`)
**Finnish:** Auttajalle aiheutuneen vahingon korvaus  **Legal basis:** §39  **Category:** compensation

Direct personal injury and property damage incurred by a person who provides immediate first aid or transport to a traffic accident victim; excludes professional rescue services.


---

## 📋 Rule

### 📋 Motor Vehicle Liability Insurance (Compulsory) (`motorLiabilityInsurance`)
**Finnish:** Liikennevakuutus  **Legal basis:** §1, §5, §13(1)  **Category:** rule

Mandatory no-fault liability insurance covering personal injury and property damage arising from traffic use of a motor vehicle. Valid in all ETA states on a single premium.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `mandatoryInsurance` | boolean | true |  | §5(1) |
| `coverageTerritory` | string | all ETA states |  | §13(1) |
| `maxPropertyDamagePerLiableInsurance` | MonetaryAmount | 5000000 |  | §38(1) |
| `policyPeriod` | string |  | First period max 13 months; subsequent periods 12 months | §12(2) |
| `continuityDespiteNonPayment` | boolean | true | Insurer's liability does not cease even if premium is unpaid | §25(1) |
| `mandatoryProvisions` | boolean | true | Contract terms deviating to detriment of policyholder/insured/claimant are void | §3 |

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `motorVehicle` | covers |  |  |
| `trafficAccident` | triggeredBy |  |  |


### 📋 Border Traffic Insurance (`borderTrafficInsurance`)
**Finnish:** Rajaliikennevakuutus  **Legal basis:** §7(1)  **Category:** rule

Temporary insurance required for third-country vehicles brought temporarily to Finland.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `temporaryInsurance` | boolean | true |  |  |
| `coverageForDriverPersonalInjury` | string | Only if accident occurred in Finland, Sweden or Norway |  | §7(3) |


### 📋 Transit Traffic Insurance (`transitTrafficInsurance`)
**Finnish:** Siirtoliikennevakuutus  **Legal basis:** §2(18), §12(2)  **Category:** rule

Temporary insurance granted for transit permit vehicles under Vehicle Act §66f.


### 📋 Strict Liability (No-Fault) Rule (`strictLiabilityRule`)
**Finnish:** Ankara (tuottamuksesta riippumaton) vastuu  **Legal basis:** §31  **Category:** rule

Traffic damage is compensated regardless of whether any person is personally liable in tort. The insurer bears absolute liability for damage arising from traffic use.


### 📋 Fault-Based Allocation Between Vehicles (`faultBasedAllocationRule`)
**Finnish:** Tuottamusperusteinen korvausvastuun jako (useamman ajoneuvon vahingot)  **Legal basis:** §33  **Category:** rule

When two or more vehicles are involved, liability between them is allocated based on fault (owner, keeper, driver, passenger), traffic rule violations, poor condition, or defective loading. Shared fault leads to proportional split. Personal injury to an occupant is always paid first from the vehicle the victim was in, then inter-insurer allocation follows.

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `insurer` | appliedAmong | §51 |  |


### 📋 Contributory Negligence — Personal Injury (`contributoryNegligenceRule`)
**Finnish:** Myötävaikutus — henkilövahinko  **Legal basis:** §47(1)  **Category:** rule

If the victim intentionally caused their own personal injury, compensation is paid only to the extent other circumstances contributed. Gross negligence may reduce or deny compensation proportionally. Does NOT apply to rehabilitation compensation. Does NOT apply if victim is under 12 or legally non-culpable (§50).

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `intentSelfInflicted` | string | Compensation only for contribution of other circumstances |  | §47(1) |
| `grossNegligence` | string | Reduction or denial as equitable in circumstances |  | §47(1) |
| `propertyDamage` | string | Reduction or denial proportional to victim's fault degree |  | §47(3) |
| `excludedPersons` | string | Under 12 years; persons of unsound mind; persons acting under necessity |  | §50 |


### 📋 Alcohol / Intoxicant Effect on Compensation (`alcoholRule`)
**Finnish:** Alkoholin tai huumaavan aineen vaikutus korvaukseen  **Legal basis:** §48  **Category:** rule

Driver with BAC ≥ 1.2 ‰ (or ≥ 0.53 mg/l exhaled air) or seriously impaired by other substance: personal injury compensation only for contribution of other circumstances (§48(1) — complete or near-complete denial). Driver with BAC ≥ 0.5 ‰ (or ≥ 0.22 mg/l) or impaired: reduction proportional to their contribution (§48(2) — partial reduction). Rehabilitation compensation not reducible.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `severeThreshold_BAC_blood` | decimal | 1.2 |  | §48(1) |
| `severeThreshold_BAC_exhaled` | decimal | 0.53 |  | §48(1) |
| `moderateThreshold_BAC_blood` | decimal | 0.5 |  | §48(2) |
| `moderateThreshold_BAC_exhaled` | decimal | 0.22 |  | §48(2) |


### 📋 Unauthorised Vehicle Use (Theft etc.) (`unauthorisedUseRule`)
**Finnish:** Luvattomasti käyttöön otettu ajoneuvo  **Legal basis:** §49  **Category:** rule

If the victim knowingly was in an unlawfully used vehicle (criminal act per RL 28:9a–9c), compensation is paid only for special reason.


### 📋 Subrogation / Right of Recourse (`subrogationRule`)
**Finnish:** Takautumisoikeus  **Legal basis:** §73  **Category:** rule

The insurer (or LVK) steps into the victim's shoes to recover from third parties. Against private individuals, employees, or vehicle parties: recourse only if the event was caused intentionally, by gross negligence, or while driving under severe alcohol/substance influence (§48(1)).

#### Relationships

| Target | Type | Legal Basis | Note |
|--------|------|-------------|------|
| `insurer` | exercisedBy | §73 |  |
| `liikennevakuutuskeskus` | exercisedBy | §74 |  |


### 📋 Claim Filing Deadline (Limitation) (`claimFilingDeadline`)
**Finnish:** Korvausvaatimuksen esittämisajankohta / Vanhentuminen  **Legal basis:** §61(1)  **Category:** rule

Claim must be filed within 3 years of when the claimant became aware of the accident and the resulting damage. Absolute bar: 10 years from when the damage occurred. Late claims may be accepted for compelling reason.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `standardDeadline` | duration | P3Y | 3 years from awareness of accident and damage | §61(1) |
| `absoluteDeadline` | duration | P10Y | 10 years from occurrence of damage consequence | §61(1) |
| `compellingReasonException` | boolean | true |  | §61(3) |


### 📋 Decision Deadline (`decisionDeadline`)
**Finnish:** Korvauksen suorittamisen määräaika  **Legal basis:** §62  **Category:** rule

Insurer must begin investigation within 7 working days of claim receipt. Must pay or notify non-payment within 1 month of receiving all required documents. Undisputed portion must be paid within 1 month even if total is disputed. If liability unclear or quantum unresolved, insurer must give reasoned response within 3 months of claim presentation.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `investigationStart` | duration | P7D |  | §62(1) |
| `paymentOrDenialDeadline` | duration | P1M | 1 month from receipt of sufficient documents | §62(2) |
| `reasonedResponseDeadline` | duration | P3M | 3 months from claim if liability or quantum unclear | §62(4) |


### 📋 Cross-Border Claim Deadline (Compensation Representative) (`crossBorderClaimDeadline`)
**Finnish:** Korvausedustajan vastauksen määräaika  **Legal basis:** §70(2)  **Category:** rule

Compensation representative must pay or make reasoned offer within 3 months of receiving the claim in cross-border ETA cases.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `deadline` | duration | P3M |  | §70(2) |


### 📋 Appeal Chain and Deadlines (`appealChain`)
**Finnish:** Muutoksenhakuketju  **Legal basis:** §65(1), §79  **Category:** rule

1. Claimant may request LVL board opinion within 1 year of insurer decision. 2. Action in court against insurer: within 3 years of written notification of
   decision and deadline. Court proceedings suspend the limitation period.
3. Municipality/joint authority may appeal täyskustannusmaksu decision per
   hallintolainkäyttölaki.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `LVLBoardOpinionDeadline` | duration | P1Y | 1 year from insurer decision | §65(1) |
| `courtActionDeadline` | duration | P3Y | 3 years from written notice of insurer decision and deadline | §79(1) |


### 📋 Premium Non-Payment Consequences (`premiumNonPaymentConsequences`)
**Finnish:** Vakuutusmaksun laiminlyönnin seuraukset  **Legal basis:** §24, §25, §26  **Category:** rule

Insurer's liability continues even if premium unpaid (§25(1)). Overdue premium accrues statutory late interest. Premium receivable is directly enforceable (ulosottokelpoinen). Limitation: 5 years from end of the calendar year following assessment/billing.


### 📋 Penalty for Failure to Insure (`penaltyForUninsuredVehicle`)
**Finnish:** Vakuutusmaksua vastaava maksu ja laiminlyöntimaksu  **Legal basis:** §27, §28, §29  **Category:** rule

Owner/keeper who fails to insure must pay: (1) an equivalent premium for the uninsured period (up to current + 5 preceding calendar years), and (2) a penalty (laiminlyöntimaksu) of up to 3× that amount, considering duration, intent, recurrence and road use. LVK proposes; Valtiokonttori decides.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `equivalentPremiumMaxYears` | integer | 6 | Current year + 5 preceding calendar years | §27(1) |
| `penaltyMultiplierMax` | integer | 3 |  | §28(1) |


### 📋 Distribution System (Jakojärjestelmä) (`distributionSystem`)
**Finnish:** Jakojärjestelmä  **Legal basis:** §75  **Category:** rule

All motor liability insurers participate annually in pooling long-tail costs and certain extraordinary costs (index adjustments, healthcare after 9 years, rehabilitation after 9 years, major accident costs above 75 M€ threshold). Each insurer's share is proportional to their distribution system premium income.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `majorAccidentPoolingThreshold` | MonetaryAmount | 75000000 |  | §75(3) |
| `longTailThreshold` | string | Healthcare and rehabilitation costs paid > 9 years after accident |  | §75(2)(3), §75(2)(4) |


### 📋 Document Retention Requirements (`documentRetention`)
**Finnish:** Asiakirjojen säilyttäminen  **Legal basis:** §85  **Category:** rule

Insurer must retain: insurance validity and personal injury documents ≥ 100 years; appeal documents ≥ 50 years; other implementation documents ≥ 10 years.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `insuranceAndPersonalInjuryDocs` | duration | P100Y |  | §85(1)(1) |
| `appealDocs` | duration | P50Y |  | §85(1)(2) |
| `otherDocs` | duration | P10Y |  | §85(1)(3) |


---

## 🔍 Scope

### 🔍 Territorial Scope of Coverage (`territorialScope`)
**Finnish:** Vakuutuksen voimassaoloalue  **Legal basis:** §13  **Category:** scope

Finnish motor liability insurance valid in all ETA states on single premium. Also covers transit damage through non-green-card states on direct journey between ETA states (for ETA nationals). Insured may choose Finnish law for personal injury occurring abroad if result under Finnish law is better.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `etaStates` | boolean | true | All ETA states on single premium | §13(1) |
| `transitCoverage` | string | Non-green-card transit states on direct ETA-to-ETA journey (ETA nationals) |  | §13(2) |
| `finnishLawChoiceForAbroad` | string | Finnish resident may choose Finnish law for personal injury abroad if more favourable |  | §13(4) |


### 🔍 Vehicles Exempt from Insurance Obligation (`exemptVehicles`)
**Finnish:** Vakuuttamisvelvollisuudesta vapautetut ajoneuvot  **Legal basis:** §8(1)  **Category:** scope

Vehicles not required to be insured: slow work machines (≤15 km/h, unregistered), combine harvesters (unregistered), unregistered trailers, vehicles exclusively for children (unregistered), electric wheelchairs (unregistered), unregistered off-road-only vehicles, state-owned vehicles, removed-from-traffic vehicles.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `slowWorkMachine` | boolean |  |  | §8(1)(1) |
| `combineHarvester` | boolean |  |  | §8(1)(2) |
| `unregisteredTrailer` | boolean |  |  | §8(1)(3) |
| `childOnlyVehicle` | boolean |  |  | §8(1)(4) |
| `disabledElectricWheelchair` | boolean |  |  | §8(1)(5) |
| `unregisteredOffRoad` | boolean |  |  | §8(1)(6) |
| `stateOwnedVehicle` | boolean |  |  | §8(1)(7) |
| `removedFromTrafficUse` | boolean |  |  | §8(1)(9) |
| `permanentlyRemoved` | boolean |  |  | §8(1)(10) |


### 🔍 Green Card System (`greenCardSystem`)
**Finnish:** Vihreä kortti -järjestelmä  **Legal basis:** §2(15), §2(16), §7(2)  **Category:** scope

International insurance certificate system managed by national bureaux. A vehicle with valid green card is exempt from Finnish border traffic insurance.


### 🔍 ETA State (European Economic Area State) (`etaState`)
**Finnish:** ETA-valtio  **Legal basis:** §2(12)  **Category:** scope

Member state of the European Economic Area.


### 🔍 Third Country (`thirdCountry`)
**Finnish:** Kolmas maa  **Legal basis:** §2(13)  **Category:** scope

Any state that is not an ETA state.


---

## 🚫 Exclusion

### 🚫 Excluded Property Damage (`excludedPropertyDamage`)
**Finnish:** Korvaamatta jäävät esinevahingot  **Legal basis:** §40, §42  **Category:** exclusion

A vehicle's own insurance does not cover: (1) damage to the insured vehicle itself or another vehicle permanently attached to it or property in those vehicles; (2) damage to property owned/controlled by the owner, keeper or driver (except other vehicle they own/control); (3) damage to property under professional work performance during stationary operation (§42). Exception: personal effects of passengers other than owner/keeper ARE covered.

#### Attributes

| Key | Type | Value / Values | Description | Legal Basis |
|-----|------|----------------|-------------|-------------|
| `ownVehicleDamage` | boolean | true |  | §40(1) |
| `ownerKeeperDriverOwnProperty` | boolean | true |  | §40(2) |
| `passengerPersonalEffectsException` | string | Personal effects of other passengers (not owner/keeper) ARE covered |  | §40(2) |
| `workPerformanceDamage` | boolean | true |  | §42 |
| `unattendedAnimalExceptReindeer` | boolean | true | Damage to unattended animal other than reindeer excluded unless caused by fault | §37(3) |


---
