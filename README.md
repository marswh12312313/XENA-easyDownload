# XENA Cancer Sequencing Cohort Data Downloader

This Python script automates the process of downloading cancer sequencing cohort research data from the XENA platform. The script parses a JSON file containing the data dictionary and organizes the downloaded files into a structured directory hierarchy based on cohort and dataset titles.

## Features

- Automatically downloads all available cancer sequencing cohort research data from XENA
- Organizes downloaded files into a structured directory hierarchy
- Supports downloading transcriptome, point mutation, copy number, and chromatin accessibility data
- Provides progress updates during the download process
- Skips downloading files that already exist and are not empty
- Generates a summary of the total files downloaded and the total size of the downloaded files

## Prerequisites

- Python 3.x
- `aria2c` command-line download utility (install instructions below)

## Installation

1. Clone the repository or download the script file.

2. Install the required dependencies:
   - Python 3.x: [Download Python](https://www.python.org/downloads/)
   - `aria2c` command-line download utility:
     - For Ubuntu/Debian: `sudo apt-get install aria2`
     - For macOS (using Homebrew): `brew install aria2`
     - For Windows: [Download aria2](https://aria2.github.io/)

3. Prepare the JSON file containing the data dictionary:
   - The JSON file should have a structure similar to the example provided in `filtered_output_dict.json`.
   - Replace the `json_file_path` variable in the script with the path to your JSON file.

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory where the script is located.

3. Run the script using the following command:
   ```
   python download.py
   ```

4. The script will start downloading the files based on the information in the JSON file.

5. Progress updates will be displayed in the console, including the number of files downloaded, the URL of the current file being downloaded, the size of each downloaded file, and the total size of all downloaded files.

6. Once the download is completed, a summary will be displayed, showing the total number of files downloaded and the total size of the downloaded files.

7. The downloaded files will be organized into a structured directory hierarchy based on the cohort and dataset titles.

## Directory Structure

The downloaded files will be organized into the following directory structure:
```
.
├── A_combined_cohort_of_TCGA,_TARGET_and_GTEx_samples
│   ├── gene_expression_RNAseq_-_RSEM_expected_count
│   │   ├── probeMap%2Fgencode.v23.annotation.gene.probemap.json
│   │   ├── TcgaTargetGtex_gene_expected_count.gz
│   │   └── TcgaTargetGtex_gene_expected_count.json
│   ├── gene_expression_RNAseq_-_RSEM_expected_count_DESeq2_standardized
│   │   ├── probeMap%2Fgencode.v23.annotation.gene.probemap.json
│   │   ├── TCGA-GTEx-TARGET-gene-exp-counts.deseq2-normalized.log2.gz
│   │   └── TCGA-GTEx-TARGET-gene-exp-counts.deseq2-normalized.log2.json
│   ├── gene_expression_RNAseq_-_RSEM_fpkm
│   │   ├── probeMap%2Fgencode.v23.annotation.gene.probemap.json
│   │   ├── TcgaTargetGtex_rsem_gene_fpkm.gz
│   │   └── TcgaTargetGtex_rsem_gene_fpkm.json
│   ├── gene_expression_RNAseq_-_RSEM_norm_count
│   │   ├── probeMap%2Fhugo_gencode_good_hg38_v23comp_probemap.json
│   │   ├── TcgaTargetGtex_RSEM_Hugo_norm_count.gz
│   │   └── TcgaTargetGtex_RSEM_Hugo_norm_count.json
│   ├── gene_expression_RNAseq_-_RSEM_tpm
│   │   ├── probeMap%2Fgencode.v23.annotation.gene.probemap.json
│   │   ├── TcgaTargetGtex_rsem_gene_tpm.gz
│   │   └── TcgaTargetGtex_rsem_gene_tpm.json
│   ├── phenotype_-_TCGA_GTEX_main_categories
│   │   ├── TCGA_GTEX_category.txt
│   │   └── TCGA_GTEX_category.txt.json
│   ├── ...
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The XENA platform for providing access to the cancer sequencing cohort research data.
- The `aria2c` command-line download utility for efficient file downloads.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## Disclaimer

This script is provided as-is without any warranty. Use it at your own risk. The authors and contributors are not responsible for any damage or loss caused by the use of this script.
