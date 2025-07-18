// Blog data
const blogData = {
  company: {
    name: "NexaSQL",
    tagline: "Expert SQL Server solutions from ex-Microsoft engineers",
    description: "NexaSQL helps businesses scale with secure, fast, and reliable database management, optimization, and consulting services.",
    domain: "blog.nexasql.com",
    services: ["SQL Server Performance Tuning", "Database Administration", "Cloud Migration", "Query Optimization", "24/7 Support"]
  },
  blogPosts: [
    {
      title: "5 SQL Server Performance Tuning Techniques That Actually Work",
      excerpt: "Learn the proven methods our ex-Microsoft engineers use to optimize SQL Server performance and reduce query execution times by up to 90%.",
      author: "David Chen",
      date: "2024-01-15",
      readTime: "8 min read",
      category: "Performance",
      tags: ["Performance", "Optimization", "Query Tuning"],
      featured: true
    },
    {
      title: "Complete Guide to SQL Server Index Optimization",
      excerpt: "Master the art of index design and optimization with practical examples and real-world scenarios from enterprise deployments.",
      author: "Sarah Martinez",
      date: "2024-01-10",
      readTime: "12 min read",
      category: "Database Administration",
      tags: ["Indexes", "Performance", "DBA"],
      featured: true
    },
    {
      title: "Migrating to Azure SQL: Lessons from 500+ Successful Migrations",
      excerpt: "Discover the best practices, common pitfalls, and proven strategies for seamless SQL Server to Azure SQL migrations.",
      author: "Michael Thompson",
      date: "2024-01-05",
      readTime: "10 min read",
      category: "Cloud Migration",
      tags: ["Azure", "Migration", "Cloud"],
      featured: true
    },
    {
      title: "Database Security Best Practices for 2024",
      excerpt: "Protect your SQL Server databases with the latest security measures and compliance strategies recommended by security experts.",
      author: "Emma Rodriguez",
      date: "2024-01-01",
      readTime: "7 min read",
      category: "Security",
      tags: ["Security", "Compliance", "Best Practices"],
      featured: false
    },
    {
      title: "Troubleshooting Common SQL Server Performance Issues",
      excerpt: "Quick solutions to the most frequent performance problems we encounter in SQL Server environments.",
      author: "James Wilson",
      date: "2023-12-28",
      readTime: "6 min read",
      category: "Performance",
      tags: ["Troubleshooting", "Performance", "DBA"],
      featured: false
    },
    {
      title: "Backup and Recovery Strategies That Save Businesses",
      excerpt: "Implement robust backup and recovery solutions that ensure zero data loss and minimal downtime.",
      author: "Lisa Park",
      date: "2023-12-25",
      readTime: "9 min read",
      category: "Database Administration",
      tags: ["Backup", "Recovery", "Business Continuity"],
      featured: false
    }
  ],
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

function createPostCard(post, featured = false) {
  const postCard = document.createElement('article');
  postCard.className = `post-card ${featured ? 'post-card--featured' : ''}`;
  
  const tagsHtml = post.tags.map(tag => 
    `<span class="post-tag" data-tag="${tag}">${tag}</span>`
  ).join('');
  
  postCard.innerHTML = `
    <div class="post-card__header">
      <h3 class="post-card__title">
        <a href="javascript:void(0)" class="post-link" data-post-title="${post.title}">${post.title}</a>
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
    // Handle post title clicks
    if (e.target.classList.contains('post-link')) {
      e.preventDefault();
      const postTitle = e.target.getAttribute('data-post-title');
      showPostDetail(postTitle);
    }
    
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

function showPostDetail(postTitle) {
  const post = blogData.blogPosts.find(p => p.title === postTitle);
  if (!post) return;
  
  // Create a simple modal-like alert for demonstration
  const message = `Full Article: "${post.title}"\n\nAuthor: ${post.author}\nRead Time: ${post.readTime}\nCategory: ${post.category}\n\n${post.excerpt}\n\nIn a real implementation, this would open the complete article with code examples, syntax highlighting, and related posts.`;
  
  alert(message);
}

// Initialize all functionality
function init() {
  console.log('Initializing NexaSQL Blog...');
  
  try {
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
  showAllPosts: showAllPosts
};