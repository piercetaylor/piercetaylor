# Pierce Taylor

I am a master's student in Plant, Insect and Microbial Sciences at the University of Missouri,
working in the Mendoza-Cózatl Lab, with a graduate certificate in Health Data Science. I came to
plant science from computer engineering at Missouri S&T, and most of what I do sits between the
two: predicting how plant transcription factors recognize DNA, then building the pipelines that
test those predictions at the bench.


I designed and teach PLNT_SCI 7001, a graduate NGS bioinformatics course that runs from read QC
through differential expression, peak calling and single-cell analysis on the university's Slurm
cluster. I also co-founded [Nexession](https://nexession.com).

## Projects

| Project | What it does |
| --- | --- |
| [CarnivorEnzyme](https://github.com/piercetaylor/CarnivorEnzyme) | Structural atlas of digestive enzymes from carnivorous plant lineages that evolved carnivory independently. AlphaFold3 structures, FoldX stability scoring, EVmutation and AutoDock Vina docking, run as a Snakemake workflow. |
| [af3-to-amber-md-sim](https://github.com/piercetaylor/af3-to-amber-md-sim) | Takes an AlphaFold3 protein–DNA model through ChimeraX cleanup, `tleap` topology building, and a staged equilibration and production MD run on a Slurm cluster, for a wild-type and a mutant system in parallel. |
| [ml-methods-health-data](https://github.com/piercetaylor/ml-methods-health-data) | Classification, clustering, association rules and regression on public medical data, sharing one gated pipeline. Includes a paired comparison of each method with and without target leakage. |
| [brain-mri-imaging](https://github.com/piercetaylor/brain-mri-imaging) | Reads 59,713 DICOM headers to report what would stop a glioblastoma cohort being pooled, then trains a convolutional network on 32×32 tumor patches from axial T1 post-contrast slices. |
| [corn-nutrient-response](https://github.com/piercetaylor/corn-nutrient-response) | Multivariate analysis of a 34 site-year Nebraska fertilizer trial, testing whether applied phosphorus and potassium raised grain yield once nitrogen supply, plant stand and irrigation were accounted for. |
| [muidsi-hackathon-2026](https://github.com/piercetaylor/muidsi-hackathon-2026) | AgriFlow, a LangGraph agent that answers questions about Missouri food supply chains from crop, census, disaster and weather data. Fourth place, MUIDSI Hackathon 2026. |

Several of these began as graduate coursework and were rebuilt from public data; each repository
names the course and the term it came from.

I also work with [@ChimdiWalter](https://github.com/ChimdiWalter) on
[alveolar-dispersion-covid19](https://github.com/ChimdiWalter/alveolar-dispersion-covid19), a
trajectory analysis of alveolar epithelial state coherence in lethal COVID-19.

Snakemake workflows for DAP-seq, RNA-seq and scRNA-seq, and the PLNT_SCI 7001 course material,
are not public yet. They will be linked here as they are released.

[Email](mailto:pmt5gt@umsystem.edu) ·
[ORCID](https://orcid.org/0009-0003-5125-5716) ·
[LinkedIn](https://www.linkedin.com/in/pierce-taylor)

<!--
Descriptions held for repositories that are not public yet. Move a line into the Projects table
once the repository is released.

PLNT_SCI-7001 — graduate NGS bioinformatics course: lectures, HPC exercises, and worked RNA-seq, ChIP/DAP-seq and scRNA-seq pipelines.
snakemake-dapseq — DAP-seq from FASTQ to peaks, motifs (MEME-ChIP/FIMO) and gene targets against Araport11, with a pure-Python peak-to-gene join.
snakemake-rnaseq — bulk RNA-seq: QC, trimming, STAR/Salmon, DESeq2 and report generation.
snakemake-scrnaseq — scRNA-seq: Cell Ranger/STARsolo, QC, integration, clustering and annotation with Scanpy.
af3-gromacs-md — AlphaFold3 model to GROMACS MD as a Snakemake workflow with Slurm profiles.
ilr3-structural-mutagenesis — the thesis work: AF3/Chai-1 dimer-DNA models, FoldX PositionScan, HADDOCK, EVcouplings, APBS, and WT vs. K76A/E80A/R84A MD, with the DAP-seq and MST analysis.
covid19-lung-snrnaseq — reanalysis of the Melms et al. 2021 COVID-19 lung atlas: QC, integration, cell-type annotation and differential abundance.
cdtb-cryoem — CryoSPARC processing of C. difficile CDTb: 501 micrographs, 31,175 particles, 4.4 A map with C7 symmetry. BIOCHEM 9200.
isoline-browser — browser-only NIL evaluation against the recurrent parent: parent-of-origin calls, recurrent-parent proportion, donor segments, linkage-drag bounds, graphical genotypes.
progeny-selector — marker-assisted backcross selection: foreground and background scoring, recombinant flanks, weighted ranking, next-round sample manifests.
field-capture-android — offline-first field app for public breeders: geotagged spoken plot notes, GPS-tracked video walks, Field Book-compatible import/export, weather and soil layers.
netbox-drift — operational-state drift detection for NetBox Community Edition: NAPALM and gNMI collectors, three-way diff engine, deviation lifecycle, Prometheus metrics, containerlab CI.
-->
