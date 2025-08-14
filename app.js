// --------------------
// NexaSQL Blog Config
// --------------------
const blogData = {
    company: {
        name: "NexaSQL",
        tagline: "Expert SQL Server solutions from ex-Microsoft engineers",
        description: "NexaSQL helps businesses scale with secure, fast, and reliable database management, optimization, and consulting services.",
        domain: "blog.nexasql.com",
        services: [
            "SQL Server Performance Tuning",
            "Database Administration",
            "Cloud Migration",
            "Query Optimization",
            "24/7 Support"
        ]
    },
    blogPosts: [], // loaded dynamically from HTML files
    categories: [
        { name: "SQL Server Performance", description: "Performance tuning, query optimization, and system monitoring", count: 25 },
        { name: "Database Administration", description: "DBA best practices, maintenance, and troubleshooting", count: 18 },
        { name: "Cloud Migration", description: "Azure SQL, AWS RDS, and hybrid cloud strategies", count: 12 },
        { name: "Security & Compliance", description: "Database security, encryption, and compliance frameworks", count: 8 }
    ]
};

// --------------------
// Utility Functions
// --------------------
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
}

function createSlug(title) {
    return title
        .toLowerCase()
        .replace(/[^\w\s-]/g, '')
        .replace(/\s+/g, '-')
        .replace(/-+/g, '-')
        .trim();
}

// Parse HTML post and extract metadata & content
function parseHTMLPost(htmlContent, filename) {
    const parser = new DOMParser();
    const doc = parser.parseFromString(htmlContent, 'text/html');

    const getMetaContent = (name) => {
        const meta = doc.querySelector(`meta[name="post:${name}"]`);
        return meta ? meta.getAttribute('content') : '';
    };

    const slugFromFile = filename.replace('.html', '');
    const slug = getMetaContent('slug') || slugFromFile;

    const tagsString = getMetaContent('tags');
    const tags = tagsString ? tagsString.split(',').map(t => t.trim()) : [];

    const bodyContent = doc.body ? doc.body.innerHTML : '';

    return {
        title: getMetaContent('title') || 'Untitled Post',
        slug: slug,
        excerpt: getMetaContent('excerpt') || '',
        author: getMetaContent('author') || 'Unknown Author',
        date: getMetaContent('date') || new Date().toISOString().split('T')[0],
        readTime: getMetaContent('readTime') || '5 min read',
        category: getMetaContent('category') || 'General',
        tags: tags,
        featured: getMetaContent('featured').toLowerCase() === 'true',
        content: bodyContent
    };
}

// --------------------
// DOM Builders
// --------------------
function createPostCard(post, featured = false) {
    const postCard = document.createElement('article');
    postCard.className = `post-card ${featured ? 'post-card--featured' : ''}`;
    const postSlug = post.slug || createSlug(post.title);

    postCard.innerHTML = `
        <a href="post.html?slug=${postSlug}" class="post-card__image-link">
            <div class="post-card__image-placeholder"></div>
        </a>
        <div class="post-card__content">
            <h2><a href="post.html?slug=${postSlug}">${post.title}</a></h2>
            <p class="post-card__meta">${formatDate(post.date)} • ${post.readTime}</p>
            <p class="post-card__excerpt">${post.excerpt}</p>
            <p class="post-card__tags">${post.tags.map(tag => `<span>${tag}</span>`).join('')}</p>
        </div>
    `;
    return postCard;
}

function createCategoryCard(category) {
    const categoryCard = document.createElement('article');
    categoryCard.className = 'category-card';
    categoryCard.innerHTML = `
        <h3>${category.name}</h3>
        <p>${category.description}</p>
        <span>${category.count} articles</span>
    `;
    return categoryCard;
}

// --------------------
// Post Loading Logic
// --------------------
async function discoverPosts() {
    try {
        const response = await fetch('posts/index.json');
        if (response.ok) {
            const index = await response.json();
            return index.posts || [];
        }
    } catch (err) {
        console.warn('No posts/index.json found, using fallback list');
    }
    return [];
}

async function loadPosts() {
    const postSlugs = await discoverPosts();
    const posts = [];

    for (const slug of postSlugs) {
        try {
            const response = await fetch(`posts/${slug}.html`);
            if (response.ok) {
                const htmlContent = await response.text();
                const post = parseHTMLPost(htmlContent, `${slug}.html`);
                posts.push(post);
            } else {
                console.warn(`Missing file: posts/${slug}.html`);
            }
        } catch (err) {
            console.error(`Error loading post ${slug}:`, err);
        }
    }
    posts.sort((a, b) => new Date(b.date) - new Date(a.date));
    blogData.blogPosts = posts;
    return posts;
}

async function loadSinglePost(slug) {
    try {
        const response = await fetch(`posts/${slug}.html`);
        if (response.ok) {
            const htmlContent = await response.text();
            return parseHTMLPost(htmlContent, `${slug}.html`);
        }
    } catch (err) {
        console.error(`Error loading single post: ${slug}`, err);
    }
    return null;
}

// --------------------
// Rendering Functions
// --------------------
function populateFeaturedPosts() {
    const container = document.getElementById('featuredPosts');
    if (!container) return;
    container.innerHTML = '';
    blogData.blogPosts.filter(p => p.featured).forEach(post => {
        container.appendChild(createPostCard(post, true));
    });
}

function populateRecentPosts() {
    const container = document.getElementById('recentPosts');
    if (!container) return;
    container.innerHTML = '';
    blogData.blogPosts.filter(p => !p.featured).forEach(post => {
        container.appendChild(createPostCard(post, false));
    });
}

function populateCategories() {
    const container = document.getElementById('categoriesGrid');
    if (!container) return;
    container.innerHTML = '';
    blogData.categories.forEach(cat => {
        container.appendChild(createCategoryCard(cat));
    });
}

function showArticleNotFound() {
    const titleEl = document.getElementById('postTitle');
    const metaEl = document.getElementById('postMeta');
    const contentEl = document.getElementById('postContent');
    if (titleEl) titleEl.textContent = "Article Not Found";
    if (metaEl) metaEl.textContent = "";
    if (contentEl) contentEl.innerHTML = `<p>Sorry, we couldn't find the article you're looking for.</p>
    <p><a href="index.html">Back to Home</a></p>`;
}

// --------------------
// Search
// --------------------
function initializeSearch() {
    const searchInput = document.getElementById('searchInput');
    const searchBtn = document.getElementById('searchBtn');
    if (!searchInput || !searchBtn) return;

    function performSearch() {
        const query = searchInput.value.toLowerCase().trim();
        const results = query === ''
            ? blogData.blogPosts
            : blogData.blogPosts.filter(post =>
                post.title.toLowerCase().includes(query) ||
                post.excerpt.toLowerCase().includes(query) ||
                post.tags.some(tag => tag.toLowerCase().includes(query)) ||
                post.category.toLowerCase().includes(query)
            );
        displaySearchResults(results, query);
    }

    searchBtn.addEventListener('click', performSearch);
    searchInput.addEventListener('keypress', e => {
        if (e.key === 'Enter') performSearch();
    });
}

function displaySearchResults(posts, query) {
    const featuredContainer = document.getElementById('featuredPosts');
    const recentContainer = document.getElementById('recentPosts');
    if (!featuredContainer || !recentContainer) return;
    featuredContainer.innerHTML = '';
    recentContainer.innerHTML = '';

    if (posts.length === 0) {
        featuredContainer.innerHTML = `<p>No articles found for "${query}".</p>`;
        return;
    }
    posts.forEach(p => {
        recentContainer.appendChild(createPostCard(p, false));
    });
}

// --------------------
// Page Initializer
// --------------------
document.addEventListener('DOMContentLoaded', async () => {
    const isPostPage = window.location.pathname.endsWith('post.html');
    if (isPostPage) {
        const params = new URLSearchParams(window.location.search);
        const slug = params.get('slug');
        if (!slug) {
            showArticleNotFound();
            return;
        }
        const post = await loadSinglePost(slug);
        if (!post) {
            showArticleNotFound();
            return;
        }
        // Inject into DOM
        if (document.getElementById('postTitle')) document.getElementById('postTitle').textContent = post.title;
        if (document.getElementById('postMeta')) document.getElementById('postMeta').textContent =
            `${formatDate(post.date)} • ${post.readTime} • By ${post.author}`;
        if (document.getElementById('postContent')) document.getElementById('postContent').innerHTML = post.content;
        document.title = `${post.title} - NexaSQL Blog`;
    } else {
        await loadPosts();
        populateFeaturedPosts();
        populateRecentPosts();
        populateCategories();
        initializeSearch();
    }
});
