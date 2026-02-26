# Liikennevakuutuslaki DMN Files

This folder contains DMN (Decision Model and Notation) files for the Finnish Traffic Insurance Act (460/2016).

## Files

| File | Description |
|------|-------------|
| `liikennevakuutuslaki.dmn` | Main DMN decision model with decision tables |
| `liikennevakuutuslaki_drd.dmn` | Decision Requirements Diagram (DRD) |
| `README.md` | This file |

## Decision Structure

### Level 1: Negative Claims Check
- **Decision_N1_NegativeClaims**: Checks exclusions (§§41-50)
  - Unauthorized use (§49)
  - Insanity/Emergency (§50)
  - Theft property (§41)
  - Competition (§41a)
  - Exempt vehicles (§43)
  - Unknown vehicle (§44)
  - No insurance (§46)
  - Victim negligence (§47)
  - Alcohol impairment (§48)

### Level 2: Coverage Determination
- **Decision_E1_Coverage**: Determines if vehicle requires insurance (§§5-13)
  - Finland vs EEA vs Third Country
  - Covered vehicle types
  - Geographic scope

### Level 3: Compensation Calculation
- **Decision_E2_CompensationCalc**: Calculates compensation (§34)
  - Employed: Net monthly / 30 × days
  - Self-employed: Annual / 365 × days
  - Unemployed: No loss of earnings

### Level 4: Limits and Caps
- **Decision_E3_PropertyMax**: Property damage maximum (§38)
  - Cap: €5,000,000
- **Decision_E4_Alcohol**: Alcohol impairment reduction (§48)
  - ≥1.2‰: Only other factors
  - ≥0.5‰: Proportional reduction

## Import into Camunda Modeler

1. Open Camunda Modeler
2. File → Open File
3. Select `liikennevakuutuslaki.dmn`
4. Edit decision tables as needed
5. Save as new file or export

## Supported Versions

- DMN 1.1 (OMG Specification)
- Camunda Modeler 5.x

## Legal Source

Finnish Traffic Insurance Act (460/2016):
- https://www.finlex.fi/fi/laki/ajantasa/2016/20160460
