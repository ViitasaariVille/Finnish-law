# Finnish Law Compliance Check - GitHub Issues to Create

**Date:** 2026-02-26  
**Reported by:** Compliance Check Agent  
**Analysis:** Detailed comparison of Liikennevakuutuslaki (460/2016) against car_insurance_dmn_rules.md

---

## Summary

- **0 open issues found** (none to verify)
- **6 documented issues analyzed** - most are already FIXED
- **6 new verified gaps identified** - need GitHub issues
- **3 issues can be CLOSED** as fixed
- **3 issues need clarification/enhancement**

---

## Previously Documented Issues Analysis

### Issue #1: [CRITICAL] Missing time limits (§§61, 62, 79)
**STATUS: MOSTLY FIXED** ✅

The DMN rules DO contain time limit rules:
- T1: §61 claim filing (3 years from knowledge, 10 years absolute)
- T2: §62 investigation start (7 business days)  
- T3: §62 payment deadline (1 month)
- T4: §79 court action (3 years, tolling rules)

**Gap:** §61 "erityisen painava syy" exception not explicitly modeled
**Action:** Close with note - core rules present, enhancement possible

---

### Issue #2: [CRITICAL] Missing €5M property damage cap (§38)
**STATUS: FIXED** ✅

DMN rules present:
- E8b: "€5,000,000 cap" explicitly stated
- E8c: Pro-rata distribution formula
- E8d: Late claimant protection

**Action:** Close as fixed

---

### Issue #3: [HIGH] Alcohol thresholds incomplete (§48)
**STATUS: FIXED** ✅

DMN rules present:
- N9: ≥1.2‰ blood OR ≥0.53 mg/L breath for denial
- N11: 0.5-1.19‰ blood OR 0.22-0.52 mg/L breath for reduction
- N11: Drug impairment conditions
- N17: Third-party victim protection

**Action:** Close as fixed

---

### Issue #4: [HIGH] Missing medical treatment rules (§§53-59)
**STATUS: PARTIAL GAP** ⚠️

Present: E5, M1, M2 cover basic requirements
**Missing:**
- §56(2) emergency treatment legal definition
- §55(2) long-term care exclusion (3-month threshold)

**Action:** Keep open - gaps identified

---

### Issue #5: [MEDIUM] Missing index adjustment (§35)
**STATUS: FIXED** ✅

DMN rules present:
- E7: Työeläkeindeksi adjustment
- E7: Palkkakerroin for income adjustment

**Action:** Close as fixed

---

### Issue #6: [MEDIUM] Missing procedural rules (§§60-72, 19)
**STATUS: PARTIAL GAP** ⚠️

Present: P1-P6 cover most requirements
**Missing:**
- §65(2) court decision preclusion
- §68 conditional notification trigger
- §70(3) justified response requirements

**Action:** Keep open - gaps identified

---

## New Verified Gaps - Create GitHub Issues

### NEW ISSUE #1: [HIGH] §56(2) Emergency Treatment Definition & §55(2) Long-term Care

**Body:**
```markdown
## Problem

The DMN rules are missing critical definitions from the medical treatment procedure sections (§§53-59):

### Missing §56(2) - Emergency Treatment Definition
**Law text:**
> "kiireellistä sairaanhoitoa, jolla tarkoitetaan välittömän hoidon tarpeen arviointia, ja hoitoa, jota ei voida siirtää ilman vamman tai sairauden olennaista pahentumista"

**Impact:** Without the legal definition, emergency vs non-emergency treatment classification may be inconsistent, leading to incorrect maksusitoumus requirements.

### Missing §55(2) - Long-term Care Exclusion  
**Law text:**
> "Täyskustannusmaksua ei makseta vahingon vuoksi annetusta pitkäaikaisesta laitoshoidosta. Pitkäaikaisella laitoshoidolla tarkoitetaan hoitoa ja hoivaa, jota annetaan sen jälkeen, kun vamman hoidollinen lopputulos on saavutettu, kuitenkin viimeistään, kun pysyvä haitta voidaan määritellä. Laitoshoitoa ei voida katsoa pitkäaikaiseksi ennen kuin hoito on jatkunut yhdenjaksoisesti vähintään kolmen kuukauden ajan."

**Impact:** The 3-month threshold for long-term institutional care exclusion from täyskustannusmaksu is not modeled. This could lead to overpayment for extended care.

## Suggested Fix

Add to DMN rules:

1. **EMERGENCY-001**: Definition matching §56(2) with conditions:
   - Immediate treatment need assessment required
   - Treatment cannot be postponed without significant worsening

2. **LONGTERM-001**: Long-term care exclusion with:
   - 3-month continuous care threshold
   - Exclusion applies after medical treatment outcome achieved
   - Applies to täyskustannusmaksu calculations

## References
- laws/liikennevakuutuslaki.txt §§55(2), 56(2)
- Current DMN: E5, M1, M2 (incomplete)

---
Severity: HIGH - Affects medical expense calculations
Tagging @VilleMoltBot for review
```

---

### NEW ISSUE #2: [MEDIUM] §65(2) Court Decision Preclusion & §68 Conditional Notification

**Body:**
```markdown
## Problem

Procedural rules have gaps that could lead to incorrect claims handling:

### Missing §65(2) - Court Decision Preclusion
**Law text:**
> "Jos korvausasiassa on annettu tuomioistuimen lainvoimainen ratkaisu, liikennevahinkolautakunta ei saa käsitellä asiaa siltä osin kuin tuomioistuin on ratkaissut sen"

**Current DMN:** P4 mentions opinion rights but not the court decision boundary.

**Impact:** System may allow Liikennevahinkolautakunta consultation on issues already decided by courts.

### Missing §68 Conditional Trigger
**Law text:**
> "Korvauksensaaja on velvollinen viipymättä ja oma-aloitteisesti ilmoittamaan...korvaukseen vaikuttavista muutoksista edellyttäen, että tästä velvollisuudesta on mainittu korvauspäätöksessä"

**Current DMN:** P6 exists but omits the critical condition that the obligation must be stated in the decision.

**Impact:** Notification obligation may be enforced when it wasn't properly established in the decision.

## Suggested Fix

1. Add **COURT-PRECL-001**: Check for existing court decision before Liikennevahinkolautakunta consultation
2. Update **P6**: Add condition `decision.notificationObligationStated == true`

## References
- laws/liikennevakuutuslaki.txt §§65(2), 68

---
Severity: MEDIUM - Procedural edge cases
Tagging @VilleMoltBot for review
```

---

### NEW ISSUE #3: [HIGH] §33 Multi-Vehicle Accident Liability Apportionment

**Body:**
```markdown
## Problem

The DMN rules lack the statutory liability apportionment rules for accidents involving multiple vehicles.

**Law (§33):**
> "Korvausvastuu osapuolten välillä jaetaan ottaen huomioon kaikki vahinkoon vaikuttaneet seikat"

**Key provisions missing:**
1. Apportionment based on all contributing factors (tuottamus, traffic violations, vehicle condition)
2. Special rule when victim was passenger/driver (choose vehicle)
3. Internal recalculation between insurers after initial payment

**Current DMN:** 
- RAIL-001 references §33 for rail accidents only
- No general multi-vehicle apportionment logic

**Impact:** Multi-vehicle accidents (common scenario) cannot be properly apportioned per statute.

## Suggested Fix

Add **MV-001 through MV-003** rules:

### MV-001: Liability Apportionment Factors
| factor.contributing | factor.type | weight |
|---------------------|-------------|--------|
| true | trafficViolation | calculated |
| true | vehicleCondition | calculated |
| true | driverFault | calculated |

### MV-002: Passenger/Driver Special Rule
| victim.wasPassenger | victim.selectedVehicle | primaryInsurer |
|---------------------|----------------------|----------------|
| true | VehicleA | VehicleA.insurer |
| true | VehicleB | VehicleB.insurer |

### MV-003: Inter-Insurer Recalculation
- After initial payment to victim
- Recalculate based on §51 (mutual liability between insurers)

## References
- laws/liikennevakuutuslaki.txt §§33, 51

---
Severity: HIGH - Common scenario, statutory requirement
Tagging @VilleMoltBot for review
```

---

### NEW ISSUE #4: [MEDIUM] §47(3) Conditional Rehabilitation Exemption

**Body:**
```markdown
## Problem

The DMN rules have an incomplete implementation of the rehabilitation exemption condition.

**Law (§47(3)):**
> "Liikennevakuutuslain perusteella korvattavasta kuntoutuksesta annetun lain mukaisiin korvauksiin ei tehdä 1 momentissa tarkoitettua vähennystä. **Jos korvaus evätään kokonaan, ei kuntoutustakaan korvata.**"

**Current DMN:** 
- N10 mentions rehabilitation is exempt from reductions
- Missing the conditional: if compensation is FULLY DENIED, rehabilitation is ALSO denied

**Impact:** Edge case where rehabilitation might be paid even when main compensation is denied.

## Suggested Fix

Update **N10** to include:
```
IF compensation.type == Rehabilitation:
    IF mainCompensation.denied == true:
        Output: NOT_COVERED
    ELSE:
        Output: COVERED_100 (no reduction)
```

## References
- laws/liikennevakuutuslaki.txt §47(3)

---
Severity: MEDIUM - Edge case but legally significant
Tagging @VilleMoltBot for review
```

---

### NEW ISSUE #5: [MEDIUM] §22 Traffic Removal Violation Premium

**Body:**
```markdown
## Problem

The DMN rules are missing the traffic removal violation premium calculation.

**Law (§22):**
> "Jos vakuutettua ajoneuvoa on käytetty liikenteessä sinä aikana, jona se on ollut ilmoitettuna rekisteriin liikennekäytöstä poistetuksi, vakuutuksenottajan on suoritettava vakuutusyhtiölle vakuutusehdoissa määritelty enintään kolminkertainen vakuutusmaksu"

**Key elements:**
- Vehicle was removed from traffic (liikennekäytöstä poistettu)
- Vehicle was used during removal period
- Premium multiplier: up to 3x normal premium
- Retroactive calculation from removal start date

**Current DMN:** 
- P6 (TERM-001) covers policy termination
- Missing §22 specific violation premium logic

**Impact:** Cannot calculate retroactive premium adjustments for traffic removal violations.

## Suggested Fix

Add **VIOLATION-001**: Traffic Removal Violation Premium
| vehicle.isRemovedFromTraffic | vehicle.usedDuringRemoval | multiplier |
|------------------------------|---------------------------|------------|
| true | true | 1.0x - 3.0x (based on conditions) |

## References
- laws/liikennevakuutuslaki.txt §22

---
Severity: MEDIUM - Premium calculation gap
Tagging @VilleMoltBot for review
```

---

### NEW ISSUE #6: [LOW] §40(3) Owner's Other Vehicle Exception

**Body:**
```markdown
## Problem

The DMN rules are missing an exception for damage to owner's other vehicles.

**Law (§40(3)):**
> "Mitä 2 momentissa säädetään, ei koske vahinkoa, joka on aiheutunut ajoneuvon omistajan, haltijan tai kuljettajan omistamalle tai hallinnassa olevalle toiselle ajoneuvolle."

**Context:**
- §40(2) excludes damage to owner/holder/driver property
- §40(3) creates exception: damage to their OTHER vehicle IS covered

**Current DMN:** 
- N18 covers passenger clothing/personal items exception
- Missing §40(3) exception for owner's other vehicle

**Impact:** May incorrectly deny claims for damage to owner's other vehicle.

## Suggested Fix

Add to **N18** or create **N18a**:
| property.ownerRelationship | property.type | vehicle.isOtherOwnedVehicle | Output |
|---------------------------|---------------|----------------------------|--------|
| Owner | OtherVehicle | true | **COVERED** |
| Holder | OtherVehicle | true | **COVERED** |

## References
- laws/liikennevakuutuslaki.txt §40(3)

---
Severity: LOW - Edge case
Tagging @VilleMoltBot for review
```

---

## Recommended Actions for @VilleMoltBot

### Close These Issues (Already Fixed):
1. Issue #2 - Property damage cap ✅
2. Issue #3 - Alcohol thresholds ✅  
3. Issue #5 - Index adjustment ✅

### Create These Issues (Verified Gaps):
1. [HIGH] §56(2) Emergency Treatment & §55(2) Long-term Care
2. [MEDIUM] §65(2) Court Preclusion & §68 Conditional Notification
3. [HIGH] §33 Multi-Vehicle Liability Apportionment
4. [MEDIUM] §47(3) Conditional Rehabilitation Exemption
5. [MEDIUM] §22 Traffic Removal Violation Premium
6. [LOW] §40(3) Owner's Other Vehicle Exception

### Keep/Enhance These Issues:
1. Issue #1 - Time limits (enhance exception handling)
2. Issue #4 - Medical treatment (gaps now specified)
3. Issue #6 - Procedural rules (gaps now specified)

---

## Files Referenced
- `laws/liikennevakuutuslaki.txt` - Full law text
- `liikennevakuutuslaki/rules/car_insurance_dmn_rules.md` - DMN rules
- `compliance_check_20260226_165224.md` - Automated check report
- `compliance_analysis_detailed.md` - Detailed analysis

---

*Report generated by: Compliance Check Agent*  
*Date: 2026-02-26*
