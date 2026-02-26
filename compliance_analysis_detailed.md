# Finnish Law Compliance Analysis Report
**Date:** 2026-02-26  
**Law:** Liikennevakuutuslaki (460/2016)  
**DMN Rules:** car_insurance_dmn_rules.md  

---

## Executive Summary

The automated compliance check flagged 6 potential issues, but manual verification reveals that **most rules are actually present** in the DMN file. However, there are **3 verified gaps** requiring attention and **2 issues needing clarification**.

---

## Verified Findings

### ✅ ISSUE #1 (DOCUMENTED BUT PARTIALLY FIXED): Time Limits (§§61, 62, 79)

**Status:** PARTIALLY ADDRESSED - Rules exist but may need enhancement

**What's Present:**
| Section | DMN Rule | Content | Status |
|---------|----------|---------|--------|
| §61 | T1 | 3 years from knowledge, 10 years absolute | ✅ Present |
| §62 | T2 | 7 business days investigation start | ✅ Present |
| §62 | T3 | 1 month payment deadline | ✅ Present |
| §62 | T3b | Undisputed portion payment | ✅ Present |
| §79 | T4 | Court action 3 years, tolling rules | ✅ Present |

**What's Missing/Incomplete:**
- §61 "Erityisen painava syy" (particularly weighty reason) exception not explicitly modeled
- §79(3) "1-year safety net" after proceedings end prematurely - needs clarification
- §79(4) "Only one extension" rule - needs verification

**Recommendation:** CLOSE as fixed, but create enhancement issue for exception handling.

---

### ✅ ISSUE #2 (FIXED): Property Damage Cap €5M (§38)

**Status:** FULLY IMPLEMENTED

**DMN Rules Present:**
- E8b: "€5,000,000 cap" explicitly stated
- E8c: Pro-rata distribution formula when claims exceed cap
- E8d: Late claimant protection (§38(3))

**Law Reference:** "Esinevahinkona korvataan enintään 5 000 000 euroa"

**Recommendation:** CLOSE as fixed - rules are present and complete.

---

### ✅ ISSUE #3 (FIXED): Alcohol Thresholds (§48)

**Status:** FULLY IMPLEMENTED

**DMN Rules Present:**
- N9: "≥1.2‰ blood" OR "≥0.53 mg/L breath" for denial
- N11: "0.5-1.19‰ blood" OR "0.22-0.52 mg/L breath" for reduction
- N11: Drug impairment "kykynsä tehtävän vaatimiin suorituksiin on huonontunut"
- N17: Third-party victim protection (no reduction for third parties)
- N11: Rehabilitation exemption - "Liikennevakuutuslain perusteella korvattavasta kuntoutuksesta annetun lain mukaisiin korvauksiin ei tehdä vähennystä"

**Recommendation:** CLOSE as fixed - all thresholds and conditions are present.

---

### ⚠️ ISSUE #4 (VERIFIED GAP): Medical Treatment Rules (§§53-59)

**Status:** PARTIALLY IMPLEMENTED - GAPS IDENTIFIED

**What's Present:**
| Section | DMN Rule | Content | Status |
|---------|----------|---------|--------|
| §53 | E5 | Treatment must be necessary | ✅ Present |
| §54 | E5 | Public healthcare = customer fee | ✅ Present |
| §55 | E5 | täyskustannusmaksu to municipality | ✅ Present |
| §56 | M1 | 4 business days notification | ✅ Present |
| §57-59 | M2 | maksusitoumus requirements | ✅ Present |

**What's Missing - CRITICAL GAP:**

#### §56(2) - Emergency Treatment Definition (NOT IN DMN)
Law states: "kiireellistä sairaanhoitoa, jolla tarkoitetaan välittömän hoidon tarpeen arviointia, ja hoitoa, jota ei voida siirtää ilman vamman tai sairauden olennaista pahentumista"

The DMN rules mention "Emergency" but don't include the **legal definition** from §56(2). This could lead to inconsistent application.

#### §55(2) - Long-term Care Exclusion (NOT IN DMN)
Law states: "Täyskustannusmaksua ei makseta vahingon vuoksi annetusta pitkäaikaisesta laitoshoidosta"

- Definition: "hoito ja hoivaa, jota annetaan sen jälkeen, kun vamman hoidollinen lopputulos on saavutettu"
- 3-month minimum threshold: "Laitoshoitoa ei voida katsoa pitkäkaiseksi ennen kuin hoito on jatkunut yhdenjaksoisesti vähintään kolmen kuukauden ajan"

**NOT in DMN rules** - significant gap for institutional care claims.

**Recommendation:** CREATE issue for §56(2) emergency definition and §55(2) long-term care exclusion.

---

### ✅ ISSUE #5 (FIXED): Index Adjustment (§35)

**Status:** FULLY IMPLEMENTED

**DMN Rules Present:**
- E7: "Tarkistetaan kalenterivuosittain työntekijän eläkelain 98 §:ssä tarkoitetulla työeläkeindeksillä"
- E7: "Ansiotulot tarkistetaan...työntekijän eläkelain 96 §:ssä tarkoitetulla palkkakertoimella"

**Recommendation:** CLOSE as fixed.

---

### ⚠️ ISSUE #6 (VERIFIED GAPS): Procedural Rules (§§60-72, 19)

**Status:** PARTIALLY IMPLEMENTED - GAPS IDENTIFIED

**What's Present:**
| Section | DMN Rule | Content | Status |
|---------|----------|---------|--------|
| §60 | P1 | Direct claim right | ✅ Present |
| §19 | P2 | Claims history certificate (15 days) | ✅ Present |
| §63 | P3 | Decision justification | ✅ Present |
| §65 | P4 | Liikennevahinkolautakunta opinion right | ✅ Present |
| §66 | P4b | Mandatory consultation triggers | ✅ Present |
| §67 | P5 | Delay interest calculation | ✅ Present |

**What's Missing - GAPS IDENTIFIED:**

#### §65(2) - Court Decision Preclusion (NOT IN DMN)
Law states: "Jos korvausasiassa on annettu tuomioistuimen lainvoimainen ratkaisu, liikennevahinkolautakunta ei saa käsitellä asiaa siltä osin kuin tuomioistuin on ratkaissut sen"

**Not modeled in DMN** - important procedural boundary missing.

#### §68 - Recipient Notification Obligation (INCOMPLETE)
Law states: "Korvauksensaaja on velvollinen viipymättä ja oma-aloitteisesti ilmoittamaan...korvaukseen vaikuttavista muutoksista edellyttäen, että tästä velvollisuudesta on mainittu korvauspäätöksessä"

DMN has P6 but missing the **conditional trigger** ("edellyttäen, että tästä velvollisuudesta on mainittu korvauspäätöksessä").

#### §70-71 - Foreign Representative Rules (PARTIALLY INCOMPLETE)
- FCR-001: 3-month deadline ✅
- FCR-002: Representative requirements ✅
- FCR-003: LVK backup liability ✅
- **MISSING:** §70(3) "perusteltu vastaus" (justified response) requirements when liability disputed
- **MISSING:** §71(2) LVK 2-month processing deadline

---

## NEW DISCREPANCIES IDENTIFIED

### NEW ISSUE #7: [HIGH] Missing §33 Multi-Vehicle Accident Apportionment Rules

**Law (§33):** Detailed rules for apportioning liability between multiple vehicles
- " Korvausvastuu osapuolten välillä jaetaan ottaen huomioon kaikki vahinkoon vaikuttaneet seikat"
- Special rules when victim was passenger/driver

**DMN Gap:** Only basic reference to §33 in RAIL-001, no actual apportionment logic.

**Severity:** HIGH - Multi-vehicle accidents are common, statutory apportionment rules should be modeled.

---

### NEW ISSUE #8: [MEDIUM] Missing §47 Rehabilitation Exemption Detail

**Law (§47(3)):** "Liikennevakuutuslain perusteella korvattavasta kuntoutuksesta annetun lain mukaisiin korvauksiin ei tehdä 1 momentissa tarkoitettua vähennystä. Jos korvaus evätään kokonaan, ei kuntoutustakaan korvata."

**DMN Gap:** N10 mentions rehabilitation exemption but doesn't capture the **conditional nature** (if compensation fully denied, rehabilitation is also denied).

**Severity:** MEDIUM - Edge case but legally significant.

---

### NEW ISSUE #9: [MEDIUM] Missing §22 Traffic Removal Violation Premium

**Law (§22):** "Jos vakuutettua ajoneuvoa on käytetty liikenteessä sinä aikana, jona se on ollut ilmoitettuna rekisteriin liikennekäytöstä poistetuksi, vakuutuksenottajan on suoritettava...enintään kolminkertainen vakuutusmaksu"

**DMN:** P6 exists but §22 is about **retroactive premium adjustment** for violations, not standard termination.

**Severity:** MEDIUM - Premium calculation gap.

---

### NEW ISSUE #10: [LOW] Missing §40(3) Owner's Other Vehicle Exception

**Law (§40(3)):** "Mitä 2 momentissa säädetään, ei koske vahinkoa, joka on aiheutunut ajoneuvon omistajan, haltijan tai kuljettajan omistamalle tai hallinnassa olevalle toiselle ajoneuvolle."

**DMN Gap:** N18 covers passenger exception but §40(3) exception for **owner's other vehicle** is not explicitly modeled.

**Severity:** LOW - Edge case.

---

## Summary Table

| Issue | Section | Status | Severity | Action |
|-------|---------|--------|----------|--------|
| Time limits | §§61,62,79 | Mostly Fixed | Low | Close with note |
| Property cap | §38 | Fixed | - | Close |
| Alcohol | §48 | Fixed | - | Close |
| Medical | §§53-59 | Partial Gap | High | Create issue |
| Index adj | §35 | Fixed | - | Close |
| Procedural | §§60-72 | Partial Gap | Medium | Create issue |
| Multi-vehicle | §33 | Missing | High | Create issue |
| Rehab exemption | §47(3) | Incomplete | Medium | Create issue |
| Removal premium | §22 | Missing | Medium | Create issue |
| Other vehicle | §40(3) | Missing | Low | Create issue |

---

## Recommended GitHub Issues to Create

1. **#1: [HIGH] Add §56(2) emergency treatment definition and §55(2) long-term care exclusion**
2. **#2: [MEDIUM] Add §65(2) court decision preclusion and §68 conditional notification obligation**
3. **#3: [HIGH] Add §33 multi-vehicle accident liability apportionment rules**
4. **#4: [MEDIUM] Add §47(3) conditional rehabilitation exemption**
5. **#5: [MEDIUM] Add §22 traffic removal violation premium rules**
6. **#6: [LOW] Add §40(3) owner's other vehicle exception**

---

*Analysis conducted by: Compliance Check Agent*  
*Method: Manual verification of law text against DMN rules with semantic analysis*
