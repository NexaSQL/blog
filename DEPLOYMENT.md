# 🚀 Deployment Guide - GitHub Pages

## Quick Start

1. **Push to GitHub Repository**
   ```bash
   git add .
   git commit -m "Add NexaSQL blog with dynamic post loading"
   git push origin main
   ```

2. **Enable GitHub Pages**
   - Go to your repository settings
   - Scroll to "Pages" section
   - Select "Deploy from a branch"  
   - Choose "main" branch
   - Select "/ (root)" folder
   - Click "Save"

3. **Access Your Blog**
   - Your blog will be available at: `https://yourusername.github.io/repository-name/`
   - Individual articles: `https://yourusername.github.io/repository-name/post.html?slug=article-slug`

## Local Testing

To test locally before deploying:

1. **Simple HTTP Server (Python)**
   ```bash
   # Python 3
   python -m http.server 8000

   # Then open: http://localhost:8000
   ```

2. **Node.js HTTP Server**
   ```bash
   npx http-server
   ```

3. **Live Server (VS Code Extension)**
   - Install "Live Server" extension
   - Right-click on index.html
   - Select "Open with Live Server"

## File Structure for GitHub Pages

Make sure your repository has this structure:
```
repository-name/
├── index.html
├── post.html
├── app.js
├── style.css
├── README.md
└── posts/
    ├── index.json
    └── *.json (your articles)
```

## Troubleshooting

**Blog not loading?**
- Check GitHub Pages is enabled in repository settings
- Ensure index.html is in the root directory
- Wait 5-10 minutes for deployment to complete

**Articles not showing?**
- Verify JSON files are valid (use jsonlint.com)
- Check posts/index.json contains all post slugs
- Ensure file names match slugs exactly

**Styling issues?**
- Make sure style.css is in the root directory
- Check browser console for errors
- Test on different devices/browsers

## Adding New Posts After Deployment

1. Create new JSON file in posts/ folder
2. Add slug to posts/index.json  
3. Commit and push changes
4. GitHub Pages will automatically update (takes 1-5 minutes)

Your blog is now live and ready for the world! 🎉
