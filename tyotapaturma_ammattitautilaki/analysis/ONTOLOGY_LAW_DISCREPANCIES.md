# Työtapaturma- ja ammattitautilaki Ontology vs Law Analysis
## Discrepancies Found by MerriMoltBot

### 1. [CRITICAL] Section 33 - RepetitiveStrainInjury Reference Error

**Ontology claim:** RepetitiveStrainInjury - Section 33 - Maximum 6 weeks
**DMN claim:** RepetitiveStrainInjury - Section 33

**Actual Law Section 33:**
The law Section 33 covers "Yksipuolinen kuormitus" (Unilateral Loading), but the content in ontology doesn't match the actual law text.

**Impact:** Wrong section reference throughout

---

### 2. [HIGH] Section 34 - ViolenceDamage vs Psychological Injury Mismatch

**Ontology claim:** ViolenceDamage - Section 34
**Expected:** Work-related violence incidents

**Actual Law Section 34:**
"Psyykkinen vamma" (Psychological Injury)
- Acute stress reaction
- PTSD
- Personality changes
- Must be related to work duties

**NOT ViolenceDamage**

**Impact:** Complete mislabeling of Section 34

---

### 3. [HIGH] Section 35 - PsychologicalShock vs Unilateral Loading Mismatch

**Ontology claim:** PsychologicalShock - Section 35
**Subclasses:** AcuteStressReaction, PTSD, PersonalityChange

**Actual Law Section 35:**
"Yksipuolinen kuormitus" (Unilateral Loading / Repetitive Strain)
- Maximum 6 weeks compensation
- Epicondylitis, bursitis, etc.

**NOT PsychologicalShock**

**Impact:** Section 35 is completely mislabeled

---

### 4. [MEDIUM] Section 28 - DMN Includes Conditions Not in Law

**DMN Rule Section 28(1) lists:**
- ✓ Tendinitis (in law)
- ✓ CarpalTunnelSyndrome (in law)
- ✗ Epicondylitis (NOT in law Section 28)
- ✗ Bursitis (NOT in law Section 28)
- ✗ VibrationDisease (NOT in law Section 28)
- ✗ NoiseInducedHearingLoss (NOT in law Section 28)

**Actual Law Section 28:**
Only mentions:
1. Tendinitis
2. Carpal tunnel syndrome

---

### Summary of Issues

| Issue | Severity | Location | Problem |
|-------|----------|----------|---------|
| Section 33 reference | CRITICAL | Ontology + DMN | Wrong content |
| Section 34 label | HIGH | Ontology | ViolenceDamage ≠ Psychological Injury |
| Section 35 label | HIGH | Ontology | PsychologicalShock ≠ Unilateral Loading |
| Section 28 content | MEDIUM | DMN | Extra conditions not in law |

---

*Analysis completed by MerriMoltBot on 2026-02-27*
