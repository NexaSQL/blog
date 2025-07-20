# Create the post.html page for individual articles
post_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title id="pageTitle">Loading... - NexaSQL Blog</title>
    <meta name="description" content="" id="pageDescription">
    <meta name="keywords" content="SQL Server, database administration, performance tuning, cloud migration, Azure SQL">
    <meta name="author" content="NexaSQL">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="" id="ogUrl">
    <meta property="og:title" content="" id="ogTitle">
    <meta property="og:description" content="" id="ogDescription">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="" id="twitterUrl">
    <meta property="twitter:title" content="" id="twitterTitle">
    <meta property="twitter:description" content="" id="twitterDescription">
    
    <link rel="stylesheet" href="style.css">
    <style>
        /* Additional styles for article page */
        .article-header {
            background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-teal-700) 100%);
            color: var(--color-white);
            padding: var(--space-32) 0;
            text-align: center;
        }
        
        .article-meta {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: var(--space-16);
            margin-top: var(--space-16);
            font-size: var(--font-size-sm);
            opacity: 0.9;
        }
        
        .article-content {
            max-width: 800px;
            margin: 0 auto;
            padding: var(--space-32) var(--space-16);
            line-height: var(--line-height-normal);
        }
        
        .article-content h2 {
            margin-top: var(--space-32);
            margin-bottom: var(--space-16);
            color: var(--color-primary);
        }
        
        .article-content h3 {
            margin-top: var(--space-24);
            margin-bottom: var(--space-12);
            color: var(--color-text);
        }
        
        .article-content p {
            margin-bottom: var(--space-16);
            font-size: var(--font-size-lg);
        }
        
        .article-content ul, .article-content ol {
            margin-bottom: var(--space-16);
            padding-left: var(--space-24);
        }
        
        .article-content li {
            margin-bottom: var(--space-8);
            font-size: var(--font-size-lg);
        }
        
        .article-content blockquote {
            border-left: 4px solid var(--color-primary);
            padding: var(--space-16);
            margin: var(--space-24) 0;
            background: var(--color-secondary);
            font-style: italic;
        }
        
        .article-content code {
            background: var(--color-secondary);
            padding: var(--space-2) var(--space-6);
            border-radius: var(--radius-sm);
            font-family: var(--font-family-mono);
        }
        
        .article-content pre {
            background: var(--color-charcoal-800);
            color: var(--color-gray-200);
            padding: var(--space-20);
            border-radius: var(--radius-lg);
            overflow-x: auto;
            margin: var(--space-24) 0;
        }
        
        .article-content pre code {
            background: none;
            padding: 0;
            color: inherit;
        }
        
        .article-tags {
            display: flex;
            flex-wrap: wrap;
            gap: var(--space-8);
            margin: var(--space-24) 0;
            justify-content: center;
        }
        
        .article-tag {
            background: var(--color-primary);
            color: var(--color-white);
            padding: var(--space-6) var(--space-12);
            border-radius: var(--radius-sm);
            font-size: var(--font-size-sm);
            text-decoration: none;
            transition: background var(--duration-fast) var(--ease-standard);
        }
        
        .article-tag:hover {
            background: var(--color-primary-hover);
        }
        
        .back-button {
            margin: var(--space-24) 0;
            text-align: center;
        }
        
        .loading-state {
            text-align: center;
            padding: var(--space-32);
        }
        
        .error-state {
            text-align: center;
            padding: var(--space-32);
            color: var(--color-error);
        }
        
        .error-state h2 {
            color: var(--color-error);
        }
        
        @media (max-width: 768px) {
            .article-content {
                padding: var(--space-20) var(--space-16);
            }
            
            .article-meta {
                flex-direction: column;
                align-items: center;
                gap: var(--space-8);
            }
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="header__content">
                <div class="header__logo">
                    <h1 class="logo">
                        <a href="index.html" style="color: inherit; text-decoration: none;">NexaSQL</a>
                    </h1>
                    <span class="logo__tagline">Expert SQL Server Solutions</span>
                </div>
                <nav class="nav">
                    <ul class="nav__list">
                        <li class="nav__item">
                            <a href="index.html" class="nav__link">Home</a>
                        </li>
                        <li class="nav__item">
                            <a href="index.html#articles" class="nav__link">Articles</a>
                        </li>
                        <li class="nav__item">
                            <a href="index.html#categories" class="nav__link">Categories</a>
                        </li>
                        <li class="nav__item">
                            <a href="index.html#about" class="nav__link">About</a>
                        </li>
                        <li class="nav__item">
                            <a href="index.html#contact" class="nav__link">Contact</a>
                        </li>
                    </ul>
                    <button class="nav__toggle" aria-label="Toggle navigation">
                        <span></span>
                        <span></span>
                        <span></span>
                    </button>
                </nav>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main>
        <!-- Loading State -->
        <div id="loadingState" class="loading-state">
            <div class="container">
                <h2>Loading article...</h2>
                <p>Please wait while we fetch the content.</p>
            </div>
        </div>

        <!-- Error State -->
        <div id="errorState" class="error-state hidden">
            <div class="container">
                <h2>Article Not Found</h2>
                <p>Sorry, we couldn't find the article you're looking for.</p>
                <div class="back-button">
                    <a href="index.html" class="btn btn--primary">Back to Home</a>
                </div>
            </div>
        </div>

        <!-- Article Content -->
        <article id="articleContent" class="hidden">
            <!-- Article Header -->
            <section class="article-header">
                <div class="container">
                    <h1 id="articleTitle">Article Title</h1>
                    <div class="article-meta">
                        <span id="articleAuthor">By Author</span>
                        <span id="articleDate">Date</span>
                        <span id="articleReadTime">Read Time</span>
                        <span id="articleCategory">Category</span>
                    </div>
                </div>
            </section>

            <!-- Article Body -->
            <section class="article-content">
                <div id="articleBody">
                    <!-- Article content will be inserted here -->
                </div>
                
                <div class="article-tags" id="articleTags">
                    <!-- Tags will be inserted here -->
                </div>
                
                <div class="back-button">
                    <a href="index.html" class="btn btn--primary">← Back to Articles</a>
                </div>
            </section>
        </article>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer__content">
                <div class="footer__section">
                    <h3>NexaSQL</h3>
                    <p>Expert SQL Server solutions from ex-Microsoft engineers</p>
                    <div class="social-links">
                        <a href="#" class="social-link" target="_blank" rel="noopener">LinkedIn</a>
                        <a href="#" class="social-link" target="_blank" rel="noopener">Twitter</a>
                        <a href="#" class="social-link" target="_blank" rel="noopener">GitHub</a>
                    </div>
                </div>
                <div class="footer__section">
                    <h4>Categories</h4>
                    <ul>
                        <li><a href="index.html#categories">SQL Server Performance</a></li>
                        <li><a href="index.html#categories">Database Administration</a></li>
                        <li><a href="index.html#categories">Cloud Migration</a></li>
                        <li><a href="index.html#categories">Security & Compliance</a></li>
                    </ul>
                </div>
                <div class="footer__section">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="#" target="_blank">Performance Tuning</a></li>
                        <li><a href="#" target="_blank">Database Administration</a></li>
                        <li><a href="#" target="_blank">Cloud Migration</a></li>
                        <li><a href="#" target="_blank">24/7 Support</a></li>
                    </ul>
                </div>
                <div class="footer__section">
                    <h4>Contact</h4>
                    <p>Ready to optimize your SQL Server?</p>
                    <a href="mailto:contact@nexasql.com" class="btn btn--primary btn--sm">Get in Touch</a>
                </div>
            </div>
            <div class="footer__bottom">
                <p>&copy; 2024 NexaSQL. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script>
        // Utility functions
        function formatDate(dateString) {
            const date = new Date(dateString);
            return date.toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            });
        }

        function getUrlParameter(name) {
            const urlParams = new URLSearchParams(window.location.search);
            return urlParams.get(name);
        }

        function showLoading() {
            document.getElementById('loadingState').classList.remove('hidden');
            document.getElementById('errorState').classList.add('hidden');
            document.getElementById('articleContent').classList.add('hidden');
        }

        function showError() {
            document.getElementById('loadingState').classList.add('hidden');
            document.getElementById('errorState').classList.remove('hidden');
            document.getElementById('articleContent').classList.add('hidden');
        }

        function showArticle() {
            document.getElementById('loadingState').classList.add('hidden');
            document.getElementById('errorState').classList.add('hidden');
            document.getElementById('articleContent').classList.remove('hidden');
        }

        function updateMetaTags(post) {
            // Update page title
            document.getElementById('pageTitle').textContent = `${post.title} - NexaSQL Blog`;
            document.title = `${post.title} - NexaSQL Blog`;
            
            // Update meta description
            const descriptionMeta = document.getElementById('pageDescription');
            if (descriptionMeta) {
                descriptionMeta.setAttribute('content', post.excerpt);
            }
            
            // Update Open Graph tags
            const currentUrl = window.location.href;
            document.getElementById('ogUrl').setAttribute('content', currentUrl);
            document.getElementById('ogTitle').setAttribute('content', post.title);
            document.getElementById('ogDescription').setAttribute('content', post.excerpt);
            
            // Update Twitter tags
            document.getElementById('twitterUrl').setAttribute('content', currentUrl);
            document.getElementById('twitterTitle').setAttribute('content', post.title);
            document.getElementById('twitterDescription').setAttribute('content', post.excerpt);
        }

        function renderArticle(post) {
            // Update meta tags
            updateMetaTags(post);
            
            // Update article header
            document.getElementById('articleTitle').textContent = post.title;
            document.getElementById('articleAuthor').textContent = `By ${post.author}`;
            document.getElementById('articleDate').textContent = formatDate(post.date);
            document.getElementById('articleReadTime').textContent = post.readTime;
            document.getElementById('articleCategory').textContent = post.category;
            
            // Update article body
            const articleBody = document.getElementById('articleBody');
            
            // If content is a simple string, wrap in paragraphs
            let contentHtml = '';
            if (typeof post.content === 'string') {
                // Split by double newlines to create paragraphs
                const paragraphs = post.content.split('\\n\\n');
                contentHtml = paragraphs.map(p => `<p>${p.trim()}</p>`).join('');
            } else {
                contentHtml = post.content || '<p>Content coming soon...</p>';
            }
            
            articleBody.innerHTML = contentHtml;
            
            // Update tags
            const tagsContainer = document.getElementById('articleTags');
            if (post.tags && post.tags.length > 0) {
                const tagsHtml = post.tags.map(tag => 
                    `<a href="index.html" class="article-tag" onclick="filterByTag('${tag}')">${tag}</a>`
                ).join('');
                tagsContainer.innerHTML = tagsHtml;
            } else {
                tagsContainer.innerHTML = '';
            }
            
            showArticle();
        }

        // Load and display the article
        async function loadArticle() {
            showLoading();
            
            const slug = getUrlParameter('slug');
            if (!slug) {
                console.error('No slug parameter provided');
                showError();
                return;
            }
            
            try {
                const response = await fetch(`posts/${slug}.json`);
                
                if (!response.ok) {
                    throw new Error(`Failed to load article: ${response.status}`);
                }
                
                const post = await response.json();
                renderArticle(post);
                
            } catch (error) {
                console.error('Error loading article:', error);
                showError();
            }
        }

        // Filter function for tags (redirect to home page)
        function filterByTag(tag) {
            window.location.href = `index.html#articles`;
            // Note: The filtering will be handled by the main page
        }

        // Mobile navigation toggle
        function initializeNavigation() {
            const navToggle = document.querySelector('.nav__toggle');
            const navList = document.querySelector('.nav__list');
            
            if (navToggle && navList) {
                navToggle.addEventListener('click', () => {
                    navList.style.display = navList.style.display === 'flex' ? 'none' : 'flex';
                });
            }
        }

        // Initialize page
        function init() {
            console.log('Initializing article page...');
            initializeNavigation();
            loadArticle();
        }

        // Wait for DOM to be ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', init);
        } else {
            init();
        }
    </script>
</body>
</html>'''

# Save the post.html file
with open('post.html', 'w') as f:
    f.write(post_html)

print("Created post.html for individual articles!")