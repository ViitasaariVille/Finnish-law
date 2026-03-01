# Data Points — Finnish Motor Vehicle Liability Insurance Rules

**Law:** Liikennevakuutuslaki (460/2016)  
**Generated:** 2026-03-01  
**Version:** 1.0  
**Author:** Lumen ⚖️ (Claude Sonnet 4.6)  

> Lists all input data points required to evaluate the DMN rules across decisions D1–D14, with sources, access methods, and automation levels. Data access rights for the insurer and LVK are primarily governed by §82 (tiedonsaantioikeus), §83 (tekninen käyttöyhteys), §86 (LVK information centre), and §80 (public healthcare reporting obligation).


## Summary

**38 data points** required to evaluate all DMN rules.

### By Category

| Category | Count |
|----------|-------|
| 🚗 Vehicle | 12 |
| 👤 Person | 8 |
| ⚡ Event | 11 |
| 📄 Insurance | 5 |
| 🏥 Medical | 4 |
| 💶 Financial | 2 |
| 📋 Procedural | 11 |
| ↩️ Subrogation | 3 |

### By Automation Level

| Level | Icon | Count | Meaning |
|-------|------|-------|---------|
| Full Auto | 🟢 | 22 | Obtainable from registries/systems automatically |
| Human Review | 🟡 | 11 | Requires professional verification |
| Human Decision | 🔴 | 5 | Requires human judgment — cannot be automated |

### ⚠️ Human Decision Data Points

These data points **cannot be determined by a computer system** — they require expert or legal judgment:

- **`dp_p003`** — Person Legally Non-Culpable at Time of Accident: Whether the injured person was legally non-culpable (syyntakeeton) at the time of the accident — i.e., incapable of bein...
- **`dp_p008`** — Victim Acting Under Necessity to Prevent Damage: Whether the victim was acting under necessity (hätätila / välttämättömyys) to prevent greater damage when they contribut...
- **`dp_proc003`** — Compelling Reason for Late Filing: Whether an exceptionally compelling reason (erityisen painava syy) exists that justifies accepting a compensation claim ...
- **`dp_s002`** — Basis of Third Party's Causation: The legal basis on which the third party caused the insured event. Determines whether recourse is available against priv...
- **`dp_m003`** — Basis for Reduction / Denial — Contributory Cause Type: The type of behaviour or circumstance on the victim's part that may reduce or deny compensation under §47–49. Includes: ...

### Primary Data Sources Used

- Traficom — Ajoneuvoliikennerekisteri (vehicle registry)
- Traficom — Liikennevakuutusrekisteri (insurance registry)
- LVK — Liikennevakuutuskeskus (databases + information centre)
- Poliisi — liikenneonnettomuusilmoitus
- DVV — Väestötietojärjestelmä
- Verohallinto — Tulorekisteri
- Kela
- Eläketurvakeskus (ETK)
- Potilastietojärjestelmät / healthcare records
- Medical experts (lääkärinlausunto)
- Liikennevahinkolautakunta (LVL Board)
- Insurer's own claims system

## Table of Contents

- [Data Source Catalogue](#data-source-catalogue)
- [🚗 Vehicle (12)](#vehicle)
- [👤 Person (8)](#person)
- [⚡ Event (11)](#event)
- [📄 Insurance (5)](#insurance)
- [🏥 Medical (4)](#medical)
- [💶 Financial (2)](#financial)
- [📋 Procedural (11)](#procedural)
- [↩️ Subrogation (3)](#subrogation)

---

## Data Source Catalogue

All sources referenced by data points are documented here.

| ID | Name | Access | Freshness | Legal Basis |
|----|------|--------|-----------|-------------|
| `traficom_vehicle_registry` | [Traficom — Ajoneuvoliikennerekisteri](https://www.traficom.fi/fi/ajoneuvoliikennerekisteri) | API via Traficom open data portal or direct system integration (technical access) | real_time | §82(4) — insurer/LVK right to technical access for traffic-use data; §83 — technical access rights |
| `traficom_insurance_registry` | [Traficom — Vakuutusrekisteri (liikennevakuutusrekisteri)](https://www.traficom.fi) | Technical access via Traficom or LVK system integration | real_time | §82(3) — LVK right to get data on uninsured vehicles from authorities and insurers |
| `lvk_database` | [LVK — Liikennevakuutuskeskus (internal databases)](https://www.lvk.fi) | Direct system access (LVK member insurers); or LVK query for Green Card/foreign insurer data | real_time | §82(3), §86 — LVK information centre; §74 — recourse; §43–§46 — LVK liability |
| `poliisi_accident_report` | [Poliisi — Liikenneonnettomuusraportti](https://www.poliisi.fi) | Request by insurer/LVK as part of claim investigation; public accident reports available via Poliisi | point_in_time | §82(1) — right to obtain data from authorities for claim resolution |
| `dvv_person_registry` | [Digi- ja väestötietovirasto (DVV) — Väestötietojärjestelmä](https://dvv.fi) | API query by insurer/LVK for claim resolution purposes | real_time | §82(1) — right to obtain from authorities data on earnings, benefits, and comparable matters |
| `employer_records` | Työnantajan palkkatiedot | Request by insurer/LVK with claimant consent or under §82(1)(2) | point_in_time | §82(1)(2) — insurer right to obtain from employer data on employee's work, remuneration and its basis |
| `verohallinto` | [Verohallinto — Tulorekisteri](https://www.vero.fi) | Request by insurer/LVK under §82(1)(1) and income register legislation | annual / near_real_time | §82(1)(1) — right to obtain from statutory insurance/pension institutions and authorities data on earnings and benefits |
| `kela` | [Kela — Kansaneläkelaitos](https://www.kela.fi) | Request by insurer/LVK under §82(1)(1) | on_request | §82(1)(1) — right to obtain from statutory insurance institutions data on benefits paid |
| `etk` | [Eläketurvakeskus (ETK)](https://www.etk.fi) | Request by insurer/LVK under §82(1)(1) | annual | §82(1)(1) — right to obtain from pension institutions data on earnings and benefits |
| `healthcare_records` | Potilastietojärjestelmä / Terveydenhuollon toimintayksiköt | Request by insurer under §82(1)(3); public healthcare units have proactive reporting obligation under §80 | on_request | §82(1)(3) — right to obtain from medical professionals and healthcare units: opinions, patient record data, health status, work capacity, treatment and rehabilitation |
| `medical_expert` | Lääketieteellinen asiantuntija / riippumaton lääkäri | Insurer commissions expert; §84 allows sharing of claimant data with the expert | point_in_time | §82(1)(3) + §84 — insurer may share claimant data with healthcare providers for expert opinion |
| `green_card` | [Vihreä kortti / kansainvälinen vakuutustodistus](https://www.cobx.org) | Physical inspection at border; or LVK Green Card bureau query | point_in_time | §7 — border insurance; §43 — LVK liability; document inspection right at border |
| `lvl_board` | [Liikennevahinkolautakunta (LVL)](https://www.liikennevahinkolautakunta.fi) | Insurer submits case; claimant may also request opinion within 1 year of insurer decision | on_request | §65, §66 — statutory right and obligation to consult LVL |
| `tuomioistuimet` | Tuomioistuimet — Tuomiorekisteri | Public records; obtainable via court inquiry | on_request | Public access; §65(2) — final court judgment bars LVL consideration |
| `korvausedustaja_registry` | [Korvausedustaja-rekisteri (LVK)](https://www.lvk.fi) | LVK query | real_time | §70, §86 — LVK information centre function; EU Directive Art. 10 |
| `fiva` | [Finanssivalvonta (FIVA) — Vakuutusyhtiörekisteri](https://www.finanssivalvonta.fi) | Public registry at FIVA website | real_time | Public register |
| `insurer_own_system` | Vakuutusyhtiön oma järjestelmä | Internal system access | real_time | Internal data |

### Source Details

#### `traficom_vehicle_registry` — **[Traficom — Ajoneuvoliikennerekisteri](https://www.traficom.fi/fi/ajoneuvoliikennerekisteri)** / Ajoneuvoliikennerekisteri
Finnish vehicle registration registry maintained by Traficom (Traffic Management Finland). Contains vehicle registration data, owner and keeper details, registration country, vehicle type and technical specifications, traffic-use removal and permanent removal status, insurance status linkage, and identification data.
**Access:** API via Traficom open data portal or direct system integration (technical access)  **Freshness:** real_time  **Legal basis for access:** §82(4) — insurer/LVK right to technical access for traffic-use data; §83 — technical access rights

#### `traficom_insurance_registry` — **[Traficom — Vakuutusrekisteri (liikennevakuutusrekisteri)](https://www.traficom.fi)** / Liikennevakuutusrekisteri
Registry of motor liability insurance policies linked to vehicles. Contains which insurer covers each vehicle and the policy validity period.
**Access:** Technical access via Traficom or LVK system integration  **Freshness:** real_time  **Legal basis for access:** §82(3) — LVK right to get data on uninsured vehicles from authorities and insurers

#### `lvk_database` — **[LVK — Liikennevakuutuskeskus (internal databases)](https://www.lvk.fi)** / Liikennevakuutuskeskus
LVK maintains databases on uninsured vehicles, Green Card bureau records, foreign insurer and compensation representative registrations, and cross-border claim records. Also acts as Finnish information centre (tietokeskus) under EU Directive.
**Access:** Direct system access (LVK member insurers); or LVK query for Green Card/foreign insurer data  **Freshness:** real_time  **Legal basis for access:** §82(3), §86 — LVK information centre; §74 — recourse; §43–§46 — LVK liability

#### `poliisi_accident_report` — **[Poliisi — Liikenneonnettomuusraportti](https://www.poliisi.fi)** / Liikenneonnettomuusilmoitus / tutkintatiedot
Police accident report containing accident location, circumstances, vehicles involved, parties' identities, preliminary fault assessment, blood/breath alcohol test results, and witness data.
**Access:** Request by insurer/LVK as part of claim investigation; public accident reports available via Poliisi  **Freshness:** point_in_time  **Legal basis for access:** §82(1) — right to obtain data from authorities for claim resolution

#### `dvv_person_registry` — **[Digi- ja väestötietovirasto (DVV) — Väestötietojärjestelmä](https://dvv.fi)** / Väestötietojärjestelmä (VTJ)
Finnish population information system. Contains person identity (henkilötunnus), date of birth, address (residence), family relations, death records, and citizenship.
**Access:** API query by insurer/LVK for claim resolution purposes  **Freshness:** real_time  **Legal basis for access:** §82(1) — right to obtain from authorities data on earnings, benefits, and comparable matters

#### `employer_records` — **Työnantajan palkkatiedot** / Työnantajan tiedot
Employment data from the employer: employment contract, salary, employment period, sick pay (sairausajan palkka), and other remuneration details.
**Access:** Request by insurer/LVK with claimant consent or under §82(1)(2)  **Freshness:** point_in_time  **Legal basis for access:** §82(1)(2) — insurer right to obtain from employer data on employee's work, remuneration and its basis

#### `verohallinto` — **[Verohallinto — Tulorekisteri](https://www.vero.fi)** / Tulorekisteri / Verorekisteri
Finnish Tax Administration's income register. Contains annual income data, employer information, and income sources. Used for loss-of-earnings calculation baseline.
**Access:** Request by insurer/LVK under §82(1)(1) and income register legislation  **Freshness:** annual / near_real_time  **Legal basis for access:** §82(1)(1) — right to obtain from statutory insurance/pension institutions and authorities data on earnings and benefits

#### `kela` — **[Kela — Kansaneläkelaitos](https://www.kela.fi)** / Kela
Social insurance institution of Finland. Provides data on sickness allowances, rehabilitation benefits, disability benefits, and other social security payments relevant to coordination with motor liability compensation.
**Access:** Request by insurer/LVK under §82(1)(1)  **Freshness:** on_request  **Legal basis for access:** §82(1)(1) — right to obtain from statutory insurance institutions data on benefits paid

#### `etk` — **[Eläketurvakeskus (ETK)](https://www.etk.fi)** / Eläketurvakeskus
Finnish Centre for Pensions. Contains earnings history for pension calculation purposes and pension benefit data. Used for palkkakerroin-adjusted loss-of-earnings calculations.
**Access:** Request by insurer/LVK under §82(1)(1)  **Freshness:** annual  **Legal basis for access:** §82(1)(1) — right to obtain from pension institutions data on earnings and benefits

#### `healthcare_records` — **Potilastietojärjestelmä / Terveydenhuollon toimintayksiköt** / Potilasasiakirjat
Medical records held by healthcare units (hospitals, clinics, GPs). Contain diagnoses, treatment history, disability assessments, rehabilitation plans, and medical expert opinions. Both public and private providers covered.
**Access:** Request by insurer under §82(1)(3); public healthcare units have proactive reporting obligation under §80  **Freshness:** on_request  **Legal basis for access:** §82(1)(3) — right to obtain from medical professionals and healthcare units: opinions, patient record data, health status, work capacity, treatment and rehabilitation

#### `medical_expert` — **Lääketieteellinen asiantuntija / riippumaton lääkäri** / Lääkärinlausunto / asiantuntijalausunto
Independent medical expert opinion commissioned by the insurer or LVK to assess injury severity, causation, disability degree, and rehabilitation needs. Required for discretionary assessments (injuryIsMajor, permanent disability degree).
**Access:** Insurer commissions expert; §84 allows sharing of claimant data with the expert  **Freshness:** point_in_time  **Legal basis for access:** §82(1)(3) + §84 — insurer may share claimant data with healthcare providers for expert opinion

#### `green_card` — **[Vihreä kortti / kansainvälinen vakuutustodistus](https://www.cobx.org)** / Vihreä kortti
International Motor Insurance Certificate issued by an insurer in the Green Card system. Proves valid insurance coverage for the vehicle in signatory states. Physical or digital.
**Access:** Physical inspection at border; or LVK Green Card bureau query  **Freshness:** point_in_time  **Legal basis for access:** §7 — border insurance; §43 — LVK liability; document inspection right at border

#### `lvl_board` — **[Liikennevahinkolautakunta (LVL)](https://www.liikennevahinkolautakunta.fi)** / Liikennevahinkolautakunta
Traffic Injury Board that issues non-binding opinions on compensation matters, especially for serious permanent disability, continuing loss of earnings/maintenance. Mandatory consultation by insurer in specified categories (§66).
**Access:** Insurer submits case; claimant may also request opinion within 1 year of insurer decision  **Freshness:** on_request  **Legal basis for access:** §65, §66 — statutory right and obligation to consult LVL

#### `tuomioistuimet` — **Tuomioistuimet — Tuomiorekisteri** / Tuomiorekisteri
Court records showing whether a final court judgment (lainvoimainen ratkaisu) has been given in a matter. Relevant for determining whether LVL Board consideration is barred.
**Access:** Public records; obtainable via court inquiry  **Freshness:** on_request  **Legal basis for access:** Public access; §65(2) — final court judgment bars LVL consideration

#### `korvausedustaja_registry` — **[Korvausedustaja-rekisteri (LVK)](https://www.lvk.fi)** / Korvausedustajat
Registry of compensation representatives named in Finland by foreign ETA insurers. Maintained by LVK as part of the information centre function.
**Access:** LVK query  **Freshness:** real_time  **Legal basis for access:** §70, §86 — LVK information centre function; EU Directive Art. 10

#### `fiva` — **[Finanssivalvonta (FIVA) — Vakuutusyhtiörekisteri](https://www.finanssivalvonta.fi)** / Vakuutusyhtiörekisteri
Finnish Financial Supervisory Authority registry of licensed insurers. Used to verify insurer identity and licence status (e.g., insolvency proceedings).
**Access:** Public registry at FIVA website  **Freshness:** real_time  **Legal basis for access:** Public register

#### `insurer_own_system` — **Vakuutusyhtiön oma järjestelmä** / Vakuutusyhtiön tietojärjestelmä
The insurer's own claims management and policy system. Contains: policy details, claim receipt timestamps, document receipt log, liability determinations, payment history, and claim correspondence.
**Access:** Internal system access  **Freshness:** real_time  **Legal basis for access:** Internal data

---

## Data Points by Category

## 🚗 Vehicle

*12 data points — 🟢 11 Full Auto · 🟡 1 Human Review*

### 🟢 `dp_v001` — Vehicle Permanent Home State
**Finnish:** Ajoneuvon pysyvä kotipaikka  **Legal basis:** §2(9), §5, §7, §43, §45, §46  **Type:** enum  **Automation:** 🟢 Full Auto  **Used in decisions:** D1, D11, D12

**Allowed values:** `Finland` · `other_ETA` · `third_country`

The country where the vehicle is permanently based, determined by: (1) state of registration plate/insurance plate/identification mark; (2) if none required, state of keeper's permanent residence; (3) if no plate or plate is false/illegal, state where the traffic accident occurred. Defined in §2(9).

> **Note:** D12 refines this into a 3-way split: other_ETA / third_country_green_card / third_country_no_green_card. The conceptual data point is the same; D12 adds the green card sub-distinction for procedural routing.

**Primary sources:**
- **src_traficom_vehicle_registry** — For Finnish-registered vehicles: Traficom is definitive. Registration plates and keeper data provide home state.
- **src_lvk_database** — For foreign ETA vehicles: LVK information centre database; data received from other ETA state information centres per §86.

**Secondary / fallback sources:**
- **src_green_card** — For third-country vehicles: home state identifiable from Green Card issuing state.
- **src_poliisi_accident_report** — Fallback: accident state used as home state if no plate exists per §2(9)(3).

<small>Rules: `D1-R1` · `D1-R10` · `D1-R11` · `D1-R12` · `D11-R1` · `D11-R4` · `D11-R5` · `D11-R6`</small>

---

### 🟢 `dp_v002` — Vehicle Type / Category
**Finnish:** Ajoneuvon laji / luokka  **Legal basis:** §8(1)(1)–(10), §2  **Type:** enum  **Automation:** 🟢 Full Auto  **Used in decisions:** D1

**Allowed values:** `standard_motor_vehicle` · `trailer_registered` · `trailer_unregistered` · `slow_work_machine_max15kmh_unregistered` · `combine_harvester_unregistered` · `child_only_vehicle_unregistered` · `disabled_wheelchair_unregistered` · `unregistered_offroad_only` · `state_owned` · `export_registered`

The technical and legal category of the vehicle, determining insurance obligation. Includes: standard motor vehicle, registered/unregistered trailer, slow work machine (≤15 km/h, unregistered), combine harvester (unregistered), child-only vehicle (unregistered), disabled electric wheelchair (unregistered), state-owned vehicle, export-registered vehicle.

> **Note:** Maximum design speed (≤15 km/h for D1-R2) must be technically verified from vehicle specifications, not just registry category. In practice, Traficom registry contains this information in the vehicle technical data.

**Primary sources:**
- **src_traficom_vehicle_registry** — Vehicle type (ajoneuvoluokka), maximum design speed, registration requirement, and ownership (state) are all in the registry.

**Secondary / fallback sources:**
- **src_poliisi_accident_report** — Corroboration of vehicle type from accident report vehicle data.

<small>Rules: `D1-R1` · `D1-R2` · `D1-R3` · `D1-R4` · `D1-R5` · `D1-R6` · `D1-R7`</small>

---

### 🟢 `dp_v003` — Vehicle Removed from Traffic Use
**Finnish:** Liikennekäytöstä poistettu  **Legal basis:** §2(10), §8(1)(9)  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D1

Whether the vehicle has been temporarily removed from traffic use (liikennekäytöstä poisto). Defined in §2(10) as temporary removal of a first-registered vehicle and recording of that fact in the registry.

> **Note:** Must be combined with dp_v005 (usedInTraffic) for D1-R8: exemption only applies if vehicle was removed AND not actually used in traffic. §82(4) also gives insurer/LVK right to data on traffic-removed vehicles that were used in traffic.

**Primary sources:**
- **src_traficom_vehicle_registry** — Removal status (liikennekäytöstä poisto) is a registry entry with date. Real-time query.

<small>Rules: `D1-R1` · `D1-R8`</small>

---

### 🟢 `dp_v004` — Vehicle Permanently Removed from Traffic
**Finnish:** Lopullinen poisto liikennekäytöstä  **Legal basis:** §2(11), §8(1)(10)  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D1

Whether the vehicle has been permanently removed from traffic use (lopullinen poisto). Defined in §2(11) as final removal from traffic use in Finland and recording of this in the registry.

> **Note:** Once permanently removed, insurance obligation ceases entirely (no_obligation, not merely exempt).

**Primary sources:**
- **src_traficom_vehicle_registry** — Permanent removal (lopullinen poisto) is a definitive registry entry.

<small>Rules: `D1-R1` · `D1-R9`</small>

---

### 🟢 `dp_v005` — Vehicle Actually Used in Traffic Despite Removal
**Finnish:** Ajoneuvoa käytetty liikenteessä poistosta huolimatta  **Legal basis:** §8(1)(9), §21  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D1

Whether a traffic-use-removed vehicle was in fact used in traffic. Relevant for determining whether the exemption under §8(1)(9) applies and for calculating premium surcharges under §21.

> **Note:** If the vehicle was used in traffic while removed, the exemption does not apply. The insurer may also charge a triple premium surcharge for this period (§21).

**Primary sources:**
- **src_poliisi_accident_report** — Traffic use evidenced by accident report or police observation.
- **src_traficom_vehicle_registry** — §82(4) grants technical access to data on traffic-removed vehicles used in traffic.

**Secondary / fallback sources:**
- **src_insurer_own_system** — Insurer may have own observation data or traffic camera evidence.

<small>Rules: `D1-R8`</small>

---

### 🟢 `dp_v006` — Vehicle in Traffic Use at Time of Accident
**Finnish:** Ajoneuvo liikenteessä käyttämisen aikana  **Legal basis:** §1, §2(6)  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D4

Whether the vehicle was being used in traffic (liikenteessä käyttäminen) at the time of the accident. Determines whether the event is a compensable traffic event under §1.

> **Note:** 'Traffic use' (liikenteeseen käyttäminen) is defined by §2(6). Must be assessed alongside locationContext (dp_e003). Exclusions apply for off-road non-transport use, storage/repair/maintenance, and closed-area competition/testing.

**Primary sources:**
- **src_poliisi_accident_report** — Accident report establishes circumstances and vehicle use at time of accident.

**Secondary / fallback sources:**
- **src_insurer_own_system** — Insurer investigation of accident circumstances.

<small>Rules: `D4-R1`</small>

---

### 🟢 `dp_v007` — Accident Vehicle Identified
**Finnish:** Ajoneuvo tunnistettu  **Legal basis:** §44, §46  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D11

Whether the vehicle that caused the accident has been identified. If not, this is a hit-and-run (tuntematonta ajoneuvoa) case triggering limited LVK liability under §44.

**Primary sources:**
- **src_poliisi_accident_report** — Police investigation establishes whether the vehicle was identified.

**Secondary / fallback sources:**
- **src_lvk_database** — LVK cross-references own records if a partial plate or description is available.

<small>Rules: `D11-R1` · `D11-R3`</small>

---

### 🟢 `dp_v008` — Vehicle Had Valid Insurance at Time of Accident
**Finnish:** Ajoneuvolla voimassa oleva vakuutus vahingon sattuessa  **Legal basis:** §46(1)  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D11

Whether the vehicle had a valid motor liability insurance policy at the exact time of the accident. Key trigger for LVK liability under §46.

**Primary sources:**
- **src_traficom_insurance_registry** — Insurance registry shows which insurer covers the vehicle and policy validity dates.
- **src_lvk_database** — LVK maintains data on uninsured vehicles; §82(3) grants access.

<small>Rules: `D11-R1` · `D11-R2`</small>

---

### 🟢 `dp_v009` — Vehicle Exempt under §8(1)(1)–(5)
**Finnish:** Ajoneuvo vapautettu vakuuttamisvelvollisuudesta §8(1)(1)–(5) perusteella  **Legal basis:** §8(1)(1)–(5), §43(1), §45(1)  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D11

Whether the vehicle falls into one of the five exempt categories under §8(1)(1)–(5): slow work machine (≤15 km/h), combine harvester, unregistered trailer, child-only vehicle, or disabled electric wheelchair. These exempt vehicles trigger LVK liability under §43.

> **Note:** Derived from dp_v002 (vehicleType). Separate data point for clarity in D11 context.

**Primary sources:**
- **src_traficom_vehicle_registry** — Vehicle technical data and registration status determine exempt category.

<small>Rules: `D11-R4` · `D11-R5`</small>

---

### 🟢 `dp_v010` — Damage Is to the Insured Vehicle Itself
**Finnish:** Vahinko aiheutunut tälle ajoneuvolle itselleen  **Legal basis:** §40(1)  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D4

Whether the property damage suffered is to the insured vehicle itself (as opposed to another vehicle, third-party property, or personal effects). Own-vehicle damage is categorically excluded from motor liability insurance under §40(1).

**Primary sources:**
- **src_poliisi_accident_report** — Accident report identifies vehicles involved and damage descriptions.
- **src_insurer_own_system** — Claims handler identifies which vehicle suffered damage.

<small>Rules: `D4-R1` · `D4-R5`</small>

---

### 🟡 `dp_v011` — Vehicle Damage Extent (Repairable vs. Total Loss)
**Finnish:** Ajoneuvovahingon laajuus (korjattava / lunastustapaus)  **Legal basis:** §37(2)  **Type:** enum  **Automation:** 🟡 Human Review  **Used in decisions:** D7

**Allowed values:** `repairable` · `total_loss_or_uneconomical_to_repair`

Whether the vehicle damage is repairable at reasonable cost, or constitutes a total loss or is uneconomical to repair. Determines whether compensation is based on repair cost or fair market value (§37(2)).

> **Note:** Requires professional vehicle damage assessment. The 'uneconomical to repair' threshold is a professional judgment: repair cost relative to vehicle value. Not automated.

**Primary sources:**
- **src_medical_expert** — Vehicle damage assessment by qualified auto damage assessor (vahinkotarkastaja).

**Secondary / fallback sources:**
- **src_insurer_own_system** — Insurer's own damage assessment records.

<small>Rules: `D7-R1` · `D7-R2`</small>

---

### 🟢 `dp_v012` — Vehicle Insured under Finnish Law
**Finnish:** Ajoneuvo vakuutettu Suomen lain mukaisella vakuutuksella  **Legal basis:** §13  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D3

Whether the vehicle involved has a valid Finnish motor liability insurance policy. Determines whether Finnish law governs the coverage and territorial scope (D3).

**Primary sources:**
- **src_traficom_insurance_registry**
- **src_lvk_database**

<small>Rules: `D3-R1` · `D3-R2` · `D3-R3` · `D3-R4`</small>

---

## 👤 Person

*8 data points — 🟢 4 Full Auto · 🔴 2 Human Decision · 🟡 2 Human Review*

### 🟢 `dp_p001` — Person's Role in Relation to the Vehicle
**Finnish:** Henkilön rooli ajoneuvoon nähden  **Legal basis:** §33, §34, §40, §46, §49  **Type:** enum  **Automation:** 🟢 Full Auto  **Used in decisions:** D2

**Allowed values:** `driver_of_vehicle` · `passenger_of_vehicle` · `owner_of_vehicle` · `keeper_of_vehicle` · `third_party_pedestrian_cyclist`

The legal role of the injured/claiming person relative to the insured vehicle: driver, passenger, owner, keeper, or third party (pedestrian, cyclist, etc.). Determines entitlement to compensation and applicable exclusions.

**Primary sources:**
- **src_poliisi_accident_report** — Accident report identifies all persons involved and their roles.
- **src_traficom_vehicle_registry** — Owner and keeper identities from registry; compared against claimant identity.

**Secondary / fallback sources:**
- **src_dvv_person_registry** — Person identity verification.

<small>Rules: `D2-R2` · `D2-R6` · `D2-R7`</small>

---

### 🟢 `dp_p002` — Person's Age — Under 12 at Time of Accident
**Finnish:** Henkilön ikä vahinkotapahtuman hetkellä — alle 12 vuotta  **Legal basis:** §50  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D2, D13

Whether the injured person was under 12 years of age at the time of the accident. If so, the insurer may not invoke §47–49 reductions (contributory negligence, alcohol, unauthorised use) against that person (§50).

**Primary sources:**
- **src_dvv_person_registry** — Date of birth from population register gives exact age at accident date.

**Secondary / fallback sources:**
- **src_poliisi_accident_report** — Accident report may note persons' approximate ages.

<small>Rules: `D2-R4` · `D13-R1` · `D13-R2` · `D13-R4` · `D13-R5` · `D13-R7` · `D13-R8`</small>

---

### 🔴 `dp_p003` — Person Legally Non-Culpable at Time of Accident
**Finnish:** Henkilö syyntakeeton vahinkotapahtuman hetkellä  **Legal basis:** §50  **Type:** boolean  **Automation:** 🔴 Human Decision  **Used in decisions:** D2, D13

Whether the injured person was legally non-culpable (syyntakeeton) at the time of the accident — i.e., incapable of being held responsible for their actions due to mental condition. If so, §47–49 reductions cannot be applied (§50).

> **Note:** This is an inherently human_decision data point. No registry provides this; it requires a medical professional assessment of mental capacity at the time of the specific event.

**Primary sources:**
- **src_medical_expert** — Medical/psychiatric expert opinion is required to establish legal non-culpability.

**Secondary / fallback sources:**
- **src_healthcare_records** — Medical records for context on mental condition.

<small>Rules: `D2-R1` · `D2-R4` · `D13-R1` · `D13-R2` · `D13-R7` · `D13-R8`</small>

---

### 🟢 `dp_p004` — Claimant's Residence
**Finnish:** Vahinkoa kärsineen / korvauksenhakijan asuinpaikka  **Legal basis:** §13(4), §45(3), §70, §71, §86  **Type:** enum  **Automation:** 🟢 Full Auto  **Used in decisions:** D3, D12

**Allowed values:** `Finland` · `other_ETA` · `third_country`

The state where the claimant has their permanent residence. Relevant for: (1) choice-of-law (Finnish resident may choose Finnish law in ETA accidents, §13(4)); (2) procedural routing for cross-border claims (D12); (3) LVK information centre obligations (§86).

**Primary sources:**
- **src_dvv_person_registry** — For Finnish residents: DVV address registry. For foreign residents: home-state population registry or residence permit data.

**Secondary / fallback sources:**
- **src_poliisi_accident_report** — Accident report may state claimant's address.
- **src_insurer_own_system** — Claim application includes claimant's stated address.

<small>Rules: `D3-R2` · `D3-R3` · `D12-R1` · `D12-R2`</small>

---

### 🟢 `dp_p005` — Claimant is ETA National
**Finnish:** Vahinkoa kärsinyt on ETA-valtion kansalainen  **Legal basis:** §13(2)  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D3

Whether the claimant is a national of an ETA (European Economic Area) member state. Relevant for coverage of accidents during transit through non-Green-Card states on direct ETA-to-ETA journeys (§13(2)).

**Primary sources:**
- **src_dvv_person_registry** — Nationality from Finnish population register for Finnish citizens.

**Secondary / fallback sources:**
- **src_poliisi_accident_report** — Passport or ID document presented at accident scene.

<small>Rules: `D3-R3`</small>

---

### 🟡 `dp_p006` — Person Knew Vehicle Was Uninsured
**Finnish:** Henkilö tiesi ajoneuvon olevan vakuuttamaton  **Legal basis:** §46(2)  **Type:** boolean  **Automation:** 🟡 Human Review  **Used in decisions:** D2, D11

Whether the driver, passenger, owner or keeper knew (tiennyt) that the vehicle had no valid insurance at the time of the accident. If proven, LVK may deny compensation under §46(2).

> **Note:** The burden of proof lies with LVK (§46(2): 'osoittaa hänen tienneen'). This is an evidentiary assessment; the data point cannot be derived from a registry. Requires human review of all available circumstantial evidence.

**Primary sources:**
- **src_insurer_own_system** — LVK/insurer gathers evidence of claimant's awareness: relationship to owner, prior communications, duration of use, etc.

**Secondary / fallback sources:**
- **src_poliisi_accident_report** — Police investigation may reveal circumstances indicating knowledge.

<small>Rules: `D2-R1` · `D2-R2` · `D11-R1` · `D11-R2`</small>

---

### 🟡 `dp_p007` — Person Knew Vehicle Was Used Without Authorisation
**Finnish:** Henkilö tiesi ajoneuvon oikeudettomasta käytöstä  **Legal basis:** §49  **Type:** boolean  **Automation:** 🟡 Human Review  **Used in decisions:** D2, D13

Whether the person knew that the vehicle was being used without the authorisation of the owner or keeper (anastettu tai oikeudettomasti käytetty). If so, compensation is only paid for special reason (§49).

> **Note:** Knowledge of unauthorised use is a subjective fact requiring evidentiary assessment.

**Primary sources:**
- **src_poliisi_accident_report** — Police investigation into unauthorised use, theft report, relationship between parties.

**Secondary / fallback sources:**
- **src_insurer_own_system** — Insurer investigation of circumstances of vehicle acquisition/use.

<small>Rules: `D2-R3` · `D13-R8`</small>

---

### 🔴 `dp_p008` — Victim Acting Under Necessity to Prevent Damage
**Finnish:** Vahinkoa kärsinyt toiminut hätävarjelutilanteessa / välttämättömyystilanteessa  **Legal basis:** §50  **Type:** boolean  **Automation:** 🔴 Human Decision  **Used in decisions:** D13

Whether the victim was acting under necessity (hätätila / välttämättömyys) to prevent greater damage when they contributed to the accident. Relevant exception that may prevent reduction under §47–49 per §50.

> **Note:** Whether necessity conditions were met is a legal assessment requiring human judgment. No registry source; based on investigation of accident circumstances.

**Primary sources:**
- **src_poliisi_accident_report**
- **src_insurer_own_system**

<small>Rules: `D13-R7`</small>

---

## ⚡ Event

*11 data points — 🟢 7 Full Auto · 🟡 4 Human Review*

### 🟢 `dp_e001` — Accident Country
**Finnish:** Vahinkopaikka / vahingon tapahtumamaa  **Legal basis:** §13, §44, §45  **Type:** enum  **Automation:** 🟢 Full Auto  **Used in decisions:** D3, D11

**Allowed values:** `Finland` · `other_ETA` · `green_card_state_non_ETA` · `non_green_card_transit` · `third_country`

The state where the traffic accident occurred. Determines territorial scope of Finnish insurance coverage (D3) and LVK liability (D11).

**Primary sources:**
- **src_poliisi_accident_report** — Accident location from police report or accident notification form.

**Secondary / fallback sources:**
- **src_insurer_own_system** — Claimant's accident report / claim form states accident location.

<small>Rules: `D3-R1` · `D3-R2` · `D3-R3` · `D3-R4` · `D11-R3` · `D11-R4` · `D11-R6`</small>

---

### 🟢 `dp_e002` — Accident Occurred in Finland
**Finnish:** Vahinko tapahtunut Suomessa  **Legal basis:** §43(1), §44, §46  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D11

Boolean simplification of dp_e001 for rules specifically requiring Finland-only check (LVK liability rules D11-R3, D11-R4, D11-R6).

> **Note:** Derived from dp_e001. Separate for clarity in D11 rule evaluation.

**Primary sources:**
- **src_poliisi_accident_report**

<small>Rules: `D11-R3` · `D11-R4` · `D11-R6`</small>

---

### 🟡 `dp_e003` — Location Context of Vehicle Use
**Finnish:** Käyttötilanteen sijaintikonteksti  **Legal basis:** §1(1), §1(2), §1(3)  **Type:** enum  **Automation:** 🟡 Human Review  **Used in decisions:** D4

**Allowed values:** `on_road_normal_traffic` · `off_road_non_transport_purpose` · `stored_repaired_serviced_washed` · `closed_area_competition_testing` · `isolated_area_other`

The physical/operational context in which the vehicle was being used at the time of the accident. Determines whether the event qualifies as 'traffic use' and is compensable under §1.

> **Note:** The 'off_road_non_transport_purpose' classification requires human_decision per D4-R2 due to the 'olennaisesti' (substantially) qualifier. Other categories are full_auto once location is established. Overall: human_review for D4 location context.

**Primary sources:**
- **src_poliisi_accident_report** — Police accident report describes location and circumstances.

**Secondary / fallback sources:**
- **src_insurer_own_system** — Insurer site visit or investigation may clarify location context.

<small>Rules: `D4-R1` · `D4-R2` · `D4-R3` · `D4-R4`</small>

---

### 🟢 `dp_e004` — Vehicle Stationary During Work Performance
**Finnish:** Ajoneuvo liikkumattomana työnsuorituksen aikana  **Legal basis:** §42  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D4

Whether the damage occurred while the vehicle was stationary and a work performance (työnsuoritus) was being carried out using it (e.g., truck crane operation, concrete pumping). Relevant for exclusion under §42.

**Primary sources:**
- **src_poliisi_accident_report**
- **src_insurer_own_system**

<small>Rules: `D4-R6`</small>

---

### 🟢 `dp_e005` — Damage Is to the Work Object
**Finnish:** Vahinko aiheutui työsuorituksen kohteelle  **Legal basis:** §42  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D4

Whether the property damage was to the object of the work being performed using the stationary vehicle, or to another vehicle involved in the work. Relevant for the §42 exclusion of work-performance damage.

**Primary sources:**
- **src_poliisi_accident_report**
- **src_insurer_own_system**

<small>Rules: `D4-R6`</small>

---

### 🟢 `dp_e006` — Number of Vehicles Involved in Accident
**Finnish:** Vahinkoon osallisten ajoneuvojen lukumäärä  **Legal basis:** §31, §32, §33, §51  **Type:** enum  **Automation:** 🟢 Full Auto  **Used in decisions:** D5

**Allowed values:** `one` · `two_or_more`

Whether the accident involved one vehicle only, or two or more vehicles. Determines liability allocation and inter-insurer settlement rules (§51).

**Primary sources:**
- **src_poliisi_accident_report**

<small>Rules: `D5-R1` · `D5-R2` · `D5-R3` · `D5-R4`</small>

---

### 🟡 `dp_e007` — Fault / Defect Found on Parties
**Finnish:** Osapuolten tuottamus / ajoneuvon vika  **Legal basis:** §51  **Type:** enum  **Automation:** 🟡 Human Review  **Used in decisions:** D5

**Allowed values:** `no_fault_identified` · `fault_vehicle_A_only` · `fault_vehicle_B_only` · `shared_fault` · `defect_or_loading_vehicle_A` · `defect_or_loading_vehicle_B`

Assessment of which party (or whose vehicle defect/faulty loading) caused or contributed to the accident. Used for inter-insurer allocation under §51. Includes: no fault, fault of vehicle A only, fault of vehicle B only, shared fault, or damage due solely to defect/faulty loading of a specific vehicle.

> **Note:** Fault determination is a legal-factual assessment. 'Solely due to defect' (yksinomaan puutteellisuudesta) requires human expert verification of exclusive causation.

**Primary sources:**
- **src_poliisi_accident_report** — Police accident report contains preliminary fault assessment.

**Secondary / fallback sources:**
- **src_medical_expert** — Technical expert for vehicle defect assessment.
- **src_insurer_own_system** — Insurer legal team assesses fault from all available evidence.

<small>Rules: `D5-R4`</small>

---

### 🟢 `dp_e008` — Victim Was Occupant of One of the Vehicles
**Finnish:** Vahinkoa kärsinyt oli ajoneuvon matkustaja tai kuljettaja  **Legal basis:** §33(3)  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D5

Whether the injured party was an occupant (driver or passenger) of one of the vehicles involved in the multi-vehicle accident. Determines which insurer pays first under §33(3).

**Primary sources:**
- **src_poliisi_accident_report**

<small>Rules: `D5-R2` · `D5-R3`</small>

---

### 🟡 `dp_e009` — Journey Type (for Transit States)
**Finnish:** Matkan luonne (kauttakulkutilanne)  **Legal basis:** §13(2)  **Type:** enum  **Automation:** 🟡 Human Review  **Used in decisions:** D3

**Allowed values:** `direct_ETA_to_ETA` · `other`

Whether the journey on which the accident occurred was a direct ETA-to-ETA transit trip (suora matka ETA-valtiosta toiseen) or some other journey. Relevant for coverage during transit through non-Green-Card states under §13(2).

**Primary sources:**
- **src_insurer_own_system** — Journey documentation: tickets, route plans, travel itinerary.

**Secondary / fallback sources:**
- **src_poliisi_accident_report**

<small>Rules: `D3-R3`</small>

---

### 🟢 `dp_e010` — Type of Damage Suffered
**Finnish:** Vahingon laji  **Legal basis:** §31, §34, §37, §40, §47  **Type:** enum  **Automation:** 🟢 Full Auto  **Used in decisions:** D2, D4, D7, D11, D13

**Allowed values:** `personal_injury` · `property_damage` · `rehabilitation`

Whether the damage suffered is personal injury (henkilövahinko) or property damage (esinevahinko / varallisuusvahinko). Core classification used across multiple decisions to route to applicable rules.

**Primary sources:**
- **src_poliisi_accident_report**
- **src_healthcare_records** — For personal injury: medical records establish the injury.
- **src_insurer_own_system** — Claims handler categorises damage type on claim receipt.

<small>Rules: `D2-R1` · `D2-R5` · `D2-R6` · `D2-R7` · `D4-R1` · `D4-R5` · `D7-R1` · `D7-R2` · `D7-R3` · `D11-R3` · `D13-R1` · `D13-R2` · *+4 more*</small>

---

### 🟡 `dp_e011` — Property Type / Category Damaged
**Finnish:** Vahingoittuneen omaisuuden tyyppi  **Legal basis:** §37, §40  **Type:** enum  **Automation:** 🟡 Human Review  **Used in decisions:** D2, D7

**Allowed values:** `insured_vehicle_itself` · `coupled_other_vehicle` · `property_in_insured_vehicle` · `personal_effects_passenger` · `other_vehicle_owned_by_driver` · `other_third_party_property` · `excluded_property`

The category of the damaged property. Determines entitlement to compensation (D2) and applicable cap/exclusion rules (D7). Categories include: the insured vehicle itself, coupled vehicle, property in vehicle, personal effects of passenger (non-owner/keeper), owner/keeper/driver's own property, or third-party property.

**Primary sources:**
- **src_poliisi_accident_report** — Accident report identifies damaged property.
- **src_insurer_own_system** — Claims handler assesses property ownership and category.

**Secondary / fallback sources:**
- **src_traficom_vehicle_registry** — Owner/keeper identity from registry to determine if claimant is owner/keeper.

<small>Rules: `D2-R5` · `D2-R6` · `D2-R7` · `D7-R1` · `D7-R2` · `D7-R4`</small>

---

## 📄 Insurance

*5 data points — 🟢 4 Full Auto · 🟡 1 Human Review*

### 🟢 `dp_i001` — Green Card Validity
**Finnish:** Vihreä kortti voimassa  **Legal basis:** §7(2)  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D1

Whether the third-country vehicle has a valid Green Card (international motor insurance certificate) covering travel in Finland / ETA states at the time of entry. If valid, border insurance is not required (§7(2)).

**Primary sources:**
- **src_green_card** — Physical or digital Green Card presented at border; expiry date check.
- **src_lvk_database** — LVK acts as Finnish Green Card bureau; may validate via bureau.

<small>Rules: `D1-R10` · `D1-R11`</small>

---

### 🟢 `dp_i002` — LVK Has Committed to Respond for This Vehicle
**Finnish:** LVK on sitoutunut vastaamaan ajoneuvon puolesta  **Legal basis:** §7(1)  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D1

Whether LVK has made a specific commitment to handle claims for the third-country vehicle in question, substituting for the border insurance requirement under §7(1).

**Primary sources:**
- **src_lvk_database** — LVK internal records of commitments made.

<small>Rules: `D1-R10`</small>

---

### 🟢 `dp_i003` — Compensation Representative Named in Finland
**Finnish:** Korvausedustaja nimetty Suomeen  **Legal basis:** §70  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D12

Whether the foreign ETA insurer has named a compensation representative (korvausedustaja) in Finland. Relevant for cross-border claim routing under §70.

**Primary sources:**
- **src_korvausedustaja_registry**

<small>Rules: `D12-R1`</small>

---

### 🟢 `dp_i004` — Responsible Insurer Identified
**Finnish:** Korvausvelvollinen vakuutusyhtiö tunnistettu  **Legal basis:** §45(3), §71  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D12

Whether the foreign insurer responsible for the vehicle has been identified from LVK/ETA information centre data. Triggers different procedural routes under §45 and §71.

**Primary sources:**
- **src_lvk_database** — LVK information centre database and ETA information centre network.
- **src_korvausedustaja_registry**

<small>Rules: `D12-R1` · `D12-R2`</small>

---

### 🟡 `dp_i005` — Parallel Right under Tapaturma / Workers' Comp Legislation
**Finnish:** Rinnakkainen oikeus työtapaturmalain tai vastaavan mukaiseen korvaukseen  **Legal basis:** §36  **Type:** boolean  **Automation:** 🟡 Human Review  **Used in decisions:** D6

Whether the injured person has a right to compensation for the same injury under the Workers' Accident Insurance Act (työtapaturma- ja ammattitautilaki 459/2015), the Agricultural Entrepreneurs Act (873/2015), or the Athletes' Act (276/2009). If so, motor insurance covers only the residual (§36).

> **Note:** Requires coordination with the tapaturma insurer to establish what has been or will be paid before motor insurance residual obligation can be calculated.

**Primary sources:**
- **src_kela** — Kela administers certain tapaturma benefits; coordinate to establish parallel right.

**Secondary / fallback sources:**
- **src_employer_records** — Employment contract and work assignment at time of accident determines tapaturma coverage.
- **src_insurer_own_system** — Claims coordination with the tapaturma insurer.

<small>Rules: `D6-R6`</small>

---

## 🏥 Medical

*4 data points — 🟢 2 Full Auto · 🟡 2 Human Review*

### 🟢 `dp_m001` — Type of Personal Injury Compensation Sought
**Finnish:** Haettavan henkilövahingon korvauslaji  **Legal basis:** §34, §35, §36  **Type:** enum  **Automation:** 🟢 Full Auto  **Used in decisions:** D6

**Allowed values:** `pain_suffering_temporary` · `loss_of_earnings` · `permanent_disability` · `death_benefits` · `loss_of_maintenance` · `rehabilitation`

The specific type of personal injury compensation being claimed, which determines eligibility rules, calculation basis, indexation, and coordination requirements (D6).

**Primary sources:**
- **src_insurer_own_system** — Determined from claimant's compensation claim form.

**Secondary / fallback sources:**
- **src_healthcare_records** — Medical records establish injury type and consequences.

<small>Rules: `D6-R1` · `D6-R2` · `D6-R3` · `D6-R4` · `D6-R5` · `D6-R6`</small>

---

### 🟡 `dp_m002` — Injury Severity — More than Minor
**Finnish:** Vamman vakavuus — ei vähäinen  **Legal basis:** §34(1)  **Type:** boolean  **Automation:** 🟡 Human Review  **Used in decisions:** D6

Whether the personal injury is 'more than minor' (ei vähäinen) within the meaning of §34(1). Only non-minor injuries qualify for pain-and-suffering (kipu ja särky) compensation. The 'vähäinen' threshold is a medical-legal determination.

> **Note:** This is a human_review data point. The medical community and LVL Board have developed practical thresholds (e.g., whiplash grades, soft tissue injury durations), but the determination cannot be automated for individual cases.

**Primary sources:**
- **src_medical_expert** — Independent medical expert assesses injury severity against the vähäinen threshold.

**Secondary / fallback sources:**
- **src_healthcare_records** — Patient records provide clinical basis for assessment.
- **src_lvl_board** — LVL Board recommendations on what qualifies as non-minor injury (non-binding guidance).

<small>Rules: `D6-R1` · `D6-R2`</small>

---

### 🟡 `dp_m003` — Basis for Reduction / Denial — Contributory Cause Type
**Finnish:** Korvauksen alentamisen tai epäämisen peruste  **Legal basis:** §47, §48, §49  **Type:** enum  **Automation:** 🟡 Human Review  **Used in decisions:** D13

**Allowed values:** `victim_self_inflicted_intentionally` · `victim_gross_negligence` · `victim_ordinary_negligence` · `alcohol_severe_BAC_1_2_permille_or_0_53_mg` · `alcohol_moderate_BAC_0_5_permille_or_0_22_mg` · `impairment_other_substance_severe` · `impairment_other_substance_moderate` · `knowing_unauthorised_vehicle_use` · `no_reduction_basis`

The type of behaviour or circumstance on the victim's part that may reduce or deny compensation under §47–49. Includes: self-inflicted intentional injury, gross negligence, ordinary negligence, alcohol (severe: BAC ≥ 1.2‰ or ≥ 0.53 mg/l; moderate: ≥ 0.5‰ or ≥ 0.22 mg/l), impairment by other substances (severe/moderate), knowing unauthorised use.

> **Note:** BAC thresholds (severe ≥ 1.2‰ / moderate ≥ 0.5‰) are objectively measurable (full_auto for the threshold check). However, determining gross negligence, intentionality, and 'ordinary negligence' requires human legal assessment (human_decision). The sub-values have different automation levels; the overall data point is human_review.

**Primary sources:**
- **src_poliisi_accident_report** — Police report contains BAC test results (alcohol), circumstances, and preliminary fault assessment.

**Secondary / fallback sources:**
- **src_healthcare_records** — Hospital blood alcohol records; substance impairment evidence.
- **src_insurer_own_system** — Insurer investigation findings.

<small>Rules: `D13-R1` · `D13-R2` · `D13-R3` · `D13-R4` · `D13-R5` · `D13-R8`</small>

---

### 🟢 `dp_m004` — Compensation Is Continuous (Jatkuva korvaus)
**Finnish:** Korvaus on jatkuvaa  **Legal basis:** §35(1), §66(1)(1)  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D6

Whether the compensation being assessed is a continuing payment (jatkuva korvaus) as opposed to a lump sum. Triggers mandatory annual index adjustment by työeläkeindeksi (§35) and mandatory LVL Board consultation for certain categories (§66(1)(1)).

**Primary sources:**
- **src_insurer_own_system** — Determined from compensation decision type: lump sum vs. continuing annuity.

<small>Rules: `D6-R3` · `D6-R4` · `D6-R5`</small>

---

## 💶 Financial

*2 data points — 🟢 1 Full Auto · 🟡 1 Human Review*

### 🟢 `dp_f001` — Total Property Claims Exceed €5 000 000 Cap
**Finnish:** Esinevahingot ylittävät €5 000 000 enimmäismäärän  **Legal basis:** §38(1)  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D7

Whether the aggregate property damage claims against a single liable motor insurance in this accident exceed the statutory cap of €5 000 000 per §38(1). If so, claimants receive proportional shares.

> **Note:** The €5 000 000 cap amount is a fixed statutory figure (not index-linked per law text).

**Primary sources:**
- **src_insurer_own_system** — Insurer aggregates all property claims received against the policy for this accident.

<small>Rules: `D7-R3`</small>

---

### 🟡 `dp_f002` — Historical Earnings / Wage Data for Loss-of-Earnings Calculation
**Finnish:** Historiallinen ansiotulo ansionmenetyksen laskemiseksi  **Legal basis:** §34(1), §35(2)  **Type:** string  **Automation:** 🟡 Human Review  **Used in decisions:** D6

The claimant's pre-accident earnings history, required to calculate loss of earnings under §34–35. Historical wages from different years are adjusted using palkkakerroin to the accident year (§35(2)).

> **Note:** Calculation formula (palkkakerroin adjustment) is mechanical once earnings data is obtained. However, determining correct earnings base (especially for variable income, multiple employers, self-employment) requires professional review.

**Primary sources:**
- **src_verohallinto** — Tax records and income register provide annual income data per year.
- **src_employer_records** — Employer salary certificate; §82(1)(2) grants access.

**Secondary / fallback sources:**
- **src_etk** — ETK pension earnings records for salary history, especially for self-employed.
- **src_kela** — Kela sickness allowance records may reflect prior earnings.

<small>Rules: `D6-R3` · `D6-R6`</small>

---

## 📋 Procedural

*11 data points — 🟡 5 Human Review · 🟢 5 Full Auto · 🔴 1 Human Decision*

### 🟡 `dp_proc001` — Date Claimant Became Aware of Accident and Damage
**Finnish:** Päivä, jona korvauksenhakija sai tiedon vahinkotapahtumasta ja vahingon seurauksesta  **Legal basis:** §61(1)  **Type:** date  **Automation:** 🟡 Human Review  **Used in decisions:** D8

The date on which the claimant acquired actual knowledge of (1) the traffic accident (vahinkotapahtuma) and (2) the resulting damage consequence (vahingon seuraus). Start of the 3-year limitation period under §61(1).

> **Note:** Awareness of 'damage consequence' (vahingon seuraus) may differ from accident date for latent injuries. This requires professional assessment in contested limitation cases.

**Primary sources:**
- **src_insurer_own_system** — Claim form typically includes claimant's stated awareness date.

**Secondary / fallback sources:**
- **src_poliisi_accident_report** — Accident date from police report (often coincides with awareness for direct victims).
- **src_healthcare_records** — For late-onset injuries: medical records establish date diagnosis was communicated.

<small>Rules: `D8-R1` · `D8-R2`</small>

---

### 🟢 `dp_proc002` — Date Damage Consequence Occurred
**Finnish:** Päivä, jona vahingon seuraus ilmeni  **Legal basis:** §61(1)  **Type:** date  **Automation:** 🟢 Full Auto  **Used in decisions:** D8

The date the damage consequence occurred or manifested. Start date for the 10-year absolute limitation period under §61(1), regardless of claimant's awareness.

**Primary sources:**
- **src_poliisi_accident_report** — Accident date for immediate consequences.
- **src_healthcare_records** — Medical records for latent injury manifestation dates.

<small>Rules: `D8-R1`</small>

---

### 🔴 `dp_proc003` — Compelling Reason for Late Filing
**Finnish:** Erityisen painava syy myöhästyneelle korvausvaatimukselle  **Legal basis:** §61(3)  **Type:** boolean  **Automation:** 🔴 Human Decision  **Used in decisions:** D8

Whether an exceptionally compelling reason (erityisen painava syy) exists that justifies accepting a compensation claim filed after the 3-year limitation period under §61(3). Inherently discretionary; no objective statutory criteria defined.

> **Note:** This is a paradigmatic human_decision data point. No automation possible.

**Primary sources:**
- **src_insurer_own_system** — Claimant provides reasons in claim; insurer legal team assesses.

**Secondary / fallback sources:**
- **src_healthcare_records** — Medical incapacity may constitute compelling reason.
- **src_lvl_board** — LVL Board guidance on what has been accepted as erityisen painava syy.

<small>Rules: `D8-R2`</small>

---

### 🟢 `dp_proc004` — Date Claim Received by Insurer
**Finnish:** Korvausvaatimuksen vastaanottopäivä  **Legal basis:** §62(1)  **Type:** date  **Automation:** 🟢 Full Auto  **Used in decisions:** D9

The date the insurer received the compensation claim (vireilletulo). Starts the 7 working-day investigation deadline and all subsequent procedural deadlines under §62.

**Primary sources:**
- **src_insurer_own_system** — System timestamp on claim receipt (electronic or manual entry).

<small>Rules: `D9-R1` · `D9-R2` · `D9-R3` · `D9-R4`</small>

---

### 🟡 `dp_proc005` — Date All Required Documents and Information Received
**Finnish:** Päivä, jona kaikki tarvittavat asiakirjat ja tiedot saapuivat  **Legal basis:** §62(2)  **Type:** date  **Automation:** 🟡 Human Review  **Used in decisions:** D9

The date by which the insurer has received all documents and information needed to decide the claim. Starts the 1-month payment or reasoned-response deadline under §62(2)–(3).

> **Note:** The insurer must also actively request missing information within a reasonable time. Determining completeness ('all required' documents) requires case handler judgment.

**Primary sources:**
- **src_insurer_own_system** — Document receipt log in claims system. Determining when 'all required' documents are received is a professional assessment.

<small>Rules: `D9-R2` · `D9-R3`</small>

---

### 🟡 `dp_proc006` — Liability Disputed or Unclear
**Finnish:** Korvausvastuu riitainen tai epäselvä  **Legal basis:** §62(3), §62(4)  **Type:** boolean  **Automation:** 🟡 Human Review  **Used in decisions:** D9

Whether the insurer's liability for the claim is disputed or factually/legally unclear. If unclear, the 3-month reasoned response deadline applies under §62(4).

**Primary sources:**
- **src_insurer_own_system** — Claims handler's liability assessment.

<small>Rules: `D9-R2` · `D9-R3` · `D9-R4`</small>

---

### 🟡 `dp_proc007` — Full Quantum of Compensation Determined
**Finnish:** Korvauksen kokonaismäärä selvitetty  **Legal basis:** §62(2), §62(3)  **Type:** boolean  **Automation:** 🟡 Human Review  **Used in decisions:** D9

Whether the full amount of compensation owed has been determined. If not, the insurer must still pay the undisputed portion within 1 month, with a 3-month deadline for a reasoned response on the remainder (§62(3)).

**Primary sources:**
- **src_insurer_own_system**

<small>Rules: `D9-R2` · `D9-R3`</small>

---

### 🟡 `dp_proc008` — Type of Dispute / Appeal Matter
**Finnish:** Riita- / muutoksenhakuasian tyyppi  **Legal basis:** §65, §66, §79, §81  **Type:** enum  **Automation:** 🟡 Human Review  **Used in decisions:** D10

**Allowed values:** `compensation_amount_or_denial` · `serious_permanent_disability_compensation` · `continuing_loss_of_earnings_or_maintenance` · `full_cost_payment_municipality` · `other_insurer_decision`

Classification of the dispute for determining the appeal route (D10): standard compensation amount/denial, serious permanent disability compensation, continuing loss of earnings/maintenance, full-cost payment (municipality), or other insurer decision.

> **Note:** The classification into 'serious permanent disability' or 'continuing compensation' requires the underlying medical/legal determination to have been made first.

**Primary sources:**
- **src_insurer_own_system** — Insurer decision identifies the type of compensation involved.

**Secondary / fallback sources:**
- **src_lvl_board** — LVL Board determines whether it falls within mandatory consultation categories.

<small>Rules: `D10-R1` · `D10-R2` · `D10-R3`</small>

---

### 🟢 `dp_proc009` — Written Insurer Decision Received with Deadline Notice
**Finnish:** Kirjallinen päätös annettu muutoksenhakuajan ilmoittamisen kanssa  **Legal basis:** §65(1), §79(1)  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D10

Whether the claimant has received a written insurer decision (kirjallinen päätös) that includes notification of the applicable deadline for requesting LVL Board opinion and/or bringing a court action (§65(1), §79(1)).

**Primary sources:**
- **src_insurer_own_system** — Document dispatch log confirms written decision was sent.

<small>Rules: `D10-R1`</small>

---

### 🟢 `dp_proc010` — Final Court Judgment Already Given on the Matter
**Finnish:** Tuomioistuimen lainvoimainen ratkaisu annettu  **Legal basis:** §65(2)  **Type:** boolean  **Automation:** 🟢 Full Auto  **Used in decisions:** D10

Whether a final, binding court judgment (lainvoimainen ratkaisu) has already been given on the compensation matter. If so, LVL Board may not consider that aspect of the case (§65(2)).

**Primary sources:**
- **src_tuomioistuimet** — Court registry confirms whether a final judgment has been entered.

<small>Rules: `D10-R1` · `D10-R4`</small>

---

### 🟢 `dp_proc011` — Months Elapsed Since Accident
**Finnish:** Vahingosta kulunut aika kuukausina  **Legal basis:** §45(3)  **Type:** integer  **Automation:** 🟢 Full Auto  **Used in decisions:** D12

The number of months that have elapsed since the accident. Used to trigger the 2-month deadline after which LVK acts as compensation body when the foreign ETA insurer has not been identified (§45(3)).

**Primary sources:**
- **src_insurer_own_system** — Calculated from accident date (from accident report) to current date.
- **src_poliisi_accident_report** — Accident date.

<small>Rules: `D12-R2`</small>

---

## ↩️ Subrogation

*3 data points — 🟡 1 Human Review · 🔴 1 Human Decision · 🟢 1 Full Auto*

### 🟡 `dp_s001` — Third Party Type (Recourse Target)
**Finnish:** Takautumisoikeuden kohteen tyyppi  **Legal basis:** §73, §74  **Type:** enum  **Automation:** 🟡 Human Review  **Used in decisions:** D14

**Allowed values:** `private_individual` · `employee_or_civil_servant` · `vehicle_owner_keeper_driver_passenger` · `company_or_organization` · `national_guarantee_fund_ETA` · `foreign_compensation_body_ETA`

The legal category of the party against whom the insurer or LVK seeks recourse under §73–74. Determines applicable recourse conditions (fault threshold, etc.).

**Primary sources:**
- **src_insurer_own_system**
- **src_lvk_database**
- **src_fiva** — For company/insurer identification.

<small>Rules: `D14-R1` · `D14-R2` · `D14-R3` · `D14-R4` · `D14-R5`</small>

---

### 🔴 `dp_s002` — Basis of Third Party's Causation
**Finnish:** Kolmannen osapuolen syyllisyyden peruste  **Legal basis:** §73  **Type:** enum  **Automation:** 🔴 Human Decision  **Used in decisions:** D14

**Allowed values:** `intent` · `gross_negligence` · `driving_under_severe_alcohol_influence` · `ordinary_negligence_or_strict`

The legal basis on which the third party caused the insured event. Determines whether recourse is available against private individuals (§73: only intent, gross negligence, or severe alcohol driving).

> **Note:** Intent and gross negligence are mental state determinations requiring human legal assessment. Severe alcohol driving (BAC ≥ 1.2‰) is objectively measurable from police test results.

**Primary sources:**
- **src_poliisi_accident_report** — Police report and criminal proceedings findings.

**Secondary / fallback sources:**
- **src_insurer_own_system** — Insurer legal team's fault assessment.
- **src_tuomioistuimet** — Criminal conviction for intoxicated driving or intentional damage.

<small>Rules: `D14-R1` · `D14-R2`</small>

---

### 🟢 `dp_s003` — Recovery Context — Basis of LVK Payment
**Finnish:** Takautumisperusteen konteksti — LVK:n maksamisen peruste  **Legal basis:** §73, §74  **Type:** enum  **Automation:** 🟢 Full Auto  **Used in decisions:** D14

**Allowed values:** `LVK_paid_for_uninsured_vehicle` · `LVK_paid_for_unknown_vehicle` · `LVK_paid_because_no_insurer_identified` · `LVK_paid_insurer_insolvency` · `insurer_paid_and_subrogates`

The legal basis on which LVK or the insurer made the original payment that gives rise to the recourse claim. Determines which §74 sub-rule applies and who the recourse target is.

**Primary sources:**
- **src_lvk_database** — LVK payment records identify the legal basis of each payment.
- **src_insurer_own_system**

<small>Rules: `D14-R1` · `D14-R2` · `D14-R3` · `D14-R4` · `D14-R5` · `D14-R6`</small>

---
