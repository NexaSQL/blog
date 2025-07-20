document.addEventListener("DOMContentLoaded", () => {
  const featuredSection = document.getElementById("featuredPosts");
  const latestSection = document.getElementById("recentPosts");

  fetch("posts/index.json")
    .then(res => res.json())
    .then(posts => {
      const sortedPosts = posts.sort((a, b) => new Date(b.date) - new Date(a.date));
      const featuredPosts = sortedPosts.filter(post => post.featured);

      featuredSection.innerHTML = featuredPosts.map(renderPostCard).join("");
      latestSection.innerHTML = sortedPosts.filter(p => !p.featured).map(renderPostCard).join("");
    })
    .catch(err => {
      console.error("Failed to load blog posts:", err);
      featuredSection.innerHTML = "<p>Unable to load posts.</p>";
      latestSection.innerHTML = "<p>Unable to load posts.</p>";
    });
});

function renderPostCard(post) {
  const dateFormatted = new Date(post.date).toLocaleDateString("en-US", {
    year: "numeric",
    month: "short",
    day: "numeric"
  });

  const tagsHTML = post.tags?.map(tag => `<span class="tag">${tag}</span>`).join(" ") || "";

  return `
    <div class="post-card">
      <a class="post-link" href="posts/post.html?slug=${post.slug}">
        <h3 class="post-title">${post.title}</h3>
      </a>
      <div class="post-meta">
        By <strong>${post.author}</strong> | ${dateFormatted} | ${post.readTime}
      </div>
      <p class="post-excerpt">${post.excerpt}</p>
      <div class="post-tags">${tagsHTML}</div>
    </div>
  `;
}

