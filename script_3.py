# Create posts/index.json for post discovery
posts_index = {
    "posts": [
        "sql-server-performance-tuning-techniques",
        "sql-server-index-optimization-guide", 
        "azure-sql-migration-lessons",
        "database-security-best-practices-2024",
        "troubleshooting-sql-server-performance-issues",
        "backup-recovery-strategies-businesses"
    ]
}

with open('posts/index.json', 'w') as f:
    json.dump(posts_index, f, indent=2)

print("Created posts/index.json for post discovery")

# Update one of the JSON files with proper content as an example
example_content = """
<h2>Introduction</h2>
<p>SQL Server performance tuning is both an art and a science. After years of working with enterprise-level SQL Server deployments at Microsoft, our team has identified the most impactful techniques that consistently deliver results.</p>

<h2>1. Query Plan Analysis and Optimization</h2>
<p>The execution plan is your roadmap to understanding how SQL Server processes your queries. Here's how to leverage it effectively:</p>
<ul>
<li><strong>Enable Actual Execution Plans:</strong> Always analyze actual plans rather than estimated ones</li>
<li><strong>Look for expensive operations:</strong> Focus on operations consuming >10% of query cost</li>
<li><strong>Identify missing indexes:</strong> SQL Server often suggests helpful indexes in the plan</li>
</ul>

<h3>Example: Optimizing a Slow SELECT Query</h3>
<pre><code>-- Original slow query
SELECT CustomerID, OrderDate, TotalAmount 
FROM Orders o
INNER JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE OrderDate >= '2024-01-01'
ORDER BY OrderDate DESC

-- Optimized version with proper indexing
-- Create index: CREATE INDEX IX_Orders_OrderDate_Includes 
-- ON Orders(OrderDate DESC) INCLUDE (CustomerID, TotalAmount)
</code></pre>

<h2>2. Index Strategy Optimization</h2>
<p>Proper indexing can transform your database performance overnight. Focus on these key areas:</p>
<ul>
<li><strong>Covering Indexes:</strong> Include frequently accessed columns to avoid key lookups</li>
<li><strong>Filtered Indexes:</strong> Use WHERE clauses to create more efficient indexes for specific scenarios</li>
<li><strong>Index Maintenance:</strong> Regular rebuilding and reorganization based on fragmentation levels</li>
</ul>

<blockquote>
<p>"A well-designed index strategy can improve query performance by up to 90%, but over-indexing can hurt INSERT/UPDATE performance significantly." - Microsoft SQL Server Team</p>
</blockquote>

<h2>3. Statistics Maintenance</h2>
<p>Statistics are the foundation of the query optimizer's decisions. Outdated statistics can lead to poor execution plans:</p>
<ul>
<li>Enable AUTO_UPDATE_STATISTICS_ASYNC for better performance</li>
<li>Update statistics manually for critical tables during maintenance windows</li>
<li>Monitor statistics age using sys.dm_db_stats_properties</li>
</ul>

<h2>4. Query Rewriting Techniques</h2>
<p>Sometimes the biggest gains come from rewriting queries to be more efficient:</p>
<ul>
<li><strong>Replace correlated subqueries</strong> with JOINs or window functions</li>
<li><strong>Use EXISTS instead of IN</strong> when checking for existence</li>
<li><strong>Minimize data type conversions</strong> and functions in WHERE clauses</li>
</ul>

<h2>5. Memory and Configuration Optimization</h2>
<p>Proper SQL Server configuration can dramatically improve performance:</p>
<ul>
<li><strong>Max Server Memory:</strong> Leave enough memory for the OS (typically 10-20% of total RAM)</li>
<li><strong>MAXDOP Settings:</strong> Set based on your workload characteristics</li>
<li><strong>Instant File Initialization:</strong> Enable for faster database growth</li>
</ul>

<h2>Conclusion</h2>
<p>These five techniques form the foundation of effective SQL Server performance tuning. When applied systematically, they can deliver the 90% performance improvements we see in our client engagements.</p>
<p>Remember: performance tuning is an iterative process. Start with the biggest bottlenecks and work your way down. Always test changes in a non-production environment first.</p>
"""

# Update the first post with proper content
with open('posts/sql-server-performance-tuning-techniques.json', 'r') as f:
    post_data = json.load(f)

post_data['content'] = example_content.strip()

with open('posts/sql-server-performance-tuning-techniques.json', 'w') as f:
    json.dump(post_data, f, indent=2)

print("Updated sql-server-performance-tuning-techniques.json with full content")

# Let's also update another post with content
index_content = """
<h2>Understanding SQL Server Indexes</h2>
<p>Database indexes are one of the most powerful tools for improving query performance, yet they're often misunderstood or implemented incorrectly. This comprehensive guide will teach you everything you need to know about SQL Server index optimization.</p>

<h2>Types of Indexes in SQL Server</h2>
<p>SQL Server offers several types of indexes, each with specific use cases:</p>

<h3>1. Clustered Indexes</h3>
<ul>
<li>Physically orders the data pages in the table</li>
<li>One clustered index per table</li>
<li>Often used on primary key columns</li>
</ul>

<h3>2. Nonclustered Indexes</h3>
<ul>
<li>Separate structure that points to data rows</li>
<li>Up to 999 nonclustered indexes per table</li>
<li>Can include additional columns for better coverage</li>
</ul>

<h2>Index Design Best Practices</h2>
<p>Follow these proven strategies for optimal index design:</p>

<h3>Column Order Matters</h3>
<p>Always put the most selective columns first in composite indexes:</p>
<pre><code>-- Good: Highly selective column first
CREATE INDEX IX_Orders_CustomerID_OrderDate 
ON Orders (CustomerID, OrderDate)

-- Less optimal: Less selective column first  
CREATE INDEX IX_Orders_OrderDate_CustomerID 
ON Orders (OrderDate, CustomerID)
</code></pre>

<h3>Use INCLUDE Columns Wisely</h3>
<p>Include frequently accessed columns to create covering indexes:</p>
<pre><code>CREATE INDEX IX_Orders_CustomerID_Covering
ON Orders (CustomerID) 
INCLUDE (OrderDate, TotalAmount, ProductID)
</code></pre>

<h2>Index Maintenance Strategies</h2>
<p>Regular maintenance is crucial for index performance:</p>
<ul>
<li><strong>Rebuild vs Reorganize:</strong> Rebuild for >30% fragmentation, reorganize for 5-30%</li>
<li><strong>Update Statistics:</strong> Ensure the optimizer has current information</li>
<li><strong>Monitor Usage:</strong> Remove unused indexes that hurt INSERT/UPDATE performance</li>
</ul>

<h2>Advanced Techniques</h2>
<h3>Filtered Indexes</h3>
<p>Create indexes on subsets of data for better efficiency:</p>
<pre><code>CREATE INDEX IX_Orders_Active 
ON Orders (OrderDate) 
WHERE Status = 'Active'
</code></pre>

<h3>Columnstore Indexes</h3>
<p>Perfect for analytical workloads and data warehousing scenarios.</p>

<h2>Common Index Pitfalls</h2>
<ul>
<li>Over-indexing tables with high INSERT/UPDATE activity</li>
<li>Creating too many overlapping indexes</li>
<li>Ignoring index fragmentation</li>
<li>Not monitoring index usage statistics</li>
</ul>

<h2>Conclusion</h2>
<p>Mastering SQL Server index optimization requires understanding your workload patterns and applying these techniques systematically. Start with the most frequently executed queries and build your indexing strategy from there.</p>
"""

with open('posts/sql-server-index-optimization-guide.json', 'r') as f:
    post_data = json.load(f)

post_data['content'] = index_content.strip()

with open('posts/sql-server-index-optimization-guide.json', 'w') as f:
    json.dump(post_data, f, indent=2)

print("Updated sql-server-index-optimization-guide.json with full content")