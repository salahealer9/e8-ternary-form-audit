# E8 Cartan 3-form manuscript — bibliography audit v0.3

Date: 9 September 2026

## Result

STATUS: BIBLIOGRAPHY_AUDIT_PASS_WITH_TARGETED_REVISIONS

The bibliography was checked entry-by-entry against publisher, journal, arXiv,
PyPI, and source-repository records where applicable.

## Active references after audit

| Key | Audit result | Manuscript role |
|---|---|---|
| `Djokovic2000` | VERIFIED | Explicit E8 Chevalley constants; appendix lists nonzero constants |
| `GeckLang2025` | VERIFIED | Modern epsilon-canonical Chevalley basis and canonical constants |
| `Kollross2025` | ADDED / VERIFIED | Explicit alternative formula for the E8 bracket |
| `McGirl2026` | VERIFIED / TITLE CORRECTED | Public sparse machine-readable E8 bracket; 16,694 scalar entries |
| `Le2013` | VERIFIED | Cartan 3-form literature |
| `KoepsellNicolaiSamtleben1999` | VERIFIED / DOI ADDED | Fully antisymmetric lowered E8 structure constants |
| `Manivel2006` | VERIFIED | Ternary models of exceptional Lie algebras / E8 context |
| `BordnerMantonSasaki2000` | ADDED / VERIFIED | Older direct source explicitly listing E8 = 1120 x A2 |
| `WinterVanLuijk2021` | VERIFIED | 240-root system and fixed-root inner-product census 1,56,126,56,1 |
| `BohningBothmerMarquand2026` | VERIFIED | Direct modern derivation of exactly 1120 A2 subsystems from 240*56/12 |
| `Humphreys1972` | VERIFIED / DOI ADDED | Standard root-space and semisimple Lie-algebra conventions |

## Source-claim corrections

### Brini 2020

The bibliographic metadata for Andrea Brini, *E8 spectral curves*, is correct.
However, it is not the most direct source for the manuscript's statement about
explicit or sparse E8 Lie brackets. It has therefore been removed from that
specific prior-art claim.

### Kollross 2025

Added because it directly supplies an explicit formula for the E8 Lie bracket
in an alternative oct-octonionic/triality realization.

### Bordner–Manton–Sasaki 2000

Added because the paper explicitly lists

    E8 = 1120 x A2

in its two-dimensional root-subsystem census, giving an older direct source for
the 1120 count.

### McGirl 2026

The citation title was changed to the official project title:

    DHL-MM: Dynamic Hodge-Lie Matrix Multiplication

The citation records version 0.2.2, released 23 March 2026, and includes both
PyPI and source-repository locations.

## Metadata additions

Added missing DOI/arXiv metadata where available, including:

- Koepsell--Nicolai--Samtleben: DOI `10.1088/1126-6708/1999/04/023`
- Humphreys: DOI `10.1007/978-1-4612-6398-2`
- Geck--Lang: arXiv `2404.07652`
- Lê: arXiv `1103.1201`
- Manivel: arXiv `math/0507118`
- Winter--van Luijk: arXiv `1901.06945`

## Compilation result

The audited v0.3 manuscript compiles successfully with:

- 12 pages;
- zero LaTeX warnings;
- zero overfull boxes;
- zero underfull boxes;
- zero unresolved references;
- zero unresolved citations.

## Bibliographic boundary

The audit strengthens the paper's prior-art section without changing the
novelty conclusion:

- classical mathematical structures remain explicitly acknowledged;
- the 1120 A2 count now has both older and recent direct references;
- sparse E8 brackets have explicit software prior art;
- the manuscript continues to avoid "first" and "previously unknown" claims.
