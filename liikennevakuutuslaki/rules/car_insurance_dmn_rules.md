# Liikennevakuutuslaki DMN Rules - Hierarchical Structure

## Finnish Traffic Insurance Act (460/2016) - Negative Claim Decision Rules

### Hierarchy Overview

| Category | Description | Sections | Rules |
|----------|-------------|----------|-------|
| **Full Denial** | Complete claim rejection | §41, §41a, §43, §44, §46, §47, §48, §49, §50 | 9 |
| **Reduced Compensation** | Fault-based percentage reduction | §47, §48 | 3 |
| **Conditional Compensation** | Exceptions allowing coverage | §41, §41a, §43, §44, §46, §48 | 6 |

---

## 1. FULL DENIAL Rules (§§41, 41a, 43, 44, 46, 47, 48, 49, 50)

### §49 - Unauthorized Use
| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Vehicle used without owner consent | NOT COVERED | §49(1) |

### §50 - Insanity/Emergency
| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Driver insane/not responsible | NOT COVERED | §50(1) |
| Emergency situation not justified | NOT COVERED | §50(2) |

### §41 - Theft (Property Damage)
| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Property damage after theft, insurance terminated | NOT COVERED | §41(1) |

### §41a - Unauthorized Competition
| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Competition without authorization | NOT COVERED | §41a(1) |
| Competition with invalid license | NOT COVERED | §41a(2) |

### §43 - Exempt Vehicles (Property Damage)
| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Military vehicle property damage | NOT COVERED | §43(1) |
| Diplomatic vehicle property damage | NOT COVERED | §43(2) |
| Government vehicle property damage | NOT COVERED | §43(2) |

### §44 - Unknown Vehicle (No Police Report)
| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Unknown vehicle, no police report (property) | NOT COVERED | §44(2) |

### §46 - No Insurance (Property Damage)
| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| No insurance, property damage | NOT COVERED | §46(1) |

### §47 - Victim Gross Negligence
| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Victim gross negligence | NOT COVERED | §47(1) |

### §48 - Drunk Driving (Sole Fault)
| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| BAC ≥1.2‰, driver solely responsible | NOT COVERED | §48(1) |

---

## 2. REDUCED COMPENSATION Rules (§47, §48)

### §47 - Victim Contribution
| Victim Contribution | Damage Type | Compensation | Legal Basis |
|--------------------|-------------|--------------|-------------|
| Negligence | Property | 50% | §47(2) |
| Slight | Any | 75% | §47(2) |
| Moderate | Any | 50% | §47(2) |

### §48 - Alcohol Impairment
| BAC Level | Fault | Compensation | Legal Basis |
|-----------|-------|--------------|-------------|
| ≥1.2‰ | Partial | 50% | §48(1) |
| 0.5-1.19‰ | Partial | 75% | §48(2) |
| 0.5-1.19‰ | Sole | NOT COVERED | §48(2) |

---

## 3. CONDITIONAL COMPENSATION Rules (§41, 41a, 43, 44, 46, 48)

### §41 - Theft (Exceptions)
| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Personal injury after theft, insurance active | COVERED | §41(2) |
| Normal accident (no theft) | COVERED | §41 |

### §41a - Competition (Exceptions)
| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Personal injury in authorized competition | COVERED | §41a(2) |
| Property damage in authorized competition | COVERED | §41a(2) |
| Normal driving | COVERED | §41a |

### §43 - Exempt Vehicles (Exceptions)
| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Personal injury (any exempt vehicle) | COVERED | §43(3) |

### §44 - Unknown Vehicle (Exceptions)
| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Personal injury (unknown vehicle) | COVERED | §44(1) |
| Property damage (from guarantee fund) | COVERED | §44(2) |

### §46 - No Insurance (Exceptions)
| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Personal injury (from guarantee fund) | COVERED | §46(1) |
| Insurance exists but violated | COVERED | §46(2) |

### §48 - Alcohol (Exceptions)
| Condition | Output | Legal Basis |
|-----------|--------|-------------|
| Third party victim (not at fault) | COVERED | §48(3) |
| BAC <0.5‰, no victim fault | COVERED | §48(2) |

---

## Decision Flow

```
Claim Received
       │
       ▼
┌──────────────────┐
│ Full Denial      │───→ DENY CLAIM
│ Check (§49, §50) │
└────────┬─────────┘
         │ No
         ▼
┌──────────────────┐
│ Reduced Comp     │───→ CALCULATE %
│ Check (§47, §48) │     (50%, 75%)
└────────┬─────────┘
         │ No
         ▼
┌──────────────────┐
│ Conditional      │───→ CHECK
│ Check (§41-§48) │     EXCEPTIONS
└────────┬─────────┘
         │ Yes
         ▼
    APPROVE CLAIM
```

---

## Metadata

- **Law**: Liikennevakuutuslaki (Traffic Insurance Act) 460/2016
- **Source**: finlex.fi/fi/lainsaadanto/2016/460
- **Version**: 1.1 (Hierarchical)
- **Total Rules**: 68
- **Categories**: 3 (Full Denial, Reduced, Conditional)
