// Blog data with dynamic post loading from HTML files
const blogData = {
  company: {
    name: "NexaSQL",
    tagline: "Expert SQL Server solutions from ex-Microsoft engineers",
    description: "NexaSQL helps businesses scale with secure, fast, and reliable database management, optimization, and consulting services.",
    domain: "blog.nexasql.com",
    services: ["SQL Server Performance Tuning", "Database Administration", "Cloud Migration", "Query Optimization", "24/7 Support"]
  },
  blogPosts: [], // Will be populated dynamically from HTML files
  categories: [
    {
      name: "SQL Server Performance",
      description: "Performance tuning, query optimization, and system monitoring",
      count: 25
    },
    {
      name: "Database Administration", 
      description: "DBA best practices, maintenance, and troubleshooting",
      count: 18
    },
    {
      name: "Cloud Migration",
      description: "Azure SQL, AWS RDS, and hybrid cloud strategies", 
      count: 12
    },
    {
      name: "Security & Compliance",
      description: "Database security, encryption, and compliance frameworks",
      count: 8
    }
  ]
};

// Utility functions
function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long', 
    day: 'numeric'
  });
}

function createSlug(title) {
  return title
    .toLowerCase()
    .replace(/[^\w\s-]/g, '') // Remove special characters
    .replace(/\s+/g, '-') // Replace spaces with hyphens
    .replace(/-+/g, '-') // Replace multiple hyphens with single hyphen
    .trim();
}

// Parse HTML post file and extract metadata + content
function parseHTMLPost(htmlContent, filename) {
  // Create a DOM parser
  const parser = new DOMParser();
  const doc = parser.parseFromString(htmlContent, 'text/html');
  
  // Extract metadata from meta tags
  const getMetaContent = (name) => {
    const meta = doc.querySelector(`meta[name="post:${name}"]`);
    return meta ? meta.getAttribute('content') : '';
  };
  
  // Get post slug from filename if not in metadata
  const slug = getMetaContent('slug') || filename.replace('.html', '');
  
  // Parse tags (comma-separated string to array)
  const tagsString = getMetaContent('tags');
  const tags = tagsString ? tagsString.split(',').map(tag => tag.trim()) : [];
  
  // Extract content from body
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

function createPostCard(post, featured = false) {
  const postCard = document.createElement('article');
  postCard.className = `post-card ${featured ? 'post-card--featured' : ''}`;

  const tagsHtml = post.tags.map(tag => 
    `<span class="tag">${tag}</span>`
  ).join('');

  const postSlug = post.slug || createSlug(post.title);

  postCard.innerHTML = `
    <div class="post-card__content">
      <div class="post-card__meta">
        <span class="post-card__category">${post.category}</span>
        <span class="post-card__date">${formatDate(post.date)}</span>
      </div>
      <h3 class="post-card__title">
        <a href="post.html?slug=${postSlug}" class="post-card__link">
          ${post.title}
        </a>
      </h3>
      <p class="post-card__excerpt">${post.excerpt}</p>
      <div class="post-card__footer">
        <div class="post-card__author-info">
          <span class="post-card__author">${post.author}</span>
          <span class="post-card__read-time">${post.readTime}</span>
        </div>
        <div class="post-card__tags">
          ${tagsHtml}
        </div>
      </div>
    </div>
  `;

  return postCard;
}

function createCategoryCard(category) {
  const categoryCard = document.createElement('div');
  categoryCard.className = 'category-card';
  
  categoryCard.innerHTML = `
    <h3 class="category-card__title">${category.name}</h3>
    <p class="category-card__description">${category.description}</p>
    <span class="category-card__count">${category.count} articles</span>
  `;
  
  return categoryCard;
}

// Dynamic post loading from HTML files
async function loadPosts() {
  try {
    console.log('Loading posts from HTML files...');
    
    // Get list of post filenames from index
    const postSlugs = await discoverPosts();
    const posts = [];
    
    for (const slug of postSlugs) {
      try {
        const response = await fetch(`posts/${slug}.html`);
        if (response.ok) {
          const htmlContent = await response.text();
          const post = parseHTMLPost(htmlContent, `${slug}.html`);
          posts.push(post);
          console.log(`Loaded: ${post.title}`);
        } else {
          console.warn(`Failed to load posts/${slug}.html: ${response.status}`);
        }
      } catch (error) {
        console.warn(`Error loading posts/${slug}.html:`, error);
      }
    }
    
    // Sort posts by date (newest first)
    posts.sort((a, b) => new Date(b.date) - new Date(a.date));
    
    blogData.blogPosts = posts;
    console.log(`Successfully loaded ${posts.length} posts`);
    return posts;
    
  } catch (error) {
    console.error('Error loading posts:', error);
    // Fallback to empty array
    blogData.blogPosts = [];
    return [];
  }
}

// Auto-discover posts from posts directory
async function discoverPosts() {
  try {
    const response = await fetch('posts/index.json');
    if (response.ok) {
      const index = await response.json();
      return index.posts || [];
    }
  } catch (error) {
    console.log('No posts index found, using default list');
  }
  
  // Fallback to hardcoded list
  return [
    'sql-server-performance-tuning-techniques',
    'sql-server-index-optimization-guide', 
    'azure-sql-migration-lessons',
    'database-security-best-practices-2024',
    'troubleshooting-sql-server-performance-issues',
    'backup-recovery-strategies-businesses'
  ];
}

async function loadPostsFromDirectory() {
  try {
    console.log('Discovering and loading posts...');
    const postSlugs = await discoverPosts();
    const posts = [];
    
    for (const slug of postSlugs) {
      try {
        const response = await fetch(`posts/${slug}.html`);
        if (response.ok) {
          const htmlContent = await response.text();
          const post = parseHTMLPost(htmlContent, `${slug}.html`);
          posts.push(post);
          console.log(`Loaded: ${post.title}`);
        }
      } catch (error) {
        console.warn(`Error loading posts/${slug}.html:`, error);
      }
    }
    
    // Sort posts by date (newest first)
    posts.sort((a, b) => new Date(b.date) - new Date(a.date));
    
    blogData.blogPosts = posts;
    console.log(`Successfully loaded ${posts.length} posts`);
    return posts;
    
  } catch (error) {
    console.error('Error loading posts:', error);
    blogData.blogPosts = [];
    return [];
  }
}

// Load individual post for post.html page
async function loadSinglePost(slug) {
  try {
    const response = await fetch(`posts/${slug}.html`);
    if (response.ok) {
      const htmlContent = await response.text();
      const post = parseHTMLPost(htmlContent, `${slug}.html`);
      return post;
    } else {
      console.error(`Failed to load post: ${slug}`);
      return null;
    }
  } catch (error) {
    console.error(`Error loading post ${slug}:`, error);
    return null;
  }
}

// Main functions (unchanged)
function populateFeaturedPosts() {
  const featuredContainer = document.getElementById('featuredPosts');
  if (!featuredContainer) return;
  
  featuredContainer.innerHTML = '';
  const featuredPosts = blogData.blogPosts.filter(post => post.featured);
  
  featuredPosts.forEach(post => {
    const postCard = createPostCard(post, true);
    featuredContainer.appendChild(postCard);
  });
}

function populateRecentPosts() {
  const recentContainer = document.getElementById('recentPosts');
  if (!recentContainer) return;
  
  recentContainer.innerHTML = '';
  const recentPosts = blogData.blogPosts.filter(post => !post.featured);
  
  recentPosts.forEach(post => {
    const postCard = createPostCard(post, false);
    recentContainer.appendChild(postCard);
  });
}

function populateCategories() {
  const categoriesContainer = document.getElementById('categoriesGrid');
  if (!categoriesContainer) return;
  
  categoriesContainer.innerHTML = '';
  blogData.categories.forEach(category => {
    const categoryCard = createCategoryCard(category);
    categoriesContainer.appendChild(categoryCard);
  });
}

// Search functionality (unchanged)
function initializeSearch() {
  const searchInput = document.getElementById('searchInput');
  const searchBtn = document.getElementById('searchBtn');
  
  if (!searchInput || !searchBtn) return;
  
  function performSearch() {
    const query = searchInput.value.toLowerCase().trim();
    
    if (query === '') {
      showAllPosts();
      return;
    }
    
    const filteredPosts = blogData.blogPosts.filter(post =>
      post.title.toLowerCase().includes(query) ||
      post.excerpt.toLowerCase().includes(query) ||
      post.tags.some(tag => tag.toLowerCase().includes(query)) ||
      post.category.toLowerCase().includes(query)
    );
    
    displaySearchResults(filteredPosts, query);
  }
  
  searchBtn.addEventListener('click', performSearch);
  searchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      performSearch();
    }
  });
  
  // Add input event for real-time feedback
  searchInput.addEventListener('input', function() {
    if (this.value.trim() === '') {
      showAllPosts();
    }
  });
}

function displaySearchResults(posts, query) {
  const featuredContainer = document.getElementById('featuredPosts');
  const recentContainer = document.getElementById('recentPosts');
  
  if (!featuredContainer || !recentContainer) return;
  
  // Clear existing content
  featuredContainer.innerHTML = '';
  recentContainer.innerHTML = '';
  
  if (posts.length === 0) {
    featuredContainer.innerHTML = `
      <div class="search-no-results">
        <h3>No articles found for "${query}"</h3>
        <p>Try adjusting your search terms or browse our categories.</p>
      </div>
    `;
    return;
  }
  
  // Show search results
  const resultsTitle = document.createElement('h2');
  resultsTitle.textContent = `Search Results for "${query}" (${posts.length})`;
  resultsTitle.className = 'search-results-title';
  featuredContainer.appendChild(resultsTitle);
  
  posts.forEach(post => {
    const postCard = createPostCard(post);
    recentContainer.appendChild(postCard);
  });
}

function showAllPosts() {
  populateFeaturedPosts();
  populateRecentPosts();
}

// Post page functionality
function displaySinglePost(post) {
  if (!post) {
    document.getElementById('postContent').innerHTML = `
      <div class="post-not-found">
        <h1>Article Not Found</h1>
        <p>Sorry, we couldn't find the article you're looking for.</p>
        <a href="index.html" class="btn btn-primary">Back to Home</a>
      </div>
    `;
    return;
  }
  
  // Update page title
  document.title = `${post.title} - NexaSQL Blog`;
  
  // Update meta description
  const metaDescription = document.querySelector('meta[name="description"]');
  if (metaDescription) {
    metaDescription.setAttribute('content', post.excerpt);
  }
  
  // Populate post content
  const postContent = document.getElementById('postContent');
  if (postContent) {
    const tagsHtml = post.tags.map(tag => 
      `<span class="tag">${tag}</span>`
    ).join('');
    
    postContent.innerHTML = `
      <article class="post-article">
        <header class="post-header">
          <h1 class="post-title">${post.title}</h1>
          <div class="post-meta">
            <span class="post-author">By ${post.author}</span>
            <span class="post-date">${formatDate(post.date)}</span>
            <span class="post-read-time">${post.readTime}</span>
            <span class="post-category">${post.category}</span>
          </div>
          <div class="post-tags">
            ${tagsHtml}
          </div>
        </header>
        <div class="post-body">
          ${post.content}
        </div>
      </article>
      <div class="post-navigation">
        <a href="index.html" class="btn btn-secondary">← Back to Articles</a>
      </div>
    `;
  }
}

// Initialize the blog
async function initializeBlog() {
  // Load posts
  await loadPostsFromDirectory();
  
  // Initialize page-specific functionality
  if (document.getElementById('featuredPosts')) {
    // Homepage
    populateFeaturedPosts();
    populateRecentPosts();
    populateCategories();
    initializeSearch();
  } else if (document.getElementById('postContent')) {
    // Individual post page
    const urlParams = new URLSearchParams(window.location.search);
    const slug = urlParams.get('slug');
    
    if (slug) {
      const post = await loadSinglePost(slug);
      displaySinglePost(post);
    } else {
      displaySinglePost(null);
    }
  }
}

// Start the blog when DOM is loaded
document.addEventListener('DOMContentLoaded', initializeBlog);
