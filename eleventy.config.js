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
  eleventyConfig.addPassthroughCopy("src/sitemap.xml");
  eleventyConfig.addPassthroughCopy("src/robots.txt");

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
