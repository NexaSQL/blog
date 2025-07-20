# First, let me analyze the current blog structure and create the updated files
# Starting with extracting the current post data to create individual JSON files

current_posts = [
    {
        "title": "5 SQL Server Performance Tuning Techniques That Actually Work",
        "slug": "sql-server-performance-tuning-techniques",
        "excerpt": "Learn the proven methods our ex-Microsoft engineers use to optimize SQL Server performance and reduce query execution times by up to 90%.",
        "author": "David Chen",
        "date": "2024-01-15",
        "readTime": "8 min read",
        "category": "Performance",
        "tags": ["Performance", "Optimization", "Query Tuning"],
        "featured": True,
        "content": "This is where the full article content would go..."
    },
    {
        "title": "Complete Guide to SQL Server Index Optimization",
        "slug": "sql-server-index-optimization-guide",
        "excerpt": "Master the art of index design and optimization with practical examples and real-world scenarios from enterprise deployments.",
        "author": "Sarah Martinez",
        "date": "2024-01-10",
        "readTime": "12 min read",
        "category": "Database Administration",
        "tags": ["Indexes", "Performance", "DBA"],
        "featured": True,
        "content": "This is where the full article content would go..."
    },
    {
        "title": "Migrating to Azure SQL: Lessons from 500+ Successful Migrations",
        "slug": "azure-sql-migration-lessons",
        "excerpt": "Discover the best practices, common pitfalls, and proven strategies for seamless SQL Server to Azure SQL migrations.",
        "author": "Michael Thompson",
        "date": "2024-01-05",
        "readTime": "10 min read",
        "category": "Cloud Migration",
        "tags": ["Azure", "Migration", "Cloud"],
        "featured": True,
        "content": "This is where the full article content would go..."
    },
    {
        "title": "Database Security Best Practices for 2024",
        "slug": "database-security-best-practices-2024",
        "excerpt": "Protect your SQL Server databases with the latest security measures and compliance strategies recommended by security experts.",
        "author": "Emma Rodriguez",
        "date": "2024-01-01",
        "readTime": "7 min read",
        "category": "Security",
        "tags": ["Security", "Compliance", "Best Practices"],
        "featured": False,
        "content": "This is where the full article content would go..."
    },
    {
        "title": "Troubleshooting Common SQL Server Performance Issues",
        "slug": "troubleshooting-sql-server-performance-issues",
        "excerpt": "Quick solutions to the most frequent performance problems we encounter in SQL Server environments.",
        "author": "James Wilson",
        "date": "2023-12-28",
        "readTime": "6 min read",
        "category": "Performance",
        "tags": ["Troubleshooting", "Performance", "DBA"],
        "featured": False,
        "content": "This is where the full article content would go..."
    },
    {
        "title": "Backup and Recovery Strategies That Save Businesses",
        "slug": "backup-recovery-strategies-businesses",
        "excerpt": "Implement robust backup and recovery solutions that ensure zero data loss and minimal downtime.",
        "author": "Lisa Park",
        "date": "2023-12-25",
        "readTime": "9 min read",
        "category": "Database Administration",
        "tags": ["Backup", "Recovery", "Business Continuity"],
        "featured": False,
        "content": "This is where the full article content would go..."
    }
]

# Create individual JSON files for each post
import json
import os

# Create posts directory structure
os.makedirs('posts', exist_ok=True)

for post in current_posts:
    filename = f"posts/{post['slug']}.json"
    with open(filename, 'w') as f:
        json.dump(post, f, indent=2)
    print(f"Created: {filename}")

print("\nPost JSON files created successfully!")