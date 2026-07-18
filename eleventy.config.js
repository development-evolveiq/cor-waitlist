export default function(eleventyConfig) {
  // Static assets copied as-is into the output, same relative path
  eleventyConfig.addPassthroughCopy("src/images");
  eleventyConfig.addPassthroughCopy("src/videos");
  eleventyConfig.addPassthroughCopy("src/favicon.ico");
  eleventyConfig.addPassthroughCopy("src/icon-16.png");
  eleventyConfig.addPassthroughCopy("src/icon-32.png");
  eleventyConfig.addPassthroughCopy("src/icon-180.png");
  eleventyConfig.addPassthroughCopy("src/icon-192.png");
  eleventyConfig.addPassthroughCopy("src/icon-512.png");
  eleventyConfig.addPassthroughCopy("src/robots.txt");

  // Drafts live in src/blog/_drafts/ and are never built
  eleventyConfig.ignores.add("src/blog/_drafts/**");

  // Blog posts collection, newest first
  eleventyConfig.addCollection("posts", (collectionApi) =>
    collectionApi.getFilteredByGlob("src/blog/*.md").sort((a, b) => b.date - a.date)
  );

  // Date helpers
  eleventyConfig.addFilter("dateISO", (d) => new Date(d).toISOString().split("T")[0]);
  eleventyConfig.addFilter("dateDisplay", (d) =>
    new Date(d).toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric", timeZone: "UTC" })
  );
  eleventyConfig.addFilter("dateRFC3339", (d) => new Date(d).toISOString());

  // Reading time (~220 wpm)
  eleventyConfig.addFilter("readingTime", (content) => {
    const words = String(content || "").replace(/<[^>]*>/g, " ").split(/\s+/).filter(Boolean).length;
    return Math.max(1, Math.round(words / 220));
  });

  return {
    dir: {
      input: "src",
      includes: "_includes",
      output: "_site"
    },
    // .njk templates use Nunjucks; .html files pass through untouched if not templated
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk"
  };
}
