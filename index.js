import express from 'express';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import fs from 'fs/promises'; // Using fs.promises for async file operations

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
const port = process.env.PORT || 3000;

// Define paths for Express config
const publicDirectoryPath = join(__dirname, 'website');
const outputDirectoryPath = join(__dirname, 'output');

// Serve static files from the 'website' directory
app.use(express.static(publicDirectoryPath));

// Route to serve markdown files dynamically based on ID
app.get('/markdown/:id', async (req, res) => {
    try {
        const markdownFilePath = join(outputDirectoryPath, `${req.params.id}.md`);
        const markdownContent = await fs.readFile(markdownFilePath, 'utf-8');
        res.send(markdownContent);
    } catch (error) {
        console.error('Error reading markdown file:', error);
        res.status(500).send('Error fetching markdown file');
    }
});

// Catch-all route to serve 'index.html'
app.get('*', (req, res) => {
    res.sendFile(join(publicDirectoryPath, 'index.html'));
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
