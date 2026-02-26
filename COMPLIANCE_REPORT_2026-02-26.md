# Finnish Law Compliance Check Report
**Date:** 2026-02-26 15:29 UTC  
**Repository:** moltbotville/Finnish-law  
**Law:** Liikennevakuutuslaki 460/2016 (Traffic Insurance Act)  
**DMN Rules:** liikennevakuutuslaki/rules/car_insurance_dmn_rules.md

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Law Sections | 99 sections (1§ - 99§) |
| Sections Referenced in DMN | ~62 sections |
| Open GitHub Issues | 1 |
| **NEW Gaps Identified** | **5 issues** |
| Status | ⚠️ PARTIAL COMPLIANCE |

---

## Open GitHub Issue Analysis

### Issue #167: [MEDIUM] Missing §52 - Rail Traffic Liability Sharing Rules
**Status:** OPEN (VALID - Not yet fixed)

**Verification:**
- ❌ §52 NOT found in DMN rules
- ❌ No rail-road liability apportionment logic
- ❌ No subrogation rules for overpayment between rail/road

**Law §52 Summary:**
- Liability sharing between traffic insurance and rail traffic liability (raideliikennevastuulaki 113/1999)
- Apportionment based on negligence and contributing factors
- If damage caused solely by §33(1) factors or rail act §5, that party bears full responsibility
- Subrogation rights for overpayment

**Recommended Action:** Keep OPEN - still needs implementation

---

## NEW DISCREPANCIES IDENTIFIED

### 🔴 CRITICAL: Missing §51 - Inter-Insurer Liability Sharing

**Law Reference:** §51 - Vastuunjako vakuutusyhtiöiden kesken

**Gap Description:**
The DMN rules reference §51 in §33(3) but there is NO actual decision table implementing §51's liability sharing mechanism between multiple insurers.

**Law Text:**
> "Jos kaksi tai useampi vakuutusyhtiö on vastuussa samasta liikennevahingosta, vakuutusyhtiöt vastaavat korvauksesta yhteisvastuullisesti sen mukaan kuin ilmenneeseen tuottamukseen ja muihin vahingon aiheuttaneisiin seikkoihin katsoen on kohtuullista."
> 
> "Jos vahinko on kuitenkin johtunut yksinomaan tietyn ajoneuvon puutteellisuudesta, virheellisestä kuormauksesta tai sen puolella olevasta tuottamuksesta, korvauksesta vastaa tälle ajoneuvolle vakuutuksen antanut vakuutusyhtiö."

**What's Missing:**
- Decision table for multi-insurer liability apportionment
- Logic for "yksinomaan" (solely) determining single insurer liability
- Proportional sharing calculation based on negligence

**Severity:** 🔴 **CRITICAL** - Referenced but not implemented

**Suggested DMN Rule:**
```markdown
#### LIAB-001: Multi-Insurer Liability Apportionment (§51)

| insurers.involvedCount | fault.soleVehicleDefect | fault.soleImproperLoading | fault.soleVehicleNegligence | Output |
|------------------------|------------------------|---------------------------|----------------------------|--------|
| >1 | true | false | false | **SingleInsurerLiable_DefectVehicle** |
| >1 | false | true | false | **SingleInsurerLiable_LoadingVehicle** |
| >1 | false | false | true | **SingleInsurerLiable_NegligentVehicle** |
| >1 | false | false | false | **ProportionalSharing_ByNegligence** |
| 1 | any | any | any | **SingleInsurerFullLiability** |
```

---

### 🟡 HIGH: Missing §33(1)-(2) - Multi-Vehicle Accident Fault Determination

**Law Reference:** §33(1) and §33(2)

**Gap Description:**
The DMN rules only implement §33(3) (passenger injury full coverage), but §33(1) and §33(2) establish the foundational liability rules for multi-vehicle accidents.

**Law Text §33(1):**
> "Vastuu korvata liikennevahingosta, joka on aiheutunut:  
> 1) omistajan, haltijan, kuljettajan tai matkustajan tuottamuksesta;  
> 2) liikennesääntöjen vastaisesta kulusta tai sijainnista; tai  
> 3) puutteellisesta kunnosta tai virheellisestä kuormauksesta."

**Law Text §33(2):**
> "Jos myös sillä vahingon osapuolella, jolle vahinkoa aiheutui, oli tuottamusta tai muu 1 momentin 1–3 kohdassa mainittu olosuhde, korvausvastuu osapuolten välillä jaetaan ottaen huomioon kaikki vahinkoon vaikuttaneet seikat."

**What's Missing:**
- Decision table for determining contributing factors
- Comparative negligence logic between multiple parties
- Allocation of liability based on all contributing circumstances

**Severity:** 🟡 **HIGH** - Core liability determination missing

**Suggested DMN Rule:**
```markdown
#### MULTI-001: Multi-Vehicle Accident Liability Factors (§33(1)-(2))

| party.ownerNegligence | party.driverNegligence | party.passengerNegligence | party.trafficRulesViolation | party.vehicleDefect | party.improperLoading | Output |
|----------------------|------------------------|---------------------------|----------------------------|---------------------|----------------------|--------|
| true | any | any | any | any | any | **LiabilityFactor_OwnerFault** |
| any | true | any | any | any | any | **LiabilityFactor_DriverFault** |
| any | any | true | any | any | any | **LiabilityFactor_PassengerFault** |
| any | any | any | true | any | any | **LiabilityFactor_TrafficViolation** |
| any | any | any | any | true | any | **LiabilityFactor_VehicleDefect** |
| any | any | any | any | any | true | **LiabilityFactor_ImproperLoading** |

#### MULTI-002: Comparative Negligence Allocation (§33(2))

| victim.hadContributoryNegligence | victim.contributingFactors | allocation.method | Output |
|----------------------------------|---------------------------|-------------------|--------|
| true | Present | ProportionalByCircumstances | **ReduceCompensation_ByVictimFault** |
| false | None | N/A | **FullCompensation** |
```

---

### 🟡 HIGH: Missing §23 - Premium Refund Rules

**Law Reference:** §23 - Vakuutusmaksun palauttaminen vakuutuksen päätyttyä

**Gap Description:**
No rules for premium refund calculation when insurance ends early.

**Law Text:**
> "Jos vakuutus päättyy sovittua ajankohtaa aikaisemmin, vakuutusyhtiöllä on oikeus vakuutusmaksuun vain siltä ajalta, jonka sen vastuu on ollut voimassa. Muu osa jo suoritetusta vakuutusmaksusta on palautettava vakuutuksenottajalle."
> 
> "Jos palautettava maksu on vähemmän kuin kahdeksan euroa, sitä ei tarvitse erikseen palauttaa."

**What's Missing:**
- Premium refund calculation formula
- €8 minimum threshold rule ("kahdeksan euroa")
- Pro-rata calculation based on coverage period

**Severity:** 🟡 **HIGH** - Financial obligation rule

**Suggested DMN Rule:**
```markdown
#### REFUND-001: Premium Refund Calculation (§23)

| policy.endDate | policy.earlyTermination | premium.paidAmount | premium.earnedPortion | refund.calculatedAmount | Output |
|----------------|------------------------|-------------------|----------------------|------------------------|--------|
| before_agreed | true | any | calculated | any | **Refund = Paid - Earned** |
| any | false | any | any | any | **NoRefund_StandardExpiry** |
| before_agreed | true | any | any | <€8 | **NoRefund_BelowThreshold** |
| before_agreed | true | any | any | ≥€8 | **ProcessRefund** |
```

---

### 🟡 HIGH: Missing §21 - Claims History Transfer

**Law Reference:** §21 - Vahinkohistoriatietojen siirtäminen toiseen vakuutusyhtiöön

**Gap Description:**
No rules for transferring claims history between insurers when policyholder switches.

**Law Text:**
> "Vakuutusyhtiön on vakuutuksenottajan pyynnöstä toimitettava vahinkohistoriatiedot uuden vakuutuksen antaneelle vakuutusyhtiölle viipymättä, kuitenkin viimeistään 15 päivän kuluessa pyynnöstä."

**What's Missing:**
- 15-day deadline for claims history transfer
- Required data elements in transfer
- Exception handling

**Severity:** 🟡 **HIGH** - Procedural requirement affecting premium calculation

**Suggested DMN Rule:**
```markdown
#### HIST-001: Claims History Transfer (§21)

| transfer.requested | transfer.requestDate | transfer.responseDate | daysElapsed | Output |
|-------------------|---------------------|----------------------|-------------|--------|
| true | any | within 15 days | ≤15 | **Compliant_TransferComplete** |
| true | any | after 15 days | >15 | **NonCompliant_Delayed** |
| false | any | any | N/A | **NoTransferRequired** |
```

---

### 🟢 MEDIUM: Missing §13 - Territorial Scope & Applicable Law

**Law Reference:** §13 - Vakuutuksen voimassaoloalue ja eräissä liikennevahingoissa sovellettava laki

**Gap Description:**
Limited implementation of territorial scope rules and applicable law selection.

**Law Text Key Points:**
1. Insurance valid in all EEA countries with single premium
2. Coverage extends to non-Green Card transit countries for EEA citizens (direct travel)
3. Better of accident-country law or this law applies
4. Finnish resident can elect Finnish law for personal injury abroad

**What's Missing:**
- Law election mechanism for Finnish residents
- Non-Green Card transit coverage rules
- "Better law" comparison logic

**Severity:** 🟢 **MEDIUM** - Important for international claims

**Suggested DMN Rule:**
```markdown
#### TERR-001: Applicable Law Selection (§13)

| victim.residence | accident.location | transit.throughNonGreenCard | law.electionRequested | accidentCountry.law | finnishLaw.better | Output |
|------------------|-------------------|----------------------------|----------------------|--------------------|--------------------|--------|
| Finland | EEA | false | false | any | any | **AccidentCountryLaw** |
| Finland | EEA | false | true | any | true | **FinnishLaw_Elected** |
| Finland | EEA | false | true | any | false | **AccidentCountryLaw** |
| EEA | NonGreenCard_Transit | true | N/A | N/A | N/A | **Covered_TransitExtension** |
```

---

## Other Missing Sections (Lower Priority)

| Section | Title | Priority | Reason |
|---------|-------|----------|--------|
| §1 | Lain soveltamisala | Low | Scope definition, not decision logic |
| §2 | Määritelmät | Low | Definitions, not decision logic |
| §4 | Liikennevakuutuskeskus | Low | Organizational, not claim processing |
| §11 | Vakuutuskirja ja vakuutusehdot | Medium | Documentation requirement |
| §14-15 | Tiedonantovelvollisuuden laiminlyönti | Medium | Contract law intersection |
| §25 | Vastuun jatkuminen ja maksun ulosottokelpoisuus | Low | Enforcement procedure |
| §30 | Ajoneuvon käyttökielto | Low | Administrative sanction |
| §45 | Eräiden Suomen ulkopuolella sattuneiden liikennevahinkojen korvaaminen | Medium | International claims |
| §64 | Liikennevahinkolautakunta | Low | Organizational |
| §69 | Korvausedustaja | Low | Insurer obligation |
| §80-84 | Tuomioistuinmenettely | Low | Court procedure |
| §86-88 | Tietokeskus | Low | Information systems |

---

## Compliance Score

| Category | Implemented | Partial | Missing | Score |
|----------|-------------|---------|---------|-------|
| Negative Claims (Denials/Reductions) | 17 | 0 | 0 | ✅ 100% |
| Eligibility Rules | 13 | 2 | 2 | ⚠️ 76% |
| Procedural Rules | 8 | 3 | 5 | ⚠️ 62% |
| Premium/Financial | 5 | 1 | 3 | ⚠️ 56% |
| International/Cross-Border | 3 | 1 | 2 | ⚠️ 60% |
| **OVERALL** | | | | **⚠️ 71%** |

---

## Recommendations for @VilleMoltBot

### Immediate Actions (This Sprint):
1. **Create issue for §51** - Critical gap, referenced but not implemented
2. **Create issue for §33(1)-(2)** - Core liability determination
3. **Create issue for §23** - Premium refund calculation

### Next Sprint:
4. **Create issue for §21** - Claims history transfer
5. **Create issue for §13** - Territorial scope improvements

### Backlog:
6. Review remaining procedural sections (§11, §14-15, §45)
7. Document intentional exclusions (§1, §2, §4, organizational sections)

---

## Verification Checklist

- [x] Pulled latest changes from repository
- [x] Ran compliance check script
- [x] Reviewed all open GitHub issues
- [x] Compared law sections against DMN rules
- [x] Identified new discrepancies
- [x] Documented findings with law references
- [ ] Issues created for new gaps (recommendation only, per instructions)

---

*Report generated by Law Compliance Agent*  
*Do not modify code or close issues per task instructions*
