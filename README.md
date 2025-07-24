<!--
SPDX-FileCopyrightText: 2025 Open Energy Transition (OET)

SPDX-License-Identifier: CC0-1.0
-->

# Awesome Grid Model Data

<table>
<tr>
<td>
<b>A curated collection of publicly available electricity grid (production cost, power flow, etc.) model datasets for academic and industry research. </b>
</td>
<td>

<img src="https://raw.githubusercontent.com/open-energy-transition/Awesome-Electric-Grid-Mapping/refs/heads/main/ohmygrid-logo.png" alt="Global Grid Mapping" width="350">

</td>
</tr>
</table>

This list includes datasets for both open-source and commercial/proprietary modeling tools.

[![Link Health](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/pz-max/8eca1f79637060fbbc23a602ce534994/raw/link-status.json)](https://github.com/open-energy-transition/Awesome-Grid-Model-Data/actions/workflows/link-check.yml)

## Disclaimer

This repository is for educational and research use only. We do not host, own, or guarantee the availability of any linked datasets. Some datasets may require proprietary software (e.g., PLEXOS, PowerWorld, PSSE, PSLF) to access or use. Inclusion of such datasets does not imply endorsement, affiliation, or sponsorship by any software vendor.  All trademarks, including PLEXOS, are the property of their respective owners and are used here solely for identification and interoperability purposes. Users are responsible for obtaining appropriate software licenses and complying with all applicable terms. For dataset-specific inquiries, contact the original data providers.

## Table of contents
- [Disclaimer](#disclaimer)
- [Table of contents](#table-of-contents)
- [Contribution Guide](#contribution-guide)
  - [Contribution Tips](#contribution-tips)
  - [How to Contribute](#how-to-contribute)
- [Non-Open Source Modeling Tools](#non-open-source-modeling-tools)
  - [PLEXOS (`.xml`)](#plexos-xml)
  - [PowerWorld (`.pwb/.pwd`)](#powerworld-pwbpwd)
  - [PSSE (`.raw`)](#psse-raw)
  - [PSLF (`.epc` / `.dyd`)](#pslf-epc--dyd)
  - [DIgSILENT PowerFactory (`.pfd`)](#digsilent-powerfactory-pfd)
- [Open Source Modeling Tools](#open-source-modeling-tools)
  - [PyPSA](#pypsa)
  - [MATPOWER (`.m`)](#matpower-m)

## Contribution Guide

### Contribution Tips

- Prefer official or well-maintained sources.
- Ensure the dataset is publicly available for download (or add any additional relevant instructions).
- Avoid duplicate entries.
- If a dataset is no longer available, feel free to open an issue or submit a PR to remove or update the link.

### How to Contribute

1. **Fork the Repository**
   Click the "Fork" button at the top right of this page to create your own copy.
2. **Create a Branch**Create a new branch for your contribution (replace `my-dataset-addition` with your own branch name):

   ```bash
   git checkout -b my-dataset-addition
   ```
3. **Add or Update Content**

   - Add new datasets in the appropriate section (e.g., MATPOWER, PSSE, PSLF, PLEXOS, etc.) or create a new section for a modelling tool that is not already listed.
   - Include a short description and a direct link to the dataset source.
4. **Follow Formatting**

   - Use the existing Markdown style for consistency.
   - Place new entries in alphabetical or logical order within each section.
5. **Commit and Push**Again replace `my-dataset-addition` with your own branch name.

   ```bash
   git add README.md
   git commit -m "Add [dataset name] to [section]"
   git push origin my-dataset-addition
   ```
6. **Open a Pull Request**

   - Go to your fork on GitHub and click "Compare & pull request".
   - Provide a clear description of your changes in your pull request, then create the pull request for review.

---

## Non-Open Source Modeling Tools

### PLEXOS (`.xml`)

PLEXOS model data listed here are input XML files that are meant to contain the inputs required to run a PLEXOS model.

#### AEMO (Australian Energy Market Operator)

- **2024 Integrated System Plan (ISP)** [AEMO ISP 2024 PLEXOS Model](https://aemo.com.au/-/media/files/major-publications/isp/2024/supporting-materials/2024-isp-model.zip?la=en)
- **2022 Integrated System Plan (ISP)** [AEMO ISP 2022 PLEXOS Model](https://aemo.com.au/-/media/files/major-publications/isp/2022/2022-documents/2022-isp-model.zip?la=en)
- **2020 Integrated System Plan (ISP)** [AEMO ISP 2020 PLEXOS Model](https://aemo.com.au/-/media/files/major-publications/isp/2020/2020-final-isp-model.zip?la=en)
- **2018 Integrated System Plan (ISP)** 
  [AEMO ISP 2018 Input Data &amp; PLEXOS DLT Model](https://aemo.com.au/energy-systems/major-publications/integrated-system-plan-isp/2018-integrated-system-plan-isp)

#### CAISO (California ISO)

- **2024 IRP 25 MMT Stochastic PLEXOS Model** [CAISO IRP 2024 PLEXOS Model](https://www.caiso.com/documents/caiso-irp23-stochastic-2024-0517.zip)
- **2021 IRP 38MMT PSP Stochastic/Deterministic PLEXOS Models** 
  - [CAISO IRP 2021 Stochastic 2026](https://www.caiso.com/documents/caiso-integrated-resource-planning-38mmt-coreportfolio-plexos-stochastic-2026.zip)
  - [CAISO IRP 2021 Stochastic 2030](https://www.caiso.com/documents/caiso-integrated-resource-planning-38mmt-coreportfolio-plexos-stochastic-2030.zip)
  - [CAISO IRP 2021 Deterministic 2026/2030](https://www.caiso.com/documents/caiso-integrated-resource-planning-38mmt-coreportfolio-plexos-deterministic-2026-2030.zip)
- **2025 Summer Loads and Resources Assessment** [CAISO 2025 Summer Stochastic Model](https://www.caiso.com/documents/2025-summer-loads-and-resources-assessment-public-stochastic-model.zip)

#### NREL (National Renewable Energy Laboratory)

- **Extended IEEE 118-bus Test System (High Renewables)** 
  [NREL IEEE 118-bus PLEXOS Model](https://db.bettergrids.org/bettergrids/handle/1001/120?mode=full#:~:text=File%20Description%20Size%20Format%20Export,on%20IEEE%20Transactions%20on%20Power)

#### SEM (Ireland)

- **2025 SEM PLEXOS Model Validation (2024-2032)** [SEM 2025 PLEXOS Model](https://www.semcommittee.com/publications/sem-25-010-sem-plexos-model-validation-2024-2032-and-backcast-report)
- **2021 SEM PLEXOS Model Validation (2021-2029)** [SEM 2021 PLEXOS Model](https://www.semcommittee.com/publications/sem-21-086-sem-plexos-model-validation-2021-2029-and-backcast-report)
- **2020 SEM PLEXOS Forecast Model (2020-2025)**
  [SEM 2020 PLEXOS Model](https://www.semcommittee.com/publications/sem-20-003-sem-plexos-forecast-model-2020-2025)

#### University College Cork

- **2024 PLEXOS-World - Spatial Resolution Case Study** [UCC 2024 PLEXOS-World Model](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/NY1QW0)
- **2015 PLEXOS-World** [UCC 2015 PLEXOS-World Model](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/CBYXBY)
- **EU Gas and Electricity Model** 
  [UCC EU Power &amp; Gas Model](https://www.dropbox.com/scl/fi/biv5n52x8s5pxeh06u2b1/EU-Power-Gas-Model.zip?rlkey=hmscke4vsknxbj6w18vosfyxb&e=1&dl=0)

### PowerWorld (`.pwb/.pwd`)

The following test cases are available in PowerWorld format:

#### IEEE Test Systems

- **IEEE 14-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-14-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-14-bus-system/) | [University of Cyprus PWD](https://www.kios.ucy.ac.cy/testsystems/wp-content/uploads/2020/03/IEEE-14-Bus_modified_pwd.7z) | [University of Cyprus PWB](https://www.kios.ucy.ac.cy/testsystems/wp-content/uploads/2020/03/IEEE-14-Bus_modified_pwb.7z)
- **IEEE 24-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-24-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-24-bus-system/)
- **IEEE 30-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-30-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-30-bus-system/) | [University of Cyprus](https://www2.kios.ucy.ac.cy/testsystems/index.php/ieee-30-bus-modified-test-system/)
- **IEEE 39-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-39-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-39-bus-system/) | [University of Cyprus](https://www2.kios.ucy.ac.cy/testsystems/index.php/ieee-39-bus-modified-test-system/)
- **IEEE 57-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-57-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-57-bus-system/) | [University of Cyprus](https://www2.kios.ucy.ac.cy/testsystems/index.php/ieee-57-bus-modified-test-system/)
- **IEEE 118-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-118-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-118-bus-system/) | [University of Cyprus](https://www2.kios.ucy.ac.cy/testsystems/index.php/ieee-118-bus-modified-test-system/)
- **IEEE 300-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-300-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-300-bus-system/) | [University of Cyprus](https://www2.kios.ucy.ac.cy/testsystems/index.php/ieee-300-bus-modified-test-system/)
- **IEEE 9-bus (WSCC)**: [University of Cyprus](https://www2.kios.ucy.ac.cy/testsystems/index.php/ieee-9-bus-modified-test-system/)
- **IEEE 96-RTS**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-96-rts-test-system/)

#### UIUC / Illinois Synthetic Grids

- **UIUC 150-bus**: [ICSEG](https://icseg.iti.illinois.edu/synthetic-power-cases/uiuc-150-bus-system/)
- **Illinois 200-bus (ACTIVSg200)**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg200/) | [ICSEG](http://icseg.iti.illinois.edu/illinois200/)
- **SC 500-bus (ACTIVSg500)**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg500/)
- **Texas 2000-bus**: [ICSEG](https://icseg.iti.illinois.edu/synthetic-power-cases/texas2000-june2016/)
- **Illini 42 Tornado**: [ICSEG](http://icseg.iti.illinois.edu/illini-42-tornado/)
- **IlliniGMD 42 HEMP**: [ICSEG](http://icseg.iti.illinois.edu/illinigmd-42-hemp/)

#### Texas A&M University (TAMU) Synthetic Grids

- **Texas2k Series25**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/texas2k-series25/)
- **Hawaii 37-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/hawaii40/)
- **Texas 6717-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/texas7k/)
- **Texas 6717-bus with Distribution**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/texas7k-td/)
- **Texas 6717-bus with Gas Pipeline**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/7k-electric-gas/)
- **Combined East-West US Grid (80,000 buses)**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/combined-synthetic-east-and-west-80000-bus-system-with-synchronously-interconnected-synthetic-eastern-and-western-united-states/)
- **Texas2k Series24**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/activsg2000-dynamics-cases-2024/)
- **EIA-860 Generator Data Cases**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/eia-860-generator-data-cases/)
- **Travis 150-bus T+D**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/combined-td-synthetic-dataset/)
- **ACTIVSg200**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg200/)
- **ACTIVSg500**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg500/)
- **ACTIVSg2000**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg2000/)
- **ACTIVSg10k**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg10k/)
- **ACTIVSg25k**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg25k/)
- **ACTIVSg70k**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg70k/)
- **All EPIGRIDS Cases**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/) (Eastern Network, Florida, Midwest, New England, Synthetic USA, Texas)
- **All GO Competition Cases**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/) (Tgo500, Tgo2000, Tgo10K, Tgo30K)
- **Polish Grid with TAMU Enhancements**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/polish-grid/)

#### Small Signal Stability Test Cases

- **Three Machines Infinite Bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/three-machines-infinite-bus-benchmark-system/) | [ICSEG](http://icseg.iti.illinois.edu/three-machines-infinite-bus-benchmark-system/)
- **Brazilian Seven Bus System**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/brazilian-seven-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/brazilian-7-bus-system/)
- **Two-Area (Four-Generator) System**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/four-generator-system/) | [ICSEG](http://icseg.iti.illinois.edu/two-area-system-2/)
- **New England IEEE 39-Bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/new-england-ieee-39-bus-system/) | [ICSEG](https://icseg.iti.illinois.edu/ieee-39-bus-system/)
- **Simplified 14-Generator Australian Power System**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/simplified-14-generator-australian-power-system/) | [ICSEG](http://icseg.iti.illinois.edu/simplified-14-generator-australian-power-system/)
- **New England 68-Bus Test System**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/new-england-68-bus-test-system/) | [ICSEG](http://icseg.iti.illinois.edu/new-england-68-bus-test-system/)

#### Other Academic Test Cases

- **Kundur Two-Area**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/two-area-system) | [ICSEG](http://icseg.iti.illinois.edu/two-area-system/)
- **WSCC 9-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/wscc-9-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/wscc-9-bus-system/)

### PSSE (`.raw`)

The following test cases are available in PSSE format:

#### IEEE Test Systems

- **IEEE 14-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-14-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-14-bus-system/)
- **IEEE 24-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-24-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-24-bus-system/)
- **IEEE 30-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-30-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-30-bus-system/)
- **IEEE 39-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-39-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-39-bus-system/)
- **IEEE 57-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-57-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-57-bus-system/)
- **IEEE 118-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-118-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-118-bus-system/)
- **IEEE 300-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-300-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-300-bus-system/)
- **IEEE 96-RTS**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-96-rts-test-system/)

#### UIUC / Illinois Synthetic Grids

- **UIUC 150-bus**: [ICSEG](https://icseg.iti.illinois.edu/synthetic-power-cases/uiuc-150-bus-system/)
- **Illinois 200-bus (ACTIVSg200)**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg200/) | [ICSEG](http://icseg.iti.illinois.edu/illinois200/)
- **SC 500-bus (ACTIVSg500)**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg500/)
- **Texas 2000-bus**: [ICSEG](https://icseg.iti.illinois.edu/synthetic-power-cases/texas2000-june2016/)
- **Illini 42 Tornado**: [ICSEG](http://icseg.iti.illinois.edu/illini-42-tornado/)
- **IlliniGMD 42 HEMP**: [ICSEG](http://icseg.iti.illinois.edu/illinigmd-42-hemp/)

#### Texas A&M University (TAMU) Synthetic Grids

- **Texas2k Series25**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/texas2k-series25/)
- **Hawaii 37-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/hawaii40/)
- **Texas 6717-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/texas7k/)
- **Texas 6717-bus with Distribution**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/texas7k-td/)
- **Texas 6717-bus with Gas Pipeline**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/7k-electric-gas/)
- **Combined East-West US Grid (80,000 buses)**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/combined-synthetic-east-and-west-80000-bus-system-with-synchronously-interconnected-synthetic-eastern-and-western-united-states/)
- **Texas2k Series24**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/activsg2000-dynamics-cases-2024/)
- **EIA-860 Generator Data Cases**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/eia-860-generator-data-cases/)
- **Travis 150-bus T+D**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/combined-td-synthetic-dataset/)
- **ACTIVSg200**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg200/)
- **ACTIVSg500**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg500/)
- **ACTIVSg2000**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg2000/)
- **ACTIVSg10k**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg10k/)
- **ACTIVSg25k**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg25k/)
- **ACTIVSg70k**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg70k/)
- **All EPIGRIDS Cases**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/) (Eastern Network, Florida, Midwest, New England, Synthetic USA, Texas)
- **All GO Competition Cases**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/) (Tgo500, Tgo2000, Tgo10K, Tgo30K)
- **Polish Grid with TAMU Enhancements**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/polish-grid/)

#### Small Signal Stability Test Cases

- **Three Machines Infinite Bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/three-machines-infinite-bus-benchmark-system/) | [ICSEG](http://icseg.iti.illinois.edu/three-machines-infinite-bus-benchmark-system/)
- **Brazilian Seven Bus System**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/brazilian-seven-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/brazilian-7-bus-system/)
- **Two-Area (Four-Generator) System**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/four-generator-system/) | [ICSEG](http://icseg.iti.illinois.edu/two-area-system-2/)
- **New England IEEE 39-Bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/new-england-ieee-39-bus-system/) | [ICSEG](https://icseg.iti.illinois.edu/ieee-39-bus-system/)
- **Simplified 14-Generator Australian Power System**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/simplified-14-generator-australian-power-system/) | [ICSEG](http://icseg.iti.illinois.edu/simplified-14-generator-australian-power-system/)
- **New England 68-Bus Test System**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/new-england-68-bus-test-system/) | [ICSEG](http://icseg.iti.illinois.edu/new-england-68-bus-test-system/)

#### Other Academic Test Cases

- **Kundur Two-Area**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/two-area-system) | [ICSEG](http://icseg.iti.illinois.edu/two-area-system/)
- **WSCC 9-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/wscc-9-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/wscc-9-bus-system/)

#### ALSETLab - Nordic Test Systems

- **Nordic 44**: [GitHub Repository](https://github.com/ALSETLab/Nordic44-Nordpool/tree/master/nordic44/models)

#### New Zealand Electricity Authority (EA)

- **New Zealand Transmission System Models (North & South Islands)**: Representative PSSE `.sav` and `.raw` files of New Zealand's transmission system. Separate models for North Island and South Island. [NZ EA PSSE files](https://www.emi.ea.govt.nz/Wholesale/Datasets/Transmission/PowerSystemAnalysis/PSSErawFiles)


### PSLF (`.epc` / `.dyd`)

The following test cases are available in GE PSLF format:

#### IEEE Test Systems

- **IEEE 14-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-14-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-14-bus-system/)
- **IEEE 24-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-24-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-24-bus-system/)
- **IEEE 30-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-30-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-30-bus-system/)
- **IEEE 39-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-39-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-39-bus-system/)
- **IEEE 57-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-57-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-57-bus-system/)
- **IEEE 118-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-118-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-118-bus-system/)
- **IEEE 300-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-300-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/ieee-300-bus-system/)
- **IEEE 96-RTS**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-96-rts-test-system/)

#### UIUC / Illinois Synthetic Grids

- **UIUC 150-bus**: [ICSEG](https://icseg.iti.illinois.edu/synthetic-power-cases/uiuc-150-bus-system/)
- **Illinois 200-bus (ACTIVSg200)**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg200/) | [ICSEG](http://icseg.iti.illinois.edu/illinois200/)
- **SC 500-bus (ACTIVSg500)**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg500/)
- **Texas 2000-bus**: [ICSEG](https://icseg.iti.illinois.edu/synthetic-power-cases/texas2000-june2016/)
- **Illini 42 Tornado**: [ICSEG](http://icseg.iti.illinois.edu/illini-42-tornado/)
- **IlliniGMD 42 HEMP**: [ICSEG](http://icseg.iti.illinois.edu/illinigmd-42-hemp/)

#### Texas A&M University (TAMU) Synthetic Grids

- **Texas2k Series25**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/texas2k-series25/)
- **Hawaii 37-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/hawaii40/)
- **Texas 6717-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/texas7k/)
- **Texas 6717-bus with Distribution**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/texas7k-td/)
- **Texas 6717-bus with Gas Pipeline**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/7k-electric-gas/)
- **Combined East-West US Grid (80,000 buses)**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/combined-synthetic-east-and-west-80000-bus-system-with-synchronously-interconnected-synthetic-eastern-and-western-united-states/)
- **Texas2k Series24**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/activsg2000-dynamics-cases-2024/)
- **EIA-860 Generator Data Cases**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/eia-860-generator-data-cases/)
- **Travis 150-bus T+D**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/combined-td-synthetic-dataset/)
- **ACTIVSg200**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg200/)
- **ACTIVSg500**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg500/)
- **ACTIVSg2000**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg2000/)
- **ACTIVSg10k**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg10k/)
- **ACTIVSg25k**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg25k/)
- **ACTIVSg70k**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg70k/)
- **All EPIGRIDS Cases**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/) (Eastern Network, Florida, Midwest, New England, Synthetic USA, Texas)
- **All GO Competition Cases**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/) (Tgo500, Tgo2000, Tgo10K, Tgo30K)
- **Polish Grid with TAMU Enhancements**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/polish-grid/)

#### Small Signal Stability Test Cases

- **Three Machines Infinite Bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/three-machines-infinite-bus-benchmark-system/) | [ICSEG](http://icseg.iti.illinois.edu/three-machines-infinite-bus-benchmark-system/)
- **Brazilian Seven Bus System**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/brazilian-seven-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/brazilian-7-bus-system/)
- **Two-Area (Four-Generator) System**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/four-generator-system/) | [ICSEG](http://icseg.iti.illinois.edu/two-area-system-2/)
- **New England IEEE 39-Bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/new-england-ieee-39-bus-system/) | [ICSEG](https://icseg.iti.illinois.edu/ieee-39-bus-system/)
- **Simplified 14-Generator Australian Power System**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/simplified-14-generator-australian-power-system/) | [ICSEG](http://icseg.iti.illinois.edu/simplified-14-generator-australian-power-system/)
- **New England 68-Bus Test System**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/new-england-68-bus-test-system/) | [ICSEG](http://icseg.iti.illinois.edu/new-england-68-bus-test-system/)

#### Other Academic Test Cases

- **Kundur Two-Area**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/two-area-system) | [ICSEG](http://icseg.iti.illinois.edu/two-area-system/)
- **WSCC 9-bus**: [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/wscc-9-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/wscc-9-bus-system/)

#### ALSETLab - Nordic Test Systems

- **Nordic 44**: [GitHub Repository](https://github.com/ALSETLab/Nordic44-Nordpool/tree/master/nordic44/models)

#### NREL Test Case Repository

- **18-Bus 4-Area Test System**: [NREL Repository](https://www.nrel.gov/grid/test-case-repository) (GE PSLF demonstration system)

### DIgSILENT PowerFactory (`.pfd`)

#### New Zealand Electricity Authority (EA)

- **New Zealand Transmission System Models (North & South Islands)**: PowerFactory case files of New Zealand's transmission system, updated annually by Transpower. Separate models for North Island and South Island. [NZ EA PowerFactory Files](https://www.emi.ea.govt.nz/Wholesale/Datasets/Transmission/PowerSystemAnalysis/PowerFactoryCaseFiles)

#### Comité de Operación Económica del Sistema Interconectado Nacional (COES) – Peru

- **Peru SEIN Transmission System Models (DIgSILENT PowerFactory)**: COES, the independent system operator for Peru, publishes PowerFactory case files for the Peruvian interconnected electricity system (SEIN). These datasets include both pre-operational studies ([Pre-operational Studies](https://www.coes.org.pe/Portal/Planificacion/NuevosProyectos/EstudiosPO)) and operational studies ([Operational Studies](https://www.coes.org.pe/Portal/Planificacion/NuevosProyectos/EstudiosO)).

## Open Source Modeling Tools

### PyPSA

#### PyPSA-Eur
- **PyPSA-Eur: An open sector-coupled optimisation model of the European energy system**. [Zenodo](https://zenodo.org/records/15163251)

#### PyPSA-Earth
- **The impact of temporal hydrogen regulation on hydrogen exporters and their domestic energy transition**. [Zenodo](https://zenodo.org/records/10951650)

### MATPOWER (`.m`)

Many MATPOWER test cases are available on their [Github](https://github.com/MATPOWER/matpower/tree/master/data).

#### IEEE Test Systems

- **IEEE 14-bus**: 14-bus AEP system (1962), 5 generators, 11 loads; academic test case. [MATPOWER case14.m](https://github.com/MATPOWER/matpower/blob/master/data/case14.m) | [UW Archive](https://labs.ece.uw.edu/pstca/pf14/pg_tca14bus.htm)
- **IEEE 24-bus**: 24-bus Reliability Test System (1979); academic test case. [MATPOWER case24_ieee_rts.m](https://github.com/MATPOWER/matpower/blob/master/data/case24_ieee_rts.m) | [UW Archive RTS](https://labs.ece.uw.edu/pstca/rts/pg_tcarts.htm)
- **IEEE 30-bus**: 30-bus AEP system (1961), 6 generators; academic test case. [MATPOWER case30.m](https://github.com/MATPOWER/matpower/blob/master/data/case30.m) | [UW Archive](https://labs.ece.uw.edu/pstca/pf30/pg_tca30bus.htm)
- **IEEE 33-bus**: Common radial distribution feeder; academic test case. [case33bw.m](https://web.archive.org/web/20220619162123/https://egriddata.org/sites/default/files/case33bw.m) (link opens download)
- **IEEE 39-bus**: "New England" 39-bus system (10 machines); academic test case. [MATPOWER case39.m](https://github.com/MATPOWER/matpower/blob/master/data/case39.m) | [Edinburgh Network](https://webhomes.maths.ed.ac.uk/OptEnergy/NetworkData/39buscase/)
- **IEEE 57-bus**: 57-bus AEP Midwest system (circa 1960s); academic test case. [MATPOWER case57.m](https://github.com/MATPOWER/matpower/blob/master/data/case57.m) | [UW Archive](https://labs.ece.uw.edu/pstca/pf57/pg_tca57bus.htm)
- **IEEE 118-bus**: 118-bus IEEE system (Midwest 1962); academic test case. [MATPOWER case118.m](https://github.com/MATPOWER/matpower/blob/master/data/case118.m) | [UW Archive](https://labs.ece.uw.edu/pstca/pf118/pg_tca118bus.htm)
- **IEEE 300-bus**: 300-bus IEEE test system (1993); academic test case.
  [MATPOWER case300.m](https://github.com/MATPOWER/matpower/blob/master/data/case300.m) | [UW Archive](https://labs.ece.uw.edu/pstca/pf300/pg_tca300bus.htm)

#### University of Washington Additional IEEE Test Cases

- **IEEE 9-bus (WSCC)**: 9-bus Western System Coordinating Council case. [University of Cyprus](https://www2.kios.ucy.ac.cy/testsystems/index.php/ieee-9-bus-modified-test-system/)
- **IEEE 96-RTS**: 96-bus Reliability Test System.
  [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/ieee-96-rts-test-system/)

#### Dynamic Test Cases (UW Archive)

- **162-bus with 17 Generators**: Dynamic test case with classic generator models. [UW Archive](https://labs.ece.uw.edu/pstca/dyn17/pg_tcadd17.htm)
- **New England 30-bus Dynamic**: Dynamic version of New England system. [UW Archive](https://labs.ece.uw.edu/pstca/dyn30/pg_tcadyn30.htm)
- **145-bus with 50 Generators**: Large dynamic test case with excitation data.
  [UW Archive](https://labs.ece.uw.edu/pstca/dyn50/pg_tcadd50.htm)

#### UIUC / Illinois Synthetic Grids

- **UIUC 150-bus**: 150-bus synthetic grid (IL) with substation GIC data. [ICSEG page](https://icseg.iti.illinois.edu/synthetic-power-cases/uiuc-150-bus-system/)
- **Illinois 200-bus**: 200-bus synthetic Illinois grid (ACTIVSg200). [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg200/) | [ICSEG](http://icseg.iti.illinois.edu/illinois200/)
- **SC 500-bus**: 500-bus synthetic South Carolina grid (ACTIVSg500). [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg500/)
- **Texas 2000-bus**: 2000-bus synthetic ERCOT grid (June 2016). [Electric Grids TAMU](https://icseg.iti.illinois.edu/synthetic-power-cases/texas2000-june2016/)
- **Illini 42 Tornado**: 42-bus fictitious system with tornado scenarios. [ICSEG](http://icseg.iti.illinois.edu/illini-42-tornado/)
- **IlliniGMD 42 HEMP**: 42-bus system for geomagnetic disturbance studies.
  [ICSEG](http://icseg.iti.illinois.edu/illinigmd-42-hemp/)

#### Texas A&M University (TAMU) Synthetic Grids

##### Latest Synthetic Cases (2024-2025)

- **Texas2k Series25**: 2025 level wind, solar, and batteries with improved dynamics. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/texas2k-series25/)
- **Hawaii 37-bus**: Synthetic 138/69 kV transmission network on Oahu footprint. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/hawaii40/)
- **Texas 6717-bus**: Synthetic ERCOT footprint with 345/138/69 kV levels. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/texas7k/) | [With Distribution](https://electricgrids.engr.tamu.edu/texas7k-td/) | [With Gas Pipeline](https://electricgrids.engr.tamu.edu/7k-electric-gas/)
- **Combined East-West US Grid (80,000 buses)**: Synchronously interconnected synthetic eastern and western US.
  [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/combined-synthetic-east-and-west-80000-bus-system-with-synchronously-interconnected-synthetic-eastern-and-western-united-states/)

##### ARPA-E PERFORM Program Cases

- **6717-bus Texas Case and 24,000-bus Midwest Case**: Created for ARPA-E PERFORM program. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/texas-am-perform-cases)
- **All ARPA-E PERFORM Cases**: Complete collection from the program.
  [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/datasets-for-arpa-e-perform-program/)

##### Synthetic Cases (2021-2024)

- **Texas2k Series24**: 2000-bus synthetic Texas grid with improved dynamics. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/activsg2000-dynamics-cases-2024/)
- **EIA-860 Generator Data Cases**: US Energy Information Administration generator data. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/eia-860-generator-data-cases/)
- **Full Texas Gas-Electric Test Case**: 6717 electric buses, 2459 gas nodes. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/7k-electric-gas/)
- **Full Texas T+D**: Very large synthetic transmission & distribution case for ERCOT. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/texas7k-td/)
- **Travis 150-bus T+D**: Travis County, Texas with over 200,000 distribution nodes in OpenDSS. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/combined-td-synthetic-dataset/)
- **ACTIVSg200 Restoration Data**: Restoration scenarios for the Illinois 200-bus system. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/restoration-data-and-scenarios-for-activsg200/)
- **Travis 150 Gas-Electric**: Travis County with associated natural gas pipeline network.
  [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/synthetic-gas-electric-test-case-for-the-travis-150-system/)

##### ARPA-E GridData Program Cases

- **ACTIVSg200**: 200-bus synthetic grid on Central Illinois footprint. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg200/)
- **ACTIVSg500**: 500-bus synthetic grid on South Carolina footprint. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg500/)
- **ACTIVSg2000**: 2000-bus synthetic grid on Texas footprint. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg2000/)
- **ACTIVSg10k**: 10,000-bus synthetic grid on western United States footprint. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg10k/)
- **ACTIVSg25k**: 25,000-bus synthetic grid. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg25k/)
- **ACTIVSg70k**: 70,000-bus synthetic grid. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg70k/)
- **Synthetic PMU Data**: PMU data for the 2000-bus case.
  [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/synthetic-pmu-data/)

##### EPIGRIDS Cases

- **Eastern Network**: 78,484-bus synthetic grid. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/EPIGRIDS-EasternNetwork/)
- **Florida**: 5,658-bus synthetic grid. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/EPIGRIDS-Florida/)
- **Midwest**: 10,192-bus synthetic grid. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/EPIGRIDS-Midwest/)
- **New England**: 250-bus synthetic grid. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/EPIGRIDS-NewEngland/)
- **Synthetic USA**: 82,000-bus synthetic grid. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/EPIGRIDS-SyntheticUSA/)
- **Texas**: 7,336-bus synthetic grid.
  [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/EPIGRIDS-Texas/)

##### GO Competition Cases

- **Tgo500**: 500-bus synthetic test case for GO competition Challenge 1. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/tgo-500/)
- **Tgo2000**: 2000-bus synthetic test case for GO competition Challenge 1. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/tgo2000-bus-synthetic-test-case-for-go-competition-challenge-1/)
- **Tgo10K**: 10,000-bus synthetic test case for GO competition Challenge 1. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/tgo10k-10000-bus-synthetic-test-case-for-go-competition-challenge-1/)
- **Tgo30K**: 30,000-bus synthetic test case for GO competition Challenge 1.
  [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/tgo30k-30000-bus-synthetic-test-case-for-go-competition-challenge-1/)

##### Small Signal Stability Test Cases

- **Three Machines Infinite Bus**: Benchmark system for small signal stability. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/about-us/three-machines-infinite-bus-benchmark-system/) | [ICSEG](http://icseg.iti.illinois.edu/three-machines-infinite-bus-benchmark-system/)
- **Brazilian Seven Bus System**: Seven-bus equivalent model. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/about-us/brazilian-seven-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/brazilian-7-bus-system/)
- **Two-Area (Four-Generator) System**: Four-generator stability test. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/about-us/four-generator-system/) | [ICSEG](http://icseg.iti.illinois.edu/two-area-system-2/)
- **New England IEEE 39-Bus**: IEEE 39-bus for stability analysis. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/about-us/new-england-ieee-39-bus-system/) | [ICSEG](https://icseg.iti.illinois.edu/ieee-39-bus-system/)
- **Simplified 14-Generator Australian Power System**: Australian equivalent system. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/about-us/simplified-14-generator-australian-power-system/) | [ICSEG](http://icseg.iti.illinois.edu/simplified-14-generator-australian-power-system/)
- **New England 68-Bus Test System**: Extended New England system.
  [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/about-us/new-england-68-bus-test-system/) | [ICSEG](http://icseg.iti.illinois.edu/new-england-68-bus-test-system/)

##### Other Synthetic Cases

- **UIUC150**: 150-bus synthetic grid on Tennessee footprint. [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/about-us/uiuc-150-bus-system/)
- **Polish Grid with TAMU Enhancements**: Enhanced Polish system model.
  [Electric Grids TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/polish-grid/)

#### Other Academic Test Cases

- **Kundur Two-Area**: 11-bus two-area stability system from Kundur's textbook. [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/two-area-system) | [ICSEG](http://icseg.iti.illinois.edu/two-area-system/)
- **WSCC 9-bus**: 9-bus Western Systems case with 3 generators.
  [TAMU Electric Grids](https://electricgrids.engr.tamu.edu/about-us/wscc-9-bus-system/) | [ICSEG](http://icseg.iti.illinois.edu/wscc-9-bus-system/)

#### NREL Test Case Repository

- **9-Bus 3-Generator Test System**: Simple approximation of WECC to 9-bus equivalent. [NREL Repository](https://www.nrel.gov/grid/test-case-repository)
- **18-Bus 4-Area Test System**: GE PSLF demonstration system with wind and battery. [NREL Repository](https://www.nrel.gov/grid/test-case-repository)
- **240-Bus WECC Test System**: Reduced WECC model with high renewables and dynamics.
  [NREL OSL Contest Cases](https://www.nrel.gov/media/docs/libraries/grid/wecc-osl.zip?sfvrsn=f85a054e_1)

#### University of Cyprus - Dynamic IEEE Test Systems

- **IEEE 9-Bus Dynamic**: WSCC 9-bus with dynamic models. [KIOS Cyprus](https://www2.kios.ucy.ac.cy/testsystems/index.php/ieee-9-bus-modified-test-system/)
- **IEEE 14-Bus Dynamic**: IEEE 14-bus with dynamic parameters. [KIOS Cyprus](https://www2.kios.ucy.ac.cy/testsystems/index.php/ieee-14-bus-modified-test-system/)
- **IEEE 30-Bus Dynamic**: IEEE 30-bus with dynamic models. [KIOS Cyprus](https://www2.kios.ucy.ac.cy/testsystems/index.php/ieee-30-bus-modified-test-system/)
- **IEEE 39-Bus Dynamic**: New England 39-bus with dynamic parameters. [KIOS Cyprus](https://www2.kios.ucy.ac.cy/testsystems/index.php/ieee-39-bus-modified-test-system/)
- **IEEE 57-Bus Dynamic**: IEEE 57-bus with dynamic models. [KIOS Cyprus](https://www2.kios.ucy.ac.cy/testsystems/index.php/ieee-57-bus-modified-test-system/)
- **IEEE 118-Bus Dynamic**: IEEE 118-bus with dynamic parameters. [KIOS Cyprus](https://www2.kios.ucy.ac.cy/testsystems/index.php/ieee-118-bus-modified-test-system/)
- **IEEE 300-Bus Dynamic**: IEEE 300-bus with dynamic models.
  [KIOS Cyprus](https://www2.kios.ucy.ac.cy/testsystems/index.php/ieee-300-bus-modified-test-system/)

#### ALSETLab - Nordic Test Systems

- **Nordic 44**: Equivalent Nordic grid model with market data processing tools.
  [GitHub Repository](https://github.com/ALSETLab/Nordic44-Nordpool/tree/master/nordic44/models)

#### European Test Systems

- **Danish Static Power System Model**: 2020 Danish transmission system model. [Energinet](https://web.archive.org/web/20160212020359/http://www.energinet.dk/EN/El/Nyheder/Sider/Nu-kan-du-downloade-data-om-det-danske-elsystem-i-2020.aspx)
  Dataset seems to be no longer released. Could also check Danish Energi dataset on [transmission lines](https://www.energidataservice.dk/tso-electricity/Transmissionlines) (also discontinued) or their currently active [data catalog](https://en.energinet.dk/energy-data/data-catalog/).
- **Continental Europe Dynamic Model**: ENTSO-E full continental Europe power system. [ENTSO-E](https://www.entsoe.eu/publications/system-operations-reports/continental-europe/Initial-Dynamic-Model/Pages/default.aspx) (Restricted access)

#### University of Edinburgh / Strathclyde

*Note: University of Edinburgh test systems are only available in MATPOWER format, not in PowerWorld, PSSE, or PSLF formats.*

- **GB full network (2224 buses)**: Transmission operations. [Edinburgh Network](https://webhomes.maths.ed.ac.uk/OptEnergy/NetworkData/fullGB/)
- **GB reduced network (29 buses)**: Simplified UK grid. [Edinburgh Network](https://webhomes.maths.ed.ac.uk/OptEnergy/NetworkData/reducedGB/)
- **Revised Reduced GB Network (29 buses)**: Updated reduced UK grid model. [Edinburgh Network](https://webhomes.maths.ed.ac.uk/OptEnergy/NetworkData/rev_reducedGB/)
- **Iceland 118-bus**: Static and PSAT dynamics. [Edinburgh Network Static](https://webhomes.maths.ed.ac.uk/OptEnergy/NetworkData/iceland/) | [Edinburgh Network Dynamic](https://webhomes.maths.ed.ac.uk/OptEnergy/NetworkData/icelandDyn/)
- **Irish Network**: Ireland electricity transmission network.
  [Edinburgh Network](https://webhomes.maths.ed.ac.uk/OptEnergy/NetworkData/Ireland/)

