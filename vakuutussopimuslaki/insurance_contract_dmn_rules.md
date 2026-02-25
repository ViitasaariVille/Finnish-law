# Finnish Insurance Contract Act - DMN Business Rules

**Based on:** Vakuutussopimuslaki (Insurance Contract Act) 543/1994  
**Version:** 1.0  
**Source:** https://www.finlex.fi/fi/lainsaadanto/1994/543

---

## 1. Scope of Act

| **OUTPUT: Applies** | Insurance Type | Legal Basis | Source Text |
|---------------------|----------------|-------------|-------------|
| Excluded | Statutory insurance | Section 1(1) | Lakisääteinen vakuutus |
| Applies per special law | Traffic insurance | Section 1(2) | Liikennevakuutus |
| Applies per special law | Patient insurance | Section 1(2) | Potilasvakuutus |
| Applies per special law | Environmental insurance | Section 1(3) | Ympäristövahinkovakuutus |
| Excluded | Reinsurance | Section 1(4) | Jälleenvakuutus |

---

## 2. Insurance Type Classification

| **OUTPUT: Type** | Subject | Legal Basis | Source Text |
|-----------------|---------|-------------|-------------|
| Life Insurance | Natural person as subject | Section 2(1) | Henkilövakuutus |
| Non-Life Insurance | Property damage | Section 2(2) | Vahinkovakuutus |
| Investment Insurance | With investment component | Section 2(2a) | Sijoitusvakuutus |
| Capital Redemption | No insured person | Section 4a | Kapitalisaatiosopimus |
| Group Insurance | Group members | Section 2(6) | Ryhmävakuutus |

---

## 3. Contractual Terms - Mandatory

| **OUTPUT: Valid** | Term | Legal Basis | Source Text |
|------------------|------|-------------|-------------|
| Void | Against insured | Section 3(1) | Mitätön vakuutetun vahingoksi |
| Void | Against consumer | Section 3(2) | Mitätön kuluttajaa kohtaan |
| Not mandatory | Credit insurance | Section 3(3) | Luottovakuutus |
| Not mandatory | Transport insurance | Section 3(3) | Kuljetusvakuutus |

---

## 4. Pre-Contract Information

| **OUTPUT: Required** | Information | Legal Basis | Source Text |
|---------------------|-------------|-------------|-------------|
| Required | Insurance forms | Section 5(1) | Vakuutusmuodot |
| Required | Premium information | Section 5(1) | Vakuutusmaksut |
| Required | Terms and conditions | Section 5(1) | Vakuutusehdot |
| Required | Policyholder needs | Section 5(1) | Vakuutustarve |
| Required | Investment risks warning | Section 5(2) | Sijoitusriskit |

---

## 5. Information Delivery Method

| **OUTPUT: Allowed** | Method | Legal Basis | Source Text |
|--------------------|--------|-------------|-------------|
| Allowed | Paper | Section 5a(1) | Paperilla |
| Allowed | Durable medium | Section 5a(1) | Pysyvällä tavalla |
| Allowed | Website | Section 5a(1) | Verkkosivustolla |
| Required | On request - paper | Section 5a(3) | Pyynnöstä paperilla |

---

## 6. Policy Document Delivery

| **OUTPUT: Required** | Timing | Legal Basis | Source Text |
|---------------------|--------|-------------|-------------|
| Required | Without undue delay | Section 6(1) | Ilman aiheetonta viivytystä |
| Required | Key terms | Section 6(1) | Sopimuksen keskeinen sisältö |
| Required | Conditions | Section 6(1) | Vakuutusehdot |
| Required | If premium variable | Section 6(2) | Maksun muuttumisoikeus |

---

## 7. Annual Notice Requirement

| **OUTPUT: Required** | Content | Legal Basis | Source Text |
|---------------------|---------|-------------|-------------|
| Required | Annual notice | Section 7(1) | Vuositiedote |
| Required | Insurance sum | Section 7(1) | Vakuutusmäärä |
| Required | Cost information | Section 7(2) | Kulut |
| Required | Suitability assessment | Section 7(3) | Soveltuvuuden arviointi |

---

## 8. Coverage Start

| **OUTPUT: Liability** | Condition | Legal Basis | Source Text |
|----------------------|-----------|-------------|-------------|
| Begins | Offer accepted | Section 11(1) | Hyväksyvä vastaus |
| Begins | Written application | Section 11(2) | Kirjallinen hakemus |
| May require | Premium first | Section 11(3) | Vakuutusmaksu |
| Considered | Representative | Section 11(4) | Edustajalle annettu |

---

## 9. Policyholder Termination Right

| **OUTPUT: Right** | Condition | Legal Basis | Source Text |
|-------------------|-----------|-------------|-------------|
| Yes | Anytime | Section 12(1) | Milloin tahansa |
| Required | Written form | Section 12(1) | Kirjallisesti |
| Ends | Current period | Section 12(1) | Päättyy vakuutuskauden aikana |
| No right | Short period <30 days | Section 12(2) | Alle 30 päivää |

---

## 10. Surrender Value Right

| **OUTPUT: Right** | Condition | Legal Basis | Source Text |
|-------------------|-----------|-------------|-------------|
| Yes | With savings | Section 13(1) | Vapaakirja |
| Yes | With savings | Section 13(1) | Takaisinostoarvo |
| Yes | On ending | Section 13(2) | Päättyessä |
| May exclude | Pension insurance | Section 13(3) | Eläkevakuutus |

---

## 11. Cancellation Right

| **OUTPUT: Right** | Insurance Type | Legal Basis | Source Text |
|-------------------|----------------|-------------|-------------|
| 30 days | Pension insurance | Section 13a(1) | 30 päivää |
| 30 days | Savings life insurance | Section 13a(1) | Säästöhenkivakuutus |
| From | Acceptance notification | Section 13a(1) | Hyväksymisestä |
| Within 30 days | Refund premium | Section 13a(2) | Palautus 30 päivässä |

---

## 12. Transfer Right

| **OUTPUT: Right** | Condition | Legal Basis | Source Text |
|-------------------|-----------|-------------|-------------|
| Yes | Pension terminated | Section 13b(1) | Siirto-oikeus |
| Yes | To another pension | Section 13b(1) | Toiseen eläkevakuutukseen |
| Yes | To long-term savings | Section 13b(1) | Pitkäaikaissäästötili |
| Within 30 days | Transfer deadline | Section 13b(2) | 30 päivän kuluessa |

---

## 13. Continuation Insurance Right

| **OUTPUT: Right** | Condition | Legal Basis | Source Text |
|-------------------|-----------|-------------|-------------|
| Yes | Insurance surrendered | Section 14(1) | Jatkovakuutusoikeus |
| Yes | No health assessment | Section 14(1) | Ei terveysselvitystä |
| Adjusted | By surrender value | Section 14(1) | Takaisinostoarvon mukaisesti |
| Within 6 months | Application deadline | Section 14(3) | 6 kuukauden kuluessa |

---

## 14. Insurer Termination - Non-Life

| **OUTPUT: Right** | Condition | Legal Basis | Source Text |
|-------------------|-----------|-------------|-------------|
| Yes | During period | Section 15(1) | Vakuutuskauden aikana |
| Required | Valid reason | Section 15(1) | Pätevä syy |
| 14 days | Notice period | Section 15(2) | 14 päivää |
| Required | Refund unearned | Section 15(3) | Palautus |

---

## 15. Continuous Insurance Termination

| **OUTPUT: Right** | Condition | Legal Basis | Source Text |
|-------------------|-----------|-------------|-------------|
| Yes | At period end | Section 16(1) | Vakuutuskauden päättyessä |
| 1 month | Notice period | Section 16(1) | Kuukauden irtisanomisaika |
| No right | If claims-free | Section 16(2) | Korvaukseton |
| Possible | Increase premium | Section 16(3) | Korotettu maksu |

---

## 16. Policyholder Disclosure Duty

| **OUTPUT: Required** | Information | Legal Basis | Source Text |
|---------------------|-------------|-------------|-------------|
| Required | All known risk factors | Section 22(1) | Tunnetut riskitekijät |
| Required | Answer all questions | Section 22(1) | Kysymyksiin vastaaminen |
| Required | Same for insured | Section 22(2) | Vakuutettu |
| Required | Notify of changes | Section 22(3) | Muutoksista ilmoittaminen |

---

## 17. Non-Life Disclosure Breach

| **OUTPUT: Consequence** | Type | Legal Basis | Source Text |
|------------------------|------|-------------|-------------|
| No liability | Intentional | Section 23(1) | Tahallinen |
| May reduce | Negligent | Section 23(2) | Huolimaton |
| Affected | Material breach | Section 23(3) | Olennainen |
| Full liability | If immaterial | Section 35 | Olennaisuus |

---

## 18. Life Insurance Disclosure Breach

| **OUTPUT: Consequence** | Condition | Legal Basis | Source Text |
|-------------------------|-----------|-------------|-------------|
| No liability | Fraud | Section 24(1) | Petollinen |
| Full liability | After 10 years | Section 24(2) | 10 vuotta |
| Proportionate | Contributory | Section 24(3) | Osittainen vastuu |
| Special rules | Within 2 years | Section 24(4) | 2 vuoden sisällä |

---

## 19. Risk Increase

| **OUTPUT: Required** | Type | Legal Basis | Source Text |
|---------------------|------|-------------|-------------|
| Notify | Non-life | Section 26(1) | Vaaran lisääntyminen |
| May adjust | Terms | Section 26(2) | Ehtojen muuttaminen |
| Different rules | Life insurance | Section 27 | Henkilövakuutus |
| No adjustment | If immaterial | Section 35 | Olennaisuus |

---

## 20. Premium Payment

| **OUTPUT: Required** | Condition | Legal Basis | Source Text |
|---------------------|-----------|-------------|-------------|
| Must pay | When due | Section 38(1) | Maksuvelvollisuus |
| To bank | Payment location | Section 38(2) | Pankkiin |
| May apply | Late fee | Section 39 | Viivästyskorko |
| May lapse | Non-payment | Section 40 | Vastuun lakkaaminen |

---

## 21. Late Premium Consequences

| **OUTPUT: Consequence** | Type | Legal Basis | Source Text |
|------------------------|------|-------------|-------------|
| Interest | Late payment | Section 39(1) | Viivästyskorko |
| May apply | Reminder fee | Section 39(2) | Muistutusmaksu |
| May use | Debt collection | Section 39(3) | Perintä |
| Exempt | In some cases | Section 39(4) | Poikkeukset |

---

## 22. Coverage Lapse - Non-Payment

| **OUTPUT: Result** | Condition | Legal Basis | Source Text |
|-------------------|-----------|-------------|-------------|
| Lapses | Non-payment | Section 40(1) | Vastuu lakkaa |
| Required | Written demand | Section 40(1) | Kirjallinen vaatimus |
| 14 days | Grace period | Section 40(1) | 14 päivää |
| Possible | Reinstatement | Section 40(2) | Jälleenvoimaansaattaminen |

---

## 23. Beneficiary Designation

| **OUTPUT: Rule** | Type | Legal Basis | Source Text |
|------------------|------|-------------|-------------|
| Can designate | Life insurance | Section 47(1) | Edunsaajan määrääminen |
| Required | Written form | Section 48(1) | Kirjallinen muoto |
| Can revoke | Any time | Section 49 | Peruuttaminen |
| Falls | If beneficiary predeceases | Section 49 | Raukeaminen |

---

## 24. Over-Insurance

| **OUTPUT: Rule** | Condition | Legal Basis | Source Text |
|------------------|-----------|-------------|-------------|
| Is over-insurance | Exceeds value | Section 57(1) | Ylivakuutus |
| Void | If intentional | Section 57(2) | Tahallinen |
| Pay only | Actual loss | Section 57(3) | Todellinen vahinko |
| Refund | Of excess premium | Section 57(4) | Maksun palautus |

---

## 25. Under-Insurance

| **OUTPUT: Rule** | Condition | Legal Basis | Source Text |
|------------------|-----------|-------------|-------------|
| Is under-insurance | Less than value | Section 58(1) | Alivakuutus |
| Proportional | Compensation | Section 58(1) | Suhteellinen korvaus |
| Can require | Full value | Section 58(2) | Täysi arvo |
| Possible | Premium adjustment | Section 58(3) | Maksun tarkistus |

---

## 26. Multiple Insurance

| **OUTPUT: Rule** | Condition | Legal Basis | Source Text |
|------------------|-----------|-------------|-------------|
| Is multiple | Same risk | Section 59(1) | Monivakuutus |
| Can claim | From any insurer | Section 59(2) | Vaatia keneltä tahansa |
| Share | Insurers liable | Section 60 | Vastuun jakaminen |
| Can recover | From others | Section 60(2) | Takautumisoikeus |

---

## 27. Salvage Costs

| **OUTPUT: Covered** | Type | Legal Basis | Source Text |
|---------------------|------|-------------|-------------|
| Covered | If reasonable | Section 61(1) | Pelastamiskustannukset |
| Covered | Prevention costs | Section 61(1) | Ehkäisykustannukset |
| Must be | Reasonable | Section 61(2) | Kohtuulliset |
| Limited to | Insurance sum | Section 61(3) | Vakuutusmäärään |

---

## 28. Third Party Rights

| **OUTPUT: Right** | Condition | Legal Basis | Source Text |
|-------------------|-----------|-------------|-------------|
| Has rights | Property insured | Section 62(1) | Kolmas henkilö |
| Covered | New owner | Section 63 | Omistajan vaihtuminen |
| Can claim | Directly | Section 65 | Vaatia korvausta |
| Applies | Liability insurance | Section 67 | Vastuuvakuutus |

---

## 29. Claim Procedure

| **OUTPUT: Required** | Type | Legal Basis | Source Text |
|---------------------|------|-------------|-------------|
| Required | Documentation | Section 69(1) | Selvitykset |
| Without delay | Timing | Section 69(2) | Viipymättä |
| Within 30 days | Payment | Section 70(1) | 30 päivää |
| Required | Denial reasons | Section 70(2) | Hylkäyksen perusteet |

---

## 30. Claim Limitation Period

| **OUTPUT: Limit** | Type | Legal Basis | Source Text |
|-------------------|------|-------------|-------------|
| 3 years | From right arose | Section 73(1) | 3 vuotta |
| From | When learned | Section 73(1) | Tieto tapahtumasta |
| Max 10 years | From event | Section 73(2) | 10 vuotta |
| 10 years | Life insurance | Section 73(3) | Henkilövakuutus 10 vuotta |

---

## 31. Group Insurance Rules

| **OUTPUT: Required** | Type | Legal Basis | Source Text |
|---------------------|------|-------------|-------------|
| Required | Group information | Section 76(1) | Ryhmätiedot |
| Notify | Of termination | Section 77 | Päättymisilmoitus |
| Apply | Member rights | Section 78 | Jäsenen oikeudet |
| Right | Continue individually | Section 80 | Jatkaminen yksilöllisenä |

---

*Total: 31 decision tables covering the Insurance Contract Act (543/1994)*
