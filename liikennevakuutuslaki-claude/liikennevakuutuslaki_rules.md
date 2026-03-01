# Finnish Motor Vehicle Liability Insurance — DMN Business Rules

**Effective date:** 2017-01-01  
**Version:** 1.0  
**Author:** Lumen ⚖️ — Finnish Legal Engineer  

## Table of Contents

- [D1: Insurance Obligation](#d1)
- [D2: Personal Scope — Who May Claim Compensation](#d2)
- [D3: Territorial Scope — Where Coverage Applies](#d3)
- [D4: Compensable Event Classification](#d4)
- [D5: Liability Determination — Insurer vs Insurer](#d5)
- [D6: Personal Injury Compensation — Eligibility and Amount](#d6)
- [D7: Property Damage Compensation — Amount and Limits](#d7)
- [D8: Claim Filing Deadline](#d8)
- [D9: Insurer Decision Deadline](#d9)
- [D10: Appeal Chain and Deadlines](#d10)
- [D11: LVK Liability — Uninsured, Unknown and Exempt Vehicle Claims](#d11)
- [D12: Foreign Vehicle — Applicable Procedure](#d12)
- [D13: Reduction or Denial of Compensation](#d13)
- [D14: Subrogation / Right of Recourse](#d14)

---

## D1: Insurance Obligation
**Finnish:** Vakuuttamisvelvollisuus
**Legal basis:** §5, §6, §7, §8

Determines whether a vehicle must be insured under Finnish law, whether a border traffic insurance is needed, and who bears the obligation.


### Inputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `permanentHomeState` | Vehicle's permanent home state | enum | Finland, other_ETA, third_country |
| `vehicleType` | Vehicle type / category | enum | standard_motor_vehicle, trailer_registered, trailer_unregistered, slow_work_machine_max15kmh_unregistered, combine_harvester_unregistered, child_only_vehicle_unregistered, disabled_wheelchair_unregistered, unregistered_offroad_only, state_owned, export_registered |
| `removedFromTrafficUse` | Vehicle removed from traffic use (liikennekäytöstä poistettu) | boolean |  |
| `permanentlyRemoved` | Vehicle permanently removed from traffic use (lopullinen poisto) | boolean |  |
| `usedInTraffic` | Vehicle actually used in traffic despite removal status | boolean |  |
| `greenCardValid` | Vehicle has valid green card | boolean |  |
| `LVKCommitmentToRespond` | LVK has committed to respond for this vehicle | boolean |  |

### Outputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `insuranceObligation` | Insurance obligation | enum | mandatory, exempt_may_insure_voluntarily, border_traffic_required, no_obligation |
| `obligedParties` | Obliged parties | string |  |
| `obligationStartDate` | When obligation begins | string |  |

### Decision Table

| Rule | Description | Conditions | Result | Legal Basis | Note |
|------|-------------|------------|--------|-------------|------|
| D1-R1 | Standard Finnish vehicle — mandatory insurance | **permanentHomeState** = `Finland`<br>**vehicleType** = `standard_motor_vehicle`<br>**removedFromTrafficUse** = `false`<br>**permanentlyRemoved** = `false` | **insuranceObligation** → `mandatory`<br>**obligedParties** → `owner and keeper, jointly and severally`<br>**obligationStartDate** → `From date of ownership/keepership transfer` | §5(1), §6(1) |  |
| D1-R2 | Slow work machine (≤15 km/h, unregistered) — exempt | **vehicleType** = `slow_work_machine_max15kmh_unregistered` | **insuranceObligation** → `exempt_may_insure_voluntarily`<br>**obligedParties** → `none (voluntary)`<br>**obligationStartDate** → `N/A` | §8(1)(1) |  |
| D1-R3 | Combine harvester / farm harvest machine (unregistered) — exempt | **vehicleType** = `combine_harvester_unregistered` | **insuranceObligation** → `exempt_may_insure_voluntarily`<br>**obligedParties** → `none (voluntary)`<br>**obligationStartDate** → `N/A` | §8(1)(2) |  |
| D1-R4 | Unregistered trailer — exempt | **vehicleType** = `trailer_unregistered` | **insuranceObligation** → `exempt_may_insure_voluntarily`<br>**obligedParties** → `none (voluntary)`<br>**obligationStartDate** → `N/A` | §8(1)(3) |  |
| D1-R5 | Child-only unregistered vehicle — exempt | **vehicleType** = `child_only_vehicle_unregistered` | **insuranceObligation** → `exempt_may_insure_voluntarily`<br>**obligedParties** → `none (voluntary)`<br>**obligationStartDate** → `N/A` | §8(1)(4) |  |
| D1-R6 | Disabled electric wheelchair / similar light vehicle (unregistered) — exempt | **vehicleType** = `disabled_wheelchair_unregistered` | **insuranceObligation** → `exempt_may_insure_voluntarily`<br>**obligedParties** → `none (voluntary)`<br>**obligationStartDate** → `N/A` | §8(1)(5) |  |
| D1-R7 | State-owned vehicle — exempt (Valtiokonttori acts as insurer) | **vehicleType** = `state_owned` | **insuranceObligation** → `no_obligation`<br>**obligedParties** → `N/A — Valtiokonttori bears liability`<br>**obligationStartDate** → `N/A` | §8(1)(7), §32(2) |  |
| D1-R8 | Vehicle removed from traffic use AND not used in traffic — exempt | **removedFromTrafficUse** = `true`<br>**usedInTraffic** = `false` | **insuranceObligation** → `exempt_may_insure_voluntarily`<br>**obligedParties** → `none (voluntary)`<br>**obligationStartDate** → `N/A` | §8(1)(9) |  |
| D1-R9 | Vehicle permanently removed — no obligation | **permanentlyRemoved** = `true` | **insuranceObligation** → `no_obligation`<br>**obligedParties** → `none`<br>**obligationStartDate** → `N/A` | §8(1)(10) |  |
| D1-R10 | Third-country vehicle brought temporarily to Finland — border traffic insurance required (unless green card or LVK commitment) | **permanentHomeState** = `third_country`<br>**greenCardValid** = `false`<br>**LVKCommitmentToRespond** = `false` | **insuranceObligation** → `border_traffic_required`<br>**obligedParties** → `person bringing vehicle to Finland`<br>**obligationStartDate** → `Before entry into Finland` | §7(1) |  |
| D1-R11 | Third-country vehicle with valid green card — no border traffic insurance needed | **permanentHomeState** = `third_country`<br>**greenCardValid** = `true` | **insuranceObligation** → `no_obligation`<br>**obligedParties** → `N/A`<br>**obligationStartDate** → `N/A` | §7(2) |  |
| D1-R12 | Other ETA vehicle — insured per home state law; LVK bears Finnish liability | **permanentHomeState** = `other_ETA` | **insuranceObligation** → `no_obligation`<br>**obligedParties** → `home state rules apply`<br>**obligationStartDate** → `N/A` | §43(2), §32(4) | LVK is primarily liable for accidents in Finland caused by these vehicles |


---

## D2: Personal Scope — Who May Claim Compensation
**Finnish:** Henkilöllinen soveltamisala — korvaukseen oikeutetut
**Legal basis:** §33, §34, §37, §40, §46, §49, §50

Determines whether a specific person is entitled to claim compensation from the insurance of a specific vehicle.


### Inputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `personRole` | Role of the person in relation to the vehicle | enum | driver_of_vehicle, passenger_of_vehicle, owner_of_vehicle, keeper_of_vehicle, third_party_pedestrian_cyclist |
| `damageType` | Type of damage suffered | enum | personal_injury, property_damage |
| `propertyType` | Property damaged (if property damage) | enum | insured_vehicle_itself, coupled_other_vehicle, property_in_insured_vehicle, personal_effects_passenger, other_vehicle_owned_by_driver, other_third_party_property |
| `knewVehicleUninsured` | Person knew vehicle was uninsured (§46 case) | boolean |  |
| `knewUnauthorisedUse` | Person knew vehicle was taken without authorisation | boolean |  |
| `ageUnder12` | Person is under 12 years of age | boolean |  |
| `legallyNonCulpable` | Person was legally non-culpable at time of accident | boolean |  |

### Outputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `entitled` | Entitled to claim | boolean |  |
| `fromWhichInsurance` | Which insurance to claim against | string |  |
| `restrictions` | Restrictions / notes | string |  |

### Decision Table

| Rule | Description | Conditions | Result | Legal Basis | Note |
|------|-------------|------------|--------|-------------|------|
| D2-R1 | Personal injury to any person (driver, passenger, third party) — generally covered | **damageType** = `personal_injury`<br>**knewVehicleUninsured** = `false`<br>**knewUnauthorisedUse** = `false` | **entitled** → `true`<br>**fromWhichInsurance** → `Vehicle's insurer (or LVK where applicable)`<br>**restrictions** → `Subject to §47/48 reductions if contributory negligence or alcohol` | §31, §34 |  |
| D2-R2 | Occupant/driver knew vehicle was uninsured — generally not entitled from LVK | **knewVehicleUninsured** = `true`<br>**personRole** = `{'in': ['driver_of_vehicle', 'passenger_of_vehicle', 'owner_of_vehicle', 'keeper_of_vehicle']}` | **entitled** → `false`<br>**fromWhichInsurance** → `N/A`<br>**restrictions** → `LVK can exclude per §46(2) if it can prove knowledge` | §46(2) |  |
| D2-R3 | Person in unlawfully used vehicle and knew of it — compensation only for special reason | **knewUnauthorisedUse** = `true` | **entitled** → `false`<br>**fromWhichInsurance** → `N/A`<br>**restrictions** → `Only compensated for special reason (erityinen syy)` | §49 |  |
| D2-R4 | Under 12 / legally non-culpable — §47-49 contributory negligence rules cannot be invoked | **ageUnder12** = `true` | **entitled** → `true`<br>**fromWhichInsurance** → `Full coverage regardless of own conduct`<br>**restrictions** → `§47, §48, §49 reductions cannot be applied` | §50 |  |
| D2-R5 | Property damage — own vehicle damage NOT covered by own insurance | **damageType** = `property_damage`<br>**propertyType** = `insured_vehicle_itself` | **entitled** → `false`<br>**fromWhichInsurance** → `N/A`<br>**restrictions** → `Own vehicle damage excluded from own motor liability insurance` | §40(1) |  |
| D2-R6 | Property damage — personal effects of passenger (not owner/keeper) — covered | **damageType** = `property_damage`<br>**propertyType** = `personal_effects_passenger`<br>**personRole** = `passenger_of_vehicle` | **entitled** → `true`<br>**fromWhichInsurance** → `Vehicle's insurance`<br>**restrictions** → `Passenger must not be owner or keeper of the vehicle` | §40(2) |  |
| D2-R7 | Property damage — owner/keeper/driver own property — NOT covered (except another vehicle they own) | **damageType** = `property_damage`<br>**propertyType** = `{'in': ['property_in_insured_vehicle', 'other_third_party_property']}`<br>**personRole** = `{'in': ['driver_of_vehicle', 'owner_of_vehicle', 'keeper_of_vehicle']}` | **entitled** → `false`<br>**fromWhichInsurance** → `N/A`<br>**restrictions** → `Owner/keeper/driver own property excluded; exception for other vehicle they own` | §40(2) |  |


---

## D3: Territorial Scope — Where Coverage Applies
**Finnish:** Alueellinen soveltamisala
**Legal basis:** §13
### Inputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `accidentCountry` | Country where accident occurred | enum | Finland, other_ETA, green_card_state_non_ETA, non_green_card_transit, third_country |
| `vehicleInsuredInFinland` | Vehicle insured under Finnish law | boolean |  |
| `claimantResidenceFinland` | Claimant has residence in Finland | boolean |  |
| `journeyType` | Nature of journey (for transit states) | enum | direct_ETA_to_ETA, other |
| `claimantEtaNational` | Claimant is ETA national | boolean |  |

### Outputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `covered` | Covered by Finnish insurance | boolean |  |
| `applicableLaw` | Applicable compensation law | string |  |
| `claimantChoice` | Claimant may choose Finnish law | boolean |  |

### Decision Table

| Rule | Description | Conditions | Result | Legal Basis | Note |
|------|-------------|------------|--------|-------------|------|
| D3-R1 | Accident in Finland — always covered, Finnish law applies | **accidentCountry** = `Finland`<br>**vehicleInsuredInFinland** = `true` | **covered** → `true`<br>**applicableLaw** → `Finnish law (liikennevakuutuslaki)`<br>**claimantChoice** → `false` | §13(1) |  |
| D3-R2 | Accident in other ETA state — covered, law of accident state (or Finnish if better) | **accidentCountry** = `other_ETA`<br>**vehicleInsuredInFinland** = `true` | **covered** → `true`<br>**applicableLaw** → `Accident state law OR Finnish law if Finnish law is better`<br>**claimantChoice** → `true` | §13(1), §13(3), §13(4) | Finnish resident may choose Finnish law per §13(4) if damage would otherwise be governed by non-Finnish ETA law |
| D3-R3 | Transit through non-green-card state on direct ETA-to-ETA journey — covered for ETA nationals | **accidentCountry** = `non_green_card_transit`<br>**vehicleInsuredInFinland** = `true`<br>**journeyType** = `direct_ETA_to_ETA`<br>**claimantEtaNational** = `true` | **covered** → `true`<br>**applicableLaw** → `Finnish law`<br>**claimantChoice** → `false` | §13(2) |  |
| D3-R4 | Accident in non-ETA, non-green-card third country — not covered | **accidentCountry** = `third_country`<br>**vehicleInsuredInFinland** = `true` | **covered** → `false`<br>**applicableLaw** → `N/A`<br>**claimantChoice** → `false` | §13 |  |


---

## D4: Compensable Event Classification
**Finnish:** Korvattavan tapahtuman luokittelu
**Legal basis:** §1, §2(6), §31, §37, §40, §42
### Inputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `vehicleInTrafficUse` | Vehicle was in traffic use at time of accident | boolean |  |
| `locationContext` | Location context of vehicle use | enum | on_road_normal_traffic, off_road_non_transport_purpose, stored_repaired_serviced_washed, closed_area_competition_testing, isolated_area_other |
| `damageToOwnVehicle` | Damage is to the insured vehicle itself | boolean |  |
| `vehicleStationary_workPerformance` | Damage occurred while vehicle stationary during work performance | boolean |  |
| `damageToWorkObject` | Damage is to the object of work or other vehicle involved in that work | boolean |  |

### Outputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `compensable` | Event is compensable as traffic damage | boolean |  |
| `damageCategory` | Damage category | enum | personal_injury, property_damage, excluded |
| `exclusionReason` | Reason for exclusion if not compensable | string |  |

### Decision Table

| Rule | Description | Conditions | Result | Legal Basis | Note |
|------|-------------|------------|--------|-------------|------|
| D4-R1 | Vehicle in normal traffic use on road — compensable | **vehicleInTrafficUse** = `true`<br>**locationContext** = `on_road_normal_traffic`<br>**damageToOwnVehicle** = `false` | **compensable** → `true`<br>**damageCategory** → `personal_injury or property_damage (based on type)`<br>**exclusionReason** → `—` | §1, §31 |  |
| D4-R2 | Vehicle used off road for non-transport purpose — NOT compensable | **locationContext** = `off_road_non_transport_purpose` | **compensable** → `false`<br>**damageCategory** → `excluded`<br>**exclusionReason** → `§1(1) — off-road use for non-transport purpose` | §1(1) |  |
| D4-R3 | Vehicle stored, repaired, serviced or washed off road — NOT compensable | **locationContext** = `stored_repaired_serviced_washed` | **compensable** → `false`<br>**damageCategory** → `excluded`<br>**exclusionReason** → `§1(2) — storage/maintenance off road` | §1(2) |  |
| D4-R4 | Vehicle in competition/testing on traffic-isolated area — NOT compensable | **locationContext** = `closed_area_competition_testing` | **compensable** → `false`<br>**damageCategory** → `excluded`<br>**exclusionReason** → `§1(3) — competition or testing on isolated area` | §1(3) |  |
| D4-R5 | Damage to own vehicle — excluded from own insurance | **damageToOwnVehicle** = `true` | **compensable** → `false`<br>**damageCategory** → `excluded`<br>**exclusionReason** → `§40(1) — own vehicle damage not covered by own insurance` | §40(1) |  |
| D4-R6 | Damage during work performance while stationary — to worker or work object — excluded | **vehicleStationary_workPerformance** = `true`<br>**damageToWorkObject** = `true` | **compensable** → `false`<br>**damageCategory** → `excluded`<br>**exclusionReason** → `§42 — work performance damage excluded` | §42 |  |


---

## D5: Liability Determination — Insurer vs Insurer
**Finnish:** Korvausvastuun määräytyminen
**Legal basis:** §31, §32, §33, §51
### Inputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `numberOfVehiclesInvolved` | Number of vehicles involved in accident | enum | one, two_or_more |
| `faultOfParties` | Fault found on parties' side | enum | no_fault_identified, fault_vehicle_A_only, fault_vehicle_B_only, shared_fault, defect_or_loading_vehicle_A, defect_or_loading_vehicle_B |
| `victimWasOccupant` | Victim was occupant (driver or passenger) of one vehicle | boolean |  |
| `vehicleOccupiedByVictim` | Vehicle in which victim was an occupant (if applicable) | string |  |

### Outputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `primaryLiableInsurer` | Insurer primarily liable to claimant | string |  |
| `interInsurerAllocation` | Inter-insurer allocation basis | string |  |

### Decision Table

| Rule | Description | Conditions | Result | Legal Basis | Note |
|------|-------------|------------|--------|-------------|------|
| D5-R1 | Single vehicle — strict liability, own insurer compensates | **numberOfVehiclesInvolved** = `one` | **primaryLiableInsurer** → `Insurer of the vehicle`<br>**interInsurerAllocation** → `N/A (single vehicle)` | §31, §32(1) |  |
| D5-R2 | Multiple vehicles — victim was occupant — personal injury paid by occupant's vehicle insurer first | **numberOfVehiclesInvolved** = `two_or_more`<br>**victimWasOccupant** = `true` | **primaryLiableInsurer** → `Insurer of the vehicle in which victim was occupant/driver`<br>**interInsurerAllocation** → `Inter-insurer split per §51 based on fault and circumstances` | §33(3), §51 |  |
| D5-R3 | Multiple vehicles — third party victim may choose any involved vehicle's insurer | **numberOfVehiclesInvolved** = `two_or_more`<br>**victimWasOccupant** = `false` | **primaryLiableInsurer** → `Any insurer of vehicles involved (claimant's choice)`<br>**interInsurerAllocation** → `Inter-insurer split per §51 based on fault and circumstances` | §33(3), §60(2) |  |
| D5-R4 | Damage due solely to one vehicle's defect/loading — that vehicle's insurer bears full cost | **numberOfVehiclesInvolved** = `two_or_more`<br>**faultOfParties** = `{'in': ['defect_or_loading_vehicle_A', 'defect_or_loading_vehicle_B']}` | **primaryLiableInsurer** → `Insurer of the defective/misladen vehicle`<br>**interInsurerAllocation** → `100% to defective vehicle insurer` | §51 |  |


---

## D6: Personal Injury Compensation — Eligibility and Amount
**Finnish:** Henkilövahingon korvauksen oikeus ja määrä
**Legal basis:** §34, §35, §36, §47, §48, §50
### Inputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `injuryIsMajor` | Injury is more than minor (vähäinen) | boolean |  |
| `injuryType` | Type of personal injury | enum | pain_suffering_temporary, loss_of_earnings, permanent_disability, death_benefits, loss_of_maintenance |
| `parallelTapaturmaRight` | Right to compensation under työtapaturma/maatalousyrittäjä/urheilija act | boolean |  |
| `continuousCompensation` | Is compensation continuous (jatkuva korvaus) | boolean |  |

### Outputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `eligible` | Eligible for this compensation type | boolean |  |
| `compensationBasis` | Basis for calculation | string |  |
| `coordinationRequired` | Coordination with other statutory schemes required | boolean |  |
| `indexAdjusted` | Subject to annual index adjustment | boolean |  |
| `indexMechanism` | Index mechanism if applicable | string |  |

### Decision Table

| Rule | Description | Conditions | Result | Legal Basis | Note |
|------|-------------|------------|--------|-------------|------|
| D6-R1 | Pain and suffering — only if injury is more than minor | **injuryType** = `pain_suffering_temporary`<br>**injuryIsMajor** = `true` | **eligible** → `true`<br>**compensationBasis** → `VahL §5:2 — non-economic loss`<br>**coordinationRequired** → `false`<br>**indexAdjusted** → `false`<br>**indexMechanism** → `—` | §34(1) |  |
| D6-R2 | Pain and suffering — minor injury → not eligible | **injuryType** = `pain_suffering_temporary`<br>**injuryIsMajor** = `false` | **eligible** → `false`<br>**compensationBasis** → `N/A`<br>**coordinationRequired** → `false`<br>**indexAdjusted** → `false`<br>**indexMechanism** → `—` | §34(1) |  |
| D6-R3 | Loss of earnings — eligible; index adjusted; coordinate with työtapaturma | **injuryType** = `loss_of_earnings` | **eligible** → `true`<br>**compensationBasis** → `VahL §5:2 — actual loss; historical earnings adjusted by palkkakerroin to accident year`<br>**coordinationRequired** → `true`<br>**indexAdjusted** → `true`<br>**indexMechanism** → `Continuing compensation adjusted annually by työeläkeindeksi (§35(1)); historical wages adjusted by palkkakerroin to accident year (§35(2))` | §34(1), §35, §36 |  |
| D6-R4 | Permanent disability — eligible; board opinion mandatory if serious | **injuryType** = `permanent_disability` | **eligible** → `true`<br>**compensationBasis** → `VahL §5:2 — functional impairment; LVL board opinion mandatory if serious (vaikea vamma)`<br>**coordinationRequired** → `true`<br>**indexAdjusted** → `true`<br>**indexMechanism** → `Continuing compensation adjusted annually by työeläkeindeksi` | §34(1), §35, §66(1)(3) |  |
| D6-R5 | Death benefits / loss of maintenance — eligible; board opinion for continuing compensation | **injuryType** = `{'in': ['death_benefits', 'loss_of_maintenance']}` | **eligible** → `true`<br>**compensationBasis** → `VahL §§5:4, 5:4a, 5:4b — survivors' benefits and grief compensation`<br>**coordinationRequired** → `false`<br>**indexAdjusted** → `true`<br>**indexMechanism** → `Continuing maintenance loss compensation adjusted by työeläkeindeksi annually` | §34(1), §35, §66(1)(1) |  |
| D6-R6 | Parallel työtapaturma right — motor insurance pays only excess | **parallelTapaturmaRight** = `true` | **eligible** → `true`<br>**compensationBasis** → `Only the portion not compensated under tapaturma law`<br>**coordinationRequired** → `true`<br>**indexAdjusted** → `true`<br>**indexMechanism** → `Per injury type above` | §36 |  |


---

## D7: Property Damage Compensation — Amount and Limits
**Finnish:** Esinevahingon korvaus — määrä ja enimmäismäärä
**Legal basis:** §37, §38, §40
### Inputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `vehicleDamageType` | Extent of vehicle damage | enum | repairable, total_loss_or_uneconomical_to_repair |
| `propertyCategory` | Category of property damaged | enum | vehicle, personal_effects_of_non_owner_passenger, other_third_party_property, excluded_property |
| `totalClaimsExceedCap` | Total property claims in this accident exceed €5 000 000 cap | boolean |  |

### Outputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `compensationAmount` | Compensation amount / basis | string |  |
| `capped` | Subject to per-insurance cap | boolean |  |
| `titleTransfer` | Vehicle title transfers to insurer | boolean |  |

### Decision Table

| Rule | Description | Conditions | Result | Legal Basis | Note |
|------|-------------|------------|--------|-------------|------|
| D7-R1 | Repairable vehicle — repair cost or equivalent amount | **propertyCategory** = `vehicle`<br>**vehicleDamageType** = `repairable` | **compensationAmount** → `Repair cost or equivalent amount; vehicle value depreciation NOT compensated`<br>**capped** → `true`<br>**titleTransfer** → `false` | §37(2) |  |
| D7-R2 | Total loss vehicle — fair market value before accident | **propertyCategory** = `vehicle`<br>**vehicleDamageType** = `total_loss_or_uneconomical_to_repair` | **compensationAmount** → `Fair market value immediately before accident`<br>**capped** → `true`<br>**titleTransfer** → `true` | §37(2) |  |
| D7-R3 | Property cap per liable insurance — €5 000 000 max | **totalClaimsExceedCap** = `true` | **compensationAmount** → `Claims paid proportionally to claimants' relative entitlements up to €5 000 000 per liable insurer`<br>**capped** → `true`<br>**titleTransfer** → `false` | §38(1) | Amount of €5 000 000 is not index-linked by law text. If cap is insufficient, later claimants still receive their proportional share even if cap is technically exceeded.
 |
| D7-R4 | Excluded property — no compensation | **propertyCategory** = `excluded_property` | **compensationAmount** → `No compensation`<br>**capped** → `false`<br>**titleTransfer** → `false` | §40 |  |


---

## D8: Claim Filing Deadline
**Finnish:** Korvausvaatimuksen esittämisen määräaika ja vanhentuminen
**Legal basis:** §61
### Inputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `awarenessDate` | Date claimant became aware of accident and damage | date |  |
| `damageSufferingDate` | Date damage consequence occurred | date |  |
| `compellingReason` | Compelling reason exists for late filing | boolean |  |

### Outputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `filingDeadline` | Filing deadline | string |  |
| `absoluteDeadline` | Absolute deadline regardless of awareness | string |  |
| `lateFilingPossible` | Late filing may still be accepted | boolean |  |

### Decision Table

| Rule | Description | Conditions | Result | Legal Basis | Note |
|------|-------------|------------|--------|-------------|------|
| D8-R1 | Standard deadline — 3 years from awareness | **compellingReason** = `false` | **filingDeadline** → `3 years from awareness of accident and damage consequence`<br>**absoluteDeadline** → `10 years from occurrence of damage consequence`<br>**lateFilingPossible** → `false` | §61(1) |  |
| D8-R2 | Compelling reason — late claim may be accepted | **compellingReason** = `true` | **filingDeadline** → `May be accepted after the 3-year deadline`<br>**absoluteDeadline** → `Not specified — case-by-case assessment`<br>**lateFilingPossible** → `true` | §61(3) |  |


---

## D9: Insurer Decision Deadline
**Finnish:** Vakuutusyhtiön päätöksenteon määräaika
**Legal basis:** §62
### Inputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `receiptOfClaim` | Date claim received | date |  |
| `receiptOfDocuments` | Date all required documents and information received | date |  |
| `liabilityDisputed` | Liability is disputed or unclear | boolean |  |
| `quantumFullyDetermined` | Full quantum of compensation has been determined | boolean |  |

### Outputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `investigationDeadline` | Investigation start deadline | string |  |
| `paymentOrDenialDeadline` | Deadline to pay or deny | string |  |
| `reasonedResponseDeadline` | Deadline for reasoned response if disputed | string |  |

### Decision Table

| Rule | Description | Conditions | Result | Legal Basis | Note |
|------|-------------|------------|--------|-------------|------|
| D9-R1 | Investigation must begin within 7 working days of claim receipt | — | **investigationDeadline** → `7 working days from claim receipt`<br>**paymentOrDenialDeadline** → `N/A (separate)`<br>**reasonedResponseDeadline** → `N/A (separate)` | §62(1) |  |
| D9-R2 | Clear liability and quantum — pay within 1 month of receiving all docs | **liabilityDisputed** = `false`<br>**quantumFullyDetermined** = `true` | **investigationDeadline** → `7 working days`<br>**paymentOrDenialDeadline** → `1 month from receipt of all required documents`<br>**reasonedResponseDeadline** → `N/A` | §62(2) |  |
| D9-R3 | Undisputed portion — must pay within 1 month even if total is disputed | **liabilityDisputed** = `false`<br>**quantumFullyDetermined** = `false` | **investigationDeadline** → `7 working days`<br>**paymentOrDenialDeadline** → `1 month — undisputed portion must be paid`<br>**reasonedResponseDeadline** → `3 months from claim — reasoned response for disputed remainder` | §62(2), §62(3), §62(4) |  |
| D9-R4 | Liability unclear — reasoned response within 3 months | **liabilityDisputed** = `true` | **investigationDeadline** → `7 working days`<br>**paymentOrDenialDeadline** → `1 month — undisputed portion if any`<br>**reasonedResponseDeadline** → `3 months from claim presentation` | §62(4) |  |


---

## D10: Appeal Chain and Deadlines
**Finnish:** Muutoksenhakuketju ja määräajat
**Legal basis:** §65, §66, §79, §81
### Inputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `disputeType` | Type of dispute | enum | compensation_amount_or_denial, serious_permanent_disability_compensation, continuing_loss_of_earnings_or_maintenance, full_cost_payment_municipality, other_insurer_decision |
| `writtenDecisionReceived` | Written insurer decision received with deadline notice | boolean |  |
| `courtDecisionFinal` | Final court judgment already given on the matter | boolean |  |

### Outputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `step1_LVLBoard` | Step 1 — LVL Board opinion | string |  |
| `step2_generalCourt` | Step 2 — General court action | string |  |
| `obligatoryLVLConsultation` | Insurer must consult LVL Board before deciding | boolean |  |

### Decision Table

| Rule | Description | Conditions | Result | Legal Basis | Note |
|------|-------------|------------|--------|-------------|------|
| D10-R1 | Standard compensation dispute — LVL board optional for claimant (1 year), court action (3 years) | **disputeType** = `compensation_amount_or_denial`<br>**courtDecisionFinal** = `false` | **step1_LVLBoard** → `Optional — claimant, insurer or court may request opinion within 1 year of insurer decision`<br>**step2_generalCourt** → `Court action within 3 years of written insurer decision + deadline notice; LVL/board proceedings suspend limitation`<br>**obligatoryLVLConsultation** → `false` | §65(1), §79(1) |  |
| D10-R2 | Serious permanent disability, continuing loss of earnings/maintenance — insurer MUST consult LVL Board | **disputeType** = `{'in': ['serious_permanent_disability_compensation', 'continuing_loss_of_earnings_or_maintenance']}` | **step1_LVLBoard** → `Mandatory — insurer must request LVL board opinion before issuing decision`<br>**step2_generalCourt** → `Court action within 3 years of written insurer decision`<br>**obligatoryLVLConsultation** → `true` | §66(1) |  |
| D10-R3 | Full cost payment (täyskustannusmaksu) dispute by municipality/joint authority | **disputeType** = `full_cost_payment_municipality` | **step1_LVLBoard** → `Not applicable (municipality is not claimant)`<br>**step2_generalCourt** → `Administrative appeal per hallintolainkäyttölaki`<br>**obligatoryLVLConsultation** → `false` | §81(2) |  |
| D10-R4 | Court judgment already final — LVL Board cannot consider that aspect | **courtDecisionFinal** = `true` | **step1_LVLBoard** → `LVL Board may not consider aspects already determined by final court judgment`<br>**step2_generalCourt** → `N/A (already decided)`<br>**obligatoryLVLConsultation** → `false` | §65(2) |  |


---

## D11: LVK Liability — Uninsured, Unknown and Exempt Vehicle Claims
**Finnish:** Liikennevakuutuskeskuksen korvausvastuu
**Legal basis:** §43, §44, §45, §46
### Inputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `vehicleIdentified` | Vehicle identified | boolean |  |
| `vehicleHadInsurance` | Vehicle had valid insurance at time of accident | boolean |  |
| `vehicleExemptFromObligation_cat1to5` | Vehicle exempt per §8(1)(1)-(5) (slow, combine, trailer, child, wheelchair) | boolean |  |
| `permanentHomeState` | Vehicle's permanent home state | enum | Finland, other_ETA, third_country |
| `accidentInFinland` | Accident occurred in Finland | boolean |  |
| `damageType` | Type of damage | enum | personal_injury, property_damage_hoofed_animals, property_damage_significant_with_personal, other_property_damage |
| `claimantKnewUninsured` | Claimant (occupant/driver) knew vehicle was uninsured | boolean |  |

### Outputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `LVKLiable` | LVK is liable | boolean |  |
| `conditionsForLiability` | Conditions and scope of LVK liability | string |  |

### Decision Table

| Rule | Description | Conditions | Result | Legal Basis | Note |
|------|-------------|------------|--------|-------------|------|
| D11-R1 | Uninsured Finnish vehicle — LVK liable regardless of fault | **vehicleIdentified** = `true`<br>**vehicleHadInsurance** = `false`<br>**permanentHomeState** = `Finland`<br>**claimantKnewUninsured** = `false` | **LVKLiable** → `true`<br>**conditionsForLiability** → `LVK compensates as if it were the insurer` | §46(1) |  |
| D11-R2 | Claimant (occupant/driver) knew vehicle was uninsured — LVK may deny | **vehicleHadInsurance** = `false`<br>**claimantKnewUninsured** = `true` | **LVKLiable** → `false`<br>**conditionsForLiability** → `LVK may deny if it can prove claimant's knowledge of no insurance` | §46(2) |  |
| D11-R3 | Unknown (hit-and-run) vehicle — LVK covers personal injury and hoofed animal damage; also other property damage if significant personal injury | **vehicleIdentified** = `false`<br>**accidentInFinland** = `true`<br>**damageType** = `{'in': ['personal_injury', 'property_damage_hoofed_animals', 'property_damage_significant_with_personal']}` | **LVKLiable** → `true`<br>**conditionsForLiability** → `LVK liable for personal injury, hoofed animal property damage, and significant property damage connected to significant personal injury` | §44 |  |
| D11-R4 | Exempt Finnish vehicle (§8(1)(1)-(5)) — LVK liable in Finland | **vehicleExemptFromObligation_cat1to5** = `true`<br>**permanentHomeState** = `Finland`<br>**accidentInFinland** = `true` | **LVKLiable** → `true`<br>**conditionsForLiability** → `LVK compensates for accidents in Finland caused by these exempt vehicles` | §43(1) |  |
| D11-R5 | Exempt Finnish vehicle causing accident in another ETA state — LVK liable | **vehicleExemptFromObligation_cat1to5** = `true`<br>**permanentHomeState** = `Finland`<br>**accidentInFinland** = `false` | **LVKLiable** → `true`<br>**conditionsForLiability** → `LVK liable for ETA accidents by exempt Finnish vehicles (unless state-owned)` | §45(1) |  |
| D11-R6 | Foreign ETA vehicle — LVK primarily liable for accidents in Finland | **permanentHomeState** = `other_ETA`<br>**accidentInFinland** = `true` | **LVKLiable** → `true`<br>**conditionsForLiability** → `LVK primarily liable; may reclaim from home state national guarantee fund` | §32(4), §74 |  |


---

## D12: Foreign Vehicle — Applicable Procedure
**Finnish:** Ulkomaisen ajoneuvon käsittely
**Legal basis:** §7, §32(4), §45, §70, §71, §72, §91
### Inputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `vehicleHomeState` | Vehicle's permanent home state | enum | other_ETA, third_country_green_card, third_country_no_green_card |
| `claimantResidence` | Claimant's residence | enum | Finland, other_ETA |
| `insurerIdentified` | Responsible insurer identified | boolean |  |
| `timeSinceAccident_months` | Months elapsed since accident | integer |  |
| `compensationRepresentativeNamed` | Compensation representative named in Finland | boolean |  |

### Outputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `claimProcedure` | Correct claim procedure | string |  |
| `LVKRole` | LVK's role | string |  |

### Decision Table

| Rule | Description | Conditions | Result | Legal Basis | Note |
|------|-------------|------------|--------|-------------|------|
| D12-R1 | ETA vehicle, insurer identified, Finnish claimant — claim against insurer or Finnish rep within 3 months | **vehicleHomeState** = `other_ETA`<br>**claimantResidence** = `Finland`<br>**insurerIdentified** = `true`<br>**compensationRepresentativeNamed** = `true` | **claimProcedure** → `File claim with responsible insurer or its Finnish compensation representative; 3-month response deadline`<br>**LVKRole** → `Fallback if no response within 3 months (§71)` | §70(1), §70(2), §71 |  |
| D12-R2 | ETA vehicle, Finnish claimant, insurer not identified within 2 months — claim to LVK | **vehicleHomeState** = `other_ETA`<br>**claimantResidence** = `Finland`<br>**insurerIdentified** = `false`<br>**timeSinceAccident_months** = `{'greaterThan': 2}` | **claimProcedure** → `File claim directly with LVK as compensation body`<br>**LVKRole** → `Acts as compensation body (korvauselin) under EU Directive art. 10` | §45(3), §71 |  |
| D12-R3 | Third-country vehicle with no green card arriving in Finland — Customs collects border insurance premium | **vehicleHomeState** = `third_country_no_green_card` | **claimProcedure** → `Customs (Tulli) collects border insurance premium at border; issues ETA-valid certificate on behalf of insurers`<br>**LVKRole** → `Receives premium collected by Customs` | §91(2) |  |


---

## D13: Reduction or Denial of Compensation
**Finnish:** Korvauksen alentaminen tai epääminen
**Legal basis:** §47, §48, §49, §50
### Inputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `causeType` | Basis for reduction/denial | enum | victim_self_inflicted_intentionally, victim_gross_negligence, victim_ordinary_negligence, alcohol_severe_BAC_1_2_permille_or_0_53_mg, alcohol_moderate_BAC_0_5_permille_or_0_22_mg, impairment_other_substance_severe, impairment_other_substance_moderate, knowing_unauthorised_vehicle_use, no_reduction_basis |
| `damageType` | Type of damage | enum | personal_injury, property_damage, rehabilitation |
| `ageUnder12` | Victim under 12 years | boolean |  |
| `legallyNonCulpable` | Victim legally non-culpable | boolean |  |
| `actingUnderNecessity` | Victim acting under necessity to prevent damage | boolean |  |

### Outputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `reductionApplied` | Reduction applied | boolean |  |
| `reductionDegree` | Degree of reduction | string |  |
| `rehabilitationAffected` | Rehabilitation compensation affected | boolean |  |

### Decision Table

| Rule | Description | Conditions | Result | Legal Basis | Note |
|------|-------------|------------|--------|-------------|------|
| D13-R1 | Self-inflicted intentional injury — personal injury compensated only for contribution of other circumstances | **causeType** = `victim_self_inflicted_intentionally`<br>**damageType** = `personal_injury`<br>**ageUnder12** = `false`<br>**legallyNonCulpable** = `false` | **reductionApplied** → `true`<br>**reductionDegree** → `Only proportion attributable to other circumstances compensated (can approach zero)`<br>**rehabilitationAffected** → `false` | §47(1) |  |
| D13-R2 | Gross negligence — personal injury may be reduced or denied | **causeType** = `victim_gross_negligence`<br>**damageType** = `personal_injury`<br>**ageUnder12** = `false`<br>**legallyNonCulpable** = `false` | **reductionApplied** → `true`<br>**reductionDegree** → `Reduction or denial proportional to circumstances`<br>**rehabilitationAffected** → `false` | §47(1) |  |
| D13-R3 | Property damage contributory negligence — proportional reduction | **damageType** = `property_damage` | **reductionApplied** → `true`<br>**reductionDegree** → `Equitable reduction proportional to victim's degree of fault`<br>**rehabilitationAffected** → `false` | §47(3) |  |
| D13-R4 | Severe alcohol impairment (BAC ≥ 1.2 ‰ or ≥ 0.53 mg/l) — near-full denial of personal injury | **causeType** = `{'in': ['alcohol_severe_BAC_1_2_permille_or_0_53_mg', 'impairment_other_substance_severe']}`<br>**damageType** = `personal_injury`<br>**ageUnder12** = `false`<br>**legallyNonCulpable** = `false` | **reductionApplied** → `true`<br>**reductionDegree** → `Only contribution of other circumstances compensated (typically minimal)`<br>**rehabilitationAffected** → `false` | §48(1) | BAC 1.2 ‰ in blood or 0.53 mg/l exhaled air triggers severe rule |
| D13-R5 | Moderate alcohol impairment (BAC ≥ 0.5 ‰ or ≥ 0.22 mg/l) — proportional reduction | **causeType** = `{'in': ['alcohol_moderate_BAC_0_5_permille_or_0_22_mg', 'impairment_other_substance_moderate']}`<br>**damageType** = `personal_injury`<br>**ageUnder12** = `false`<br>**legallyNonCulpable** = `false` | **reductionApplied** → `true`<br>**reductionDegree** → `Reduction proportional to victim's contribution to accident`<br>**rehabilitationAffected** → `false` | §48(2) |  |
| D13-R6 | Rehabilitation compensation — NEVER reduced under §47 or §48 | **damageType** = `rehabilitation` | **reductionApplied** → `false`<br>**reductionDegree** → `No reduction regardless of contributory negligence or alcohol`<br>**rehabilitationAffected** → `false` | §47(2), §48(3) | Exception — if personal injury compensation is denied entirely, rehabilitation is also not paid |
| D13-R7 | Under 12 / legally non-culpable / necessity — no reduction under §47-49 | **ageUnder12** = `true` | **reductionApplied** → `false`<br>**reductionDegree** → `No reduction; §47, §48, §49 cannot be invoked`<br>**rehabilitationAffected** → `false` | §50 |  |
| D13-R8 | Knowing unauthorised use of vehicle — compensation only for special reason | **causeType** = `knowing_unauthorised_vehicle_use`<br>**ageUnder12** = `false`<br>**legallyNonCulpable** = `false` | **reductionApplied** → `true`<br>**reductionDegree** → `Generally denied; paid only for special reason (erityinen syy)`<br>**rehabilitationAffected** → `true` | §49 |  |


---

## D14: Subrogation / Right of Recourse
**Finnish:** Takautumisoikeus
**Legal basis:** §73, §74
### Inputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `thirdPartyType` | Type of party against whom recourse is sought | enum | private_individual, employee_or_civil_servant, vehicle_owner_keeper_driver_passenger, company_or_organization, national_guarantee_fund_ETA, foreign_compensation_body_ETA |
| `causationBasis` | Basis on which third party caused the event | enum | intent, gross_negligence, driving_under_severe_alcohol_influence, ordinary_negligence_or_strict |
| `recoveryContext` | Context of the LVK payment giving rise to recourse | enum | LVK_paid_for_uninsured_vehicle, LVK_paid_for_unknown_vehicle, LVK_paid_because_no_insurer_identified, LVK_paid_insurer_insolvency, insurer_paid_and_subrogates |

### Outputs

| ID | Label | Type | Values / Notes |
|----|-------|------|----------------|
| `recourseAvailable` | Right of recourse available | boolean |  |
| `recourseAgainst` | Recourse against whom | string |  |
| `conditions` | Conditions for recourse | string |  |

### Decision Table

| Rule | Description | Conditions | Result | Legal Basis | Note |
|------|-------------|------------|--------|-------------|------|
| D14-R1 | Insurer subrogates against private individuals / vehicle parties — only for intent, gross negligence, or severe alcohol driving | **thirdPartyType** = `{'in': ['private_individual', 'employee_or_civil_servant', 'vehicle_owner_keeper_driver_passenger']}`<br>**causationBasis** = `{'in': ['intent', 'gross_negligence', 'driving_under_severe_alcohol_influence']}`<br>**recoveryContext** = `insurer_paid_and_subrogates` | **recourseAvailable** → `true`<br>**recourseAgainst** → `The individual who caused the event intentionally, with gross negligence or while severely intoxicated`<br>**conditions** → `Insurer steps into claimant's shoes up to amount paid` | §73 |  |
| D14-R2 | Insurer subrogates against company/organization — for any causation basis | **thirdPartyType** = `company_or_organization`<br>**recoveryContext** = `insurer_paid_and_subrogates` | **recourseAvailable** → `true`<br>**recourseAgainst** → `The company or organisation`<br>**conditions** → `Full subrogation without restriction to intent/gross negligence` | §73 |  |
| D14-R3 | LVK recourse against national guarantee fund — for uninsured ETA vehicle | **recoveryContext** = `LVK_paid_for_uninsured_vehicle`<br>**thirdPartyType** = `national_guarantee_fund_ETA` | **recourseAvailable** → `true`<br>**recourseAgainst** → `National guarantee fund of ETA state where vehicle has permanent home (§74(1)(5))`<br>**conditions** → `LVK has paid and vehicle's home state fund is liable` | §74(1)(5) |  |
| D14-R4 | LVK recourse against national guarantee fund — for unknown vehicle | **recoveryContext** = `LVK_paid_for_unknown_vehicle`<br>**thirdPartyType** = `national_guarantee_fund_ETA` | **recourseAvailable** → `true`<br>**recourseAgainst** → `National guarantee fund of ETA state where accident occurred (§74(1)(3))`<br>**conditions** → `LVK has paid and vehicle remained unidentified` | §74(1)(3) |  |
| D14-R5 | LVK recourse against foreign compensation body — where LVK paid due to insurer delay | **recoveryContext** = `LVK_paid_because_no_insurer_identified`<br>**thirdPartyType** = `foreign_compensation_body_ETA` | **recourseAvailable** → `true`<br>**recourseAgainst** → `Compensation body of ETA state where responsible insurer has its seat`<br>**conditions** → `LVK subrogates to claimant's rights up to amount paid; and claimant's rights against tortfeasor/insurer also transfer to LVK` | §74(2) |  |
| D14-R6 | LVK recourse following insurer insolvency — against liquidation/bankruptcy estate | **recoveryContext** = `LVK_paid_insurer_insolvency` | **recourseAvailable** → `true`<br>**recourseAgainst** → `Liquidation or bankruptcy estate of insolvent insurer`<br>**conditions** → `Claimant's rights against estate transfer to LVK to the extent LVK has paid` | §74(3) |  |


---
