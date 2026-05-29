# Columbia Off-Campus Residential Traffic

Static website for the Columbia off-campus residential traffic dataset project. The site describes the dataset, approved usage, collection methodology, findings, publications, and contact information.

## Contents

- `index.html` - project overview and related publications
- `datadescription.html` - dataset description and sharing details
- `approved.html` - approved data usage information
- `methodology.html` - collection, anonymization, and service-mapping methodology
- `findings.html` - analysis results and figures
- `contact.html` - project contact page
- `figures/` - logos, diagrams, and result images used by the site
- `*.css` - page-specific and shared styles

## Viewing Locally

Open `index.html` directly in a browser, or serve the folder with a simple static server:

```sh
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Editing

This project has no build step or package dependencies. Update the relevant `.html` file, adjust the matching `.css` file when styling changes are needed, and keep image references relative to the site root, such as `./figures/example.png`.

## Attribution

The website presents research from Columbia University on Internet service usage and delivery in an off-campus residential network.
