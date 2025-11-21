# Visualization SOP: Viewing HFO Architecture

## Option 1: The Custom HTML Viewer (Recommended)
We have created a standalone HTML viewer that supports tabs and infinite zooming.
1. Open `hfo_gem/gen_35/diagram_viewer.html` in VS Code.
2. Right-click the file tab and select **"Open in Default Browser"** (if available) or use the **"Live Server"** extension if you have it.
3. Alternatively, reveal the file in your OS file explorer and double-click it to open in Chrome/Edge/Firefox.

## Option 2: VS Code Extension (Simpler Integration)
If you prefer to stay strictly within VS Code without managing HTML files:

1. **Install Extension**:
   - Open the Extensions view (Ctrl+Shift+X).
   - Search for `Mermaid Chart Preview`.
   - Install the one by **namnguyen240795** (ID: `namnguyen240795.mermaid-chart-preview`).
   - *Why this one?* It explicitly supports Pan & Zoom, which is critical for our large diagrams.

2. **Usage**:
   - Open `hfo_gem/gen_35/README.md`.
   - Place your cursor inside a mermaid code block.
   - Press `Ctrl+Shift+P` and run **"Mermaid: Preview"** (or look for a button/lens if the extension provides one).
   - You should see a preview pane with zoom controls.

## Option 3: Export to SVG (For Documentation)
If you need static files to share:
1. We can install the Mermaid CLI: `npm install -g @mermaid-js/mermaid-cli`
2. Run: `mmdc -i hfo_gem/gen_35/README.md -o hfo_gem/gen_35/architecture.svg`
