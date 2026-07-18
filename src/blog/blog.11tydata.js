export default {
  layout: "post.njk",
  author: "COR Team",
  ogType: "article",
  eleventyComputed: {
    permalink: (data) =>
      data.page.inputPath.endsWith(".md") ? `/blog/${data.page.fileSlug}/` : data.permalink,
    canonicalUrl: (data) =>
      data.page.inputPath.endsWith(".md") ? `https://corgtm.com/blog/${data.page.fileSlug}/` : data.canonicalUrl,
    layout: (data) => (data.page.inputPath.endsWith(".md") ? "post.njk" : data.layout)
  }
};
