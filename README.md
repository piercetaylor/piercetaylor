<h1 align="center">Pierce Taylor</h1>

<p align="center">
  Computational biologist working on transcription-factor structure and DNA recognition, NGS pipelines, and reproducible workflows for plant science.
</p>

<p align="center">
  <a href="mailto:pmt5gt@umsystem.edu">
    <img src="https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://orcid.org/0009-0003-5125-5716">
    <img src="https://img.shields.io/badge/ORCID-0009--0003--5125--5716-A6CE39?style=for-the-badge&logo=orcid&logoColor=white" alt="ORCID" />
  </a>
  <a href="https://www.linkedin.com/in/pierce-taylor">
    <img src="https://img.shields.io/badge/LinkedIn-pierce--taylor-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://github.com/piercetaylor">
    <img src="https://img.shields.io/github/followers/piercetaylor?style=for-the-badge&label=Followers&color=24292f" alt="GitHub followers" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white" alt="R" />
  <img src="https://img.shields.io/badge/Snakemake-Workflows-039475?style=flat-square" alt="Snakemake" />
  <img src="https://img.shields.io/badge/Structural-Biology-1F6FEB?style=flat-square" alt="Structural biology" />
  <img src="https://img.shields.io/badge/Molecular-Dynamics-7C3AED?style=flat-square" alt="Molecular dynamics" />
  <img src="https://img.shields.io/badge/NGS-Bioinformatics-0A7EA4?style=flat-square" alt="NGS bioinformatics" />
  <img src="https://img.shields.io/badge/Single--Cell-Omics-0F766E?style=flat-square" alt="Single-cell omics" />
  <img src="https://img.shields.io/badge/Plant-Science-16A34A?style=flat-square" alt="Plant science" />
  <img src="https://img.shields.io/badge/HPC-Slurm-B45309?style=flat-square" alt="HPC" />
</p>

## About Me

<table>
<tr>
<td valign="top" width="55%">

- I work at the intersection of structural biology, genomics, and software engineering, mostly in plants.
- M.S. candidate in Plant, Insect & Microbial Sciences at the [University of Missouri](https://cafnr.missouri.edu/) (Mendoza-Cózatl Lab), with a Graduate Certificate in Health Data Science. Transferred in from Computer Engineering at Missouri S&T.
- Thesis: structure-guided mutagenesis of ILR3, a bHLH regulator of iron homeostasis in *Arabidopsis* — AlphaFold3/Chai-1 modeling, FoldX and HADDOCK, MD simulation, then DAP-seq, EMSA, and MST to test the predictions.
- I designed and teach PLNT_SCI 7001, a graduate NGS bioinformatics course (read QC through differential expression, peak calling, and single-cell analysis on an HPC cluster).
- I build the pipelines and tools behind that work — Snakemake workflows, analysis scripts, and small applications for breeders and lab groups — and try to keep every result reproducible from primary data.
- Co-founder at [Nexession](https://nexession.com). Open to collaboration on computational structural biology, plant genomics, and research software.

</td>
<td valign="top" width="45%">

**Current focus**

- Transcription-factor / DNA recognition in plant bHLHs
- AlphaFold3 → MD workflows (GROMACS, AMBER)
- DAP-seq, RNA-seq, and scRNA-seq pipelines in Snakemake
- Comparative structural biology of carnivorous-plant digestive enzymes
- Decision-support tools for marker-assisted breeding

**Methods I use**

- AlphaFold3, Chai-1, FoldX, HADDOCK, APBS, EVcouplings
- GROMACS, AMBER, CryoSPARC, ChimeraX
- Scanpy / Seurat, MEME-ChIP, Bioconductor
- Y2H, EMSA, MST, In-Fusion / Gateway cloning

</td>
</tr>
</table>

## Featured Work

<table width="100%">
<thead>
<tr><th align="left">Project</th><th align="left">Stack</th><th align="left">★</th><th align="left">What it does</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/piercetaylor/CarnivorEnzyme">CarnivorEnzyme</a></td>
<td><img alt="Python" src="https://img.shields.io/badge/python-3776AB?style=flat-square&logo=python&logoColor=white"> <img alt="Snakemake" src="https://img.shields.io/badge/snakemake-039475?style=flat-square"></td>
<td><img alt="Stars" src="https://img.shields.io/github/stars/piercetaylor/CarnivorEnzyme?style=flat-square&label=%20"></td>
<td>Predicts 3D structures of digestive enzymes from independently evolved carnivorous plant lineages. AlphaFold3 structures, FoldX ΔΔG, EVmutation, and AutoDock Vina docking, orchestrated with Snakemake behind a Streamlit interface.</td>
</tr>
<tr>
<td><a href="https://github.com/piercetaylor/af3-to-amber-md-sim">af3-to-amber-md-sim</a></td>
<td><img alt="Shell" src="https://img.shields.io/badge/shell-89e051?style=flat-square&logo=gnubash&logoColor=black"> <img alt="AMBER" src="https://img.shields.io/badge/AMBER%2024-7C3AED?style=flat-square"></td>
<td><img alt="Stars" src="https://img.shields.io/github/stars/piercetaylor/af3-to-amber-md-sim?style=flat-square&label=%20"></td>
<td>Takes an AlphaFold3 protein–DNA model through ChimeraX preparation, <code>tleap</code> topology building, solvation, equilibration, and GPU production MD on a Slurm cluster. Wild-type and mutant systems run side by side.</td>
</tr>
<tr>
<td><a href="https://github.com/piercetaylor/ml-methods-health-data">ml-methods-health-data</a></td>
<td><img alt="Python" src="https://img.shields.io/badge/python-3776AB?style=flat-square&logo=python&logoColor=white"> <img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white"></td>
<td><img alt="Stars" src="https://img.shields.io/github/stars/piercetaylor/ml-methods-health-data?style=flat-square&label=%20"></td>
<td>Four machine learning method families on public medical data — classification, clustering, association rules, and regression — sharing one gated pipeline with a paired leakage comparison.</td>
</tr>
<tr>
<td><a href="https://github.com/piercetaylor/brain-mri-imaging">brain-mri-imaging</a></td>
<td><img alt="Jupyter" src="https://img.shields.io/badge/jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white"> <img alt="CNN" src="https://img.shields.io/badge/CNN-EE4C2C?style=flat-square&logo=pytorch&logoColor=white"></td>
<td><img alt="Stars" src="https://img.shields.io/github/stars/piercetaylor/brain-mri-imaging?style=flat-square&label=%20"></td>
<td>Reads 59,713 DICOM headers to report what would stop a glioblastoma cohort being pooled, then trains a convolutional network on 32×32 patches of axial T1 post-contrast slices. The QC half establishes what the classifier is entitled to assume.</td>
</tr>
<tr>
<td><a href="https://github.com/piercetaylor/corn-nutrient-response">corn-nutrient-response</a></td>
<td><img alt="R" src="https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white"></td>
<td><img alt="Stars" src="https://img.shields.io/github/stars/piercetaylor/corn-nutrient-response?style=flat-square&label=%20"></td>
<td>Multivariate analysis of a 34 site-year Nebraska corn fertilizer trial, testing whether applied phosphorus and potassium raised grain yield once nitrogen, stand, and irrigation were accounted for.</td>
</tr>
<tr>
<td><a href="https://github.com/piercetaylor/muidsi-hackathon-2026">muidsi-hackathon-2026</a></td>
<td><img alt="Python" src="https://img.shields.io/badge/python-3776AB?style=flat-square&logo=python&logoColor=white"> <img alt="LangGraph" src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white"></td>
<td><img alt="Stars" src="https://img.shields.io/github/stars/piercetaylor/muidsi-hackathon-2026?style=flat-square&label=%20"></td>
<td>AgriFlow — a LangGraph agent that answers natural-language questions about Missouri food supply chains across crop, census, disaster, and weather data. Built for the MUIDSI Hackathon 2026.</td>
</tr>
</tbody>
</table>

### Collaborations

<table width="100%">
<thead>
<tr><th align="left">Project</th><th align="left">Role</th><th align="left">What it does</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/ChimdiWalter/alveolar-dispersion-covid19">alveolar-dispersion-covid19</a></td>
<td>Joint work with <a href="https://github.com/ChimdiWalter">@ChimdiWalter</a></td>
<td>Trajectory analysis of alveolar epithelial state coherence in lethal COVID-19. Dispersion-dominated loss of homeostatic identity, replicated across 618 donors and 35 datasets. Development continues in the upstream repository.</td>
</tr>
</tbody>
</table>

### CarnivorEnzyme

Build the structural atlas for one lineage and score the stability of every substitution:

```bash
snakemake --profile profiles/slurm --config lineage=Nepenthes
streamlit run app/main.py
```

### af3-to-amber-md-sim

Prepare an AlphaFold3 model, then run the wild-type and mutant systems through equilibration and production MD:

```bash
chimerax --nogui chimerax/prep_and_mutate.cxc
tleap -f inputs/tleap_WT.in
sbatch slurm/01_minimize.sh && sbatch slurm/02_heat.sh
sbatch --dependency=afterok:$JOBID slurm/03_production.sh
```

## Pinned Repositories

<p>
  <a href="https://github.com/piercetaylor/CarnivorEnzyme">
    <img src="https://github-readme-stats-fast.vercel.app/api/pin/?username=piercetaylor&repo=CarnivorEnzyme&theme=tokyonight&hide_border=true" alt="CarnivorEnzyme" />
  </a>
  <a href="https://github.com/piercetaylor/af3-to-amber-md-sim">
    <img src="https://github-readme-stats-fast.vercel.app/api/pin/?username=piercetaylor&repo=af3-to-amber-md-sim&theme=tokyonight&hide_border=true" alt="af3-to-amber-md-sim" />
  </a>
</p>
<p>
  <a href="https://github.com/piercetaylor/ml-methods-health-data">
    <img src="https://github-readme-stats-fast.vercel.app/api/pin/?username=piercetaylor&repo=ml-methods-health-data&theme=tokyonight&hide_border=true" alt="ml-methods-health-data" />
  </a>
  <a href="https://github.com/piercetaylor/brain-mri-imaging">
    <img src="https://github-readme-stats-fast.vercel.app/api/pin/?username=piercetaylor&repo=brain-mri-imaging&theme=tokyonight&hide_border=true" alt="brain-mri-imaging" />
  </a>
</p>

## GitHub Dashboard

<p align="center">
  <img height="170" src="https://github-readme-stats-fast.vercel.app/api?username=piercetaylor&show_icons=true&theme=tokyonight&hide_border=true&rank_icon=github" alt="GitHub stats" />
  <img height="170" src="https://streak-stats.demolab.com?user=piercetaylor&theme=tokyonight&hide_border=true" alt="GitHub streak" />
</p>

<p align="center">
  <img height="165" src="https://github-readme-stats-fast.vercel.app/api/top-langs/?username=piercetaylor&layout=compact&theme=tokyonight&hide_border=true" alt="Top languages" />
  <img height="165" src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=piercetaylor&theme=tokyonight&utcOffset=-5" alt="Productive time" />
</p>

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=piercetaylor&theme=tokyonight" alt="Repositories per language" />
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=piercetaylor&theme=tokyonight" alt="Most committed language" />
</p>

<p align="center">
  <img src="https://github-profile-trophy.screw-hand.vercel.app/?username=piercetaylor&theme=algolia&no-frame=true&no-bg=true&row=1&column=6" alt="GitHub trophies" />
</p>

## Recent Activity

<table><tr><td valign="top" width="50%">

**Latest releases**
<!-- recent_releases starts -->
No tagged releases yet.
<!-- recent_releases ends -->

</td><td valign="top" width="50%">

**Recently pushed**
<!-- recent_activity starts -->
[piercetaylor](https://github.com/piercetaylor/piercetaylor) - 2026-09-06

[ml-methods-health-data](https://github.com/piercetaylor/ml-methods-health-data) - 2026-09-04

[CarnivorEnzyme](https://github.com/piercetaylor/CarnivorEnzyme) - 2026-09-02

[brain-mri-imaging](https://github.com/piercetaylor/brain-mri-imaging) - 2026-09-02

[af3-to-amber-md-sim](https://github.com/piercetaylor/af3-to-amber-md-sim) - 2026-09-01

[corn-nutrient-response](https://github.com/piercetaylor/corn-nutrient-response) - 2026-08-27
<!-- recent_activity ends -->

</td></tr></table>

<p align="right">
  <a href="https://github.com/piercetaylor/piercetaylor/actions/workflows/build.yml"><img src="https://github.com/piercetaylor/piercetaylor/actions/workflows/build.yml/badge.svg" alt="Build README" /></a>
</p>

These two lists are rewritten each night by [`build_readme.py`](build_readme.py), running from
[a scheduled Action](.github/workflows/build.yml) in this repository. It reads only public
repositories, and commits only when something has actually changed.

## Pipelines and Course Material

Teaching material and the Snakemake workflows are being prepared for release. The course
repository for PLNT_SCI 7001 and the DAP-seq, RNA-seq, and scRNA-seq pipelines will be linked
here as each is published.

<!--
Planned repositories — uncomment a row once the repository is public, so that the link and the
star badge both resolve.

| Repository | Type | Description |
| --- | --- | --- |
| [PLNT_SCI-7001](https://github.com/piercetaylor/PLNT_SCI-7001) | Course | Graduate NGS bioinformatics course I designed and teach at Mizzou: lectures, HPC exercises, and worked pipelines for RNA-seq, ChIP/DAP-seq, and scRNA-seq. |
| [snakemake-dapseq](https://github.com/piercetaylor/snakemake-dapseq) | Pipeline | DAP-seq from FASTQ to peaks, motifs (MEME-ChIP/FIMO), and gene targets against Araport11, with a pure-Python peak-to-gene join. |
| [snakemake-rnaseq](https://github.com/piercetaylor/snakemake-rnaseq) | Pipeline | Bulk RNA-seq: QC, trimming, STAR/Salmon, DESeq2, and report generation. |
| [snakemake-scrnaseq](https://github.com/piercetaylor/snakemake-scrnaseq) | Pipeline | scRNA-seq: Cell Ranger/STARsolo, QC, integration, clustering, and annotation with Scanpy. |
| [af3-gromacs-md](https://github.com/piercetaylor/af3-gromacs-md) | Pipeline | AlphaFold3 model to GROMACS MD as a Snakemake workflow with Slurm profiles. |
| [ilr3-structural-mutagenesis](https://github.com/piercetaylor/ilr3-structural-mutagenesis) | Thesis | Structure-guided mutagenesis of the Arabidopsis bHLH ILR3: AF3/Chai-1 dimer-DNA models, FoldX PositionScan, HADDOCK, EVcouplings, APBS, and WT vs. K76A/E80A/R84A MD, with the DAP-seq and MST analysis behind the thesis. |
| [covid19-lung-snrnaseq](https://github.com/piercetaylor/covid19-lung-snrnaseq) | Single-cell | Reanalysis of the Melms et al. 2021 COVID-19 lung atlas (snRNA-seq): QC, integration, cell-type annotation, and differential abundance. |
| [cdtb-cryoem](https://github.com/piercetaylor/cdtb-cryoem) | Cryo-EM | CryoSPARC processing of *C. difficile* CDTb: 501 micrographs, 31,175 particles, 4.4 A map with C7 symmetry. BIOCHEM 9200. |
| [isoline-browser](https://github.com/piercetaylor/isoline-browser) | TypeScript, React | Browser-only NIL evaluation against the recurrent parent: parent-of-origin calls, recurrent-parent proportion, donor segments, linkage-drag bounds, graphical genotypes. |
| [progeny-selector](https://github.com/piercetaylor/progeny-selector) | Python, NumPy, Shiny | Marker-assisted backcross selection: foreground and background scoring, recombinant flanks, weighted ranking, and next-round sample manifests. |
| [field-capture-android](https://github.com/piercetaylor/field-capture-android) | Kotlin, Compose, Room | Offline-first field app for public breeders: geotagged spoken plot notes at the planter, GPS-tracked video walks, Field Book-compatible import/export, weather and soil layers. |
| [netbox-drift](https://github.com/piercetaylor/netbox-drift) | Network automation | Operational-state drift detection and reconciliation for NetBox Community Edition: NAPALM and gNMI collectors, three-way diff engine, deviation lifecycle, Prometheus metrics, containerlab CI. |
-->

## Research and Tooling Stack

<p>
  <img src="https://img.shields.io/badge/Workflow-Snakemake%20%2B%20Slurm-039475?style=flat-square" alt="Workflow" />
  <img src="https://img.shields.io/badge/Structure-AlphaFold3%20%2F%20Chai--1-1F6FEB?style=flat-square" alt="Structure prediction" />
  <img src="https://img.shields.io/badge/MD-GROMACS%20%2F%20AMBER-7C3AED?style=flat-square" alt="Molecular dynamics" />
  <img src="https://img.shields.io/badge/Energetics-FoldX%20%2F%20HADDOCK-0891B2?style=flat-square" alt="Energetics and docking" />
  <img src="https://img.shields.io/badge/NGS-DAP--seq%20%2F%20RNA--seq-0A7EA4?style=flat-square" alt="NGS" />
  <img src="https://img.shields.io/badge/Single--Cell-Scanpy%20%2F%20Seurat-0F766E?style=flat-square" alt="Single-cell" />
  <img src="https://img.shields.io/badge/Cryo--EM-CryoSPARC-B45309?style=flat-square" alt="Cryo-EM" />
  <img src="https://img.shields.io/badge/Wet_lab-EMSA%20%2F%20MST%20%2F%20Y2H-DC2626?style=flat-square" alt="Wet lab" />
  <img src="https://img.shields.io/badge/Practice-Reproducibility-16A34A?style=flat-square" alt="Reproducibility" />
</p>

## Elsewhere

[![LinkedIn](https://img.shields.io/badge/LinkedIn-pierce--taylor-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pierce-taylor)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--5125--5716-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0009-0003-5125-5716)
[![Nexession](https://img.shields.io/badge/Nexession-website-1F6FEB?style=flat-square)](https://nexession.com)
[![Repositories](https://img.shields.io/badge/GitHub-repositories-24292f?style=flat-square&logo=github&logoColor=white)](https://github.com/piercetaylor?tab=repositories)
[![Stars](https://img.shields.io/badge/GitHub-stars-24292f?style=flat-square&logo=github&logoColor=white)](https://github.com/piercetaylor?tab=stars)

## Collaboration

If you are working on transcription-factor structure, plant genomics pipelines, or open-source
tools for breeding programs and research labs, feel free to reach out.
