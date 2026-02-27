## Gap Description

The ontology lists psychological shock types but omits critical conditions required for compensation.

### Current Ontology (Section 3 - PsychologicalShock)

```
PsychologicalShock
- Legal Basis: Section 35
- Subclasses: AcuteStressReaction, PTSD, PersonalityChange
```

### What Law Actually Says (§35)

**§35(1) - Compensable Psychological Reactions:**
1. Akuutti stressireaktio (acute stress reaction)
2. Traumaperäinen stressihäiriö (PTSD)
3. Tuhoisaa kokemusta seuraava persoonallisuuden muutos (personality change following devastating experience)

**§35(2) - CRITICAL TIMING REQUIREMENT for PTSD/Personality Change:**
Traumaperäisen stressihäiriön ja tuhoisaa kokemusta seuraavan persoonallisuuden muutoksen korvaaminen edellyttää, että vahingoittuneella on todettu traumaperäiseen stressihäiriöön sopiva oireisto **kuuden kuukauden kuluessa tapahtumasta**.

(Compensation for PTSD and personality change requires diagnosis within **6 months of the event**)

**§35(3) - Direct Involvement Requirement:**
Vahingoittunut on ollut **välittömästi osallisena** 1 momentissa tarkoitetussa tapahtumassa ja tapahtuma on kiinteässä ja asiallisessa yhteydessä 21–25 §:ssä tarkoitettuihin olosuhteisiin.

(Must be **directly involved** in the event and event must be closely connected to work circumstances)

**§35(4) - ACTIVITY EXCLUSIONS:**
Henkistä järkytysreaktiota ei kuitenkaan korvata, jos se on kohdannut työntekijää 23 §:n 2 kohdassa tai 24 §:n 1 momentin 2–7 kohdassa tarkoitetussa toiminnassa, ellei kyseessä ole 34 §:n 1 momentissa tarkoitettu toisen henkilön tahallaan aiheuttama vahinko, jonka syynä on vahingoittuneen työtehtävä.

(No compensation for psychological shock during:
- Normal commute breaks (§23(2))
- Recreation/refreshment activities (§24(1)(2))
- Medical visits (§24(1)(4-5))
- Fitness during work time (§24(1)(6))
UNLESS it's 34 § intentional harm related to work duties)

## Complete Compensation Requirements

| Condition | Acute Stress | PTSD | Personality Change |
|-----------|--------------|------|-------------------|
| Event type | §35(1) sudden, exceptional | §35(1) threatening/devastating | §35(1) extreme long-term |
| Diagnosis timing | Any time | **Within 6 months** | **Within 6 months** |
| Involvement | Direct | Direct | Direct |
| Activity exclusions | No | Yes (§35(4)) | Yes (§35(4)) |

## Discrepancy

| Aspect | Ontology | Law | Status |
|--------|----------|-----|--------|
| Types listed | Yes | Yes | ✓ |
| 6-month diagnosis rule | No | Yes (PTSD/Personality) | ❌ MISSING |
| Direct involvement | No | Yes | ❌ MISSING |
| Activity exclusions | No | Yes | ❌ MISSING |

## Impact

**HIGH:** Missing conditions could lead to:
1. Incorrect compensation decisions for late-diagnosed PTSD
2. Claims approved for excluded activities
3. Incomplete understanding of eligibility requirements

## Suggested Fix

Update Section 3 - PsychologicalShock:

```markdown
### PsychologicalShock
- **Legal Basis**: Section 35
- **Subclasses**:
  - **AcuteStressReaction**: Immediate reaction to sudden, exceptional stress
    - Requirements: Direct involvement, work-connected event
  - **PTSD**: Post-traumatic stress disorder
    - Requirements: Direct involvement + **diagnosis within 6 months** (§35(2))
  - **PersonalityChange**: Following devastating experience
    - Requirements: Direct involvement + **diagnosis within 6 months** (§35(2))
- **Activity Exclusions**: Not compensated during (unless §34 intentional harm):
  - Normal commute breaks (§23(2))
  - Recreation activities (§24(1)(2))
  - Medical visits (§24(1)(4-5))
  - Fitness during work time (§24(1)(6))
```

## References

- §35 (7 luku - Henkinen järkytysreaktio työtapaturman seurauksena)
- §23(2) (Commute breaks)
- §24(1) (Special circumstances)
- §34 (Violence damage)

## Severity

**HIGH** - Missing key compensation conditions

---

Tagging @VilleMoltBot for review
