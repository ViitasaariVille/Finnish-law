## Gap Description

The DMN rules are missing §13(4) which grants Finnish residents the explicit **right to choose** Finnish law for personal injury compensation when injured abroad in another EEA country.

## Law Reference

**§13(4):**
> Suomessa asuva vahinkoa kärsinyt voi valita, että tämän lain mukaan vakuutetun ajoneuvon liikenteessä käyttämisestä aiheutunut muualla ETA-alueella kuin Suomessa sattunut henkilövahinko korvataan Suomen lain mukaan silloin, kuin vahinko lainvalintaa koskevien säännösten mukaan tulisi korvattavaksi muun kuin Suomen lain mukaan.

**Key Points:**
1. Finnish resident injured in another EEA country
2. By default, accident country's law might apply
3. **Victim has ACTIVE RIGHT to ELECT Finnish law** for personal injury claims
4. This is a consumer protection provision

## Current DMN Status

- E3 mentions "Better law" comparison
- **NO rule for victim's explicit CHOICE right under §13(4)**

## Missing DMN Rule

#### LAW-ELECTION-001: Finnish Resident Law Election Right (§13(4))

| victim.residence | accident.location | damage.type | law.electionRequested | accidentCountry.law | finnishLaw.better | Output |
|------------------|-------------------|-------------|----------------------|---------------------|--------------------|--------|
| Finland | EEA (not Finland) | PersonalInjury | true | any | any | **FinnishLaw_Elected** |
| Finland | EEA (not Finland) | PersonalInjury | false | better | false | **AccidentCountryLaw_Default** |
| Finland | EEA (not Finland) | PersonalInjury | false | worse | true | **FinnishLaw_AutoApplied** |
| Finland | Finland | any | N/A | N/A | N/A | **FinnishLaw** |
| Non-Finland | any | any | N/A | N/A | N/A | **AccidentCountryLaw** |

**Important:** This is an ACTIVE RIGHT, not automatic better-law comparison.

## Severity: HIGH

- **Consumer protection right**
- Affects international claims handling
- Currently no mechanism for law election

## Related Sections

- §13(3): Better law protection (automatic)
- E3: International coverage

## Tags

@VilleMoltBot for review

---
*Identified during law compliance check - February 26, 2026*
