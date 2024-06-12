// import marked from 'https://cdn.jsdelivr.net/npm/marked/marked.min.js';

document.addEventListener('DOMContentLoaded', () => {
    const markdownId = "10"; // Replace with the specific ID you want to fetch


    fetch(`/markdown/${markdownId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch Markdown content');
            }
            return response.text();
        })
        .then(markdown => {
            const htmlContent = marked.parse(markdown); // Use marked.marked to access the functionality
          
           
            document.getElementById('markdown-content').innerHTML = htmlContent;


            // Placeholder logic for extraction (replace with actual logic)
            const leanProof = "Lean proof content here"; 
            const humanExplanation = "Human explanation here";
            // const buttonID = 'ID'
          
          
            // document.getElementById('button').innerHTML = buttonID;
           
            // buttonID.addEventListener('click', () => {
            //     markdownId = i + 1;
            // });
            document.getElementById('lean-proof').innerHTML = leanProof;
            document.getElementById('human-explanation').innerHTML = humanExplanation;
            // const button = document.createElement('button');
         
            
            // Auto-render LaTeX math in the rendered HTML
               renderMathInElement(document.body, {
                    delimiters: [
                        { left: "$$", right: "$$", display: true },
                        { left: "\\[", right: "\\]", display: true },
                        { left: "$", right: "$", display: false },
                        { left: "\\(", right: "\\)", display: false }
                    ]
                });
        })
        .catch(error => console.error('Error fetching or converting Markdown:', error));
});
