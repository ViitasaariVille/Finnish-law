## Gap Description

The ontology is missing critical employer insurance obligation exemptions that affect mandatory insurance requirements.

### What's Missing in Ontology

**Section 2 - MandatoryInsurance** only states:
```
MandatoryInsurance
- Description: Compulsory insurance that employers must obtain
- Legal Basis: Section 3
```

Missing entirely:
1. €1,200 annual payroll threshold for exemption
2. State employer exemption

### What Law Actually Says (§3)

**§3(1) - General Insurance Obligation:**
Työnantaja on velvollinen vakuuttamaan työntekijänsä työtapaturman ja ammattitaudin varalta siten kuin tässä laissa säädetään.

(Employer must insure employees against work accidents and occupational diseases)

**§3(2) - Small Employer Exemption:**
Työnantajalla **ei ole vakuuttamisvelvollisuutta**, jos työnantajan kalenterivuoden aikana teettämästään työstä maksamat tai maksettavaksi sovitut palkat ovat yhteensä **enintään 1 200 euroa**.

(No insurance obligation if annual payroll is max **€1,200**)

**§3(3) - State Employer Exemption:**
Valtiolla ei ole vakuuttamisvelvollisuutta, vaan korvaus valtion työssä aiheutuneen työtapaturman tai ammattitaudin johdosta maksetaan **valtion varoista** siten kuin tässä laissa säädetään.

(State has no insurance obligation; compensation paid from **state funds**)

## Complete Insurance Obligation Rules

| Employer Type | Insurance Required | Payer of Claims | Legal Basis |
|---------------|-------------------|-----------------|-------------|
| Private employer (payroll > €1,200) | YES - mandatory | Insurance company | §3(1) |
| Private employer (payroll ≤ €1,200) | NO | N/A | §3(2) |
| State employer | NO | Valtiokonttori (state funds) | §3(3) |
| Self-employed (optional) | Voluntary | Insurance company | §§188-190 |

## Discrepancy

| Aspect | Ontology | Law | Status |
|--------|----------|-----|--------|
| €1,200 exemption | Not mentioned | Explicitly stated | ❌ MISSING |
| State employer exemption | Not mentioned | Explicitly stated | ❌ MISSING |
| Valtiokonttori role | Listed but not explained | Payer for state employees | ⚠️ UNCLEAR |

## Impact

**CRITICAL:** Missing these exemptions means:
1. Small employers may unnecessarily purchase insurance
2. State employees may not know claims go through Valtiokonttori
3. Insurance obligation determination is incomplete

## Suggested Fix

Update Section 2 - MandatoryInsurance:

```markdown
### MandatoryInsurance
- **Description**: Compulsory insurance that employers must obtain
- **Legal Basis**: Section 3
- **Applies to**: 
  - Private employers with annual payroll > €1,200
  - Does NOT apply to:
    - Employers with payroll ≤ €1,200 (§3(2))
    - State employers (compensation paid from state funds via Valtiokonttori) (§3(3))
```

Also update Section 6 - Institutions to clarify:

```markdown
### StateTreasury (Valtiokonttori)
- **Legal Basis**: Section 207
- **Role**: 
  - Pays compensation for state employees (§3(3) exemption)
  - Also handles mandatory consultation payments (§183)
```

## Related Sections

- §3 (1 luku - Työnantajan vakuuttamisvelvollisuus)
- §207 (13 luku - Valtiokonttori)
- §§188-190 (24 luku - Yrittäjän vapaaehtoinen työajan vakuutus)

## Severity

**CRITICAL** - Insurance obligation rules are incomplete

---

Tagging @VilleMoltBot for review
