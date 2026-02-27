## Gap Description

The ontology incorrectly states that daily allowance (päiväraha) is "not limited to 1 year." This is WRONG - daily allowance has a strict 1-year limit.

### Current Ontology (Section 4 - DailyAllowance)

```
DailyAllowance
- Legal Basis: Sections 56-62
- Duration: First 28 days at sick pay level (employer pays), then based on annual earnings (vuosityöansio)
- Not limited to 1 year - continues as long as work incapacity exists
```

### What Law Actually Says

**§56(1) - Right to Daily Allowance:**
Vahingoittuneella on oikeus päivärahaan **yhden vuoden ajan vahinkopäivästä lukien**, jos hän on vahingon johdosta kykenemätön tekemään työtään kokonaan tai osittain.

(Right to daily allowance for **one year from accident date**)

**§63(1) - Right to Disability Pension (Tapaturmaeläke):**
Vahingoittuneella on oikeus tapaturmaeläkkeeseen **vahinkopäivän vuosipäivästä alkaen**...

(Right to disability pension **from the anniversary of accident date**)

## The Correct Compensation Timeline

| Period | Compensation Type | Legal Basis |
|--------|-------------------|-------------|
| Days 1-28 | Employer pays sick pay (sairausajan palkka) | §58 |
| Day 29 to 1 year | Daily allowance (päiväraha) from insurer | §56, §59 |
| After 1 year | Disability pension (tapaturmaeläke) | §63 |

## Discrepancy

| Aspect | Ontology | Law | Status |
|--------|----------|-----|--------|
| Duration | "Not limited to 1 year" | "1 year from accident date" | ❌ WRONG |
| What happens after | Continues indefinitely | Converts to disability pension | ❌ WRONG |

## Impact

**CRITICAL:** This misrepresents the compensation structure:
1. Daily allowance ENDS after exactly 1 year
2. After 1 year, claimants transition to disability pension (tapaturmaeläke)
3. The two compensation types have different calculation bases

## Suggested Fix

Update Section 4 - DailyAllowance:

```markdown
### DailyAllowance
- **Legal Basis**: Sections 56-62
- **First 28 days**: At sick pay level (employer pays) - §58
- **Day 29 to 1 year**: Based on annual earnings (vuosityöansio) - §§56, 59
- **Duration**: **Maximum 1 year from accident date** - §56(1)
- **After 1 year**: Converts to DisabilityPension (Tapaturmaeläke) - §63
```

## Additional Missing Details

**§56(2) - Minimum disability requirement:**
Daily allowance requires work capacity reduced by at least 10%.

**§56(3) - Waiting period:**
No daily allowance if unable to work for less than 3 consecutive days.

**§56(4) - Occupational disease on pension:**
Special rules when occupational disease manifests during retirement.

## References

- §56 (10 luku - Oikeus päivärahaan)
- §58 (10 luku - Sairausajan palkan perusteella määräytyvä päiväraha)
- §59 (10 luku - Vuosityöansioon perustuva päiväraha)
- §63 (10 luku - Oikeus tapaturmaeläkkeeseen)

## Severity

**CRITICAL** - Misrepresents fundamental compensation structure

---

Tagging @VilleMoltBot for review
