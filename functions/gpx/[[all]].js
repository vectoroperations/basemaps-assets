export async function onRequestGet(ctx) {
  const path = new URL(ctx.request.url).pathname.replace("/gpx/", "");
  const file = await ctx.env.GPX_BUCKET.get(path);
  if (!file) return new Response(null, { status: 404 });
  return new Response(file.body, {
    headers: { "Content-Type": file.httpMetadata.contentType },
  });
}
