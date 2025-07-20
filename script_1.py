# Create the updated app.js that loads posts dynamically from JSON files
updated_app_js = '''// Blog data with dynamic post loading
const blogData = {
  company: {
    name: "NexaSQL",
    tagline: "Expert SQL Server solutions from ex-Microsoft engineers",
    description: "NexaSQL helps businesses scale with secure, fast, and reliable database management, optimization, and consulting services.",
    domain: "blog.nexasql.com",
    services: ["SQL Server Performance Tuning", "Database Administration", "Cloud Migration", "Query Optimization", "24/7 Support"]
  },
  blogPosts: [], // Will be populated dynamically
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
    .replace(/[^\\w\\s-]/g, '') // Remove special characters
    .replace(/\\s+/g, '-') // Replace spaces with hyphens
    .replace(/-+/g, '-') // Replace multiple hyphens with single hyphen
    .trim();
}

function createPostCard(post, featured = false) {
  const postCard = document.createElement('article');
  postCard.className = `post-card ${featured ? 'post-card--featured' : ''}`;
  
  const tagsHtml = post.tags.map(tag => 
    `<span class="post-tag" data-tag="${tag}">${tag}</span>`
  ).join('');
  
  const postSlug = post.slug || createSlug(post.title);
  
  postCard.innerHTML = `
    <div class="post-card__header">
      <h3 class="post-card__title">
        <a href="post.html?slug=${postSlug}" class="post-link">${post.title}</a>
      </h3>
      <p class="post-card__excerpt">${post.excerpt}</p>
      <div class="post-card__meta">
        <span class="post-card__author">By ${post.author}</span>
        <span class="post-card__date">${formatDate(post.date)}</span>
        <span class="post-card__read-time">${post.readTime}</span>
      </div>
    </div>
    <div class="post-card__footer">
      <span class="post-card__category">${post.category}</span>
      <div class="post-card__tags">
        ${tagsHtml}
      </div>
    </div>
  `;
  
  return postCard;
}

function createCategoryCard(category) {
  const categoryCard = document.createElement('div');
  categoryCard.className = 'category-card';
  categoryCard.style.cursor = 'pointer';
  categoryCard.innerHTML = `
    <h3 class="category-card__name">${category.name}</h3>
    <p class="category-card__description">${category.description}</p>
    <span class="category-card__count">${category.count} articles</span>
  `;
  
  return categoryCard;
}

// Dynamic post loading functionality
async function loadPosts() {
  try {
    console.log('Loading posts from JSON files...');
    
    // List of post slugs (you can also dynamically discover these)
    const postSlugs = [
      'sql-server-performance-tuning-techniques',
      'sql-server-index-optimization-guide', 
      'azure-sql-migration-lessons',
      'database-security-best-practices-2024',
      'troubleshooting-sql-server-performance-issues',
      'backup-recovery-strategies-businesses'
    ];
    
    const posts = [];
    
    for (const slug of postSlugs) {
      try {
        const response = await fetch(`posts/${slug}.json`);
        if (response.ok) {
          const post = await response.json();
          posts.push(post);
          console.log(`Loaded: ${post.title}`);
        } else {
          console.warn(`Failed to load posts/${slug}.json: ${response.status}`);
        }
      } catch (error) {
        console.warn(`Error loading posts/${slug}.json:`, error);
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

// Auto-discover posts from posts directory (GitHub Pages friendly)
async function discoverPosts() {
  // Since we can't list directory contents directly in browser,
  // we'll maintain a posts index file for discovery
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
        const response = await fetch(`posts/${slug}.json`);
        if (response.ok) {
          const post = await response.json();
          posts.push(post);
          console.log(`Loaded: ${post.title}`);
        }
      } catch (error) {
        console.warn(`Error loading posts/${slug}.json:`, error);
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

// Main functions
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

// Search functionality
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
      <div class="search-no-results" style="text-align: center; padding: 2rem;">
        <h3>No results found for "${query}"</h3>
        <p>Try adjusting your search terms or browse our categories.</p>
        <button class="btn btn--primary" onclick="showAllPosts()">Show All Posts</button>
      </div>
    `;
    return;
  }
  
  // Update section titles
  const featuredTitle = document.querySelector('.featured-articles .section-title');
  const recentTitle = document.querySelector('.recent-posts .section-title');
  
  if (featuredTitle) featuredTitle.textContent = `Search Results for "${query}"`;
  if (recentTitle) recentTitle.textContent = `${posts.length} articles found`;
  
  // Display all results in the featured section
  posts.forEach(post => {
    const postCard = createPostCard(post, false);
    featuredContainer.appendChild(postCard);
  });
}

function showAllPosts() {
  // Reset section titles
  const featuredTitle = document.querySelector('.featured-articles .section-title');
  const recentTitle = document.querySelector('.recent-posts .section-title');
  
  if (featuredTitle) featuredTitle.textContent = 'Featured Articles';
  if (recentTitle) recentTitle.textContent = 'Recent Posts';
  
  // Clear search input
  const searchInput = document.getElementById('searchInput');
  if (searchInput) searchInput.value = '';
  
  // Repopulate posts
  populateFeaturedPosts();
  populateRecentPosts();
}

function filterPostsByCategory(categoryName) {
  const filteredPosts = blogData.blogPosts.filter(post => 
    post.category.toLowerCase().includes(categoryName.toLowerCase())
  );
  
  displaySearchResults(filteredPosts, categoryName);
  
  // Scroll to articles section
  const articlesSection = document.getElementById('articles');
  if (articlesSection) {
    articlesSection.scrollIntoView({ behavior: 'smooth' });
  }
}

function filterPostsByTag(tag) {
  const filteredPosts = blogData.blogPosts.filter(post => 
    post.tags.includes(tag)
  );
  
  displaySearchResults(filteredPosts, `#${tag}`);
  
  // Scroll to articles section
  const articlesSection = document.getElementById('articles');
  if (articlesSection) {
    articlesSection.scrollIntoView({ behavior: 'smooth' });
  }
}

// Navigation functionality
function initializeNavigation() {
  const navToggle = document.querySelector('.nav__toggle');
  const navList = document.querySelector('.nav__list');
  const navLinks = document.querySelectorAll('.nav__link');
  
  // Mobile menu toggle
  if (navToggle && navList) {
    navToggle.addEventListener('click', () => {
      navList.style.display = navList.style.display === 'flex' ? 'none' : 'flex';
    });
  }
  
  // Smooth scrolling for navigation links
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = link.getAttribute('href');
      
      if (targetId && targetId.startsWith('#')) {
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          targetElement.scrollIntoView({ behavior: 'smooth' });
          
          // Update active state
          navLinks.forEach(l => l.classList.remove('nav__link--active'));
          link.classList.add('nav__link--active');
          
          // Close mobile menu
          if (navList) {
            navList.style.display = 'none';
          }
        }
      }
    });
  });
}

// Newsletter functionality
function initializeNewsletter() {
  const newsletterForm = document.getElementById('newsletterForm');
  
  if (!newsletterForm) return;
  
  newsletterForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const emailInput = newsletterForm.querySelector('input[type="email"]');
    const submitBtn = newsletterForm.querySelector('button[type="submit"]');
    
    if (!emailInput || !submitBtn) return;
    
    // Simple validation
    const emailValue = emailInput.value.trim();
    if (!emailValue || !emailValue.includes('@')) {
      alert('Please enter a valid email address.');
      return;
    }
    
    // Simulate newsletter signup
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Subscribing...';
    submitBtn.disabled = true;
    
    setTimeout(() => {
      alert('Thank you for subscribing to our newsletter!');
      emailInput.value = '';
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
    }, 1000);
  });
}

// Hero section actions
function initializeHeroActions() {
  const exploreBtn = document.querySelector('.hero__actions .btn--primary');
  const subscribeBtn = document.querySelector('.hero__actions .btn--outline');
  
  if (exploreBtn) {
    exploreBtn.addEventListener('click', () => {
      const articlesSection = document.getElementById('articles');
      if (articlesSection) {
        articlesSection.scrollIntoView({ behavior: 'smooth' });
      }
    });
  }
  
  if (subscribeBtn) {
    subscribeBtn.addEventListener('click', () => {
      const newsletterSection = document.querySelector('.newsletter');
      if (newsletterSection) {
        newsletterSection.scrollIntoView({ behavior: 'smooth' });
      }
    });
  }
}

// Post and category interaction handlers
function initializeInteractions() {
  document.addEventListener('click', (e) => {
    // Handle tag clicks
    if (e.target.classList.contains('post-tag')) {
      e.preventDefault();
      const tag = e.target.getAttribute('data-tag');
      filterPostsByTag(tag);
    }
    
    // Handle category card clicks
    if (e.target.closest('.category-card')) {
      const categoryCard = e.target.closest('.category-card');
      const categoryName = categoryCard.querySelector('.category-card__name').textContent;
      filterPostsByCategory(categoryName);
    }
  });
}

// Initialize all functionality
async function init() {
  console.log('Initializing NexaSQL Blog...');
  
  try {
    // Load posts first
    await loadPostsFromDirectory();
    
    // Populate content
    populateFeaturedPosts();
    populateRecentPosts();
    populateCategories();
    
    // Initialize interactions
    initializeSearch();
    initializeNavigation();
    initializeNewsletter();
    initializeHeroActions();
    initializeInteractions();
    
    console.log('NexaSQL Blog initialized successfully!');
  } catch (error) {
    console.error('Error initializing blog:', error);
  }
}

// Make functions globally available
window.showAllPosts = showAllPosts;
window.filterPostsByCategory = filterPostsByCategory;
window.filterPostsByTag = filterPostsByTag;

// Wait for DOM to be ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}

// Export for potential external use
window.NexaSQLBlog = {
  data: blogData,
  search: displaySearchResults,
  filterByCategory: filterPostsByCategory,
  filterByTag: filterPostsByTag,
  showAllPosts: showAllPosts,
  loadPosts: loadPostsFromDirectory
};'''

# Save the updated app.js
with open('app.js', 'w') as f:
    f.write(updated_app_js)

print("Created updated app.js with dynamic post loading!")