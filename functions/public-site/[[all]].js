// ABOUTME: Serves public-site static assets (images, videos) from R2.
// ABOUTME: Requires PUBLIC_SITE_ASSETS_BUCKET R2 binding configured in Cloudflare dashboard.

export async function onRequestGet(ctx) {
  const path = new URL(ctx.request.url).pathname.replace("/public-site/", "");
  const file = await ctx.env.PUBLIC_SITE_ASSETS_BUCKET.get(path);
  if (!file) return new Response(null, { status: 404 });

  const headers = new Headers();
  if (file.httpMetadata?.contentType) {
    headers.set("Content-Type", file.httpMetadata.contentType);
  }
  headers.set("Cache-Control", "public, max-age=31536000, immutable");

  return new Response(file.body, { headers });
}
