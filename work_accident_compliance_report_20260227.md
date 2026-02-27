# Finnish Work Accident Law Compliance Check Report
**Date:** February 27, 2026  
**Law:** Työtapaturma- ja ammattitautilaki (459/2015)  
**Ontology:** tyotapaturma_ammattitautilaki/ontology/work_accident_ontology.md  
**Checked by:** VilleMoltBot

---

## Executive Summary

The compliance analysis of the Finnish Work Accident and Occupational Disease Insurance Ontology against the Työtapaturma- ja ammattitautilaki (459/2015) identified **3 CRITICAL discrepancies** and **4 MEDIUM/HIGH priority gaps** requiring immediate attention.

### Severity Summary
| Severity | Count | Issues |
|----------|-------|--------|
| **CRITICAL** | 3 | Wrong filing deadline, Wrong daily allowance limit, Missing employer insurance threshold |
| **HIGH** | 2 | Missing state employer exception, Missing psychological shock conditions |
| **MEDIUM** | 2 | Missing §35 PTSD timing condition, Missing haittaraha calculation formula |

---

## Critical Discrepancies (CRITICAL)

### Issue #1: WRONG CLAIM FILING DEADLINE (CRITICAL)
**Ontology Section:** Section 5 - Key Relationships

**What Ontology Says:**
> "InjuredParty | must_file_claim_within | 1 year | From date of knowledge of injury and compensability"
> "InjuredParty | must_file_claim_within | 10 years | Absolute maximum from accident/disease date"

**What Law Says (§116):**
> "Korvausasia on saatettava vireille vakuutuslaitoksessa **viiden vuoden kuluessa vahinkopäivästä**. Jos kyse on ammattitautiasiasta, määräaika lasketaan kuitenkin päivästä, jolloin lääkäri on ensimmäisen kerran arvioinut sairauden johtuvan työstä."

**Translation:** Claim must be filed within **5 years** from accident date (not 1 year). For occupational diseases, from when doctor first assessed work-relatedness.

**Discrepancy:**
- Ontology: 1 year from knowledge + 10 year absolute
- Law: 5 years from accident date

**Impact:** This is a FUNDAMENTAL ERROR that could mislead claimants into missing their filing deadline. The 1-year deadline mentioned in ontology does NOT exist in the law.

**Law Reference:** §116 (15 luku - Korvausasian vireille saattamista koskeva määräaika)

---

### Issue #2: WRONG DAILY ALLOWANCE DURATION (CRITICAL)
**Ontology Section:** Section 4 - DailyAllowance

**What Ontology Says:**
> "Duration: First 28 days at sick pay level (employer pays), then based on annual earnings (vuosityöansio)"
> "**Not limited to 1 year** - continues as long as work incapacity exists"

**What Law Says (§56):**
> "Vahingoittuneella on oikeus päivärahaan **yhden vuoden ajan vahinkopäivästä lukien**, jos hän on vahingon johdosta kykenemätön tekemään työtään kokonaan tai osittain."

**Translation:** Right to daily allowance for **one year** from accident date if unable to work.

**What Law Says (§63):**
> "Vahingoittuneella on oikeus tapaturmaeläkkeeseen **vahinkopäivän vuosipäivästä alkaen**..."

**Translation:** Right to accident pension (disability pension) from the anniversary of accident date.

**Discrepancy:**
- Ontology: Daily allowance "not limited to 1 year"
- Law: Daily allowance limited to exactly 1 year (§56), then converts to disability pension (§63)

**Impact:** This misrepresents the compensation structure. After 1 year, daily allowance ends and disability pension begins.

**Law Reference:** §56 (10 luku - Oikeus päivärahaan), §63 (10 luku - Oikeus tapaturmaeläkkeeseen)

---

### Issue #3: MISSING EMPLOYER INSURANCE THRESHOLD (CRITICAL)
**Ontology Section:** Section 2 - MandatoryInsurance (missing)

**What Law Says (§3(2)):**
> "Työnantajalla ei ole vakuuttamisvelvollisuutta, jos työnantajan kalenterivuoden aikana teettämästään työstä maksamat tai maksettavaksi sovitut palkat ovat yhteensä enintään **1 200 euroa**."

**Translation:** No insurance obligation if employer's annual payroll is max €1,200.

**What Law Says (§3(3)):**
> "Valtiolla ei ole vakuuttamisvelvollisuutta, vaan korvaus valtion työssä aiheutuneen työtapaturman tai ammattitaudin johdosta maksetaan valtion varoista..."

**Translation:** State employers are exempt; compensation paid from state funds (via Valtiokonttori).

**Discrepancy:**
- Ontology: No mention of €1,200 payroll threshold for exemption
- Ontology: No mention of state employer exemption

**Impact:** Insurance obligation rules are incomplete. Small employers and state employees have different rules.

**Law Reference:** §3 (1 luku - Työnantajan vakuuttamisvelvollisuus)

---

## High Priority Gaps (HIGH)

### Issue #4: MISSING PSYCHOLOGICAL SHOCK CONDITIONS (HIGH)
**Ontology Section:** Section 3 - PsychologicalShock

**What Ontology Says:**
> "PsychologicalShock: Legal Basis: Section 35, Subclasses: AcuteStressReaction, PTSD, PersonalityChange"

**What Law Says (§35(2)):**
> "Traumaperäisen stressihäiriön ja tuhoisaa kokemusta seuraavan persoonallisuuden muutoksen korvaaminen edellyttää, että vahingoittuneella on todettu traumaperäiseen stressihäiriöön sopiva oireisto **kuuden kuukauden kuluessa tapahtumasta**."

**Translation:** PTSD and personality change compensation requires diagnosis within **6 months** of event.

**What Law Says (§35(3)):**
> "Vahingoittunut on ollut **välittömästi osallisena** 1 momentissa tarkoitetussa tapahtumassa..."

**Translation:** Must be **directly involved** in the event.

**Discrepancy:**
- Ontology: Lists the types but omits critical conditions:
  - 6-month diagnosis requirement for PTSD/personality change
  - Direct involvement requirement
  - Exclusions for recreational activities (§35(4))

**Law Reference:** §35 (7 luku - Henkinen järkytysreaktio työtapaturman seurauksena)

---

### Issue #5: MISSING STATE EMPLOYER INSTITUTION (HIGH)
**Ontology Section:** Section 6 - Institutions

**What Ontology Lists:**
- InsuranceCompany (§205)
- StateTreasury (Valtiokonttori) (§207)
- AccidentInsuranceCentre (Tapaturmavakuutuskeskus) (§§209-225)
- ClaimAppealBoard (§§226-228)

**What's Missing:**
The ontology lists Valtiokonttori (State Treasury) but doesn't clearly explain its role as the **payer for state employees** who are exempt from mandatory insurance.

**What Law Says (§3(3)):**
State employees are NOT covered by mandatory insurance; Valtiokonttori pays compensation directly from state funds.

**Impact:** The distinction between private sector (insurance company) and public sector (Valtiokonttori) claims is not clear.

**Law Reference:** §3(3), §207

---

## Medium Priority Gaps (MEDIUM)

### Issue #6: MISSING HAITTARAHA CALCULATION FORMULA (MEDIUM)
**Ontology Section:** Section 4 - PermanentDamageCompensation

**What Ontology Says:**
> "PermanentDamageCompensation: Classes: 1-20 based on severity"

**What's Missing:**
The specific calculation formula for combining multiple injuries is not included:

**What Law Says (§84(4)):**
```
A x B
K = A + B - --------
      20
```
Where K = total disability class, A = larger injury class, B = smaller injury class

**Law Reference:** §84 (11 luku - Haittaluokan määrittäminen)

---

### Issue #7: MISSING REPETITIVE STRAIN INJURY LIMIT (MEDIUM)
**Ontology Section:** Section 3 - RepetitiveStrainInjury

**What Ontology Says:**
> "RepetitiveStrainInjury: Legal Basis: Section 33, Note: Maximum 6 weeks compensation"

**Verification:** ✓ Correct. §33 states:
> "Korvausta maksetaan...enintään kuuden viikon ajalta kipeytymisestä lukien."

However, the ontology is missing the **exclusion conditions**:
- Not compensated if due to pre-existing injury/disease
- Not compensated if tissue damage could only occur from accident

**Law Reference:** §33 (7 luku - Työliikekipeytyminen)

---

## Correct Elements (VERIFIED ✓)

The following ontology elements correctly reflect the law:

| Ontology Element | Law Section | Status |
|------------------|-------------|--------|
| Investigation within 7 business days | §119 | ✓ Correct |
| Rehabilitation assessment within 3 months | §120 | ✓ Correct |
| Licensed physician must participate | §121 | ✓ Correct |
| Parties: injured party and survivors only | §117 | ✓ Correct |
| Employer is NOT a party | §117 | ✓ Correct |
| Close relative can represent | §118 | ✓ Correct |
| 28 days employer-paid sick leave | §58 | ✓ Correct |
| 10% minimum for disability pension | §63 | ✓ Correct |
| Haittaraha classes 1-20 | §§83-87 | ✓ Correct |
| Perusmäärä €12,440 | §86 | ✓ Correct |
| Minimum vuosityöansio €13,680 | §79 | ✓ Correct |

---

## Recommendations for @VilleMoltBot

### Immediate Action Required (Critical)

1. **FIX Issue #1:** Change filing deadline from "1 year / 10 years" to "5 years from accident date"
   - File: `tyotapaturma_ammattitautilaki/ontology/work_accident_ontology.md`
   - Section: 5. Key Relationships

2. **FIX Issue #2:** Correct daily allowance duration
   - Current: "Not limited to 1 year"
   - Correct: "Limited to 1 year from accident date, then converts to disability pension"

3. **ADD Issue #3:** Include employer exemptions
   - Add €1,200 annual payroll threshold for exemption
   - Clarify state employer exemption and Valtiokonttori's role

### Short-term Fixes (High/Medium)

4. **ENHANCE Issue #4:** Add psychological shock conditions
   - 6-month diagnosis requirement for PTSD
   - Direct involvement requirement
   - Activity exclusions

5. **CLARIFY Issue #5:** State employer vs private sector distinction

6. **ADD Issue #6:** Haittaraha combination formula

---

## GitHub Issues to Create

Based on this analysis, the following issues should be created:

| Issue | Title | Severity | Section |
|-------|-------|----------|---------|
| #1 | [CRITICAL] Wrong claim filing deadline - should be 5 years not 1 year | Critical | §116 |
| #2 | [CRITICAL] Daily allowance IS limited to 1 year | Critical | §56 |
| #3 | [CRITICAL] Missing €1,200 employer exemption threshold | Critical | §3 |
| #4 | [HIGH] Missing psychological shock 6-month diagnosis requirement | High | §35 |
| #5 | [MEDIUM] Add haittaraha combination formula | Medium | §84 |

---

## Law Sections Referenced

| Chapter | Sections | Topic |
|---------|----------|-------|
| 1 luku | §§1-7 | General provisions |
| 2 luku | §§8-12 | Personal scope |
| 3 luku | §§13-14 | Territorial scope |
| 5 luku | §§17-25 | Work accidents |
| 6 luku | §§26-32 | Occupational diseases |
| 7 luku | §§33-35 | Special injuries |
| 8 luku | §§36-49 | Medical care |
| 9 luku | §§50-54 | Other costs |
| 10 luku | §§55-82 | Income loss compensation |
| 11 luku | §§83-87 | Permanent disability |
| 12 luku | §§88-98 | Rehabilitation |
| 13 luku | §§99-109 | Death compensation |
| 14 luku | §§110-116 | Claim procedures |
| 15 luku | §§117-118 | Parties |
| 16 luku | §§119-121 | Processing rules |

---

*Report generated by: VilleMoltBot  
Date: February 27, 2026  
Ontology Version: 1.0  
Law Version: 459/2015 (effective 2016-01-01)*
