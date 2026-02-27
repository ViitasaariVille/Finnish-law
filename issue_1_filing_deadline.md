## Gap Description

The ontology contains a CRITICAL error regarding claim filing deadlines that could mislead claimants.

### Current Ontology (Section 5 - Key Relationships)

```
InjuredParty | must_file_claim_within | 1 year | From date of knowledge of injury and compensability
InjuredParty | must_file_claim_within | 10 years | Absolute maximum from accident/disease date
```

### What Law Actually Says (§116)

**§116(1):** 
Korvausasia on saatettava vireille vakuutuslaitoksessa **viiden vuoden kuluessa vahinkopäivästä**. 

(Claim must be filed within **5 years** from accident date)

**§116(2) - Occupational Disease Exception:**
Jos kyse on ammattitautiasiasta, määräaika lasketaan kuitenkin päivästä, jolloin lääkäri on ensimmäisen kerran arvioinut sairauden johtuvan työstä.

(For occupational diseases, deadline runs from when doctor first assessed work-relatedness)

**§116(2) - Late Filing Exception:**
Korvausasia voidaan saattaa vireille myös 1 momentissa säädetyn määräajan jälkeen, jos vireilletulon viivästyminen ei ole aiheutunut vahingoittuneesta johtuvasta syystä ja korvausoikeuden tutkimatta jättäminen olisi olosuhteet huomioon ottaen kohtuutonta.

(Can file after deadline if delay not claimant's fault and denying claim would be unreasonable)

## Discrepancy Summary

| Aspect | Ontology | Law | Match |
|--------|----------|-----|-------|
| Standard deadline | 1 year from knowledge | 5 years from accident | ❌ WRONG |
| Absolute maximum | 10 years | 5 years | ❌ WRONG |
| Occupational disease | Not specified | From doctor assessment | ❌ MISSING |
| Late filing exception | Not mentioned | Allowed under conditions | ❌ MISSING |

## Impact

**CRITICAL:** Claimants relying on the ontology may:
1. Miss their actual 5-year deadline by waiting too long
2. Incorrectly believe they have 10 years when the actual limit is 5 years
3. Not understand the occupational disease special rule

## Suggested Fix

Update Section 5 - Key Relationships:

```
| Subject | Predicate | Object | Condition |
|---------|-----------|--------|-----------|
| InjuredParty | must_file_claim_within | 5 years | From accident date (§116) |
| InjuredParty | must_file_claim_within | From doctor assessment | Occupational disease only (§116) |
| InjuredParty | may_file_claim_after_deadline | If justified | When delay not claimant's fault (§116) |
```

## References

- Law: §116 (15 luku - Korvausasian vireille saattamista koskeva määräaika)
- Line 747 in tyotapaturma_ammattitautilaki.txt

## Severity

**CRITICAL** - Fundamental procedural requirement

---

Tagging @VilleMoltBot for review
